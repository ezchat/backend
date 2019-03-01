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
db = client.ezchat


class Root:
    @cherrypy.expose
    def index(self):
        return open('homepage/index.html', 'r').read()


if __name__ == '__main__':
    cherrypy.quickstart(Root(), '/')
