import falcon

from .models import User

from generics.views  import BaseView
from utils.utils import validate_jsonschema

class List(BaseView):
    

    def on_get(self,req,resp):
        #users=self.db.table('users').select()
        #users=self.db.table('users','id,email').select()
        #users=self.db.table('users').get(1)
        #users=self.db.table('users').search("first_name like '%mosoti%' ")

        #users=self.db.table('users').update(terms="first_name='ogega' ",condition="id=3")
        #users=self.db.table('users').search("first_name like '%o%' ")

        #users=self.db.table('users').insert("6,'mosoti@me.com','mogaka','F','L'")
        #users=self.db.table('users','id,email,password').insert("7,'mosoti@me.com','mogaka'")
        #users=self.db.table('users').select()
        #users=self.db.table('users').delete("id=6")
        #users=self.db.table('users').count("id=3")

        users=User(self.db).all().paginate(url=req.uri,query_params=req.params)
        #print (users)

        #req.log_error("Sample error logged")
        
        resp.media=self.format_media(response=users[0],pagination=users[1],message="Request successful")
      
        

    def on_post(self,req,resp):
        user=User(self.db)
        user.validate(req.media) #validate data
        #create 
        created=user.create()
        #user.validated_data
        resp.media=self.format_media(response=created,message="User Created Successfully")



class Detail(BaseView):
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


class Authenticate(BaseView):
    #get user authenticated
    login_required=False


    def on_post(self,req,resp):
        #authenticate user given username and password
        schema={"properties":{"email": {"type": "string","format":"email"},
                               "password": {"type": "string"}
                               },
                "required":["email","password"]
               }

        data=validate_jsonschema(schema,req.media)
        user=User(self.db)
        user_data=user.get_by_email(email=data.get('email'))
        if not user_data:
            raise falcon.HTTPBadRequest('Invalid Credentials',description="Login Failed")
        
        #verify password
        #password_hash=user_data.pop('password')

        if not user.verify_password(hash=password_hash,password=data.get('password')):
            raise falcon.HTTPBadRequest('Invalid Credentials',description="Invalid username or password")    
        resp.media=user_data


        
