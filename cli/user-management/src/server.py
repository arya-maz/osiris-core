import grpc
from concurrent import futures
import users #user.py file

#import genereated classes
import osirisService_pb2
import osirisService_pb2_grpc



class OsirisService(osirisService_pb2_grpc.UserServicer):  # Use `UserServicer` as generated in `osirisService_pb2_grpc`
    
    def __init__(self):
        self.users = {}  # In-memory store for users; consider persistent storage for production

    def CreateUser(self, request, context):
        user_id = len(self.users) + 1  # Simple ID generation for example
        self.users[user_id] = {"name": request.name}
        return osirisService_pb2.UserResponse(user_id=user_id, name=request.name)

    def GetUser(self, request, context):
        user = self.users.get(request.user_id)
        if not user:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User not found")
            return osirisService_pb2.UserResponse()
        return osirisService_pb2.UserResponse(user_id=request.user_id, name=user["name"])

    def UpdateUser(self, request, context):
        user = self.users.get(request.user_id)
        if not user:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User not found")
            return osirisService_pb2.UserResponse()
        self.users[request.user_id]["name"] = request.name
        return osirisService_pb2.UserResponse(user_id=request.user_id, name=request.name)

    def DeleteUser(self, request, context):
        if request.user_id not in self.users:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User not found")
            return osirisService_pb2.DeleteUserResponse(success=False, message="User not found")
        del self.users[request.user_id]
        return osirisService_pb2.DeleteUserResponse(success=True, message="User deleted successfully")


# Function to start the gRPC server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    osirisService_pb2_grpc.add_UserServicer_to_server(OsirisService(), server)  # Add OsirisService to the server
    server.add_insecure_port("[::]:50051")  # Listen on port 50051
    server.start()
    print("Server started on port 50051.")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

