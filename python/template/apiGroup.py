from restHelpers import RestHelpers


class ApiGroup:
    def __init__(self, *args):
        if len(args) == 1:
            self.oauth_access_token = args[0].oauth_access_token
            self.target = args[0].target
            self.access = args[0].access
            self.secret = args[0].secret
        else:
            self.oauth_access_token = args[0]
            self.access = args[1]
            self.secret = args[2]
            self.target = args[3]
        self.restHelpers = RestHelpers(self.oauth_access_token, self.access, self.secret, self.target)