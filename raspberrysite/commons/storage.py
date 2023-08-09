import os
from minio import Minio
from dotenv import load_dotenv

load_dotenv()
client = Minio(
    os.environ.get('MINIO_CLIENT_IP'),
    access_key=os.environ.get('MINIO_ACCESS_KEY'),
    secret_key=os.environ.get('MINIO_SECRET_KEY'),
    secure=False,
    region=os.environ.get('MINIO_REGION')
)

def getBucket(bucket_name):
    found = client.bucket_exists(bucket_name)
    if not found:
        return False
    return True
    
def putObject(bucket_name, object_name, object_location):
    result = client.fput_object(
        bucket_name, object_name, object_location,
    )
    return result.object_name


