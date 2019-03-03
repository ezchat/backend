import cherrypy
from json import load
from os import path
from pymongo import MongoClient

from api.channel import Channel

# Read configuration.
mongo_url = 'mongodb://localhost:27017'
if path.exists('config.json'):
    mongo_url = load(open('config.json'))['MONGO_URL']

# Connect to MongoDB.
client = MongoClient(mongo_url)
cherrypy.log('Connected to MongoDB!')
db = client.ezchat


class Api:
    def __init__(self):
        self.channel = Channel(db)

    @cherrypy.expose
    def index(self):
        return 'Under progress..'

    @cherrypy.expose
    def channels(self):
        return 'WIP'
