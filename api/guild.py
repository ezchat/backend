import cherrypy
from pymongo.database import Database

from api.base import Base


@cherrypy.expose
class Guild(Base):
    def __init__(self, db: Database):
        self.guilds = db.guilds

    @cherrypy.tools.json_out()
    @cherrypy.popargs('guild_id')
    def GET(self, guild_id):
        return self.guilds.find_one({'id': guild_id})
