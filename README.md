# ClickBench: DataFusion / DuckDB comparision scripts

This benchmark compares DataFusion to DuckDB performance with the  [ClickBench](https://github.com/ClickHouse/ClickBench) queries aganst the unmodified ClickBench parquet files.

# Results
![Result Chart](chart.png)


## Versions
* DataFusion 27.0.0
* DataFusion 28.0.0
* DuckDB 0.8.1

## Scenarios
* Single parquet file (hits.parquet)

## Download Data:
```shell
bash setup.sh
```

## Install DataFusion-CLI

Install from crates.io:
```shell
cargo install datafusion-cli --version 28.0.0
```

Or build from source

```shell
git clone https://github.com/apache/arrow-datafusion.git
cd datafusion
cargo install --path datafusion-cli
```

## Install DuckDB
```shell
python3 -m venv `pwd`/venv
source venv/bin/activate
pip install duckdb psutil
```

## Run queries
queres are run with `run-datafusion.sh` or `run-duckdb.sh`.

DuckDB:
```shell
CREATE=create-single-duckdb.sql bash run-duckdb.sh
```

DataFusion
```shell
DATAFUSION_CLI=./datafusion-cli.413eba1 CREATE=create-single-datafusion.sql bash run-datafusion.sh
```

More examples in [benchmark.sh](benchmark.sh)

# Results
Results are written into [`result.csv`](result.csv)


## Python Example

The example python script is [hash.py](hash.py)

```shell
python3 hash.py
```
