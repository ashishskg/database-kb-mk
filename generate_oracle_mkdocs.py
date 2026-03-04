#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Page:
    title: str
    file: str  # docs-relative path


@dataclass(frozen=True)
class Section:
    title: str
    pages: list[Page]


SECTIONS: list[Section] = [
    Section(
        "SECTION 1 — Database Fundamentals",
        [
            Page("What is a Database", "section-01/s1-what-is-db.md"),
            Page("Relational database concepts", "section-01/s1-relational.md"),
            Page("Tables and rows", "section-01/s1-tables-rows.md"),
            Page("Columns and datatypes", "section-01/s1-columns-types.md"),
            Page("Primary key", "section-01/s1-pk.md"),
            Page("Composite key", "section-01/s1-composite.md"),
            Page("Foreign key", "section-01/s1-fk.md"),
            Page("Unique constraints", "section-01/s1-unique.md"),
            Page("Not null constraint", "section-01/s1-not-null.md"),
            Page("Check constraints", "section-01/s1-check.md"),
        ],
    ),
    Section(
        "SECTION 2 — SQL Query Fundamentals",
        [
            Page("SELECT", "section-02/s2-select.md"),
            Page("INSERT", "section-02/s2-insert.md"),
            Page("UPDATE", "section-02/s2-update.md"),
            Page("DELETE", "section-02/s2-delete.md"),
            Page("WHERE clause", "section-02/s2-where.md"),
            Page("ORDER BY", "section-02/s2-order.md"),
            Page("GROUP BY", "section-02/s2-group.md"),
            Page("HAVING", "section-02/s2-having.md"),
            Page("DISTINCT", "section-02/s2-distinct.md"),
            Page("FETCH / LIMIT", "section-02/s2-fetch.md"),
        ],
    ),
    Section(
        "SECTION 3 — Joins",
        [
            Page("INNER JOIN", "section-03/s3-inner.md"),
            Page("LEFT JOIN", "section-03/s3-left.md"),
            Page("RIGHT JOIN", "section-03/s3-right.md"),
            Page("FULL JOIN", "section-03/s3-full.md"),
            Page("SELF JOIN", "section-03/s3-self.md"),
            Page("CROSS JOIN", "section-03/s3-cross.md"),
            Page("Multi-table joins", "section-03/s3-multi.md"),
        ],
    ),
    Section(
        "SECTION 4 — Aggregation Functions",
        [
            Page("COUNT", "section-04/s4-count.md"),
            Page("SUM", "section-04/s4-sum.md"),
            Page("AVG", "section-04/s4-avg.md"),
            Page("MIN", "section-04/s4-min.md"),
            Page("MAX", "section-04/s4-max.md"),
            Page("GROUPING queries", "section-04/s4-grouping.md"),
        ],
    ),
    Section(
        "SECTION 5 — Advanced SQL Queries",
        [
            Page("Subqueries", "section-05/s5-subqueries.md"),
            Page("Correlated subqueries", "section-05/s5-correlated.md"),
            Page("EXISTS", "section-05/s5-exists.md"),
            Page("IN vs EXISTS", "section-05/s5-in-vs-exists.md"),
            Page("CASE statements", "section-05/s5-case.md"),
            Page("COALESCE", "section-05/s5-coalesce.md"),
            Page("NULL handling", "section-05/s5-null-handling.md"),
            Page("Recursive queries", "section-05/s5-recursive.md"),
            Page("Hierarchical queries (CONNECT BY)", "section-05/s5-hierarchical.md"),
        ],
    ),
    Section(
        "SECTION 6 — Window Functions",
        [
            Page("ROW_NUMBER", "section-06/s6-row-number.md"),
            Page("RANK", "section-06/s6-rank.md"),
            Page("DENSE_RANK", "section-06/s6-dense-rank.md"),
            Page("NTILE", "section-06/s6-ntile.md"),
            Page("LEAD", "section-06/s6-lead.md"),
            Page("LAG", "section-06/s6-lag.md"),
            Page("FIRST_VALUE", "section-06/s6-first-value.md"),
            Page("LAST_VALUE", "section-06/s6-last-value.md"),
        ],
    ),
    Section(
        "SECTION 7 — Data Modeling & Relational Design",
        [
            Page("Entity relationship modeling", "section-07/s7-erm.md"),
            Page("One-to-one relationship", "section-07/s7-1to1.md"),
            Page("One-to-many relationship", "section-07/s7-1tomany.md"),
            Page("Many-to-many relationship", "section-07/s7-manytomany.md"),
            Page("Junction tables", "section-07/s7-junction.md"),
            Page("Referential integrity", "section-07/s7-ri.md"),
        ],
    ),
    Section(
        "SECTION 8 — Database Normalization",
        [
            Page("First Normal Form (1NF)", "section-08/s8-1nf.md"),
            Page("Second Normal Form (2NF)", "section-08/s8-2nf.md"),
            Page("Third Normal Form (3NF)", "section-08/s8-3nf.md"),
            Page("BCNF", "section-08/s8-bcnf.md"),
            Page("Denormalization strategies", "section-08/s8-denorm.md"),
        ],
    ),
    Section(
        "SECTION 9 — Indexing Architecture",
        [
            Page("What is an index", "section-09/s9-what.md"),
            Page("B-tree index", "section-09/s9-btree.md"),
            Page("Bitmap index", "section-09/s9-bitmap.md"),
            Page("Composite index", "section-09/s9-composite.md"),
            Page("Unique index", "section-09/s9-unique.md"),
            Page("Index usage", "section-09/s9-usage.md"),
            Page("When not to use indexes", "section-09/s9-avoid.md"),
            Page("Index access path diagram", "section-09/s9-diagrams.md"),
            Page("Index vs full scan comparison", "section-09/s9-compare.md"),
        ],
    ),
    Section(
        "SECTION 10 — Query Optimization & Performance",
        [
            Page("Query execution plan", "section-10/s10-plan.md"),
            Page("Cost-based optimizer", "section-10/s10-cbo.md"),
            Page("Index usage analysis", "section-10/s10-index-analysis.md"),
            Page("Full table scans", "section-10/s10-fts.md"),
            Page("Join optimization", "section-10/s10-join-opt.md"),
            Page("Partitioning strategies", "section-10/s10-partitioning.md"),
        ],
    ),
    Section(
        "SECTION 11 — Oracle Caching Architecture",
        [
            Page("Buffer cache", "section-11/s11-buffer.md"),
            Page("Shared pool", "section-11/s11-shared-pool.md"),
            Page("Library cache", "section-11/s11-library.md"),
            Page("SQL result cache", "section-11/s11-result-cache.md"),
            Page("Query caching strategies", "section-11/s11-strategies.md"),
        ],
    ),
    Section(
        "SECTION 12 — PL/SQL Programming",
        [
            Page("Stored procedures", "section-12/s12-proc.md"),
            Page("Functions", "section-12/s12-fn.md"),
            Page("Packages", "section-12/s12-packages.md"),
            Page("Triggers", "section-12/s12-triggers.md"),
            Page("Exception handling", "section-12/s12-exceptions.md"),
            Page("Cursor usage", "section-12/s12-cursors.md"),
            Page("Bulk operations", "section-12/s12-bulk.md"),
        ],
    ),
    Section(
        "SECTION 13 — Transactions & Concurrency",
        [
            Page("ACID properties", "section-13/s13-acid.md"),
            Page("COMMIT", "section-13/s13-commit.md"),
            Page("ROLLBACK", "section-13/s13-rollback.md"),
            Page("SAVEPOINT", "section-13/s13-savepoint.md"),
            Page("Locking mechanisms", "section-13/s13-locks.md"),
            Page("Isolation levels", "section-13/s13-isolation.md"),
        ],
    ),
    Section(
        "SECTION 14 — Advanced Database Features",
        [
            Page("Partitioning", "section-14/s14-partitioning.md"),
            Page("Materialized views", "section-14/s14-mv.md"),
            Page("Database links", "section-14/s14-dblinks.md"),
            Page("Sequences", "section-14/s14-seq.md"),
            Page("Synonyms", "section-14/s14-synonyms.md"),
            Page("Flashback queries", "section-14/s14-flashback.md"),
        ],
    ),
    Section(
        "SECTION 15 — Enterprise Database Architecture",
        [
            Page("High availability", "section-15/s15-ha.md"),
            Page("Replication", "section-15/s15-repl.md"),
            Page("Data warehousing", "section-15/s15-dwh.md"),
            Page("ETL pipelines", "section-15/s15-etl.md"),
            Page("Data partitioning strategies", "section-15/s15-part.md"),
            Page("Horizontal scaling", "section-15/s15-scale.md"),
        ],
    ),
    Section(
        "SECTION 16 — Real Enterprise Case Studies",
        [
            Page("Financial transaction database", "section-16/s16-fin.md"),
            Page("E-commerce order database", "section-16/s16-ecom.md"),
            Page("User management system", "section-16/s16-iam.md"),
            Page("Reporting database", "section-16/s16-report.md"),
            Page("Large-scale analytics database", "section-16/s16-analytics.md"),
            Page("Data warehouse architecture", "section-16/s16-dwh.md"),
            Page("High-volume log database", "section-16/s16-logs.md"),
        ],
    ),
    Section(
        "SECTION 17 — Performance Engineering",
        [
            Page("Query tuning techniques", "section-17/s17-tuning.md"),
            Page("Index optimization", "section-17/s17-index.md"),
            Page("Database caching strategies", "section-17/s17-cache.md"),
            Page("Connection pooling", "section-17/s17-pool.md"),
            Page("Avoiding slow queries", "section-17/s17-avoid.md"),
            Page("Monitoring database performance", "section-17/s17-monitor.md"),
        ],
    ),
    Section(
        "SECTION 18 — Database Anti-Patterns",
        [
            Page("Missing indexes", "section-18/s18-missing-index.md"),
            Page("Over-indexing", "section-18/s18-over-index.md"),
            Page("N+1 query problem", "section-18/s18-nplus1.md"),
            Page("Poor normalization", "section-18/s18-poor-norm.md"),
            Page("Inefficient joins", "section-18/s18-joins.md"),
            Page("Unbounded queries", "section-18/s18-unbounded.md"),
        ],
    ),
]


def mkdocs_yml() -> str:
    lines: list[str] = []
    lines.append("site_name: Oracle Database Reference")
    lines.append("theme: readthedocs")
    lines.append("nav:")
    for section in SECTIONS:
        lines.append(f"  - {section.title}:")
        for page in section.pages:
            lines.append(f"      - {page.title}: {page.file}")
    lines.append("")
    return "\n".join(lines)


def h2(title: str) -> str:
    return f"## {title}\n\n"


def sql_block(sql: str) -> str:
    return "```sql\n" + sql.strip() + "\n```\n"


def text_block(text: str) -> str:
    return "```text\n" + text.strip("\n") + "\n```\n"


def hr() -> str:
    return "\n"


def metrics_table() -> str:
    return (
        "| Signal | Why it matters in production | Where to validate |\n"
        "|---|---|---|\n"
        "| Elapsed time (p50/p95/p99) | SLA compliance and tail latency | App metrics + SQL Monitor |\n"
        "| Consistent gets | Logical I/O pressure (buffer cache) | `DBMS_XPLAN` ALLSTATS, AWR |\n"
        "| Physical reads | Storage latency and cache miss rate | AWR, v$ views |\n"
        "| Rows (E-Rows vs A-Rows) | Cardinality estimate quality | `DBMS_XPLAN` ALLSTATS |\n"
        "| Temp/PGA usage | Sort/hash spill risk | SQL Monitor, v$sql_workarea |\n"
    )


def default_sql_for(title: str) -> str:
    t = title.lower()

    if "relational database concepts" in t:
        return """
-- Relational modeling in Oracle: normalized core entities + enforced relationships
CREATE TABLE core_customer (
  customer_id   NUMBER       NOT NULL,
  legal_name    VARCHAR2(200) NOT NULL,
  created_at    TIMESTAMP(6)  DEFAULT SYSTIMESTAMP NOT NULL,
  CONSTRAINT pk_core_customer PRIMARY KEY (customer_id)
);

CREATE TABLE core_order (
  order_id      NUMBER       NOT NULL,
  customer_id   NUMBER       NOT NULL,
  order_status  VARCHAR2(30) NOT NULL,
  created_at    TIMESTAMP(6) DEFAULT SYSTIMESTAMP NOT NULL,
  CONSTRAINT pk_core_order PRIMARY KEY (order_id),
  CONSTRAINT fk_core_order_customer
    FOREIGN KEY (customer_id)
    REFERENCES core_customer(customer_id),
  CONSTRAINT chk_core_order_status
    CHECK (order_status IN ('NEW','PAID','SHIPPED','CANCELLED'))
);

-- Relational query: projection + selection + join
SELECT c.customer_id,
       c.legal_name,
       o.order_id,
       o.order_status,
       o.created_at
FROM   core_customer c
JOIN   core_order o
  ON   o.customer_id = c.customer_id
WHERE  c.customer_id = :customer_id
ORDER  BY o.created_at DESC;
"""

    if "primary key" in t:
        return """
CREATE TABLE core_customer (
  customer_id   NUMBER       NOT NULL,
  legal_name    VARCHAR2(200) NOT NULL,
  created_at    TIMESTAMP(6)  DEFAULT SYSTIMESTAMP NOT NULL,
  CONSTRAINT pk_core_customer PRIMARY KEY (customer_id)
);
"""

    if "composite key" in t:
        return """
CREATE TABLE dwh_sales_fact (
  business_date DATE          NOT NULL,
  store_id      NUMBER        NOT NULL,
  sku_id        NUMBER        NOT NULL,
  net_amount    NUMBER(18,2)  NOT NULL,
  CONSTRAINT pk_dwh_sales_fact PRIMARY KEY (business_date, store_id, sku_id)
);
"""

    if "foreign key" in t:
        return """
CREATE TABLE core_order (
  order_id      NUMBER       NOT NULL,
  customer_id   NUMBER       NOT NULL,
  order_status  VARCHAR2(30) NOT NULL,
  created_at    TIMESTAMP(6) DEFAULT SYSTIMESTAMP NOT NULL,
  CONSTRAINT pk_core_order PRIMARY KEY (order_id),
  CONSTRAINT fk_core_order_customer
    FOREIGN KEY (customer_id)
    REFERENCES core_customer(customer_id)
);
"""

    if "unique" in t and "index" not in t:
        return """
ALTER TABLE iam_user_account
  ADD CONSTRAINT uq_iam_user_account_email
  UNIQUE (email);
"""

    if "not null" in t:
        return """
ALTER TABLE core_customer
  MODIFY (legal_name NOT NULL);
"""

    if "check" in t:
        return """
ALTER TABLE core_order
  ADD CONSTRAINT chk_core_order_status
  CHECK (order_status IN ('NEW','PAID','SHIPPED','CANCELLED'));
"""

    if t in {"select", "where clause", "order by", "distinct", "fetch / limit"}:
        return """
SELECT /*+ gather_plan_statistics */
       o.order_id,
       o.customer_id,
       o.order_status,
       o.created_at
FROM   core_order o
WHERE  o.created_at >= SYSTIMESTAMP - INTERVAL '7' DAY
AND    o.order_status IN ('PAID','SHIPPED')
ORDER  BY o.created_at DESC
FETCH  FIRST 50 ROWS ONLY;
"""

    if t in {"insert", "update", "delete"}:
        verb = t.upper()
        if verb == "INSERT":
            return """
INSERT INTO core_order (order_id, customer_id, order_status, created_at)
VALUES (1009001, 42, 'NEW', SYSTIMESTAMP);
"""
        if verb == "UPDATE":
            return """
UPDATE core_order
SET    order_status = 'PAID'
WHERE  order_id = 1009001;
"""
        return """
DELETE FROM core_order
WHERE  order_id = 1009001
AND    order_status = 'CANCELLED';
"""

    if "group by" in t or "having" in t or "count" in t or "sum" in t or "avg" in t:
        return """
SELECT o.customer_id,
       COUNT(*) AS order_cnt,
       SUM(ol.extended_amount) AS net_amount
FROM   core_order o
JOIN   core_order_line ol
  ON   ol.order_id = o.order_id
WHERE  o.created_at >= SYSTIMESTAMP - INTERVAL '30' DAY
GROUP  BY o.customer_id
HAVING SUM(ol.extended_amount) >= 5000
ORDER  BY net_amount DESC;
"""

    if "inner join" in t or "left join" in t or "right join" in t or "full join" in t:
        join = "JOIN"
        if "left" in t:
            join = "LEFT JOIN"
        elif "right" in t:
            join = "RIGHT JOIN"
        elif "full" in t:
            join = "FULL OUTER JOIN"
        return f"""
SELECT c.customer_id,
       c.legal_name,
       o.order_id,
       o.order_status,
       o.created_at
FROM   core_customer c
{join} core_order o
  ON   o.customer_id = c.customer_id
WHERE  c.customer_id = :customer_id
ORDER  BY o.created_at DESC;
"""

    if "self join" in t:
        return """
SELECT e.employee_id,
       e.employee_name,
       m.employee_name AS manager_name
FROM   hr_employee e
LEFT   JOIN hr_employee m
  ON   m.employee_id = e.manager_id
WHERE  e.is_active = 'Y';
"""

    if "cross join" in t:
        return """
SELECT /* cartesian product for controlled dimension expansion */
       d.business_date,
       s.store_id
FROM   dim_date d
CROSS  JOIN dim_store s
WHERE  d.business_date BETWEEN DATE '2026-01-01' AND DATE '2026-01-31'
AND    s.region_code = 'APAC';
"""

    if "subqueries" in t or "exists" in t or "in vs exists" in t or "correlated" in t:
        return """
SELECT c.customer_id,
       c.legal_name
FROM   core_customer c
WHERE  EXISTS (
  SELECT 1
  FROM   core_order o
  WHERE  o.customer_id = c.customer_id
  AND    o.order_status = 'PAID'
  AND    o.created_at >= SYSTIMESTAMP - INTERVAL '90' DAY
);
"""

    if "case" in t or "coalesce" in t or "null" in t:
        return """
SELECT o.order_id,
       CASE
         WHEN o.order_status = 'CANCELLED' THEN 'INACTIVE'
         WHEN o.order_status IN ('NEW','PAID','SHIPPED') THEN 'ACTIVE'
         ELSE 'UNKNOWN'
       END AS order_lifecycle,
       COALESCE(o.updated_at, o.created_at) AS effective_ts
FROM   core_order o
WHERE  o.created_at >= SYSTIMESTAMP - INTERVAL '30' DAY;
"""

    if "hierarchical" in t or "connect by" in t:
        return """
SELECT employee_id,
       employee_name,
       manager_id,
       LEVEL AS org_level,
       SYS_CONNECT_BY_PATH(employee_name, ' / ') AS org_path
FROM   hr_employee
START  WITH manager_id IS NULL
CONNECT BY PRIOR employee_id = manager_id;
"""

    if "row_number" in t or "rank" in t or "dense_rank" in t or "ntile" in t:
        func = "ROW_NUMBER"
        if "dense_rank" in t:
            func = "DENSE_RANK"
        elif t.strip() == "rank":
            func = "RANK"
        elif "ntile" in t:
            func = "NTILE(10)"
        return f"""
SELECT o.customer_id,
       o.order_id,
       o.created_at,
       {func} OVER (
         PARTITION BY o.customer_id
         ORDER BY o.created_at DESC
       ) AS rn
FROM   core_order o
WHERE  o.created_at >= SYSTIMESTAMP - INTERVAL '180' DAY;
"""

    if "lead" in t or "lag" in t or "first_value" in t or "last_value" in t:
        func = "LAG"
        if "lead" in t:
            func = "LEAD"
        elif "first_value" in t:
            func = "FIRST_VALUE"
        elif "last_value" in t:
            func = "LAST_VALUE"
        return f"""
SELECT customer_id,
       order_id,
       created_at,
       {func}(created_at) OVER (
         PARTITION BY customer_id
         ORDER BY created_at
       ) AS adjacent_ts
FROM   core_order;
"""

    if "index" in t:
        if "bitmap" in t:
            return """
CREATE BITMAP INDEX bix_order_status
ON core_order (order_status);
"""
        if "composite index" in t:
            return """
CREATE INDEX ix_order_customer_created
ON core_order (customer_id, created_at);
"""
        if "unique index" in t:
            return """
CREATE UNIQUE INDEX ux_user_email
ON iam_user_account (email);
"""
        if "b-tree" in t or "b tree" in t:
            return """
CREATE INDEX ix_order_created_at
ON core_order (created_at);
"""
        return """
SELECT /* index usage inspection */
       *
FROM   TABLE(DBMS_XPLAN.DISPLAY_CURSOR(NULL, NULL, 'ALLSTATS LAST +PEEKED_BINDS'));
"""

    if "execution plan" in t or "cost-based" in t or "optimizer" in t:
        return """
SELECT /*+ gather_plan_statistics */
       o.order_id,
       o.created_at
FROM   core_order o
WHERE  o.customer_id = :customer_id
AND    o.created_at >= SYSTIMESTAMP - INTERVAL '30' DAY;

SELECT *
FROM   TABLE(DBMS_XPLAN.DISPLAY_CURSOR(NULL, NULL, 'BASIC +COST +BYTES +PREDICATE'));
"""

    if "buffer cache" in t or "shared pool" in t or "library cache" in t or "result cache" in t:
        return """
SELECT namespace,
       pins,
       pinhits,
       reloads,
       invalidations
FROM   v$librarycache
ORDER  BY reloads DESC;
"""

    if "transactions" in t or "commit" in t or "rollback" in t or "savepoint" in t:
        return """
SAVEPOINT before_status_change;

UPDATE core_order
SET    order_status = 'CANCELLED'
WHERE  order_id = :order_id;

-- If downstream validation fails:
ROLLBACK TO before_status_change;

COMMIT;
"""

    if "lock" in t or "isolation" in t:
        return """
SELECT /* concurrency diagnostics */
       s.sid,
       s.serial#,
       l.type,
       l.lmode,
       l.request,
       o.object_name
FROM   v$session s
JOIN   v$lock l
  ON   l.sid = s.sid
LEFT   JOIN dba_objects o
  ON   o.object_id = l.id1
WHERE  s.username IS NOT NULL;
"""

    if "partition" in t or "materialized" in t or "flashback" in t or "sequence" in t:
        if "flashback" in t:
            return """
SELECT *
FROM   core_order
AS OF TIMESTAMP (SYSTIMESTAMP - INTERVAL '15' MINUTE)
WHERE  order_id = :order_id;
"""
        if "sequence" in t:
            return """
CREATE SEQUENCE seq_order_id
  START WITH 1000000
  INCREMENT BY 1
  CACHE 1000
  NOORDER;
"""
        if "materialized" in t:
            return """
CREATE MATERIALIZED VIEW dwh_order_daily_mv
BUILD IMMEDIATE
REFRESH FAST ON COMMIT
AS
SELECT TRUNC(created_at) AS order_day,
       COUNT(*) AS order_cnt
FROM   core_order
GROUP  BY TRUNC(created_at);
"""
        return """
CREATE TABLE txn_payment (
  payment_id   NUMBER NOT NULL,
  booked_at    DATE   NOT NULL,
  amount       NUMBER(18,2) NOT NULL
)
PARTITION BY RANGE (booked_at) (
  PARTITION p2026_01 VALUES LESS THAN (DATE '2026-02-01'),
  PARTITION p2026_02 VALUES LESS THAN (DATE '2026-03-01'),
  PARTITION pmax     VALUES LESS THAN (MAXVALUE)
);
"""

    if "pl/sql" in t or "stored" in t or "function" in t or "package" in t or "trigger" in t:
        return """
CREATE OR REPLACE PROCEDURE proc_reprice_order (
  p_order_id IN core_order.order_id%TYPE
) AS
BEGIN
  UPDATE core_order_line
  SET    extended_amount = unit_price * quantity
  WHERE  order_id = p_order_id;

  COMMIT;
END;
/
"""

    return """
SELECT 1 AS placeholder
FROM   dual;
"""


def default_input_data_for(title: str) -> str:
    t = title.lower()
    if "relational database concepts" in t:
        return """
INSERT INTO core_customer (customer_id, legal_name, created_at)
VALUES (42, 'Apex Manufacturing Pvt Ltd', SYSTIMESTAMP - INTERVAL '365' DAY);

INSERT INTO core_order (order_id, customer_id, order_status, created_at)
VALUES (1009001, 42, 'PAID', SYSTIMESTAMP - INTERVAL '2' DAY);

INSERT INTO core_order (order_id, customer_id, order_status, created_at)
VALUES (1009002, 42, 'SHIPPED', SYSTIMESTAMP - INTERVAL '1' DAY);
"""
    if "join" in t or "select" in t or "where" in t or "order by" in t or "group" in t or "window" in t:
        return """
-- Representative OLTP entities
INSERT INTO core_customer (customer_id, legal_name, created_at)
VALUES (42, 'Apex Manufacturing Pvt Ltd', SYSTIMESTAMP - INTERVAL '365' DAY);

INSERT INTO core_order (order_id, customer_id, order_status, created_at)
VALUES (1009001, 42, 'PAID', SYSTIMESTAMP - INTERVAL '2' DAY);

INSERT INTO core_order (order_id, customer_id, order_status, created_at)
VALUES (1009002, 42, 'SHIPPED', SYSTIMESTAMP - INTERVAL '1' DAY);
"""
    if "index" in t:
        return """
-- Cardinality and skew matter for index design
-- Example distribution:
--   order_status: NEW 70%, PAID 20%, SHIPPED 8%, CANCELLED 2%
"""
    if "cache" in t or "optimizer" in t or "plan" in t:
        return """
-- Assumptions:
--   - Application uses bind variables for hot SQL
--   - Stats are current for core tables and indexes
--   - Workload includes mixed OLTP + reporting
"""
    return """
-- Use your authoritative production-like dataset.
-- Focus on realistic cardinality, selectivity, and data skew.
"""


def ascii_diagram_for(title: str) -> str:
    t = title.lower()
    if "relational" in t or "tables" in t or "entity" in t or "relationship" in t:
        return text_block(
            """
+------------------+        +------------------+
| CORE_CUSTOMER    |1      *| CORE_ORDER       |
|------------------|--------|------------------|
| CUSTOMER_ID  (PK)|        | ORDER_ID    (PK) |
| LEGAL_NAME       |        | CUSTOMER_ID (FK) |
+------------------+        | ORDER_STATUS     |
                            +------------------+
"""
        )
    if "index access path" in t or "index" in t and "diagram" in t:
        return text_block(
            """
Predicate: o.customer_id = :b1 AND o.created_at >= :b2

            +-----------------------+
            |   IX_ORDER_CUST_CRAT  |
            | (customer_id,created) |
            +-----------+-----------+
                        |
                        v
               INDEX RANGE SCAN
                        |
                        v
                 TABLE ACCESS
                 BY ROWID (BATCHED)
                        |
                        v
                 CORE_ORDER rows
"""
        )
    if "buffer cache" in t or "shared pool" in t:
        return text_block(
            """
Client Session
   |
   v
Parse/Bind/Execute
   |
   +--> Shared Pool
   |      - Library Cache (SQL areas)
   |      - Data Dictionary Cache
   |
   +--> Buffer Cache
          - Cached data blocks
          - Consistent read via undo
"""
        )
    if "execution plan" in t or "optimizer" in t:
        return text_block(
            """
SQL Text
  |
  v
CBO (Cost-Based Optimizer)
  |
  +--> Statistics (table/index/column/histograms)
  +--> Transformations (predicate pushdown, subquery unnesting)
  +--> Access path + join order selection
  |
  v
Execution Plan -> Row source operations -> Results
"""
        )
    if "transactions" in t or "locking" in t or "isolation" in t:
        return text_block(
            """
Session A                 Session B
---------                 ---------
UPDATE row X
  |  (TX lock)
  v
COMMIT/ROLLBACK      SELECT row X
                          |
                          v
               Read consistency (undo) OR wait (blocking lock)
"""
        )
    return ""


def comparison_table_for(title: str) -> str:
    t = title.lower()
    if "in vs exists" in t:
        return """
| Aspect | IN | EXISTS |
|---|---|---|
| Null semantics | `IN` can be affected by NULLs in the subquery result set | `EXISTS` is boolean and avoids NULL-trap patterns |
| Typical plan shape | Semi-join after de-duplication | Semi-join with correlated probe |
| Best fit | Small, pre-aggregated lookup sets | Selective correlated predicates on indexed columns |
"""
    if "index vs full scan" in t:
        return """
| Dimension | Index Range Scan | Full Table Scan |
|---|---|---|
| Best when | High selectivity predicates | Large fraction of table required |
| I/O pattern | Many random reads (can be batched) | Large sequential reads (smart scan on Exadata) |
| Risk | ROWID lookups dominate latency | Large buffer churn, long-running queries |
| Mitigation | Covering indexes, clustering, partition pruning | Partitioning, parallel query, predicate pushdown |
"""
    if "bitmap" in t:
        return """
| Characteristic | B-tree | Bitmap |
|---|---|---|
| Best for | OLTP, high concurrency | DSS/warehouse, low DML |
| Predicate types | Range + equality | Low-cardinality equality + complex AND/OR |
| DML impact | Localized changes | Global bitmap locking and high maintenance cost |
"""
    if "isolation" in t:
        return """
| Isolation | Oracle behavior | Operational note |
|---|---|---|
| Read committed (default) | Statement-level read consistency via undo | Balance for OLTP; beware write skew patterns |
| Serializable | Transaction-level consistency with ORA-08177 on conflict | Use for business invariants, not general OLTP |
"""
    return ""


def page_markdown(page: Page) -> str:
    title = page.title

    # Special-case the requested sample page (make it richer and explicitly Oracle-focused).
    if page.file == "section-10/s10-plan.md":
        return s10_plan_markdown()

    diag = ascii_diagram_for(title)
    table = comparison_table_for(title)

    sql = default_sql_for(title)
    inputs = default_input_data_for(title)

    parts: list[str] = []
    parts.append(f"# {title}\n\n")

    parts.append(h2("Concept explanation"))
    parts.append(
        (
            f"{title} is an Oracle Database building block or SQL construct that has direct "
            "impact on correctness, operability, and performance under production workload. "
            "Treat it as a contract between the data model, the optimizer, and application behavior "
            "(bind patterns, concurrency, and data distribution).\n\n"
            "In enterprise systems, database behavior must be predictable under growth and failure modes "
            "(hot keys, skew, plan drift, cache pressure, and lock contention). The goal of this reference is "
            "to document the intent and operational consequences, not just syntax.\n\n"
        )
    )

    parts.append(h2("Architecture intent"))
    parts.append(
        "Define clear, enforceable semantics at the database layer so that performance and "
        "consistency are not delegated to application code. In Oracle, this also helps the CBO "
        "choose stable access paths by aligning schema constraints, statistics, and query patterns.\n\n"
        "Operational intent should be explicit:\n\n"
        "- **Correctness boundary**: what the database guarantees (constraints, isolation, ordering)\n"
        "- **Workload shape**: OLTP vs reporting, concurrency expectations, and growth assumptions\n"
        "- **Observability**: what you will measure to prove it is behaving as designed\n\n"
    )

    if diag:
        parts.append(diag)

    if table:
        parts.append(table + "\n")

    parts.append(h2("SQL example"))
    parts.append(sql_block(sql))

    parts.append(h2("Sample input data"))
    parts.append(sql_block(inputs))

    parts.append(h2("Query execution"))
    parts.append(
        "Validate behavior using runtime evidence, not only estimated plans:\n\n"
        "- **Plan + actuals**: execute with realistic binds and inspect `DBMS_XPLAN.DISPLAY_CURSOR` using "
        "  `ALLSTATS LAST` (and `+PEEKED_BINDS` where relevant).\n"
        "- **System context**: confirm waits, CPU, and I/O via AWR/ASH and (for long SQL) SQL Monitor.\n"
        "- **Metadata correctness**: verify constraints/index definitions using `DBA_CONSTRAINTS`, "
        "  `DBA_INDEXES`, `DBA_IND_COLUMNS`, and `DBA_TAB_COLUMNS`.\n\n"
        "If the topic is performance-sensitive, capture baseline signals:\n\n"
        f"{metrics_table()}\n"
    )

    parts.append(h2("Output"))
    parts.append(
        "Expected results include correct row sets (or constraint enforcement) and a predictable "
        "plan shape. In production, define acceptance criteria in terms of latency percentiles, "
        "consistent gets, physical reads, and concurrency behavior, not only row counts.\n\n"
        "When documenting output for enterprise use, specify:\n\n"
        "- **Functional**: correctness rules (e.g., uniqueness, referential integrity, null semantics)\n"
        "- **Operational**: plan shape expectations and key predicates\n"
        "- **Non-functional**: performance envelope and failure behavior under load\n\n"
    )

    parts.append(h2("Real enterprise use case"))
    parts.append(
        "Use this construct to enforce core domain invariants (identity, referential integrity, "
        "status transitions) and to shape SQL patterns used by services and reporting pipelines. "
        "The database remains the source of truth for correctness; application tiers focus on "
        "workflow orchestration and resiliency.\n\n"
        "Typical systems impacted:\n\n"
        "- **Payments/ledger**: high write volume, strict auditability, contention management\n"
        "- **IAM**: unique identity constraints, predictable lookup latency, safe schema evolution\n"
        "- **Order/inventory**: mixed OLTP + reporting, hot partitions, time-window access patterns\n\n"
    )

    parts.append(h2("Performance considerations"))
    parts.append(
        "Assess data volume, skew, and concurrency. In Oracle, features such as index compression, "
        "partition pruning, bind-aware cursor sharing, and buffer cache behavior can dominate "
        "observed latency. Ensure statistics are current and representative.\n\n"
        "Decision criteria that tend to separate production-grade designs from toy designs:\n\n"
        "- **Selectivity vs volume**: is the predicate selective enough for an index path?\n"
        "- **Concurrency**: will this choice amplify lock/ITL/mutex contention?\n"
        "- **Change rate**: how often do rows change (DML) and what does that imply for index maintenance and caching?\n"
        "- **Data distribution**: do histograms/extended stats matter, and are they stable?\n\n"
    )

    parts.append(h2("Query optimization notes"))
    parts.append(
        "Optimization guidance should be specific and testable:\n\n"
        "- **Sargability**: keep predicates indexable; avoid wrapping filtered columns unless you have function-based indexes.\n"
        "- **Datatype alignment**: eliminate implicit conversions that prevent index usage.\n"
        "- **Join/filter alignment**: match composite index column order to the most selective predicates and join keys.\n"
        "- **Plan stability**: use SPM for tier-1 SQL when plan regressions have unacceptable risk.\n\n"
    )

    parts.append(h2("Best practice recommendations"))
    parts.append(
        "- Standardize naming and ownership to support incident response and safe automation\n"
        "- Enforce constraints in the schema (do not rely on application-only invariants)\n"
        "- Use bind variables for hot paths; validate cursor sharing and bind sensitivity\n"
        "- Keep statistics current; treat stats strategy as part of release management\n"
        "- Operationalize observability (AWR/ASH, SQL Monitor, v$ views) and set regression gates\n"
    )

    return "".join(parts)


def s10_plan_markdown() -> str:
    title = "Query execution plan"

    parts: list[str] = []
    parts.append(f"# {title}\n\n")

    parts.append(h2("Concept explanation"))
    parts.append(
        "An execution plan is Oracle's chosen set of row-source operations used to satisfy a SQL "
        "statement: access paths (index vs scan), join methods (nested loops, hash join, merge join), "
        "join order, and filtering/aggregation steps. The plan is an artifact of both compile-time "
        "decisions (CBO) and runtime adaptivity (cursor sharing, dynamic sampling, adaptive plans in "
        "supported releases).\n\n"
    )

    parts.append(hr())

    parts.append(h2("Architecture intent"))
    parts.append(
        "Execution plans exist to translate logical SQL into efficient physical work while preserving "
        "relational semantics. Architecturally, you want plans to be:\n\n"
        "- Stable across routine change (data growth, minor stats drift)\n"
        "- Sensitive to the right variability (bind selectivity, partition pruning)\n"
        "- Observable and diagnosable (plan hash value, row-source stats, wait events)\n\n"
        "Treat plan review as part of operational readiness for critical SQL (payments, IAM, inventory, "
        "reporting).\n\n"
    )

    parts.append(
        text_block(
            """
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
"""
        )
    )

    parts.append(hr())

    parts.append(h2("SQL example"))
    parts.append(
        sql_block(
            """
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
"""
        )
    )

    parts.append(h2("Sample input data"))
    parts.append(
        sql_block(
            """
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
"""
        )
    )

    parts.append(h2("Query execution"))
    parts.append(
        "Operationally, you validate the plan in three layers:\n\n"
        "- **Compile-time shape**: `EXPLAIN PLAN` or `DBMS_XPLAN.DISPLAY_CURSOR` after execution\n"
        "- **Runtime truth**: `ALLSTATS LAST` row counts, temp usage, and elapsed time\n"
        "- **System context**: AWR/ASH, SQL Monitor (for long-running SQL), and wait profile\n\n"
        "Prefer measuring with binds that reflect real selectivity. A plan that is good for a hot customer "
        "may be poor for a cold customer, and vice versa. Oracle may maintain multiple child cursors; capture "
        "this explicitly in diagnostics.\n\n"
        "Baseline production signals to record during validation:\n\n"
        f"{metrics_table()}\n"
    )

    parts.append(hr())

    parts.append(h2("Output"))
    parts.append(
        "You should see:\n\n"
        "- Rows ordered correctly with `FETCH FIRST` applied late (after index-ordering if possible)\n"
        "- A plan that uses `INDEX RANGE SCAN` + `TABLE ACCESS BY ROWID (BATCHED)` when selective\n"
        "- Low logical I/O (`consistent gets`) relative to table size\n\n"
        "Example of the intended plan shape:\n\n"
        + text_block(
            """
SELECT STATEMENT
  SORT ORDER BY STOPKEY
    TABLE ACCESS BY INDEX ROWID BATCHED CORE_ORDER
      INDEX RANGE SCAN IX_ORDER_CUST_CREATED
"""
        )
    )

    parts.append(hr())

    parts.append(h2("Real enterprise use case"))
    parts.append(
        "A payments or order platform typically has:\n\n"
        "- Hot key patterns (VIP customers, high-volume merchants)\n"
        "- Time-window access (last N days)\n"
        "- SLA-driven pagination (top-N recent events)\n\n"
        "Execution plan discipline is how you ensure that the *same* endpoint remains predictable as volume grows. "
        "For regulated systems, you also need to demonstrate performance determinism under load tests that resemble "
        "peak-hour contention (shared pool pressure, redo generation, buffer cache churn).\n\n"
    )

    parts.append(hr())

    parts.append(h2("Performance considerations"))
    parts.append(
        "Key drivers in Oracle:\n\n"
        "- **Cardinality estimates**: stale stats, missing histograms, extended stats on correlated columns\n"
        "- **Access path efficiency**: clustering factor, index compression, leaf block density\n"
        "- **Sorting and TEMP**: `ORDER BY`, hash joins, group-by operations; watch PGA/TEMP usage\n"
        "- **Concurrency**: buffer busy waits, ITL contention, library cache mutex contention\n\n"
        "If the query is latency-critical, validate across representative binds and consider SPM for plan stability.\n\n"
    )

    parts.append(hr())

    parts.append(h2("Query optimization notes"))
    parts.append(
        "Optimization workflow:\n\n"
        "- Confirm predicate sargability (avoid `TRUNC(date_col)` on filtered columns unless function-based indexed)\n"
        "- Ensure datatype alignment (no implicit conversions)\n"
        "- Add/adjust composite indexes that match both filtering and ordering\n"
        "- Consider partitioning and **partition pruning** for time-range predicates\n"
        "- Use SQL Monitor for long-running statements to validate where time is spent\n\n"
        "Avoid blanket hinting. If hinting is required, document the business reason and protect it with SPM.\n\n"
    )

    parts.append(hr())

    parts.append(h2("Best practice recommendations"))
    parts.append(
        "- Keep object statistics current and automate with `DBMS_STATS` (including histograms where justified)\n"
        "- Use bind variables for hot SQL; validate bind-aware behavior (multiple child cursors)\n"
        "- Capture plan baselines for business-critical SQL (SPM)\n"
        "- Standardize plan inspection using `DBMS_XPLAN.DISPLAY_CURSOR` and SQL Monitor for investigations\n"
        "- Treat plan regressions as release blockers for tier-1 flows\n"
    )

    return "".join(parts)


def index_markdown() -> str:
    return (
        "# Oracle Database Reference\n\n"
        "This site is organized as a production-oriented reference for Oracle Database fundamentals, SQL, "
        "data modeling, indexing, optimization, caching, PL/SQL, transactions, and enterprise architecture.\n"
    )


def main() -> None:
    repo_root = Path(__file__).resolve().parent
    docs_root = repo_root / "docs"

    # mkdocs.yml
    (repo_root / "mkdocs.yml").write_text(mkdocs_yml(), encoding="utf-8")

    # docs/index.md (not in nav; homepage)
    docs_root.mkdir(parents=True, exist_ok=True)
    (docs_root / "index.md").write_text(index_markdown(), encoding="utf-8")

    # pages
    for section in SECTIONS:
        for page in section.pages:
            target = docs_root / page.file
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(page_markdown(page), encoding="utf-8")


if __name__ == "__main__":
    main()
