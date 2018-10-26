from __future__ import print_function
import time
import onshape_client
from onshape_client.rest import ApiException
from pprint import pprint
from ruamel.yaml import YAML
from pathlib import Path

yaml = YAML()
creds = yaml.load(Path("../.onshapepy"))

# create an instance of the API class
configuration = onshape_client.Configuration()
configuration.api_key['SECRET_KEY'] = creds['secret_key'].encode('utf-8')
configuration.api_key['ACCESS_KEY'] = creds['access_key'].encode('utf-8')
api_instance = onshape_client.DocumentsApi(onshape_client.ApiClient(configuration=configuration))


def test_get_documents():
    try:
        api_response = api_instance.get_documents()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->documents_get: %s\n" % e)
    api_response.items()
