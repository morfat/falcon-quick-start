import falcon
import jsonschema

def validate_data(data,schema,format_checker=jsonschema.FormatChecker()):
	#make it to later return valid object given the properties

	read_only=[]
	write_only=[]

	try:
		jsonschema.validate(data, schema, format_checker=format_checker)
		#if above passes
		properties=schema.get('properties')
		for k,v in properties.items():
			if v.get('readOnly'):
				read_only.append(k)
			if v.get('writeOnly'):
				write_only.append(k)

		#remove items in data that are not in schema properties
		data={k:v for k,v in data.items() if properties.get(k)}
		return (data,write_only,read_only)

	except jsonschema.ValidationError as e:
		raise falcon.HTTPBadRequest('Data validation failed',description=e.message)

	


