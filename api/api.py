import cherrypy
from json import load
from os import path
from pymongo import MongoClient

from api.channel import Channel
from api.auth import Authenticate

# Read configuration.
mongo_url = 'mongodb://localhost:27017'
if path.exists('config.json'):
    mongo_url = load(open('config.json'))['MONGO_URL']

# Connect to MongoDB.
client = MongoClient(mongo_url)
cherrypy.log('Connected to MongoDB!')
db = client.ezchat

# Create a class for authenticating.
authenticate = Authenticate(db)


@cherrypy.expose
class UserApi:
    def __init__(self):
        self.auth = authenticate


class Api:
    def __init__(self):
        self.channel = Channel(db)
        self.users = UserApi()

    @cherrypy.expose
    def index(self):
        return 'Under progress..'

    @cherrypy.expose
    def channels(self):
        return 'WIP'
