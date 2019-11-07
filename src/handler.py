import json
import time
import os


def hello(event, context):
    body = {
        "message": "UPDATED! Go Serverless v1.0! Your function executed successfully!",
        "environment:FIRST_NAME": os.environ['FIRST_NAME'],
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    time.sleep(4)
    return response
