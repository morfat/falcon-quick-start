#This contains the deployable content for the whole project

import falcon

#General
from generics.middlewares import AuthMiddleWare
from generics.handlers import api_error_handler,CustomJSONHandler

from falcon import media


#custom 
from users.urls import patterns as users_patterns


URL_PATTERNS=[users_patterns] #register all url patterns here



def get_app():
    app=falcon.API(media_type='application/json',middleware=[AuthMiddleWare(),],)
    
    #have our custom json handler here
    handlers = media.Handlers({
    'application/json': CustomJSONHandler(),
    })
    #register the custom handler here
    app.req_options.media_handlers=handlers
    app.resp_options.media_handlers=handlers
    

    #add custom error handler
    app.add_error_handler(falcon.HTTPError,handler=api_error_handler)


    #add routes
    for up in URL_PATTERNS:
        for i in up:
             app.add_route(i[0],i[1])
             #print("Link URL ",i[0],)
    
    return app



application=get_app()