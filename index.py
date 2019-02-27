import cherrypy
# from pymongo import MongoClient


class Root:
    @cherrypy.expose
    def index(self):
        return 'Hello, world! (lmao)'


if __name__ == '__main__':
    cherrypy.quickstart(Root(), '/')
