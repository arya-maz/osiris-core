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
## Installing gRPC:

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
### gRPc:
Install gRPC:
```
$ python -m pip install grpcio
```
or, for system wide installation 
```
$ sudo python -m pip install grpcio
```
## Compiling a protobuf `.proto` file extension:
Consider a `.proto` file that is stored in a file structure such as:

```
├── src/
│   ├── example.py
│   └── example.proto
```
Change directory to `src`

```
cd src
```
To compile `example.proto`:

```
$ python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. example.proto` 
```
result is two python files should be generated:

- `example_pb2_grpc.py`
- `example_pb2.py`

This generated files for example are than used on the server & client scripts.

# Sprint 1(Prototype API):
- For Sprint 1, the prototype API created uses mock/hardcoded data and stores this data locally in JSON file.

- 4 files were created:
    -  `osirisService.proto`: Defines the structure of the service, including the methods available and their parameters.
    - `users.py`: Defines all backend methods for user info and stores them in a JSON file.
    - `server.py`: Handles server side logic
    - `client.py`: Handles client side logic


  