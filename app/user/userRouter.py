from app import api
from flask_restx import Namespace, Resource
from app.user.userModel import UserModel, UserSchema

users_ns = Namespace('users', description="User Endpoint")
api.add_namespace(users_ns)


@users_ns.route('/')
class User(Resource):
    @users_ns.doc('user_all')
    def get(self):
        user_schema = UserSchema(many=False)
        query = UserModel.query.first()
        print(user_schema.dump(query))
        return user_schema.dump(query)