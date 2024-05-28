import grpc
import gptest.proto.message_pb2
import gptest.proto.message_pb2_grpc
import concurrent.futures


class MyServiceImpl(gptest.proto.message_pb2_grpc.MyServiceServicer):

    def GetSum(self, request, context):
        a, b = request.a, request.b
        c = a + b
        print(f"a ({a}) + b ({b}) = c ({c})!")
        return gptest.proto.message_pb2.SumRep(c=c)

def main():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    gptest.proto.message_pb2_grpc.add_MyServiceServicer_to_server(MyServiceImpl(), server)

    server.add_insecure_port('[::]:50051')  # Replace with your desired port
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    main()
