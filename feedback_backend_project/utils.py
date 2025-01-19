import boto3
import os

S3_BUCKET = "yipsresearch"

def generate_presigned_url(filename):
    """
    Generate a pre-signed URL for a file in the S3 bucket.
    """
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )
    try:
        url = s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": S3_BUCKET, "Key": f"S3_Bucket_Files/{filename}"},
            ExpiresIn=3600  # URL valid for 1 hour
        )
        return url
    except Exception as e:
        print(f"Error generating pre-signed URL: {e}")
        return None


def list_videos_in_bucket():
    """
    Retrieve a list of video filenames from the S3 bucket.
    """
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )
    try:
        response = s3_client.list_objects_v2(Bucket=S3_BUCKET, Prefix="S3_Bucket_Files/")
        if "Contents" in response:
            return [obj["Key"].split("/")[-1] for obj in response["Contents"] if obj["Key"].endswith(".mp4")]
        else:
            return []
    except Exception as e:
        print(f"Error listing videos: {e}")
        return []

##########################################


import random
import string

def generate_unique_participant_number():
    return f"PN{random.randint(10000, 99999)}"

def generate_random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))
