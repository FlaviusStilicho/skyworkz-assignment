import json
import datetime
import boto3


def lambda_handler(event, context):
    try:
        validate_and_save_newsitem(event)
    except ValueError as e:
        print(str(e))
        return{
            "statusCode": 400,
            "body": str(e),
        }

    return {
        "statusCode": 201,
    }

def validate_and_save_newsitem(event):
    title = event['queryStringParameters']['title']
    description = event['queryStringParameters']['description']
    date = event['queryStringParameters']['date']

    if not title:
        raise ValueError("News item must have a title!")
    if not description:
        raise ValueError("News item must have a description!")
    if not date:
        raise ValueError("News item must have a date!")
    ## todo: add regex for date format

    insert_item_in_dynamodb(title, description, date)

    timestamp = str(datetime.datetime.now())
    print(f"[{timestamp}] New newsitem added - title={title} description={description} date={date}}}")

def insert_item_in_dynamodb(title, description, date):
    newsitems_table = boto3.resource('dynamodb').Table('newsitems')

    newsitems_table.put_item(
        Item={
            'title': title,
            'description': description,
            'date': date
        }
    )