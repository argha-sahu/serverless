import io
import boto3
import logging
import os
from PIL import Image, ImageOps

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')
size = int(os.environ['THUMBNAIL_SIZE'])


def get_s3_image(bucket_name, key):
    response = s3_client.get_object(Bucket=bucket_name, Key=key)
    image_content = response['Body'].read()
    file = io.BytesIO(image_content)
    img = Image.open(file)
    return img


def image_to_thumbnail(image):
    return ImageOps.fit(image, (size, size), Image.ANTIALIAS)


def new_filename(key):
    key_split = key.rsplit('.', 1)
    print(key)
    print(key_split[0])
    return key_split[0] + '_thumbnail.png'


def upload_to_s3(bucket_name, key, image):
    out_thumbnail = io.BytesIO()
    image.save(out_thumbnail, format="PNG")
    contents = out_thumbnail.getvalue()
    response = s3_client.put_object(
        ACL='public-read',
        Body = contents,
        Bucket = bucket_name,
        ContentType = 'image/png',
        Key = key
    )
    print(response)
    url = '{}/{}/{}'.format(s3_client.meta.endpoint_url, bucket_name, key)
    return url


def s3_thumbnail_generator(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    logger.info('Before get S3 image')
    image = get_s3_image(bucket_name, key)
    logger.info('Getting S3 image successful')
    thumbnail = image_to_thumbnail(image)
    logger.info('Image to thumbnail complete')
    thumbnail_key = new_filename(key)
    url = upload_to_s3(bucket_name, thumbnail_key, thumbnail)
    logger.info('Upload to S3 complete')
    return url
