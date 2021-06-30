from app import db
from sqlalchemy.sql import func


class TracksModel(db.Model):
    __tablename__ = 'tracks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    spotify_id = db.Column(db.String(100))
    name = db.Column(db.String(100),)
    artist = db.Column(db.String(100))

    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    #relationships
    #TODO
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel', uselist=False, back_populates='tracks')

    def __repr__(self):
        return f"Track: {self.name}"