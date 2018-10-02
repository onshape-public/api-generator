from apiGroup import ApiGroup

class BlobElements(ApiGroup):
    def create_translation(self, did, wv_pair, eid, body, options=None):
        path_params = {
            "did": did,
            "wv": wv_pair,
            "eid": eid
        }
        return self.restHelpers.post("/blobelements/d/:did/[wv]/:wv/e/:eid/translations", path_params=path_params, query_params=None, body=body, options=options)

    def download_file_from_element(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/blobelements/d/:did/[wvm]/:wvm/e/:eid", path_params=path_params, query_params=query_params, options=options)

    def get_translation_formats(self, did, wid, eid, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.get("/blobelements/d/:did/w/:wid/e/:eid/translationformats", path_params=path_params, query_params=None, options=options)

    def upload_file_update_element(self, did, wid, eid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.post("/blobelements/d/:did/w/:wid/e/:eid", path_params=path_params, query_params=None, body=body, options=options)

    def upload_file_create_element(self, did, wid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid
        }
        return self.restHelpers.post("/blobelements/d/:did/w/:wid", path_params=path_params, query_params=None, body=body, options=options)


