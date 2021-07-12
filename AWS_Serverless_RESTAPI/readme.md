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
- no : Number
- message : Notice
![Dynamodb](/AWS_Serverless_RESTAPI/Dynamodb.png)

## Lambda
### Create Lambda
```python
import json
import boto3

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    table = dynamodb.Table('Fishing_Notice')
    
    TableCounter = table.scan(Select="COUNT").get("Count")
    
    body = table.get_item(
        Key={
            "no": TableCounter
        }
    )
    items = body['Item']
    response = {
        "message" : items.get("message")
    }
    
    return {
        'statusCode': 200,
        'body': response
    }
```
### Create and connect IAM for dynamoDB
![IAM1](/AWS_Serverless_RESTAPI/IAM1.png)
![IAM2](/AWS_Serverless_RESTAPI/IAM2.png)
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
![Test1](/AWS_Serverless_RESTAPI/Test1.png)

## API Gateway
### Create REST API
- /GetNotice
### Create POST Method
![Gateway](/AWS_Serverless_RESTAPI/Gateway1.png)
### Deploy Post Method
![Deploy](/AWS_Serverless_RESTAPI/Deploy1.png)

## Result - Test
![Result](/AWS_Serverless_RESTAPI/Result.png)
