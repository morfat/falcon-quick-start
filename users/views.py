import falcon

from .models import User


#from falcon.media.validators import jsonschema

class List(object):

    def on_get(self,req,resp):
        resp.status=falcon.HTTP_200 #this is default
        #users=User(self.db).all().get()
    
        #users=User(self.db).filter(" id <=20 ").paginate(uri=req.uri)
        
        resp.media=[]



    #@jsonschema.validate(User.schema())
    def on_post(self,req,resp):
        resp.media={}




class Detail(object):

    def on_get(self,req,resp,user_id):
        #user=User(self.db).filter("id=%s"%s(user_id))
        #resp.media=user
        pass


    def on_put(self,req,resp,user_id):
        #User(self.db).update(user_id,req.media)
        pass

    def on_delete(self,req,resp,user_id):
        #
        # User(self.db).delete(user_id)
        pass
