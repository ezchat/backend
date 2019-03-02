import cherrypy
from json import load
from os import path
from pymongo import MongoClient

from api.channels import Channels

# Read configuration.
mongo_url = 'mongodb://localhost:27017'
if path.exists('config.json'):
    mongo_url = load(open('config.json'))['MONGO_URL']

# Connect to MongoDB.
client = MongoClient(mongo_url)
cherrypy.log('Connected to MongoDB!')
db = client.ezchat

# Instantiate our channel system.
channels = Channels(db)


class Api:
    @cherrypy.expose
    def index(self):
        return 'Under progress..'

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.popargs('channel_id')
    def channel(self, channel_id):
        return channels.get_channel(channel_id)

    @cherrypy.expose
    def channels(self, channel_id):
        return 'WIP'
