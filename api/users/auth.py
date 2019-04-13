import cherrypy
from base64 import b64encode
from hashlib import sha256
from os import urandom
from time import time_ns
from pymongo.database import Database

from api.base import Base


# This class is used for authorizing users with tokens.
@cherrypy.expose
class Authenticate(Base):
    def __init__(self, db: Database):
        self.users = db.users

    @cherrypy.tools.json_out()
    def POST(self):
        # We expect a Username and a Password header.
        headers: dict = cherrypy.request.headers
        hashed_password = sha256(headers['Password'].encode()).hexdigest()

        # Check for a user with these credentials.
        user: dict = self.users.find_one({
            'password': hashed_password,
            '$or': [
                {'username': headers['Username']},
                {'email': headers['Username']}
            ]
        })

        # If it's not there, we go for code 401.
        if user is None:
            raise cherrypy.HTTPError(401, 'Unauthorized')

        # If the user has a stored token, then we send it.
        if 'token' in user and user['token'] != '':
            return {'token': user['token']}
        # Else we generate a token and send.
        else:
            id = str(user['id']).encode()  # Encoded ID
            epoch = b64encode(str(time_ns()).encode()).decode()  # Epoch Base64
            token = f'{b64encode(id).decode()}.{epoch}.{urandom(16).hex()}'
            # Store the token and send it.
            self.users.update_one(user, {'$set': {'token': token}})
            return {'token': token}
