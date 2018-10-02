from apiGroup import ApiGroup

class ApplicationElements(ApiGroup):
    def commit_transaction_____deprecated__(self, did, eid, wid, body, options=None):
        path_params = {
            "did": did,
            "eid": eid,
            "wid": wid
        }
        return self.restHelpers.post("/elements/application/transaction/commit/:did/:eid/workspace/:wid", path_params=path_params, query_params=None, body=body, options=options)

    def create_element_____deprecated__(self, did, wid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid
        }
        return self.restHelpers.post("/elements/application/:did/workspace/:wid", path_params=path_params, query_params=None, body=body, options=options)

    def create_reference_____deprecated__(self, did, eid, wid, body, options=None):
        path_params = {
            "did": did,
            "eid": eid,
            "wid": wid
        }
        return self.restHelpers.post("/elements/application/references/:did/:eid/workspace/:wid", path_params=path_params, query_params=None, body=body, options=options)

    def delete_content_____deprecated__(self, did, eid, wid, options=None):
        path_params = {
            "did": did,
            "eid": eid,
            "wid": wid
        }
        return self.restHelpers.delete("/elements/application/content/:did/:eid/workspace/:wid", path_params=path_params, query_params=None, options=options)

    def delete_reference_____deprecated__(self, did, eid, wid, rid, options=None):
        path_params = {
            "did": did,
            "eid": eid,
            "wid": wid,
            "rid": rid
        }
        return self.restHelpers.delete("/elements/application/references/:did/:eid/workspace/:wid/:rid", path_params=path_params, query_params=None, options=options)

    def get_content_by_workspace_____deprecated__(self, did, eid, wid, options=None):
        path_params = {
            "did": did,
            "eid": eid,
            "wid": wid
        }
        return self.restHelpers.get("/elements/application/content/:did/:eid/workspace/:wid", path_params=path_params, query_params=None, options=options)

    def get_history_by_workspace_____deprecated__(self, did, eid, wid, options=None):
        path_params = {
            "did": did,
            "eid": eid,
            "wid": wid
        }
        return self.restHelpers.get("/elements/application/content/history/:did/:eid/workspace/:wid", path_params=path_params, query_params=None, options=options)

    def get_ids_by_workspace_____deprecated__(self, did, eid, wid, options=None):
        path_params = {
            "did": did,
            "eid": eid,
            "wid": wid
        }
        return self.restHelpers.get("/elements/application/content/ids/:did/:eid/workspace/:wid", path_params=path_params, query_params=None, options=options)

    def resolve_reference_____deprecated__(self, did, eid, wid, rid, options=None):
        path_params = {
            "did": did,
            "eid": eid,
            "wid": wid,
            "rid": rid
        }
        return self.restHelpers.get("/elements/application/references/:did/:eid/workspace/:wid/:rid", path_params=path_params, query_params=None, options=options)

    def start_transaction_____deprecated__(self, did, eid, wid, body, options=None):
        path_params = {
            "did": did,
            "eid": eid,
            "wid": wid
        }
        return self.restHelpers.post("/elements/application/transaction/:did/:eid/workspace/:wid", path_params=path_params, query_params=None, body=body, options=options)

    def update_element_____deprecated__(self, did, eid, wid, body, options=None):
        path_params = {
            "did": did,
            "eid": eid,
            "wid": wid
        }
        return self.restHelpers.post("/elements/application/content/:did/:eid/workspace/:wid", path_params=path_params, query_params=None, body=body, options=options)

    def update_reference_____deprecated__(self, did, eid, wid, rid, body, options=None):
        path_params = {
            "did": did,
            "eid": eid,
            "wid": wid,
            "rid": rid
        }
        return self.restHelpers.post("/elements/application/references/:did/:eid/workspace/:wid/:rid", path_params=path_params, query_params=None, body=body, options=options)


