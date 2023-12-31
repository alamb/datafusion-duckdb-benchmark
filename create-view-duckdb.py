#!/usr/bin/env python3

## Runs stdin as a command (like create view)
import sys
import duckdb
import timeit
import psutil

con = duckdb.connect(database="my-db.duckdb", read_only=False)

query = sys.stdin.read()

print("Set up a view over the Parquet files")

start = timeit.default_timer()
con.execute(query)
end = timeit.default_timer()
print(end - start)
