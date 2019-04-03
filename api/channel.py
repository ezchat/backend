import cherrypy
from pymongo.database import Database


@cherrypy.expose
class Channel:
    def __init__(self, db: Database):
        self.channels = db.channels

    @cherrypy.tools.json_out()
    @cherrypy.popargs('channel_id')
    def GET(self, channel_id):
        return self.channels.find_one({'id': channel_id})
