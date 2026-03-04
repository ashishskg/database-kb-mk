# Unbounded queries

## Concept explanation

Unbounded queries is an Oracle Database building block or SQL construct that has direct impact on correctness, operability, and performance under production workload. Treat it as a contract between the data model, the optimizer, and application behavior (bind patterns, concurrency, and data distribution).

In enterprise systems, database behavior must be predictable under growth and failure modes (hot keys, skew, plan drift, cache pressure, and lock contention). The goal of this reference is to document the intent and operational consequences, not just syntax.

## Architecture intent

Define clear, enforceable semantics at the database layer so that performance and consistency are not delegated to application code. In Oracle, this also helps the CBO choose stable access paths by aligning schema constraints, statistics, and query patterns.

Operational intent should be explicit:

- **Correctness boundary**: what the database guarantees (constraints, isolation, ordering)
- **Workload shape**: OLTP vs reporting, concurrency expectations, and growth assumptions
- **Observability**: what you will measure to prove it is behaving as designed

## SQL example

```sql
SELECT 1 AS placeholder
FROM   dual;
```
## Sample input data

```sql
-- Use your authoritative production-like dataset.
-- Focus on realistic cardinality, selectivity, and data skew.
```
## Query execution

Validate behavior using runtime evidence, not only estimated plans:

- **Plan + actuals**: execute with realistic binds and inspect `DBMS_XPLAN.DISPLAY_CURSOR` using   `ALLSTATS LAST` (and `+PEEKED_BINDS` where relevant).
- **System context**: confirm waits, CPU, and I/O via AWR/ASH and (for long SQL) SQL Monitor.
- **Metadata correctness**: verify constraints/index definitions using `DBA_CONSTRAINTS`,   `DBA_INDEXES`, `DBA_IND_COLUMNS`, and `DBA_TAB_COLUMNS`.

If the topic is performance-sensitive, capture baseline signals:

| Signal | Why it matters in production | Where to validate |
|---|---|---|
| Elapsed time (p50/p95/p99) | SLA compliance and tail latency | App metrics + SQL Monitor |
| Consistent gets | Logical I/O pressure (buffer cache) | `DBMS_XPLAN` ALLSTATS, AWR |
| Physical reads | Storage latency and cache miss rate | AWR, v$ views |
| Rows (E-Rows vs A-Rows) | Cardinality estimate quality | `DBMS_XPLAN` ALLSTATS |
| Temp/PGA usage | Sort/hash spill risk | SQL Monitor, v$sql_workarea |

## Output

Expected results include correct row sets (or constraint enforcement) and a predictable plan shape. In production, define acceptance criteria in terms of latency percentiles, consistent gets, physical reads, and concurrency behavior, not only row counts.

When documenting output for enterprise use, specify:

- **Functional**: correctness rules (e.g., uniqueness, referential integrity, null semantics)
- **Operational**: plan shape expectations and key predicates
- **Non-functional**: performance envelope and failure behavior under load

## Real enterprise use case

Use this construct to enforce core domain invariants (identity, referential integrity, status transitions) and to shape SQL patterns used by services and reporting pipelines. The database remains the source of truth for correctness; application tiers focus on workflow orchestration and resiliency.

Typical systems impacted:

- **Payments/ledger**: high write volume, strict auditability, contention management
- **IAM**: unique identity constraints, predictable lookup latency, safe schema evolution
- **Order/inventory**: mixed OLTP + reporting, hot partitions, time-window access patterns

## Performance considerations

Assess data volume, skew, and concurrency. In Oracle, features such as index compression, partition pruning, bind-aware cursor sharing, and buffer cache behavior can dominate observed latency. Ensure statistics are current and representative.

Decision criteria that tend to separate production-grade designs from toy designs:

- **Selectivity vs volume**: is the predicate selective enough for an index path?
- **Concurrency**: will this choice amplify lock/ITL/mutex contention?
- **Change rate**: how often do rows change (DML) and what does that imply for index maintenance and caching?
- **Data distribution**: do histograms/extended stats matter, and are they stable?

## Query optimization notes

Optimization guidance should be specific and testable:

- **Sargability**: keep predicates indexable; avoid wrapping filtered columns unless you have function-based indexes.
- **Datatype alignment**: eliminate implicit conversions that prevent index usage.
- **Join/filter alignment**: match composite index column order to the most selective predicates and join keys.
- **Plan stability**: use SPM for tier-1 SQL when plan regressions have unacceptable risk.

## Best practice recommendations

- Standardize naming and ownership to support incident response and safe automation
- Enforce constraints in the schema (do not rely on application-only invariants)
- Use bind variables for hot paths; validate cursor sharing and bind sensitivity
- Keep statistics current; treat stats strategy as part of release management
- Operationalize observability (AWR/ASH, SQL Monitor, v$ views) and set regression gates
