import cherrypy
from pymongo.database import Database


@cherrypy.expose
class DM:
    def __init__(self, db: Database):
        self.DMs = db.DMs

    @cherrypy.tools.json_out()
    @cherrypy.popargs('DM_id')
    def GET(self, DM_id):
        return self.DMs.find_one({'id': DM_id})