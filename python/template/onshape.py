from groups import *
from apiGroup import ApiGroup


class Onshape:
    """"A python wrapper for Onshape's REST API"""
    def __init__(self, oauth_access_token=None, access=None, secret=None, target="https://cad.onshape.com"):
        if oauth_access_token is not None:
            self.oauth_access_token = oauth_access_token
        else:
            self.target = target
            self.access = access
            self.secret = secret
        api_group = ApiGroup(oauth_access_token, access, secret, target)

