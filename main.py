import cherrypy
from api import Api


class Root:
    @cherrypy.expose
    def index(self):
        return open('homepage/index.html', 'r').read()


if __name__ == '__main__':
    cherrypy.tree.mount(Api(), '/api')
    cherrypy.quickstart(Root(), '/', {
        '/favicon.ico': {'tools.staticfile.on': False}
    })
