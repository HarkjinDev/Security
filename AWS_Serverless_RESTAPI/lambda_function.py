import json
import boto3

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
  return {
        'statusCode': 200,
        'body': "Hello"
  }
