# AWS Serverless RestAPI (API Gateway + Lambda with python + DynamoDB)

## Purpose
To get the notice for mobile game when a user enter the game.

## AWS Structure
- API Gateway
- Lambda(python)
- DynamoDB

## DynamoDB
### Create Table
- Table Name : Fishing_Notice
- Key : no(string)
### Put Items
- no : 1
- message : Welcome to FishingSpot!

## API Gateway
### Create REST API
- /GetNotice
### Create POST Method
![Gateway](/AWS_Serverless_RESTAPI/Gateway1.png)
### POST deploy
![Depoly](/Security/AWS_Serverless_RESTAPI/Depoly.png)

## Lambda
### Create Lambda
### Create and connect IAM for dynamoDB
### Test Function
```
{
    "path": "/GetNotice",
    "httpMethod": "POST",
    "headers": {
        "Accept": "*/*",
        "content-type": "application/json; charset=UTF-8"
    },
    "queryStringParameters": null,
    "pathParameters": null
}
```
