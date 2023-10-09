#!/bin/bash
set -e

sweep_cores="${1:-single}" # single/multi

mkdir -p ../results/latest
rm -rf ../results/latest/tpch_datafusion.csv
rm -rf ../results/latest/tpch_duckdb.csv

bash ../common/run-datafusion.sh create-single-datafusion.sql queries.sql $sweep_cores ../results/latest/tpch_datafusion.csv
bash ../common/run-duckdb.sh create-single-duckdb.sql queries.sql $sweep_cores ../results/latest/tpch_duckdb.csv
