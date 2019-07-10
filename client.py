import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc


# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')
# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)


# TEST 'SQUARE_ROOT' ENDPOINT

# create a valid request
v = 16
number = calculator_pb2.Number(value=v)
# make call to server
res = stub.SquareRoot(number)
print('result of square_root(' + str(v) + '): ', res.value)


# TEST 'ADD' ENDPOINT

# create a valid request
n1 = 4
n2 = 5
twoNumbers = calculator_pb2.TwoNumbers(n1=n1, n2=n2)
# make call to server
res = stub.Add(twoNumbers)
print('result of add(' + str(n1) + ',' + str(n2) + '): ', res.value)
















