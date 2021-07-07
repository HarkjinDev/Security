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

## API Gateway
### Create Method

