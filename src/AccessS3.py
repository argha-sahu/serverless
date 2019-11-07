import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    bucket_details = s3_client.list_buckets().get('Buckets')
    bucket_name = [x.get('Name') for x in bucket_details]
    logger.info(bucket_name)
    response = {
        'statusCode': 200,
        'body': bucket_name
    }
    return response
