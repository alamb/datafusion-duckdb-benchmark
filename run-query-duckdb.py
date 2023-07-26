#!/usr/bin/env python3

import duckdb
import timeit
import psutil
import sys

query = sys.stdin.read()
print(query)

con = duckdb.connect(database="my-db.duckdb", read_only=False)
# enable parquet metadata cache
con.execute("PRAGMA enable_object_cache")

# invoke like run-duckdb-query.py 1 << "txt of q1"
query_num = sys.argv[1]

for try_num in range(3):
    start = timeit.default_timer()
    results = con.execute(query).fetchall()
    end = timeit.default_timer()
    print(end - start)

    # Append (query,iteration,time)
    with open("result.csv", "a") as myfile:
        time = (end - start)
        myfile.write("{},{},{}\n".format(query_num, try_num, time))
