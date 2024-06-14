import os
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the database URL from the environment variable
database_url = os.getenv('POSTGRES_URL')

if not database_url:
    raise ValueError('Environment variable POSTGRES_URL is not set')

# Create the SQLAlchemy engine
engine = create_engine(database_url)

# Test the connection
try:
    with engine.connect() as connection:
        print("Connection to the database was successful!")
except OperationalError as e:
    print(f"Connection failed: {e}")
