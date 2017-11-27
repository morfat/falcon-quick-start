from utils.database import MySQL

#from .authentication import Authenticate
import falcon

from users.models import User


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
        #print (view.login_required) #use this to check if this view needed authentication.. then apply necessary info
        if view.login_required:
            view.user=self.authenticate(req)
        view.db=self._db
    

    def process_response(self,req,view,req_succeeded): #called immediately before the response is returned.
        self._db.close()
        

    def authenticate(self,request):
        """To be implemented by inheriting classes. To return app and or  user"""
        pass

    

class AuthMiddleWare(BaseMiddleWare):
    def process_request(self,req,resp):
        self._db=MySQL() #create db connection and Db object

    def authenticate(self,request):
        user=User(self._db)
        token=request.get_header('Authorization',required=True)
        #remove the keyword 'Token' from the header
        token=token[5:].strip()
        user=user.get_by_auth_token_key(token=token)
        if not user:
            raise falcon.HTTPUnauthorized(title='Invalid Token',description='Token invalid or Expired')
        return user

