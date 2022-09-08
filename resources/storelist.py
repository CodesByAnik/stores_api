from models.store import StoreModel
from flask_restful import Resource

class Store(Resource):

    def get(self, name):
        storename = StoreModel.find_store(name)
        if storename:
            return StoreModel.json(), 200
        else:
            return {'message': 'Store not found'}, 400



    def post(self, name):
        if StoreModel.find_store(name):
            return {'message': 'Store already exists in DB'}, 201

        store = StoreModel(name)

        try:
            store.insert()
        except:
            return {'message': 'An error occurred'}, 500

        return store.json(), 201
