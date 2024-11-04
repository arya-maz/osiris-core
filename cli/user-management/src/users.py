'''
  This file defines and generates a json file to store user data locally
'''

import json
import os

roles = {
    "admin": {"privileges": {"Read", "Write", "Execute"}},
    "developer": {"privileges": {"Read", "Write"}},
    "viewer": {"privileges": {"Read"}}
}

# File path to store users
USER_FILE = 'users.json'

# Load users from a JSON file if it exists
if os.path.exists(USER_FILE):
    with open(USER_FILE, 'r') as file:
        users = json.load(file)
else:
    users = {}

# Save users to a JSON file
def save_users():
    with open(USER_FILE, 'w') as file:
        json.dump(users, file)

# Show current user list
def user_list(users):
    for user_id, user_info in users.items():
        privileges = roles.get(user_info['role'], {}).get("privileges", "No privileges")  # Gets the privileges
        print(f"User ID: {user_id}, Name: {user_info['name']}, Role: {user_info['role']}, Privileges: {privileges}")

# Add a user and save to file
def add_user(user_id, name, role):
    users[user_id] = {"name": name, "role": role}
    save_users()

# Show a specific user
def get_user(userId):
    found = False # Flag to track if the user is found
    for user_id, user_info in users.items():
        if (userId == user_id):
            privileges = roles.get(user_info['role'], {}).get("privileges", "No privileges")  # Gets the privileges
            print(f"User ID: {user_id}, Name: {user_info['name']}, Role: {user_info['role']}, Privileges: {privileges}")
            found = True # Set flag to True if user is found
            break
        
    if not found: # Check if user was not found after the loop
      print(f"No user found with ID: {userId}")

# Get a user's ID by their name
def get_user_id(userName):
    for user_id, user_info in users.items():
        if user_info['name'] == userName:
            return user_id  # Return the ID if the name matches
    return None  # Return None if no user with the given name is found
 
# Delete a user
def delete_user(userId):
    if (userId in users):
        del users[userId]  # Remove the user from the dictionary
        save_users()  # Save the updated user list to the file
        print(f"User with ID: {userId} has been deleted.")
    else:
        print(f"No user found with ID: {userId}")  # Handle case where user ID is not found


# Update a user's details
def update_user(userId, field, replacementValue):
    if userId in users:
        if field in users[userId]:  # Check if the field exists in the user
            users[userId][field] = replacementValue  # Update the specified field
            save_users()  # Save the updated user list to the file
            print(f"User ID: {userId} updated. Set {field} to {replacementValue}.")
        else:
            print(f"Field '{field}' does not exist for user ID: {userId}.")
    else:
        print(f"No user found with ID: {userId}.")  # Handle case where user ID is not found


#user_list(users)
