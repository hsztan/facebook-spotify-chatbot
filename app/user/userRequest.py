from app import api
from flask_restx import fields


class UserRequest:
    @staticmethod
    def create():
        return api.model('User Create', {
            'username': fields.String('Usuario'),
            'password': fields.String('Contraseña')
        })
