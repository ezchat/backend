import cherrypy
from json import load
from os import path
from pymongo import MongoClient

# from api.guild import Guild
# from api.channel import Channel
from api.dm import DirectMessages
from api.users import Authenticate, UserMe, Register

# Read configuration.
mongo_url = 'mongodb://localhost:27017'
if path.exists('config.json'):
    mongo_url = load(open('config.json'))['MONGO_URL']

# Connect to MongoDB.
client = MongoClient(mongo_url)
cherrypy.log('Connected to MongoDB!')
db = client.ezchat

# We use this to provide /users.
@cherrypy.expose
class UserApi:
    def __init__(self):
        self.auth = Authenticate(db)
        self.register = Register(db)
        self.me = UserMe(db)


# This class provides our API endpoints.
# Each endpoint is represented by a property or method on a class.
class Api:
    def __init__(self):
        # API endpoints which use REST.
        self.users = UserApi()
        self.dm = DirectMessages(db)
        # Undeveloped.
        # self.channel = Channel(db)
        # self.guild = Guild(db)

    @cherrypy.expose
    def index(self):
        return 'Under progress..'

    @cherrypy.expose
    def channels(self):
        return 'WIP'
