from apiGroup import ApiGroup

class Companies(ApiGroup):
    def find(self, options=None):
        return self.restHelpers.get("/companies", path_params=None, query_params=None, options=options)

    def get(self, cid, options=None):
        path_params = {
            "cid": cid
        }
        return self.restHelpers.get("/companies/:cid", path_params=path_params, query_params=None, options=options)


