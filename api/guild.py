import cherrypy
from pymongo.database import Database


@cherrypy.expose
class Guild:
    def __init__(self, db: Database):
        self.guilds = db.guilds

    @cherrypy.tools.json_out()
    @cherrypy.popargs('guild_id')
    def GET(self, guild_id):
        return self.guilds.find_one({'id': guild_id})
