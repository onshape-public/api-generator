from apiGroup import ApiGroup

class Teams(ApiGroup):
    def get(self, tid, options=None):
        path_params = {
            "tid": tid
        }
        return self.restHelpers.get("/teams/:tid", path_params=path_params, query_params=None, options=options)

    def find(self, options=None):
        return self.restHelpers.get("/teams", path_params=None, query_params=None, options=options)


