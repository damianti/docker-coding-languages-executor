# Multi-Language Code Execution API

This project provides a microservice-based solution to execute code snippets in different languages including Python, Java, and Dart. It is designed to be highly scalable and provides easy extensibility for adding support to more programming languages.

## Table of Contents

- [Architecture](#architecture)
- [Services](#services)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Run](#run)
- [Contact](#contact)

## Architecture

The solution uses Docker and Flask to create language-specific services that are capable of executing code snippets. Each language has its own service (Docker container) that can be scaled independently based on demand.

## Services

- **Python Executor** : Service to execute Python code snippets.
- **Java Executor** : Service to execute Java code snippets.
- **Dart Executor** : Service to execute Dart code snippets.


## Prerequisites

- Docker
- curl or any API testing tool

## Setup

1. Clone this repository: `git clone https://github.com/Scaleup-Excellenteam/dockers-flask-damianti/tree/develop`
2. Navigate to the project directory: `cd repo`
3. Build the Docker images for each language-specific service. For example:
    ```
    docker build -t router-image router
    docker build -t python-image python-executor
    docker build -t java-image java-executor
    docker build -t dart-image dart-executor
    ```
4. Create a Docker network:
    ```
    docker network create mynetwork
    ```
5. run each executor service:
Check that the ports 5001, 5002, 5003, 5005 are free
    ```
    docker run -d --network=mynetwork --name router -p 5005:5005 router-image
    docker run -d --network=mynetwork --name python-executor -p 5001:5001 python-image
    docker run -d --network=mynetwork --name java-executor -p 5002:5002 java-image
    docker run -d --network=mynetwork --name dart-executor -p 5003:5003 dart-image
    ``` 
## Run
Now you are ready to run the  upload/execution. 
Note: in test-files you have some files to test the program

1. To upload:
    ```
   curl -X POST -F {path_to_file} http://localhost:5005/upload
   ```

2. To execute the uploaded files:
    ```
   curl http://localhost:5005/execute
   ```

---------------------
## Contact

For any questions or issues, please open an issue on GitHub or contact the maintainer at damian.tissembaum@gmail.com
