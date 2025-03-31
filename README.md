# DynamoSync-A-Serverless-API-Driven-Data-Pipeline
Serverless Architecture: S3-API Gateway-Lambda-DynamoDB

Overview

This architecture is a serverless data pipeline that collects user input from a static website hosted on Amazon S3, processes it through an API Gateway integrated with AWS Lambda, and stores the data in an Amazon DynamoDB table. This approach ensures scalability, cost-effectiveness, and easy management without provisioning or maintaining servers.

Architecture Components

Amazon S3 (Static Website Hosting)

Hosts a static HTML form with JavaScript and CSS.

Allows users to enter data (ID and Value) for submission.

Amazon API Gateway

Acts as the frontend API layer that receives HTTP requests from the S3-hosted webpage.

Configured with CORS to allow cross-origin requests.

Routes the requests to AWS Lambda.

AWS Lambda (Python Function)

Processes API requests and extracts query parameters.

Validates the input data (ID and Value).

Writes the data to an Amazon DynamoDB table.

Returns success or error messages to the client.

Amazon DynamoDB

NoSQL database storing user-submitted data.

Optimized for scalability and fast access.

Lambda has the necessary IAM role permissions to perform read/write operations.

Workflow

A user accesses the static website hosted on S3.

The user enters an ID and Value and submits the form.

JavaScript sends an HTTP POST request to API Gateway with query parameters.

API Gateway triggers an AWS Lambda function.

The Lambda function parses the request and inserts the data into DynamoDB.

A response is sent back to the user confirming success or failure.

Advantages of This Architecture

Fully Serverless: No need to manage infrastructure.

Scalability: API Gateway and Lambda scale automatically.

Low Cost: Pay-per-use pricing model.

Security: IAM roles restrict access between services.

High Availability: S3, API Gateway, Lambda, and DynamoDB are managed services with built-in reliability.
