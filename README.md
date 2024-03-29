# tfirmx
[![build](https://github.com/soda480/tfirmx/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/soda480/tfirmx/actions/workflows/main.yml)
[![coverage](https://img.shields.io/badge/coverage-25.84%25-red)](https://pybuilder.io/)
[![complexity](https://img.shields.io/badge/complexity-Simple:%203-brightgreen)](https://radon.readthedocs.io/en/latest/api.html#module-radon.complexity)
[![vulnerabilities](https://img.shields.io/badge/vulnerabilities-Low-yellow)](https://pypi.org/project/bandit/)
[![python](https://img.shields.io/badge/python-3.9-teal)](https://www.python.org/downloads/)

## Execution

Ensure the latest version of Docker is installed on your server.

Build the Docker image:
```sh
docker image build -t tfirmx:latest .
```

Run the Docker container:
```sh
docker container run --rm -it tfirmx:latest
```

## Development

Clone the repository and ensure the latest version of Docker is installed on your server.

Build the Docker image:
```sh
docker image build --target build-image -t tfirmx:latest .
```

Run the Docker container:
```sh
docker container run --rm -it -v $PWD:/code tfirmx:latest /bin/bash
```

Execute the build:
```sh
pyb -X
```
