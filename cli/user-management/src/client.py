import grpc
import osirisService_pb2
import osirisService_pb2_grpc
from users import add_user, roles, delete_user, update_user, get_user, get_user_id  

# Test: Users to be added
users_to_add = [
    {"name": "Tony Stark", "role": "admin"},
    {"name": "Elon Musk", "role": "developer"},
    {"name": "Jim Gordon", "role": "viewer"},
    {"name": "Stephen Curry", "role": "developer"},
    {"name": "LeBron James", "role": "viewer"},
    {"name": "Kate White", "role": "viewer"}
]

#Test: Users to delete
users_to_delete = ["Kate White"] # Using the username to delete

#Test: Users to update
user_info_update = [
    {"name": "LeBron James", "role": "developer"}
]



def run():
    # Connect to the gRPC server
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = osirisService_pb2_grpc.UserStub(channel)
        
        # Add each user to the gRPC server and store in users.py
        for user in users_to_add:
            request = osirisService_pb2.CreateUserRequest(name=user["name"])
            response = stub.CreateUser(request)
            add_user(response.user_id, response.name, user["role"])  # Use the new add_user function
            
            # Fetch the privileges based on the user's role
            privileges = roles.get(user['role'], {}).get("privileges", "No privileges")
            print(f"Added User - ID: {response.user_id}, Name: {response.name}, Role: {user['role']}, Privileges: {privileges}")


        # Deleting a user
        for name in users_to_delete:
            user_id = get_user_id(name)
            if user_id:
                request = osirisService_pb2.DeleteUserRequest(user_id=int(user_id))
                response = stub.DeleteUser(request)
                if response.success:
                    delete_user(user_id)  # Delete from local JSON
                    print(response.message)
                else:
                    print(f"Failed to delete user: {name}")

        # Get all users details
        for user in users_to_add:
            user_id = get_user_id(user["name"])  # Get user ID based on the username
            if user_id:
                request = osirisService_pb2.GetUserRequest(user_id=int(user_id))
                response = stub.GetUser(request)
                print(f"Retrieved User - ID: {response.user_id}, Name: {response.name}")


        # Update a user info()
        for update in user_info_update:
                user_id = get_user_id(update["name"])
                if user_id:
                    request = osirisService_pb2.UpdateUserRequest(user_id=int(user_id), name=update["role"])
                    response = stub.UpdateUser(request)

                    # Update locally in users.py
                    update_user(user_id, 'role', update["role"])  # Update the role to the new value
                    print(f"Updated User - ID: {response.user_id}, New Role: {update['role']}")


if __name__ == '__main__':
    run()
