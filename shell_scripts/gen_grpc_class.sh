
# generate gRPC calculator class
python \
-m grpc_tools.protoc \
-I. \
--python_out=. \
--grpc_python_out=. \
calculator.proto