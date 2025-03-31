import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ItemsTable')

def lambda_handler(event, context):
    params = event.get('queryStringParameters', {})
    
    item_id = params.get('id')
    value = params.get('value')

    if not item_id or not value:
        return {"statusCode": 400, "body": json.dumps({"message": "Missing id or value"})}

    # Update DynamoDB
    table.put_item(Item={"id": item_id, "value": value})

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Item updated successfully"})
    }
