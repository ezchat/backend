import cherrypy
from json import load
from os import path
from pymongo import MongoClient

from api.channel import Channel
from api.auth import Authenticate
from api.register import Register
from api.snowflake import Snowflake

# Read configuration.
mongo_url = 'mongodb://localhost:27017'
if path.exists('config.json'):
    mongo_url = load(open('config.json'))['MONGO_URL']

# Connect to MongoDB.
client = MongoClient(mongo_url)
cherrypy.log('Connected to MongoDB!')
db = client.ezchat

# Create a class for authenticating and another for Snowflakes.
authenticate = Authenticate(db)
snowflake = Snowflake()


# We use this to provide /users/auth and /users/register
@cherrypy.expose
class UserApi:
    def __init__(self):
        self.auth = authenticate
        self.register = Register(db, authenticate, snowflake)


class Api:
    def __init__(self):
        # API endpoints which use REST.
        self.channel = Channel(db)
        self.users = UserApi()

    @cherrypy.expose
    def index(self):
        return 'Under progress..'

    @cherrypy.expose
    def channels(self):
        return 'WIP'
