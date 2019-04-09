import cherrypy


@cherrypy.expose
class Base:
    def OPTIONS(self):
        # Abbreviations.
        req = cherrypy.serving.request
        res = cherrypy.serving.response
        allowed_methods = 'GET, POST, PATCH, PUT, DELETE, HEAD, OPTIONS'
        allowed_headers = 'Origin, X-Requested-With, Content-Type,\
        Accept, Username, Password, Token'
        # Setup response.
        res.headers['Access-Control-Allow-Origin'] = req.headers['Origin']
        res.headers['Access-Control-Allow-Methods'] = allowed_methods
        res.headers['Access-Control-Allow-Max-Age'] = '86400'
        res.headers['Access-Control-Allow-Headers'] = allowed_headers
