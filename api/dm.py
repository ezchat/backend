import cherrypy
from pymongo.database import Database

from api.base import Base


@cherrypy.expose
class DirectMessages(Base):
    def __init__(self, db: Database):
        self.direct_messages = db.direct_messages

    @cherrypy.tools.json_out()
    @cherrypy.popargs('direct_message_id')
    def GET(self, direct_message_id):
        return self.direct_messages.find_one({'id': direct_message_id})