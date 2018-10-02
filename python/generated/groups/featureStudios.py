from apiGroup import ApiGroup

class FeatureStudios(ApiGroup):
    def create_feature_studio(self, did, wid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid
        }
        return self.restHelpers.post("/featurestudios/d/:did/w/:wid", path_params=path_params, query_params=None, body=body, options=options)

    def get_feature_studio_contents(self, did, wvm_pair, eid, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/featurestudios/d/:did/[wvm]/:wvm/e/:eid", path_params=path_params, query_params=None, options=options)

    def get_feature_studio_specs(self, did, wvm_pair, eid, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/featurestudios/d/:did/[wvm]/:wvm/e/:eid/featurespecs", path_params=path_params, query_params=None, options=options)

    def update_feature_studio_contents(self, did, wid, eid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.post("/featurestudios/d/:did/w/:wid/e/:eid", path_params=path_params, query_params=None, body=body, options=options)


