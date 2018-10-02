from apiGroup import ApiGroup

class Applications(ApiGroup):
    def delete_app_settings(self, cid, uid, query_params=None, options=None):
        path_params = {
            "cid": cid,
            "uid": uid
        }
        return self.restHelpers.delete("/applications/clients/:cid/settings/users/:uid", path_params=path_params, query_params=query_params, options=options)

    def get_user_app_settings(self, cid, uid, options=None):
        path_params = {
            "cid": cid,
            "uid": uid
        }
        return self.restHelpers.get("/applications/clients/:cid/settings/users/:uid", path_params=path_params, query_params=None, options=options)

    def update_app_settings(self, cid, uid, body, options=None):
        path_params = {
            "cid": cid,
            "uid": uid
        }
        return self.restHelpers.post("/applications/clients/:cid/settings/users/:uid", path_params=path_params, query_params=None, body=body, options=options)


