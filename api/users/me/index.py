import cherrypy
from pymongo.database import Database
from pymongo import ReturnDocument

from api.base import Base
from api.users.me import UserMeChannels


# This class is used for getting the user.
@cherrypy.expose
class UserMe(Base):
    def __init__(self, db: Database):
        self.users = db.users
        self.channels = UserMeChannels(db)

    @cherrypy.tools.json_out()
    def GET(self):
        # We expect a Token header.
        headers: dict = cherrypy.request.headers

        # Check for a user with these credentials.
        user: dict = self.users.find_one({
            'token': headers['Token']
        })

        # If it's not there, we go for code 401.
        if user is None:
            raise cherrypy.HTTPError(401, 'Unauthorized')

        # Remove stuff for security purposes.
        user.pop('_id')
        user.pop('token')
        return user

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PATCH(self):
        # We expect a Token header.
        headers: dict = cherrypy.request.headers

        # Check for a user with these credentials.
        user: dict = self.users.find_one({
            'token': headers['Token']
        })

        # If it's not there, we go for code 401.
        if user is None:
            raise cherrypy.HTTPError(401, 'Unauthorized')

        # Update user.
        data: dict = cherrypy.request.json
        updated_user: dict = self.users.find_one_and_update(
            {'token': headers['Token']},
            {
                '$set': {
                    'username': data['username'] if data.__contains__(
                        'username'
                    ) else user['username'],
                    'email': data['email'] if data.__contains__(
                        'email'
                    ) else user['email']
                }
            },
            return_document=ReturnDocument.AFTER
        )

        # Remove stuff for security purposes and return updated user.
        updated_user.pop('_id')
        updated_user.pop('token')
        return updated_user
