from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

api = Api(app, 
        version='1.0',
        title='Bot Facebook',
        description='Webhook Facebook Messenger',
        prefix='/api/',
        doc='/docs/')
