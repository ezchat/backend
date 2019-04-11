import cherrypy
from datetime import datetime
from pymongo.database import Database

from api.base import Base
from api.helpers import Snowflake


@cherrypy.expose
class Guild(Base):
    def __init__(self, db: Database):
        self.guilds = db.guilds
        self.users = db.users
        self.snowflake = Snowflake()

    @cherrypy.tools.json_out()
    @cherrypy.popargs('guild_id')
    def GET(self, guild_id):
        return self.guilds.find_one({'id': guild_id})

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        # Read the token.
        token = cherrypy.request.headers['Token']
        # Validate the token.
        user: dict = self.users.find_one({'token': token})
        if user is None:
            raise cherrypy.HTTPError(401, 'Unauthorized')
        # If user has over 100 guilds, we do not allow guild creation.
        if user.__contains__('guilds') and len(user['guilds']) >= 100:
            raise cherrypy.HTTPError(403, 'User in too many guilds!')
        # Reference to parsed request body.
        data: dict = cherrypy.request.json
        # Create the guild.
        created_guild = self.guilds.insert_one({
            'id': self.snowflake.generate_snowflake(),
            'name': data['name'],
            'emojis': [],
            'features': [],
            'icon': data['icon'] if data.__contains__('icon') else '',
            'owner_id': user['id'],
            'channels': [],
            'members': [
                {
                    'user': user,
                    'roles': [],
                    'nickname': '',
                    'joined_at': datetime.utcnow().isoformat()
                }
            ],
            'default_message_notifications': data[
                'default_message_notifications'
            ] if data.__contains__(
                'default_message_notifications'
            ) else 0,
            'roles': []
        })
        # Fetch the guild.
        guild = self.guilds.find_one({'_id': created_guild.inserted_id})
        guild['_id'] = ''
        return str(guild)
