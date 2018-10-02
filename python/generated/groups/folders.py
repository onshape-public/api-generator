from apiGroup import ApiGroup

class Folders(ApiGroup):
    def get_acl(self, fid, options=None):
        path_params = {
            "fid": fid
        }
        return self.restHelpers.get("/folders/:fid/acl", path_params=path_params, query_params=None, options=options)

    def share_folder(self, fid, body, options=None):
        path_params = {
            "fid": fid
        }
        return self.restHelpers.post("/folders/:fid/share", path_params=path_params, query_params=None, body=body, options=options)

    def un_share(self, fid, eid, query_params=None, options=None):
        path_params = {
            "fid": fid,
            "eid": eid
        }
        return self.restHelpers.delete("/folders/:fid/share/:eid", path_params=path_params, query_params=query_params, options=options)


