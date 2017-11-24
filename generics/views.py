#Consturct base views here


class BaseView(object):
	def format_media(self,response,pagination=None,message=None):
		if pagination and message:
			return {'data':response,'pagination':pagination,'message':message}
		elif pagination:
			return {'data':response,'pagination':pagination}
		elif message:
			return {'data':response,'message':message}
		else:
			return response #return as it was/is
			
		



