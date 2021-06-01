import json
import datetime
import boto3


def lambda_handler(event, context):
    newsitems_table = boto3.resource('dynamodb').Table('newsitems')

    all_news = newsitems_table.scan()
    number_of_items = len(all_news['Items'])

    timestamp = str(datetime.datetime.now())
    print(f"[{timestamp}] Displaying {number_of_items} newsitems")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "data": all_news['Items']
        })
    }
