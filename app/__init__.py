from flask import Flask
from pathlib import Path
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
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

ma = Marshmallow(db)