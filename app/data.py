from pymongo import MongoClient
from datetime import datetime
import os

client = MongoClient(os.environ['MONGODB_URI'])


def times():
    col = client['testing']['times']
    return list(col.find())


def add_time():
    col = client['testing']['times']
    col.insert_one({'t': datetime.now()})
