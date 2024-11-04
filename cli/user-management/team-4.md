# Technologies:
Programming Language:
- Python

# API:
- Python GRPC module
- GRPC provides low latency for fast operations, which is necessary for creating users and authorizing them.

# Database:
- MySQL
- PeeWee ORM
- We are most familiar with MySQL databases and we are also planning to use an ORM to make it work better with our python environment.

# List of assignments:
- API: Omoze and Arya
- Docker: Daniel
- Database: Kyrylo and Nifesimi
- Wrapper Functions: Alen

**Trello Board:** https://trello.com/invite/b/671af1f68bce58b9b411e3aa/ATTIfd70d003fb0142651ce733badf17586f74B1D7CF/cs490-cli-and-usermanagement

# Prerequistes:
## Installing requirements:

- Python 3.7 or higher
- `pip` version 9.0.1 or higher

```
$ python -m pip install --upgrade pip
```
- if on a linux environment or any other environment that does not allow system-owned installation with `pip`,you can use virtualenv to use `pip`.

```
$ python -m pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```

Installing `requirements.txt`:

```
 pip install -r requirements.txt 
```

## Compiling a protobuf `.proto` file extension(optional):
Consider a `.proto` file that is stored in a file structure such as:

```
├── src/
│   ├── example.py
│   └── example.proto
```
Change directory to `src`:

```
cd src
```
To compile `example.proto`:

```
$ python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. example.proto
```
result is two python files should be generated:

- `example_pb2_grpc.py`
- `example_pb2.py`

This generated files for example are than used on the server & client scripts.

# Sprint 1(Prototype API):
- For Sprint 1, the prototype API created uses mock/hardcoded data and stores this data locally in JSON file.

- 7 files were created:
    -  `osirisService.proto`: Defines the structure of the service, including the methods available and their parameters.
    - `users.py`: Defines all backend methods for user info and stores them in a JSON file.
    - `server.py`: Handles server side logic
    - `client.py`: Handles client side logic
    - `osirisService_pb2.py` and `osirisService_pb2_grpc.py`: Auto generated from compiling `osirisService.proto` file.
    - `requirements.txt`: Used to install neccessary dependencies.

### Demo
Compile `server.py`:

```
$ python3 server.py
```

The client is tested with the following sample hard-coded data for `Adding`, `Deleting`, `Updating` and `Retrieving` a user:

 ```
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
```
Compile `client.py` on a new terminal window:

```
$ python3 client.py
```

 Output:

  ```
    Added User - ID: 1, Name: Tony Stark, Role: admin, Privileges: {'Execute', 'Read', 'Write'}
    Added User - ID: 2, Name: Elon Musk, Role: developer, Privileges: {'Read', 'Write'}
    Added User - ID: 3, Name: Jim Gordon, Role: viewer, Privileges: {'Read'}
    Added User - ID: 4, Name: Stephen Curry, Role: developer, Privileges: {'Read', 'Write'}
    Added User - ID: 5, Name: LeBron James, Role: viewer, Privileges: {'Read'}
    Added User - ID: 6, Name: Kate White, Role: viewer, Privileges: {'Read'}

    User with ID: 6 has been deleted.
    User deleted successfully

    Retrieved User - ID: 1, Name: Tony Stark
    Retrieved User - ID: 2, Name: Elon Musk
    Retrieved User - ID: 3, Name: Jim Gordon
    Retrieved User - ID: 4, Name: Stephen Curry
    Retrieved User - ID: 5, Name: LeBron James

  
    User ID: 5 updated. Set role to developer.
    Updated User - ID: 5, New Role: developer
  ```

  After compiling `client.py`, a JSON file(`users.json`) is created locally to store users data.

  `users.json`:

  ```
    {"1": {"name": "Tony Stark", "role": "admin"}, "2": {"name": "Elon Musk", "role": "developer"}, "3": {"name": "Jim Gordon", "role": "viewer"}, "4": {"name": "Stephen Curry", "role": "developer"}, "5": {"name": "LeBron James", "role": "developer"}}
  ```

  