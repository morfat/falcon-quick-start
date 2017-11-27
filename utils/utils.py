
from datetime import datetime
import jsonschema
import falcon

def current_date_time():
	return str(datetime.now())


def validate_jsonschema(schema,data):
    try:
        jsonschema.validate(data, schema, format_checker=jsonschema.FormatChecker())
        return data
    except jsonschema.ValidationError as e:
        raise falcon.HTTPBadRequest('Data validation failed',description=e.message)
