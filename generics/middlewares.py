from utils.database import MySQL

#from .authentication import Authenticate
import falcon


class BaseMiddleWare:
    """ This is the base middleware . Can be overridedn to create others."""

    def __init__(self,):
        self._db=None
        #self._auth={} #to hold app and or user
        
    def process_request(self,req,resp):
        #self._db=MySQL() #create db connection and Db object
        #self._auth=self.authenticate(req)

        #if not (self._auth.get('app') or self._auth.get('user')):
        #    #no authetication implemented
        #    raise falcon.HTTPUnauthorized(title='Authentication not implemented',description='Authenticate app or user credentials. As per the middleware used')

        pass

    def process_resource(self,req,resp,view,params):
        print (view.login_required) #use this to check if this view needed authentication.. then apply necessary info
        view.db=self._db
        #resource.auth=self._auth

    def process_response(self,req,view,req_succeeded): #called immediately before the response is returned.
        self._db.close()
        

    def authenticate(self,request):
        """To be implemented by inheriting classes. To return app and or  user"""
        pass

    


  
class NoAuthMiddleWare(BaseMiddleWare):
    """ Use this if you inted not to use any authentications """
    def process_request(self,req,resp):
        self._db=MySQL() #create db connection and Db object
    
"""
class AppMiddleWare(BaseMiddleWare):
    def authenticate(self,request):
        authenticate=Authenticate(self.get_db())
        app_key=request.get_header('app-key',required=True)
        app_secret=request.get_header('app-secret',required=True)
        #authenticate as per given credentials
        return {'app': authenticate.app(app_key=app_key,app_secret=app_secret)}

"""

