# Query execution plan

## Concept explanation

An execution plan is Oracle's chosen set of row-source operations used to satisfy a SQL statement: access paths (index vs scan), join methods (nested loops, hash join, merge join), join order, and filtering/aggregation steps. The plan is an artifact of both compile-time decisions (CBO) and runtime adaptivity (cursor sharing, dynamic sampling, adaptive plans in supported releases).


## Architecture intent

Execution plans exist to translate logical SQL into efficient physical work while preserving relational semantics. Architecturally, you want plans to be:

- Stable across routine change (data growth, minor stats drift)
- Sensitive to the right variability (bind selectivity, partition pruning)
- Observable and diagnosable (plan hash value, row-source stats, wait events)

Treat plan review as part of operational readiness for critical SQL (payments, IAM, inventory, reporting).

```text
Logical SQL
   |
   v
CBO compilation
   |
   +-- Query transformations
   |     - predicate pushdown
   |     - view merging
   |     - subquery unnesting
   |
   +-- Access path + join order selection
   |     - stats + histograms
   |     - system stats
   |     - bind-aware cursor sharing
   v
Row-source tree (execution plan)
   |
   v
Runtime execution
   - consistent gets / physical reads
   - temp usage (hash joins, sorts)
   - latch/mutex contention (shared pool)
```

## SQL example

```sql
-- OLTP-style query that is sensitive to selectivity and indexing
SELECT /*+ gather_plan_statistics */
       o.order_id,
       o.customer_id,
       o.order_status,
       o.created_at
FROM   core_order o
WHERE  o.customer_id = :customer_id
AND    o.created_at >= SYSTIMESTAMP - INTERVAL '30' DAY
AND    o.order_status IN ('PAID','SHIPPED')
ORDER  BY o.created_at DESC
FETCH  FIRST 50 ROWS ONLY;

-- Inspect the *actual* runtime row-source statistics (not just estimated cardinality)
SELECT *
FROM   TABLE(
  DBMS_XPLAN.DISPLAY_CURSOR(
    NULL,
    NULL,
    'ALLSTATS LAST +COST +BYTES +PREDICATE +PEEKED_BINDS'
  )
);
```
## Sample input data

```sql
-- Minimal representative data; for plan analysis use production-like volumes and skew
INSERT INTO core_customer (customer_id, legal_name, created_at)
VALUES (42, 'Apex Manufacturing Pvt Ltd', SYSTIMESTAMP - INTERVAL '365' DAY);

INSERT INTO core_order (order_id, customer_id, order_status, created_at)
VALUES (1009001, 42, 'PAID', SYSTIMESTAMP - INTERVAL '2' DAY);

INSERT INTO core_order (order_id, customer_id, order_status, created_at)
VALUES (1009002, 42, 'SHIPPED', SYSTIMESTAMP - INTERVAL '1' DAY);

-- Supporting index aligned to predicates and ordering
CREATE INDEX ix_order_cust_created
ON core_order (customer_id, created_at DESC);
```
## Query execution

Operationally, you validate the plan in three layers:

- **Compile-time shape**: `EXPLAIN PLAN` or `DBMS_XPLAN.DISPLAY_CURSOR` after execution
- **Runtime truth**: `ALLSTATS LAST` row counts, temp usage, and elapsed time
- **System context**: AWR/ASH, SQL Monitor (for long-running SQL), and wait profile

Prefer measuring with binds that reflect real selectivity. A plan that is good for a hot customer may be poor for a cold customer, and vice versa. Oracle may maintain multiple child cursors; capture this explicitly in diagnostics.

Baseline production signals to record during validation:

| Signal | Why it matters in production | Where to validate |
|---|---|---|
| Elapsed time (p50/p95/p99) | SLA compliance and tail latency | App metrics + SQL Monitor |
| Consistent gets | Logical I/O pressure (buffer cache) | `DBMS_XPLAN` ALLSTATS, AWR |
| Physical reads | Storage latency and cache miss rate | AWR, v$ views |
| Rows (E-Rows vs A-Rows) | Cardinality estimate quality | `DBMS_XPLAN` ALLSTATS |
| Temp/PGA usage | Sort/hash spill risk | SQL Monitor, v$sql_workarea |


## Output

You should see:

- Rows ordered correctly with `FETCH FIRST` applied late (after index-ordering if possible)
- A plan that uses `INDEX RANGE SCAN` + `TABLE ACCESS BY ROWID (BATCHED)` when selective
- Low logical I/O (`consistent gets`) relative to table size

Example of the intended plan shape:

```text
SELECT STATEMENT
  SORT ORDER BY STOPKEY
    TABLE ACCESS BY INDEX ROWID BATCHED CORE_ORDER
      INDEX RANGE SCAN IX_ORDER_CUST_CREATED
```

## Real enterprise use case

A payments or order platform typically has:

- Hot key patterns (VIP customers, high-volume merchants)
- Time-window access (last N days)
- SLA-driven pagination (top-N recent events)

Execution plan discipline is how you ensure that the *same* endpoint remains predictable as volume grows. For regulated systems, you also need to demonstrate performance determinism under load tests that resemble peak-hour contention (shared pool pressure, redo generation, buffer cache churn).


## Performance considerations

Key drivers in Oracle:

- **Cardinality estimates**: stale stats, missing histograms, extended stats on correlated columns
- **Access path efficiency**: clustering factor, index compression, leaf block density
- **Sorting and TEMP**: `ORDER BY`, hash joins, group-by operations; watch PGA/TEMP usage
- **Concurrency**: buffer busy waits, ITL contention, library cache mutex contention

If the query is latency-critical, validate across representative binds and consider SPM for plan stability.


## Query optimization notes

Optimization workflow:

- Confirm predicate sargability (avoid `TRUNC(date_col)` on filtered columns unless function-based indexed)
- Ensure datatype alignment (no implicit conversions)
- Add/adjust composite indexes that match both filtering and ordering
- Consider partitioning and **partition pruning** for time-range predicates
- Use SQL Monitor for long-running statements to validate where time is spent

Avoid blanket hinting. If hinting is required, document the business reason and protect it with SPM.


## Best practice recommendations

- Keep object statistics current and automate with `DBMS_STATS` (including histograms where justified)
- Use bind variables for hot SQL; validate bind-aware behavior (multiple child cursors)
- Capture plan baselines for business-critical SQL (SPM)
- Standardize plan inspection using `DBMS_XPLAN.DISPLAY_CURSOR` and SQL Monitor for investigations
- Treat plan regressions as release blockers for tier-1 flows
