from apiGroup import ApiGroup

class Elements(ApiGroup):
    def decode_configuration_string(self, did, wvm_pair, eid, cid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid,
            "cid": cid
        }
        return self.restHelpers.get("/elements/d/:did/[wvm]/:wvm/e/:eid/configurationencodings/:cid", path_params=path_params, query_params=query_params, options=options)

    def delete_element(self, did, wid, eid, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.delete("/elements/d/:did/w/:wid/e/:eid", path_params=path_params, query_params=None, options=options)

    def encode_configuration(self, did, eid, body, query_params=None, options=None):
        path_params = {
            "did": did,
            "eid": eid
        }
        return self.restHelpers.post("/elements/d/:did/e/:eid/configurationencodings", path_params=path_params, query_params=query_params, body=body, options=options)

    def get_by_version(self, did, vid, options=None):
        path_params = {
            "did": did,
            "vid": vid
        }
        return self.restHelpers.get("/elements/:did/version/:vid", path_params=path_params, query_params=None, options=options)

    def get_by_workspace(self, did, wid, options=None):
        path_params = {
            "did": did,
            "wid": wid
        }
        return self.restHelpers.get("/elements/:did/workspace/:wid", path_params=path_params, query_params=None, options=options)

    def get_element(self, emid, options=None):
        path_params = {
            "emid": emid
        }
        return self.restHelpers.get("/elements/:emid", path_params=path_params, query_params=None, options=options)

    def get_element_translator_formats(self, did, wid, eid, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.get("/elements/translatorFormats/:did/:wid/:eid", path_params=path_params, query_params=None, options=options)

    def get_element_metadata(self, did, wv_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wv": wv_pair,
            "eid": eid
        }
        return self.restHelpers.get("/elements/d/:did/[wv]/:wv/e/:eid/metadata", path_params=path_params, query_params=query_params, options=options)

    def get_translator_formats(self, options=None):
        return self.restHelpers.get("/elements/translatorFormats", path_params=None, query_params=None, options=options)

    def update_element_metadata(self, did, wv_pair, eid, body, options=None):
        path_params = {
            "did": did,
            "wv": wv_pair,
            "eid": eid
        }
        return self.restHelpers.post("/elements/d/:did/[wv]/:wv/e/:eid/metadata", path_params=path_params, query_params=None, body=body, options=options)

    def update(self, emid, body, options=None):
        path_params = {
            "emid": emid
        }
        return self.restHelpers.post("/elements/:emid", path_params=path_params, query_params=None, body=body, options=options)

    def upload_file(self, did, body, options=None):
        path_params = {
            "did": did
        }
        return self.restHelpers.post("/elements/upload/:did", path_params=path_params, query_params=None, body=body, options=options)


