#Sakshi More | Math Client/Server - Middleware-RPC

import random
import grpc
import math_service_pb2
import math_service_pb2_grpc

def run():
    #Change localhost to IP address of the server
    channel = grpc.insecure_channel('localhost:50051')
    stub = math_service_pb2_grpc.MathStub(channel)

    for _ in range(1000):
        operation = random.choice(["magicAdd", "magicSubtract", "magicFindMin", "magicFindMax"])
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        num3 = random.randint(1, 100)

        if operation == "magicAdd":
            stub.magicAdd(math_service_pb2.MagicAddRequest(num1=num1, num2=num2))
        elif operation == "magicSubtract":
            stub.magicSubtract(math_service_pb2.MagicSubtractRequest(num1=num1, num2=num2))
        elif operation == "magicFindMin":
            stub.magicFindMin(math_service_pb2.MagicFindMinRequest(num1=num1, num2=num2, num3=num3))
        elif operation == "magicFindMax":
            stub.magicFindMax(math_service_pb2.MagicFindMaxRequest(num1=num1, num2=num2, num3=num3))

    operation_counts = stub.getOperationCount(math_service_pb2.GetOperationCountRequest())

    print("Operation counts:")
    print(f"magicAdd: {operation_counts.magicAddCount}")
    print(f"magicSubtract: {operation_counts.magicSubtractCount}")
    print(f"magicFindMin: {operation_counts.magicFindMinCount}")
    print(f"magicFindMax: {operation_counts.magicFindMaxCount}")

if __name__ == '__main__':
    run()
