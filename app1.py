#a modified version using sqlite and jwt

from flask import Flask
from flask_restful import Api
from resources.user import UserRegister
from resources.itemlist import Items
from resources.storelist import Store

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

api.add_resource(Items, '/Items/<string:name>')
#api.add_resource(Item, '/Items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/Store/<string:name>')



if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
