from apiGroup import ApiGroup

class Endpoints(ApiGroup):
    def get_endpoints(self, options=None):
        return self.restHelpers.get("/endpoints", path_params=None, query_params=None, options=options)


