def api_error_handler(exception,req,resp,params):
    
    #req.log_error(exception.description) #logs to the WSGI webserver's error stream 
    #print (exception.description)
    
    raise exception
