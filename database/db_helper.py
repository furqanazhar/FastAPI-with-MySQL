from bson import ObjectId
from pymongo import MongoClient


class Database:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.database = self.client['ToDoNotes']

    async def insert_row(self, collection, data):
        _id = self.database[collection].insert(data)
        return self.database[collection].find_one({'_id': _id}, {'_id': False})

    async def get_row_by_id(self, collection, _id):
        return list(self.database[collection].find({'_id': ObjectId(_id)}, {'_id': 0}))

    async def get_all_rows(self, collection):
        return list(self.database[collection].find({}, {'_id': 0}))
