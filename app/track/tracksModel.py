from app import db, ma
from sqlalchemy.sql import func


class TracksModel(db.Model):
    __tablename__ = 'tracks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    spotify_id = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100),)
    artist = db.Column(db.String(100))

    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    #relationships
    track_id = db.Column(db.Integer)
    user = db.Relationship('UserModel', uselist=False, backpopulates='users')

    def __repr__(self):
        return f"Track: {self.name}"


class TrackSchema(ma.Schema):
    class Meta:
        fields = ['id', 'spotify_id', 'name', 'artist']
