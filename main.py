import pymongo
from yadm import Database, Document, fields


class MyDatabase:
    client = pymongo.MongoClient('localhost', 27017)
    db = Database(client, 'test')


class Model(Document):
    __collection__ = 'cillection_name'

    field = fields.Stringfield()


class BaseAdminModel:
    db = None
    collection = None
    acl = None
    group = None
    name = None
    title = None
    actions = []

    fields = [
       ("field_name", RO())
       ("field_name", RW())
       ("field_name", RC())
    ]


