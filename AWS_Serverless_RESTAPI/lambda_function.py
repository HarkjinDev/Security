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
    response = body['Item']
    
    return {
        'statusCode': 200,
        'body': response.get("message")
    }
