from generics.models import Model 

from utils.utils import current_date_time
from argon2 import PasswordHasher as ph
import uuid



class User(Model):
    db_table="users"
    properties={
        "first_name": {
            "type": "string",
            "minLength":1,
            "maxLength":100
        },
        "last_name": {
            "type": "string",
        },
        "id":{
            "type":"integer",
            "readOnly":True
        },
        "email": {
            "type": "string",
            "format":"email"
        },
        "password":{
            "type":"string",
            "writeOnly":True
        },
        "is_active":{
            "type":"boolean",
        },
        "is_superuser":{
            "type":"boolean",
        },
        "is_deleted":{
            "type":"boolean",
        },
        "is_staff":{
            "type":"boolean",

        },
        "auth_token_key": {
            "type": "string",
            "writeOnly":True
        },
        "auth_token_date_created": {
            "type": "string",
            "format":"date-time" #ther is also date
        },
    }
    required= ["first_name", "last_name","email","is_superuser","is_staff"]

    def create(self,):
        data=self.get_cleaned_data(self.read_only)
        password=self.hash_password(data.get("password","2016user"))
        auth_token_key=uuid.uuid4().hex


        id=self._db.table(self.db_table,"date_created,email,password,first_name,\
        last_name,is_superuser,is_staff,auth_token_key,auth_token_date_created,is_active\
        ").insert(current_date_time(),data.get('email'),password,
        data.get('first_name'),data.get('last_name'),data.get('is_superuser'),
        data.get('is_staff'),auth_token_key,current_date_time(),True)
        data.update({"id":id})

        return data

    def hash_password(self,password):
        return ph().hash(password)

    def verify_password(self,hash,password):
        try:
            return ph().verify(hash,password)
        except:
            return False

    def get_by_email(self,email):
        user=self._db.table(self.db_table).search(" email='%s' "%(email)).results()
        if len(user) !=1:
            return None
        del user[0]['password']
        return user[0]

    def get_by_auth_token_key(self,token):
        user=self._db.table(self.db_table).search(" auth_token_key='%s' "%(token)).results()
        if len(user) !=1:
            return None
        del user[0]['password']
        return user[0]





            


    



   













    




