import falcon

from .models import User


#from falcon.media.validators import jsonschema

class List(object):

    def on_get(self,req,resp):
        resp.status=falcon.HTTP_200 #this is default

        #users=self.db.table('users').select()
        #users=self.db.table('users','id,email').select()
        #users=self.db.table('users').get(1)
        #users=self.db.table('users').search("first_name like '%mosoti%' ")

        #users=self.db.table('users').update(terms="first_name='ogega' ",condition="id=3")
        #users=self.db.table('users').search("first_name like '%o%' ")

        #users=self.db.table('users').insert("6,'mosoti@me.com','mogaka','F','L'")
        #users=self.db.table('users','id,email,password').insert("7,'mosoti@me.com','mogaka'")
        users=self.db.table('users').select()
        #users=self.db.table('users').delete("id=6")




        resp.media=users



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
