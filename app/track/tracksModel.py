from app import db, ma
from sqlalchemy.sql import func
from app.chatbot.chatbotFlow import track_added_message
from app.user.userModel import UserModel


class TracksModel(db.Model):
    __tablename__ = 'tracks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    spotify_id = db.Column(db.String(100))
    name = db.Column(db.String(100),)
    artist = db.Column(db.String(100))
    url = db.Column(db.String(100))
    image_url = db.Column(db.String(100))

    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    # relationships
    # TODO
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel', uselist=False, back_populates='tracks')

    def __repr__(self):
        return f"Track: {self.name}"

    @staticmethod
    def add_track(spotify_id, name, artist, url, image_url, recipient_id):
        # get user_id from facebook recipient id to make relationship
        user_id = UserModel.query.filter_by(
            username=recipient_id).first().id
        if TracksModel.query.filter_by(spotify_id=spotify_id, user_id=user_id).first():
            print("track already exists")  # TODO SHOULD FIX LOGIC
            return
        try:
            db.session.add(TracksModel(spotify_id=spotify_id, name=name,
                           artist=artist, url=url, image_url=image_url, user_id=user_id))
            db.session.commit()
            track_added_message(
                name=name, recipient_id=recipient_id, error=False)
        except Exception as e:
            print(e)
            db.session.rollback()
            track_added_message(
                name=name, recipient_id=recipient_id, error=True)


class TrackSchema(ma.Schema):
    class Meta:
        fields = ['id', 'spotify_id', 'name', 'artist']
