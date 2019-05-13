import cherrypy
from datetime import datetime
from pymongo.database import Database
# from pymongo import ReturnDocument

from api.base import Base
from api.helpers import Snowflake


@cherrypy.expose
class UserMeChannels(Base):
    def __init__(self, db: Database):
        self.direct_messages = db.direct_messages
        self.users = db.users
        self.snowflake = Snowflake()

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        # Read the token.
        token = cherrypy.request.headers['Token']
        # Validate the token.
        user: dict = self.users.find_one({'token': token})
        if user is None:
            raise cherrypy.HTTPError(401, 'Unauthorized')
        # Reference to parsed request body.
        data: dict = cherrypy.request.json
        # Recipient needs to exist.
        if not data.__contains__('recipient_id'):
            raise cherrypy.HTTPError(400, 'No recipient provided!')
        recipient: dict = self.users.find_one({'id': data['recipient_id']})
        if recipient is None:
            raise cherrypy.HTTPError(404, 'Recipient not found!')
        # Create the channel.
        created_dm = self.direct_messages.insert_one({
            'id': self.snowflake.generate_snowflake(),
            'owner': user['id'],
            'icon': None,
            'type': 0,
            'recipients': [
                {
                    'id': user['id'],
                    'username': user['username'],
                    'joined_at': datetime.utcnow().isoformat()
                },
                {
                    'id': recipient['id'],
                    'username': recipient['username'],
                    'joined_at': datetime.utcnow().isoformat()
                },
            ]
        })
        # Fetch the DM.
        dm: dict = self.direct_messages.find_one({
            '_id': created_dm.inserted_id
        })
        dm.pop('_id')
        # Join the users to the DM.
        self.users.update_one(
            {'_id': user['_id']},
            {'$push': {'direct_messages': dm['id']}}
        )
        self.users.update_one(
            {'_id': recipient['_id']},
            {'$push': {'direct_messages': dm['id']}}
        )
        return dm
