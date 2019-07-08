import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc


# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

# create a valid request message
number = calculator_pb2.Number(value=16)

# make call to server
res = stub.SquareRoot(number)


print(res.value)

