import os

POSTGRES_USER = os.getenv('POSTGRES_USER', 'doc_user')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'doc_password')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'postgres')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')  # Default PostgreSQL port
POSTGRES_DB = os.getenv('POSTGRES_DB', 'doc_sign')


# Construct the DATABASE_URL
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# AWS S3 configuration
S3_BUCKET = os.getenv("S3_BUCKET_NAME")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION")    