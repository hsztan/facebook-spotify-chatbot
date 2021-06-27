from flask_restx.reqparse import RequestParser


class ChatbotRequest:
    @staticmethod
    def webhook():
        parser = RequestParser()
        parser.add_argument('hub.mode', type=str, required=True)
        parser.add_argument('hub.challenge', type=str, required=True)
        parser.add_argument('hub.verify_token', type=str, required=True)
        return parser
