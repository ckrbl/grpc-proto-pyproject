from gptest.proto.message_pb2 import SumReq

import gptest.proto.message_pb2
import gptest.proto.message_pb2_grpc
import grpc


def main():
    channel = grpc.insecure_channel('localhost:50051')  # Replace with server address
    stub = gptest.proto.message_pb2_grpc.MyServiceStub(channel)

    request = gptest.proto.message_pb2.SumReq(a=1, b=2)
    response = stub.GetSum(request)
    print("Sum:", response.c)
