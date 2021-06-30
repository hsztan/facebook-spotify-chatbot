from app import api, db
from flask_restx import Namespace, Resource
from json import dumps
from app.user.userModel import UserModel, UserSchema

users_ns = Namespace('users', description="User Endpoint")
api.add_namespace(users_ns)


@users_ns.route('/')
class User(Resource):
    @users_ns.doc('user_all')
    def get(self):
        user_schema = UserSchema
        user = UserModel.query.filter_by(username='test').first()
        return {
            "data": {
                "username": user.username,
                "tracks": [e.name for e in user.tracks]
            }
        }
        # print(user_schema.dump(query))
        # return user_schema.dump(query)