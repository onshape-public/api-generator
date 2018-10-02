from apiGroup import ApiGroup

class AppAssociativeData(ApiGroup):
    def delete_associative_data(self, did, wid, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.delete("/appelements/d/:did/w/:wid/e/:eid/associativedata", path_params=path_params, query_params=query_params, options=options)

    def get_associative_data(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/appelements/d/:did/[wvm]/:wvm/e/:eid/associativedata", path_params=path_params, query_params=query_params, options=options)

    def update_associative_data(self, did, wid, eid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.post("/appelements/d/:did/w/:wid/e/:eid/associativedata", path_params=path_params, query_params=None, body=body, options=options)


