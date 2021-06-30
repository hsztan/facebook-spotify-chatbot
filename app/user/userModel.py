from app import db, ma
from sqlalchemy.sql import func
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(150))

    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    #RELATIONSHIPS
    #TODO
    tracks = db.relationship('TracksModel', back_populates='user')

    def __repr__(self):
        return f"User: {self.username}"


class UserSchema(ma.Schema):
    class Meta:
        fields = ['id', 'username', 'tracks']