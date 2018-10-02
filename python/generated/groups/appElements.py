from apiGroup import ApiGroup

class AppElements(ApiGroup):
    def commit_transaction(self, did, wid, eid, tid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid,
            "tid": tid
        }
        return self.restHelpers.post("/appelements/d/:did/w/:wid/e/:eid/transactions/:tid", path_params=path_params, query_params=None, body=body, options=options)

    def create_element(self, did, wid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid
        }
        return self.restHelpers.post("/appelements/d/:did/w/:wid", path_params=path_params, query_params=None, body=body, options=options)

    def create_reference(self, did, wid, eid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.post("/appelements/d/:did/w/:wid/e/:eid/references", path_params=path_params, query_params=None, body=body, options=options)

    def delete_reference(self, did, wid, eid, rid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid,
            "rid": rid
        }
        return self.restHelpers.delete("/appelements/d/:did/w/:wid/e/:eid/references/:rid", path_params=path_params, query_params=query_params, options=options)

    def delete_content(self, did, wvm_pair, eid, sid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid,
            "sid": sid
        }
        return self.restHelpers.delete("/appelements/d/:did/[wvm]/:wvm/e/:eid/content/subelements/:sid", path_params=path_params, query_params=query_params, options=options)

    def get_sub_element_content(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/appelements/d/:did/[wvm]/:wvm/e/:eid/content", path_params=path_params, query_params=query_params, options=options)

    def get_history_by_workspace(self, did, wvm_pair, eid, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/appelements/d/:did/[wvm]/:wvm/e/:eid/content/history", path_params=path_params, query_params=None, options=options)

    def get_sub_element_ids(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/appelements/d/:did/[wvm]/:wvm/e/:eid/content/ids/", path_params=path_params, query_params=query_params, options=options)

    def resolve_reference(self, did, wvm_pair, eid, rid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid,
            "rid": rid
        }
        return self.restHelpers.get("/appelements/d/:did/[wvm]/:wvm/e/:eid/references/:rid", path_params=path_params, query_params=query_params, options=options)

    def start_transaction(self, did, wid, eid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.post("/appelements/d/:did/w/:wid/e/:eid/transactions/", path_params=path_params, query_params=None, body=body, options=options)

    def update_element(self, did, wid, eid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.post("/appelements/d/:did/w/:wid/e/:eid/content", path_params=path_params, query_params=None, body=body, options=options)

    def update_reference(self, did, wid, eid, rid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid,
            "rid": rid
        }
        return self.restHelpers.post("/appelements/d/:did/w/:wid/e/:eid/references/:rid", path_params=path_params, query_params=None, body=body, options=options)


