"""实验 01 环境探针：一行输出关键版本，便于在证据页中原生截图。"""
import platform
import sys

import boto3
import duckdb
import moto
import pyarrow

print(
    f"python {sys.version.split()[0]} | exe {sys.executable} | os {platform.platform()}"
    f" | boto3 {boto3.__version__} | moto {moto.__version__}"
    f" | duckdb {duckdb.__version__} | pyarrow {pyarrow.__version__}"
)
