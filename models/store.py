from db import db

class Storemodel(db.Model):

    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel')

    def __init__(self, name):
        self.name = name

    def json(self, name):
        return {'name': self.name, 'items': self.items}

    @classmethod
    def find_store(cls, name):
        return cls.query.filter_by(name=name).first()

    def insert(self):
        db.session.add(self)
        db.session.commit()
