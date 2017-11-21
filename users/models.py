from utils.models import Model 
import uuid



class User(Model):
    db_table='users'
   
    #for json schema
    schema_properties={
                "app_key":{
                    "default":uuid.uuid4,
                    "description":"Key",
                    "type":"string",

        
                },
                 "app_secret":{
                    "description":"App secret",
                    "type":"string",
                    "default":uuid.uuid4
        
                },
            
                "name":{
                    "description":"Unique Name of App",
                    "type":"string",

                    #custom definations
                    "required_field":True
                    
                },
                "id":{
                      "description":"Unique Identifier of the App model",
                      "type":"integer"
                      }
            }
   










    




