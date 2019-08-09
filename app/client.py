import grpc

# import the generated classes
import autogenerated.hello_pb2 as hello_pb2
import autogenerated.hello_pb2_grpc as hello_pb2_grpc


# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a 'hello' stub (client)
stub = hello_pb2_grpc.HelloStub(channel)

# create a request
message_text = 'GAAAARRRRRYYYYYYYY!!!'
message = hello_pb2.Message(text=message_text)

# make call to server
res = stub.SayHello(message)
print(f'gRPC server response text ========> {res.text}')

