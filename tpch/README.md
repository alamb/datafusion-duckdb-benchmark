Scripts for running TPCH benchmarks. See [Main Readme](../README.md) for usage

Queries are run using the equivalent of:

```python
#!/usr/bin/env python3

import os
import sys
import timeit


from datafusion import SessionContext, SessionConfig, RuntimeConfig

create_queries = [
    "CREATE EXTERNAL TABLE customer STORED AS PARQUET LOCATION 'tpch_dataset/customer/part-0.parquet'",
    "CREATE EXTERNAL TABLE orders STORED AS PARQUET LOCATION 'tpch_dataset/orders/part-0.parquet'",
    "CREATE EXTERNAL TABLE lineitem STORED AS PARQUET LOCATION 'tpch_dataset/lineitem/part-0.parquet'",
    "CREATE EXTERNAL TABLE part STORED AS PARQUET LOCATION 'tpch_dataset/part/part-0.parquet'",
    "CREATE EXTERNAL TABLE partsupp STORED AS PARQUET LOCATION 'tpch_dataset/partsupp/part-0.parquet'",
    "CREATE EXTERNAL TABLE region STORED AS PARQUET LOCATION 'tpch_dataset/region/part-0.parquet'",
    "CREATE EXTERNAL TABLE supplier STORED AS PARQUET LOCATION 'tpch_dataset/supplier/part-0.parquet'",
    "CREATE EXTERNAL TABLE nation STORED AS PARQUET LOCATION 'tpch_dataset/nation/part-0.parquet'",
]

query = "SELECT COUNT(*) FROM lineitem";

# Thread Count
target_partitions = 1

config = SessionConfig().with_target_partitions(target_partitions)
ctx = SessionContext(config, RuntimeConfig())

# Create all EXTERNAL TABLES
for create_query in create_queries:
    ctx.sql(create_query)

print("Running query...")

# RUN query
start = timeit.default_timer()
result = ctx.sql(query).collect()
end = timeit.default_timer()
print("Results");
print(result)
print("Done in: {}".format(end - start))
```
