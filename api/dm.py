# from api.helpers import Snowflake
# from pymongo import ReturnDocument
# from datetime import datetime
import cherrypy
from pymongo.database import Database

from api.base import Base


@cherrypy.expose
class DirectMessages(Base):
    def __init__(self, db: Database):
        self.users = db.users
        self.direct_messages = db.direct_messages

    @cherrypy.tools.json_out()
    @cherrypy.popargs('dm_id')
    def GET(self, dm_id):
        # Read the token.
        token = cherrypy.request.headers['Token']
        # Validate the token.
        user: dict = self.users.find_one({'token': token})
        if user is None:
            raise cherrypy.HTTPError(401, 'Unauthorized')
        # Check if user is in the server.
        elif not user.__contains__(
            'direct_messages'
        ) or not user['direct_messages'].__contains__(dm_id):
            raise cherrypy.HTTPError(403, 'You cannot access this guild!')
        # Check if the DM exists.
        direct_message = self.direct_messages.find_one({'id': dm_id})
        if direct_message is None:
            raise cherrypy.HTTPError(410, 'DM channel was deleted!')
        # Send the DM.
        direct_message.pop('_id')
        return direct_message
