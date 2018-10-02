from apiGroup import ApiGroup

class Billing(ApiGroup):
    def get_client_plans(self, cid, options=None):
        path_params = {
            "cid": cid
        }
        return self.restHelpers.get("/billing/plans/client/:cid", path_params=path_params, query_params=None, options=options)


