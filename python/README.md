# Onsnake
A Python wrapper around Onshape's REST API.

Works with Python 2.7+

## Getting Started
The only dependencies for this project are [requests](http://docs.python-requests.org/en/master/) and
[requests-toolbelt](https://pypi.org/project/requests-toolbelt/) which can be installed via
[pip](https://pypi.org/project/pip/).


To authenticate requests, we need either an API key pair or an OAuth bearer token. If you're not specifically 
setting out to create an application and go through the whole OAuth dance, I would recommend using your existing
key pair or getting one from [Onshape's Dev Portal](https://dev-portal.onshape.com/). You should copy those keys
into a file that looks like this:

```
keys = {
    "access": "therandomstringofcharactersthatisyouraccesskey",
    "secret": "therandomstringofcharactersthatisyoursecretkey"
}
```
__Do not__ share or commit this file.

You then can create an instance of the `Onshape` object by doing something like:
```
from onshape import Onshape
from yourKeysFile import keys

onshape = Onshape(access=keys["access"], secret=keys["secret"]))
```
For an OAuth bearer token it's very similar:
```
from onshape import Onshape

onshape = Onshape(oauth_access_token="yourOauthAccessToken")
```
 

## Usage

All return values from the methods of this library are Python
[requests](http://docs.python-requests.org/en/master/) objects. See the documentation for more details.
The following examples assume you've named your instance of the Onshape class as `onshape`.

#### making requests

```
# Get your documents
onshape.documents.get_documents()

# Make the same request with query parameters to filter to your recent docs
onshape.documents.get_documents({ "filter": 5 })

# Create a document
self.onshape.documents.create_document(body={
            "name": "my new document",
            "ownerId": myuserid, # user ID can be gotten from a call to users.get_session_info()
            "ownerType": "0",
            "betaCapabilityIds": [],
            "isPublic": True
        })

# Upload a file as an element in a document
onshape.blob_elements.upload_file_create_element(someDocumentId,
                                                 someWorkspaceId,
                                                 body={
                                                     "file_path": "some/file/path"
                                                 })

# Delete that file you just uploaded
onshape.elements.delete_element(someDocumentId,
                                someWorkspaceId,
                                theElementIdOfWhatYouJustCreated)
```
Sometimes a path parameter for the request could be for different things. E.g. getting an
element list in a document requires either a `workspace`, `version`, or `microversion`. In 
that case, the argument will be `wvmPair` and you must pass a tuple of `("option", argument)`.
In practice this looks like:
```
onshape.documents.get_element_list(someDocumentId, ("w", someWorkspaceId))
```


## Other Notes
For Onshape's API documentation you must go to [Onshape's Dev Portal](https://dev-portal.onshape.com/)
and sign the Dev Agreement. Next, visit [Onshape's App Store](https://appstore.onshape.com/) and
search for `Api Explorer` and add that to any document.
