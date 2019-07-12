# learn-grpc-protobuf
Learning gRPC and protocol buffers based on [this](https://www.semantics3.com/blog/a-simplified-guide-to-grpc-in-python-6c4e25f0c506/) tutorial blog.

## Requirements
- python3
- virtualenv


# Usage

## Virtualenv

create virtual environment directory for python
```sh
virtualenv venv
```

## Spin-up Python gRPC Server

start virtualenv
```sh
source venv/bin/activate
```
install python packages
```sh
pip install -r requirements.txt
```
autogenerate gRPC classes from .proto files
```sh
source shell_scripts/gen_grpc_classes.sh
```
spin-up gRPC server
```sh
python server.py
```

## Run Client Script

in another terminal, start virtualenv
```sh
source venv/bin/activate
```
make a request to the gRPC server via the client script
```sh
python client.py
```
you should see this output:
```sh
4.0
```

## Cleanup

spin-down python gRPC server in 1st terminal
```sh
ctrl+c
```
deactivate virtualenv in both terminals
```sh
deactivate
```




