from json import loads
from pymongo import MongoClient
#!/usr/bin/python3

from pymongo import MongoClient

client = MongoClient('mongodb://mmwserver:27017/')

with client:

    db = client.sample

    plumbergame = db.kafkasample.find()

    for deal in plumbergame:
        print('{0} {1}'.format(deal['plumber'],deal['number']))
