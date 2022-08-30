import sqlite3
from db import db

#we will put all those classes and methods in models which do not directly interact with client. UserRegister does interact as it is resource but class user did not hence we moved it here
class UsersModel(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(5))


    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def search_username(cls, username):
        return cls.query.find_by(name=username).first()

    @classmethod
    def search_id(cls, _id):
        return cls.query.find_by(name=id).first()
