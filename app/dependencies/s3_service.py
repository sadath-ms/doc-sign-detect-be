import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from app.config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, S3_BUCKET


# Initialize the S3 client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION,
)


# Function to upload file to S3
def upload_to_s3(file, file_key: str):
    try:
        # Upload the file to S3 bucket
        s3_client.upload_fileobj(file, S3_BUCKET, file_key)
        
        # Return the file URL
        file_url = f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{file_key}"
        return file_url

    except (NoCredentialsError, PartialCredentialsError) as e:
        raise Exception("AWS credentials not configured properly.")
    except Exception as e:
        raise Exception("Error uploading file to S3: " + str(e))