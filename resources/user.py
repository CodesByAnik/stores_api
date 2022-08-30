import sqlite3
from flask_restful import Resource, reqparse
from models.user import UsersModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('username',
        type=str,
        required=True,
        help="This field is empty"
    )

    parser.add_argument('password',
    type=str,
    required=True,
    help="This field is empty"
    )


    def post(self):
        data = UserRegister.parse.parse_args()

        connection = sqlite3.connect('data.db')
        cursr = connection.cursor()

        query = 'INSERT INTO user VALUES(NULL, ?, ?)'
        query.execute(data['username'], data['password'])

        connection.commit()
        connection.close()

        return {'message': "user has been added"}, 201
