import cherrypy
from json import load
from os import path
from pymongo import MongoClient

# Read configuration.
mongo_url = 'mongodb://localhost:27017'
if path.exists('config.json'):
    mongo_url = load(open('config.json'))['MONGO_URL']

# Connect to MongoDB.
client = MongoClient(mongo_url)
cherrypy.log('Connected to MongoDB!')


class Root:
    @cherrypy.expose
    def index(self):
        return '<head><title>test</title></head><body><p>Hello, world!</p><p>\
            WIP</p></body>'

    @cherrypy.expose
    def messages(self):
        # Just testing stuff..
        return str(client.ezchat.messages.find({}).count)


if __name__ == '__main__':
    cherrypy.quickstart(Root(), '/')
