import cherrypy
from json import load
from os import path
from pymongo import MongoClient

from api.guild import Guild
from api.channel import Channel
from api.dm import DirectMessages
from api.auth import Authenticate
from api.register import Register
from api.helpers import Snowflake

# Read configuration.
mongo_url = 'mongodb://localhost:27017'
if path.exists('config.json'):
    mongo_url = load(open('config.json'))['MONGO_URL']

# Connect to MongoDB.
client = MongoClient(mongo_url)
cherrypy.log('Connected to MongoDB!')
db = client.ezchat

# Create a dictionary for tokens a class for generating Snowflakes.
snowflake = Snowflake()
tokens = {}

# We use this to provide /users/auth and /users/register.
@cherrypy.expose
class UserApi:
    def __init__(self):
        self.auth = Authenticate(db, tokens)
        self.register = Register(db, tokens, snowflake)


# This class provides our API endpoints.
# Each endpoint is represented by a property or method on a class.
class Api:
    def __init__(self):
        # API endpoints which use REST.
        self.channel = Channel(db)
        self.users = UserApi()
        self.guild = Guild(db)
        self.dm = DirectMessages(db)

    @cherrypy.expose
    def index(self):
        return 'Under progress..'

    @cherrypy.expose
    def channels(self):
        return 'WIP'
