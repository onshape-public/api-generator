# Won't work by default, must be moved to get correct onshape import if not installed as pip package
from onshape import Onshape
from pprint import pprint
import requests

baseUrl = 'http://localhost:3000'
testUrl = baseUrl + '/test'

keyPair = requests.get(baseUrl + '/keypair').json()
token = requests.get(baseUrl + '/access-token').json()['token']

onshapeApiKey = Onshape(access=keyPair['access'], secret=keyPair['secret'], target=testUrl)
onshapeOauth = Onshape(oauth_access_token=token, target=testUrl)

apiKeyResponse = onshapeApiKey.documents.get_documents()
oauthResponse = onshapeOauth.documents.get_documents()
pprint(apiKeyResponse.json())
pprint(oauthResponse.json())
