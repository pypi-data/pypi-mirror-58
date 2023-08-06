# realtime_sge

This project aims to provide real-time usage of SGE for user-defined tasks.

## Install using pip

`pip install realtime_sge-wdroz`

## Building instruction

First create a virtualenv and install the dependencies from **requirements.txt**

To compile the protobuf files, type `python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. realtime_sge/protos/*.proto`

