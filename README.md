# DynamoSync-A-Serverless-API-Driven-Data-Pipeline
Serverless Architecture: S3-API Gateway-Lambda-DynamoDB

## Overview

This architecture is a serverless data pipeline that collects user input from a static website hosted on Amazon S3, processes it through an API Gateway integrated with AWS Lambda, and stores the data in an Amazon DynamoDB table. This approach ensures scalability, cost-effectiveness, and easy management without provisioning or maintaining servers.

## Architecture Components

#### Amazon S3 (Static Website Hosting)

  - Hosts a static HTML form with JavaScript and CSS.
  
  - Allows users to enter data (ID and Value) for submission.

   ![s3](https://github.com/user-attachments/assets/fed581a7-f8d3-48c0-b538-747361970baf)
   
   ![html](https://github.com/user-attachments/assets/231ebd7c-029c-4fbc-8037-a1b1f9a9eae2)

#### Amazon API Gateway

  - Acts as the frontend API layer that receives HTTP requests from the S3-hosted webpage.
  
  - Configured with CORS to allow cross-origin requests.
  
  - Routes the requests to AWS Lambda.
    
   ![APIgateway](https://github.com/user-attachments/assets/4f26807d-8d02-4ea0-9b5c-f1ddd53d1d0a)

#### AWS Lambda (Python Function)

  - Processes API requests and extracts query parameters.
  
  - Validates the input data (ID and Value).
  
  - Writes the data to an Amazon DynamoDB table.
  
  - Returns success or error messages to the client.
    
   ![Lambda](https://github.com/user-attachments/assets/2ffb5dfa-eaf0-43bd-bbd0-74ee6e237cef)

#### Amazon DynamoDB

  - NoSQL database storing user-submitted data.
  
  - Optimized for scalability and fast access.
  
  - Lambda has the necessary IAM role permissions to perform read/write operations.
    
   ![DynamoDB](https://github.com/user-attachments/assets/5a707fb0-5e28-4b2a-99de-1404fe4dd8c8)

## Workflow

  1. A user accesses the static website hosted on S3.
  
  2. The user enters an ID and Value and submits the form.
  
  3. JavaScript sends an HTTP POST request to API Gateway with query parameters.
  
  4. API Gateway triggers an AWS Lambda function.
  
  5. The Lambda function parses the request and inserts the data into DynamoDB.
  
  6. A response is sent back to the user confirming success or failure.
     
     ![Aws2](https://github.com/user-attachments/assets/01ed4e8d-b568-483b-a8a8-1039e1e57647)


## Advantages of This Architecture

  - Fully Serverless: No need to manage infrastructure.
  
  - Scalability: API Gateway and Lambda scale automatically.
  
  - Low Cost: Pay-per-use pricing model.
  
  - Security: IAM roles restrict access between services.
  
  - High Availability: S3, API Gateway, Lambda, and DynamoDB are managed services with built-in reliability.
