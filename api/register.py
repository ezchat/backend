import cherrypy
from hashlib import sha256
from base64 import b64encode
from os import urandom
from time import time_ns
from pymongo.database import Database

from api.helpers import Snowflake


@cherrypy.expose
class Register:
    def __init__(self, db: Database, tokens, snowflake: Snowflake):
        self.tokens = tokens
        self.users = db.users
        self.snowflake = snowflake

    @cherrypy.tools.json_out()
    def POST(self):
        # We expect a Username, Email and a Password header.
        headers: dict = cherrypy.request.headers
        hashed_password = sha256(headers['Password'].encode()).hexdigest()

        # Create a user with a fresh Snowflake and credentials.
        res = self.users.insert_one({
            'username': headers['Username'],
            'password': hashed_password,
            'email': headers['Email'],
            'id': self.snowflake.generate_snowflake()
        })
        user = self.users.find_one({'_id': res.inserted_id})

        # Else we generate a token and send.
        id = str(user['id']).encode()  # Encoded ID
        epoch = b64encode(str(time_ns()).encode()).decode()  # Epoch Base64
        token = f'{b64encode(id).decode()}.{epoch}.{urandom(16).hex()}'

        # Store associated token.
        self.tokens[id.decode()] = token
        return {'token': token}
