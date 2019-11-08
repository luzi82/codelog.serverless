import datetime
import logging
import boto3
import io
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def run(event, context):
    BUCKET_NAME = os.environ['BUCKET_NAME']
    OBJECT_PATH = 'tmp/ECVNUVPD'

    current_time = datetime.datetime.now().time()
    function_name = context.function_name
    logger.info('XXOIOIOJ func start current_time={current_time}'.format(current_time=current_time))
    logger.info('WEDIKLOH BUCKET_NAME={BUCKET_NAME}'.format(BUCKET_NAME=BUCKET_NAME))

    s3_client = boto3.client('s3')

    with io.BytesIO(str(current_time).encode('utf8')) as bout:
        s3_client.upload_fileobj(
            Fileobj = bout,
            Bucket = BUCKET_NAME,
            Key = OBJECT_PATH,
        )

    with io.BytesIO() as bin:
        s3_client.download_fileobj(
            Fileobj = bin,
            Bucket = BUCKET_NAME,
            Key = OBJECT_PATH,
        )
        bytes = bin.getvalue()
    download_txt = bytes.decode('utf8')

    logger.info('FAHIFWMB download_txt={download_txt}'.format(download_txt=download_txt))

    s3_client.delete_object(
        Bucket = BUCKET_NAME,
        Key = OBJECT_PATH,
    )

    logger.info('PQVOXFIA delete_object done')
