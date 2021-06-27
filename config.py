from os import getenv


class Config:
    SECRET_KEY = getenv('SECRET_KEY')
