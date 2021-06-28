from os import getenv
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

db = getenv('DATABASE_NAME')
user = getenv('DATABASE_USER')
password = getenv('DATABASE_PASSWORD')
host = getenv('DATABASE_HOST')
port = getenv('DATABASE_PORT')

class Config:
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = getenv('SECRET_KEY')
