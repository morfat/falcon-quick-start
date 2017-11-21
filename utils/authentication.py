import falcon
#from apps.models import App
"""
class Authenticate:
    def __init__(self,db):
        self._db=db

    def app(self,app_key,app_secret):
        #authenticate app
        app=App(self._db)
        app=app.filter(app_key=app_key,app_secret=app_secret)
        if len(app)==1:
            app=app[0]
            if not app.get('is_active'):
                raise falcon.HTTPForbidden(title='Permission Denied ',description='Your app account is inactive')

        elif len(app)>1:
            raise falcon.HTTPUnauthorized(title='Duplicate  Autheentication',description='Duplicate Authentication Occured')
        else:
            raise falcon.HTTPUnauthorized(title='Authentication Failed ',description='Valid app-key and app-secret are  needed')
        return app


"""

