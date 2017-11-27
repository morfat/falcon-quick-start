import json
from falcon.media import JSONHandler
from datetime import date,datetime


def api_error_handler(exception,req,resp,params):
    
    #req.log_error(exception.description) #logs to the WSGI webserver's error stream 
    #print (exception.description)
    
    raise exception


class CustomJSONHandler(JSONHandler):
    #custom seriaze json returned to users

    def serialize(self, media):
        #here we can customize to hwo we need our formats to be.
        #print ("Serilize")
      
        return json.dumps(media, default=self.json_serial,ensure_ascii=False).encode('utf-8')

    def json_serial(self,obj):
        if isinstance(obj,(datetime,date)):
            return obj.isoformat()
        raise TypeError("Type %s is not serializable"%(type(obj)))

