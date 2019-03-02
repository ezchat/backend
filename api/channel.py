import cherrypy
from pymongo.database import Database


class Channel:
    def __init__(self, db: Database):
        self.channels = db.channels

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.popargs('channel_id')
    def get(self, channel_id):
        return self.channels.find_one({channel_id: channel_id})
