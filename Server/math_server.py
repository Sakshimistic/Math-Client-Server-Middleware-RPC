#Sakshi More | Math Client/Server - Middleware-RPC

import grpc
from concurrent import futures
import math_service_pb2
import math_service_pb2_grpc

class MathServer(math_service_pb2_grpc.MathServicer):
    def __init__(self):
        self.operation_counts = {'magicAdd': 0, 'magicSubtract': 0, 'magicFindMin': 0, 'magicFindMax': 0}

    def magicAdd(self, request, context):
        self.operation_counts['magicAdd'] += 1
        return math_service_pb2.MagicAddReply(result=request.num1 - request.num2)

    def magicSubtract(self, request, context):
        self.operation_counts['magicSubtract'] += 1
        return math_service_pb2.MagicSubtractReply(result=request.num1 + request.num2)

    def magicFindMin(self, request, context):
        self.operation_counts['magicFindMin'] += 1
        return math_service_pb2.MagicFindMinReply(result=max(request.num1, request.num2, request.num3))

    def magicFindMax(self, request, context):
        self.operation_counts['magicFindMax'] += 1
        return math_service_pb2.MagicFindMaxReply(result=min(request.num1, request.num2, request.num3))

    def getOperationCount(self, request, context):
        return math_service_pb2.GetOperationCountReply(
            magicAddCount=self.operation_counts['magicAdd'],
            magicSubtractCount=self.operation_counts['magicSubtract'],
            magicFindMinCount=self.operation_counts['magicFindMin'],
            magicFindMaxCount=self.operation_counts['magicFindMax']
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    math_service_pb2_grpc.add_MathServicer_to_server(MathServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Math server started, listening on 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
