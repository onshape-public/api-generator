from apiGroup import ApiGroup

class Accounts(ApiGroup):
    def cancel_purchase(self, pid, options=None):
        path_params = {
            "pid": pid
        }
        return self.restHelpers.delete("/accounts/purchases/:pid", path_params=path_params, query_params=None, options=options)

    def cancel_purchase_new(self, aid, pid, options=None):
        path_params = {
            "aid": aid,
            "pid": pid
        }
        return self.restHelpers.delete("/accounts/:aid/purchases/:pid", path_params=path_params, query_params=None, options=options)

    def get_plan_purchases(self, planId, query_params=None, options=None):
        path_params = {
            "planId": planId
        }
        return self.restHelpers.get("/accounts/plans/:planId/purchases", path_params=path_params, query_params=query_params, options=options)

    def get_purchases(self, options=None):
        return self.restHelpers.get("/accounts/purchases", path_params=None, query_params=None, options=options)

    def consume_purchase(self, pid, body, options=None):
        path_params = {
            "pid": pid
        }
        return self.restHelpers.post("/accounts/purchases/:pid/consume", path_params=path_params, query_params=None, body=body, options=options)


