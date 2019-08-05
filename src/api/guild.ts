import { Db } from 'mongodb'
import { RequestHandler } from 'express'

export const apiGuildGET = (db: Db): RequestHandler => async (req, res) => {
  // Verify if the user exists.
  const token = req.headers['token']
  const user = await db.collection('users').findOne({ token })
  if (!user) {
    res.sendStatus(401)
    return
  }
  // Check if the user is in the guild.
  // TODO: Properly get REST parameter.
  const id = req.url.split('/').pop()
  if (!user['guilds'] || !user['guilds'].includes(id)) {
    res.sendStatus(403)
    return
  }
  // Get the guild.
  const guild = await db.collection('guilds').findOne({ id })
  if (!guild) {
    res.status(410).send('Guild was deleted!')
    return
  }
  // Send it.
  guild['_id'] = undefined
  res.send(guild)
}
/*
import cherrypy
from datetime import datetime
from pymongo.database import Database
from pymongo import ReturnDocument

from api.base import Base
from api.helpers import Snowflake

@cherrypy.expose
class Guild(Base):
    def __init__(self, db: Database):
        self.guilds = db.guilds
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
        # If user has over 100 guilds, we do not allow guild creation.
        elif user.__contains__('guilds') and len(user['guilds']) >= 100:
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
                    'id': user['id'],
                    'username': user['username'],
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
        guild: dict = self.guilds.find_one({'_id': created_guild.inserted_id})
        guild.pop('_id')
        # Join the user to the guild.
        self.users.update_one(
            {'_id': user['_id']},
            {'$push': {'guilds': guild['id']}}
        )
        return guild

    @cherrypy.tools.json_out()
    @cherrypy.popargs('guild_id')
    def DELETE(self, guild_id):
        # Read the token.
        token = cherrypy.request.headers['Token']
        # Validate the token.
        user: dict = self.users.find_one({'token': token})
        if user is None:
            raise cherrypy.HTTPError(401, 'Unauthorized')
        # Check if user is in the server.
        elif not user.__contains__(
            'guilds'
        ) or not user['guilds'].__contains__(guild_id):
            raise cherrypy.HTTPError(403, 'You cannot access this guild!')
        # Check if the guild exists.
        guild = self.guilds.find_one_and_delete({'id': guild_id})
        if guild is None:
            raise cherrypy.HTTPError(410, 'Guild was deleted!')
        # Check if user can delete the server.
        elif guild['owner_id'] != user['id']:
            raise cherrypy.HTTPError(403, 'You cannot delete this guild!')
        # Kick its members.
        for member in guild['members']:
            self.users.update_one(
                {'id': member['id']},
                {'$pull': {'guilds': guild['id']}}
            )
        # Send the guild.
        guild.pop('_id')
        return guild

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    @cherrypy.popargs('guild_id')
    def PATCH(self, guild_id):
        # Read the token.
        token = cherrypy.request.headers['Token']
        # Validate the token.
        user: dict = self.users.find_one({'token': token})
        if user is None:
            raise cherrypy.HTTPError(401, 'Unauthorized')
        # Check if user is in the server.
        elif not user.__contains__(
            'guilds'
        ) or not user['guilds'].__contains__(guild_id):
            raise cherrypy.HTTPError(403, 'You cannot access this guild!')
        # Check if the guild exists.
        guild = self.guilds.find_one({'id': guild_id})
        if guild is None:
            raise cherrypy.HTTPError(410, 'Guild was deleted!')
        # Check if user can modify the server, currently based on ownership.
        elif guild['owner_id'] != user['id']:
            raise cherrypy.HTTPError(403, 'You cannot modify this guild!')
        # Reference to parsed request body.
        data: dict = cherrypy.request.json
        # Create the guild.
        updated_guild = self.guilds.find_one_and_update(
            {'id': guild_id},
            {
                '$set': {
                    # Name.
                    'name': data['name'] if data.__contains__(
                        'name'
                    ) else guild['name'],
                    # Icon.
                    'icon': data['icon'] if data.__contains__(
                        'icon'
                    ) else guild['icon'],
                    # Owner ID.
                    'owner_id': data['owner_id'] if data.__contains__(
                        'owner_id'
                    ) else guild['owner_id'],
                    # Default user message notifications.
                    'default_message_notifications': data[
                        'default_message_notifications'
                    ] if data.__contains__(
                        'default_message_notifications'
                    ) else guild['default_message_notifications']
                }
            },
            return_document=ReturnDocument.AFTER
        )
        # Return updated guild.
        updated_guild.pop('_id')
        return updated_guild
*/
