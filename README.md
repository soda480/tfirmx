# tfirmx
[![python](https://img.shields.io/badge/python-3.9-teal)](https://www.python.org/downloads/)

Clone the repository and ensure the latest version of Docker is installed on your development server.

Build the Docker image:
```sh
docker image build \
-t \
tfirmx:latest .
```

Run the Docker container:
```sh
docker container run \
--rm \
-it \
-v $PWD:/code \
tfirmx:latest \
/bin/bash
```

Execute the build:
```sh
pyb -X
```

Run the app:
```sh
tfirmx
```