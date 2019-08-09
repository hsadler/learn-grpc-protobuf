
# init autogenerated folder
rm -rf autogenerated/


# generate gRPC class files
python \
	-m grpc_tools.protoc \
	--proto_path=autogenerated=proto \
	--python_out=. \
	--grpc_python_out=. \
	proto/*.proto

