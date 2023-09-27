# Documentation

## Task Description
I developed a module to parse PostgreSQL queries, generate an Abstract Syntax Tree (AST), replace column names with hashed values in the AST, maintain a map of original column names to hashed column names, and rebuild the SQL query with hashed column names. Using Flask, the API is available and React.js is used to present the functionality.
For local deployment without reviewing documentation, here are the details [Local Deployment](#local-deployment).

# Table of Contents

- [Implementation Steps](#implementation-steps)
  - [Parse SQL to AST](#parse-sql-to-ast)
  - [Modify AST](#modify-ast)
  - [Rebuild SQL from modified AST](#rebuild-sql-from-modified-ast)
  - [Write Unit Tests](#write-unit-tests)
- [SQL Query Parser and Modifier Module](#sql-query-parser-and-modifier-module)
  - [Installation](#installation)
    - [Requirements](#requirements)
    - [Steps](#steps)
  - [Usage](#usage)
  - [Testing](#testing)
- [Backend](#backend)
  - [Technologies Used](#technologies-used)
  - [API Endpoints](#api-endpoints)
    - [Parse SQL](#parse-sql)
    - [Modify SQL](#modify-sql)
    - [Rebuild SQL](#rebuild-sql)
  - [Database](#database)
  - [Installation](#installation-1)
    - [Requirements](#requirements-1)
    - [Steps](#steps-1)
  - [Run the Application](#run-the-application)
  - [Testing](#testing-1)
  - [Access the API](#access-the-api)
- [Frontend](#frontend)
  - [Features](#features)
  - [Technologies Used](#technologies-used-1)
  - [Installation](#installation-2)
    - [Requirements](#requirements-2)
    - [Steps](#steps-2)
  - [Run the Application](#run-the-application-1)
- [Local Deployment Steps](#local-deployment-steps)
- [AWS Deployment Steps](#aws-deployment-steps)
  - [Create AWS Resources](#create-aws-resources)
  - [Container Registry](#container-registry)
  - [Backend Deployment](#backend-deployment)
  - [Frontend Deployment](#frontend-deployment)
  - [Environment Configuration](#environment-configuration)
  - [Security](#security)
  - [Logging and Monitoring](#logging-and-monitoring)
- [Architecture Overview](#architecture-overview)


## Implementation Steps
### Parse SQL to AST:
1. I utilize the `sqlglot` library to parse the SQL query string, resulting in the generation of an AST. I did not utilize `sqlparse` because it did not provide a distinct column definition, and `psqlparse` is no longer up-to-date.

### Modify AST:
1. While traversing the AST, I will substitute all `Column` entities (column names) with their respective hashed values.
2. Throughout this procedure, I will retain a record of the initial column names and their corresponding hashed versions.

### Rebuild SQL from modified AST:
1. Using the modified AST, I will reconstruct the SQL query string using hashed column names.

### Write Unit Tests:
1. I will write unit tests to verify the correctness of our functions.
2. Test cases will include typical SQL queries and edge cases.


## SQL Query Parser and Modifier Module

This Python module provides a command-line interface for parsing SQL queries into Abstract Syntax Trees (AST) and modifying those ASTs to rebuild SQL queries.

### Installation

#### Requirements
- Python 3.11
- sqlglot ^18.8.0
- click ^8.1.7
#### Steps
1. Clone this repository.
2. Install the required Python libraries, if not already installed:

```bash
pip install -r requirements.txt
```

### Usage

To use this script specifying the action (`parse`, `modify` or `rebuild`) and provide an SQL query.

```bash
# Parsing an SQL query into an AST
python main.py --action parse --sql-query "SELECT * FROM table_name"

# Modifying an SQL query using an existing AST
python main.py --action modify --sql-query "SELECT * FROM table_name"

# Modifying an SQL query using an existing AST
python main.py --action rebuild --sql-query "SELECT * FROM table_name"
```

### Testing

For this module, unit tests were performed for the 3 main methods with some normal, border and error cases and the hash method.
To run the tests use the following command:
```bash
python -m unittest tests/test_asthash.py
```

## Backend

The backend is tasked with parsing, modifying, and reconstructing SQL queries through the application of methods from the earlier module in similar enpoints.

### Technologies Used

- **Flask:** Flask was used in this project for building a lightweight and flexible backend API to handle PostgreSQL query parsing and modification while keeping the application simple and easy to maintain.

### API Endpoints

#### Parse SQL

- **Endpoint:** `/parse`
- **HTTP Method:** POST
- **Description:** Parses the input SQL query into an Abstract Syntax Tree (AST).
- **Request Body:**
  - `query` (string): The SQL query to be parsed.
- **Response:**
  - `ast` (object): The parsed Abstract Syntax Tree.
- **Error Response:**
  - 400 Bad Request: If there's an error in parsing the SQL query.

#### Modify SQL

- **Endpoint:** `/modify`
- **HTTP Method:** POST
- **Description:** Modifies the input SQL query by hashing column names and maintains a column mapping.
- **Request Body:**
  - `query` (string): The SQL query to be modified.
- **Response:**
  - `modified_ast` (string): The modified AST with hashed column names.
  - `mapping` (object): The mapping of original column names to hashed names.
- **Error Response:**
  - 400 Bad Request: If there's an error in parsing the SQL query.

#### Rebuild SQL

- **Endpoint:** `/rebuild`
- **HTTP Method:** POST
- **Description:** Rebuilds the SQL query from a modified AST, using the column mapping.
- **Request Body:**
  - `query` (object): The SQL query to be modified.
- **Response:**
  - `rebuilded_sql` (string): The rebuilt SQL query with original column names.
- **Error Response:**
  - 400 Bad Request: If there's an error in rebuilding the SQL query.

### Database

The backend may interact with a SQLite, to store and retrieve the column mapping.

### Installation

#### Requirements
- Python 3.11
- flask ^2.3.3
#### Steps
1. Clone this repository.
2. Install the required Python libraries, if not already installed:

```bash
pip install -r requirements.txt
```

### Run the Application

Start the backend application using the following command:

```bash
python backend/app.py
```

### Testing

To test the endpoints use the following command:
```bash
python -m unittest tests/test_backend.py
```

### Access the API

The API endpoints are now accessible locally. For example, it can be accessed using Postman at:

```bash
http://localhost:5000/<endpoint-name>
```

Replace `endpoint-name` with the actual endpoint to be accessed.

## Frontend

The frontend of the application is responsible for providing a user-friendly interface where users can input PostgreSQL SQL queries. It communicates with the backend to process these queries, display the modified SQL with hashed column names, and show the column mapping.

### Features

The frontend offers the following features:

1. **SQL Query Input:** Users can enter PostgreSQL SQL queries into a text area.

2. **Dropdown for SQL Operations:** Users can select the type of SQL operation they want to perform (e.g., parse, modify, rebuild) from a dropdown menu.

3. **Submit Button:** Clicking the "Submit" button sends the SQL query and selected operation to the backend for processing.

4. **Display Result:** The generated AST, the modified AST or the SQL with hashed column names is displayed to the user.

### Technologies Used

- **React.js:** The frontend is built using React.js, a popular JavaScript library for building user interfaces.

### Installation

#### Requirements
- react version 18.2.0
#### Steps

```bash
cd frontend
npm install
```

### Run the Application

Start the frontend of the application using the following command:

```bash
npm start
```
Now the page should be accessible through this URL:

```bash
http://localhost:3000
```

## Local Deployment

The local deployment can be accomplished by executing the following commands in the main directory of the project using docker-compose:
```bash
docker-compose build
docker-compose up
```

## AWS Deployment

#### 1. Create AWS Resources:
- **Elastic Container Service (ECS):**  Set up an ECS cluster for running Docker containers.
- **RDS (Relational Database Service) (Optional):**  (For the next step) Create an RDS instance to host the database.
#### 2. Container Registry:
- **Amazon Elastic Container Registry (ECR):**  Store the Docker container images in ECR. Create a repository for both the frontend and backend images.
- **Push Docker Images:**  Use the `docker build` and `docker push` commands to build and push the Docker images to ECR.
#### 3. Backend Deployment:
- **ECS Task Definition:**  Define an ECS task definition for the backend container. This includes specifying the container image, environment variables, and any necessary resource constraints.
- **ECS Service:**  Create an ECS service to manage and deploy the backend containers. Configure auto-scaling and load balancing if needed.
- **Security Groups and IAM Roles:**  Set up security groups and IAM roles for the ECS tasks to allow them to access resources like the RDS database.
#### 4. Frontend Deployment:
- **ECS Task Definition:**  Define another ECS task definition for the frontend container, similar to the backend.
- **ECS Service:**  Create an ECS service for the frontend.
- **Load Balancer (Optional):**  Set up an Application Load Balancer (ALB) to distribute traffic.
#### 5. Environment Configuration:
- **Environment Variables:**  Ensure that the application's environment variables are set correctly for both frontend and backend containers.
#### 6. Security:
- **Security Groups and Network ACLs:**  Configure security groups and network ACLs to control inbound and outbound traffic to the containers.
- **IAM Roles:**  Use IAM roles with the principle of least privilege to grant permissions to the containers.
#### 7. Logging and Monitoring:
- **Amazon CloudWatch:**  Set up CloudWatch for logging and monitoring. Configure log groups for both frontend and backend containers to capture logs.
- **CloudWatch Alarms:**  Create alarms to monitor key metrics and set up notifications for any issues.
### Architecture Overview:

The architecture on AWS will consist of the following components:
- **ECS Clusters:**  Separate clusters for the frontend and backend containers, allowing for independent scaling and management.
- **Elastic Load Balancer (ALB):**  If needed, an ALB for the frontend to distribute incoming traffic to multiple frontend containers.
- **Amazon RDS:**  If using a database, utilize an RDS instance for storing the application data.
- **Amazon ECR:**  Docker image repositories for storing both frontend and backend containers.
- **Amazon CloudWatch:**  For logging and monitoring of container logs and key performance metrics.
- **IAM Roles:**  IAM roles associated with the ECS tasks to grant the necessary permissions to access AWS resources securely.
- **Security Groups and Network ACLs:**  Network security groups to control inbound and outbound traffic to the containers.

This architecture ensures that the application is highly available, scalable, and can be easily monitored and managed on AWS. It is also possible to implement auto-scaling policies for ECS services to handle varying traffic levels.