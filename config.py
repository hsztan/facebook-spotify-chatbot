from os import getenv
from pathlib import Path
from dotenv import load_dotenv

db = getenv('DATABASE_NAME')
user = getenv('DATABASE_USER')
password = getenv('DATABASE_PASSWORD')
host = getenv('DATABASE_HOST')
port = getenv('DATABASE_PORT')

class Config:
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
