import os

POSTGRES_USER = os.getenv('POSTGRES_USER', 'doc_user')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'doc_password')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'postgres')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')  # Default PostgreSQL port
POSTGRES_DB = os.getenv('POSTGRES_DB', 'doc_sign')

# Construct the DATABASE_URL
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

print(DATABASE_URL)  # For testing, you can print the generated URL
    