import cherrypy
from api import Api


# This responds to our requests for the homepage, playground, etc.
class Root:
    @cherrypy.expose
    def index(self):
        return open('homepage/index.html', 'r').read()

    @cherrypy.expose
    def playground(self):
        return open('homepage/playground.html', 'r').read()


# If this is the main file, then we intialize CherryPy.
if __name__ == '__main__':
    # For REST endpoints, we use this REST configuration to
    # allow us to respond to HTTP methods like POST.
    REST_conf = {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'tools.sessions.on': True,
        'tools.response_headers.on': True,
        'tools.response_headers.headers': [
            ('Content-Type', 'application/json')
        ]
    }
    # We mount the main page separately from the API.
    cherrypy.tree.mount(Api(), '/api', {
        '/guild': REST_conf,
        '/channel': REST_conf,
        '/users': REST_conf
    })
    cherrypy.quickstart(Root(), '/', {
        '/favicon.ico': {'tools.staticfile.on': False}
    })
