import cherrypy
from hashlib import sha256
from os import urandom
from pymongo.database import Database


@cherrypy.expose
class Authentication:
    def __init__(self, db: Database):
        self.users = db.users
        self.tokens = {}

    @cherrypy.tools.json_out()
    def POST(self):
        # We expect a Username and a Password header.
        headers: dict = cherrypy.request.headers
        hashed_password = sha256(headers['Password'].encode()).hexdigest()
        document = self.users.find_one({
            'password': hashed_password, 'username': headers['Username']
        })
        if document is None:
            return {'code': 401}
        token = urandom(128).hex()
        self.tokens[headers['Username']] = token
        return {'token': token}
