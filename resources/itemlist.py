import sqlite3
from flask_restful import Resource, reqparse
from models.itemmodel import ItemModel
from db import db

class Items(Resource):



    parser = reqparse.RequestParser()

    parser.add_argument('price',
    type=float,
    required=True,
    help="This feild cant be empty"
    )

    def get(self, name):
        item = ItemModel.find_item(name)
        if item:
            return item.json()

        return {'message': "ITEM NOT FOUND"}, 400




    def post(self, name):
        item = ItemModel.find_item(name)
        if item:
            return {'message': "Item already exists"}

        data = Items.parser.parse_args()

        item1 = ItemModel(name, data['price']) #assigning VALUES to class ItemModel

        try:
            item1.insert()
        except:
            return {'message': "Item failure"}, 500

        return item1.json(), 201
