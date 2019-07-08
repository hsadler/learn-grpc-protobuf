# learn-grpc-protobuf
Learning gRPC and protocol buffers based on [this](https://www.semantics3.com/blog/a-simplified-guide-to-grpc-in-python-6c4e25f0c506/) tutorial blog.

## Requirements
- python3

## Use
install python packages
```sh
pip install -r requirements.txt
```
spin-up gRPC server
```sh
python server.py
```
make a request to the gRPC server via the client script
```sh
python client.py
```
you should see this output:
```sh
4.0
```