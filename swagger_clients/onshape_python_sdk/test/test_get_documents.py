from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from ruamel.yaml import YAML
from pathlib2 import Path

yaml = YAML()
creds = yaml.load(Path("../.onshapepy"))

# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.api_key['X-API-Key'] = creds['secret_key'].encode('utf-8')
configuration.api_key_prefix['X-API-Key'] = creds['access_key'].encode('utf-8')
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration=configuration))


def test_get_documents():
    try:
        api_response = api_instance.get_documents_documents()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->documents_get: %s\n" % e)
    api_response.items()
