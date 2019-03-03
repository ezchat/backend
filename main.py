import cherrypy
from api import Api


class Root:
    @cherrypy.expose
    def index(self):
        return open('homepage/index.html', 'r').read()


if __name__ == '__main__':
    REST_conf = {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'tools.sessions.on': True,
        'tools.response_headers.on': True,
        'tools.response_headers.headers': [('Content-Type', 'text/plain')],
    }
    cherrypy.tree.mount(Api(), '/api', {
        '/channel': REST_conf
    })
    cherrypy.quickstart(Root(), '/', {
        '/favicon.ico': {'tools.staticfile.on': False}
    })
