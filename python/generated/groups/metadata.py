from apiGroup import ApiGroup

class Metadata(ApiGroup):
    def get_part_metadata(self, did, wvm_pair, eid, pid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid,
            "pid": pid
        }
        return self.restHelpers.get("/metadata/d/:did/[wvm]/:wvm/e/:eid/p/:pid", path_params=path_params, query_params=query_params, options=options)

    def get_part_list_metadata(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/metadata/d/:did/[wvm]/:wvm/e/:eid/p", path_params=path_params, query_params=query_params, options=options)

    def get_standard_content_metadata(self, did, vid, eid, oid, pid, query_params=None, options=None):
        path_params = {
            "did": did,
            "vid": vid,
            "eid": eid,
            "oid": oid,
            "pid": pid
        }
        return self.restHelpers.get("/metadata/standardcontent/d/:did/v/:vid/e/:eid/[cu]/:oid/p/:pid", path_params=path_params, query_params=query_params, options=options)

    def get_metadata(self, did, wv_pair, query_params=None, options=None):
        path_params = {
            "did": did,
            "wv": wv_pair
        }
        return self.restHelpers.get("/metadata/d/:did/[wv]/:wv", path_params=path_params, query_params=query_params, options=options)

    def get_metadata_schema_properties(self, query_params=None, options=None):
        return self.restHelpers.get("/metadataschema/properties", path_params=None, query_params=query_params, options=options)

    def get_metadata_property(self, pid, query_params=None, options=None):
        path_params = {
            "pid": pid
        }
        return self.restHelpers.get("/metadataschema/property/:pid", path_params=path_params, query_params=query_params, options=options)

    def get_metadata_schema_by_i_d(self, sid, query_params=None, options=None):
        path_params = {
            "sid": sid
        }
        return self.restHelpers.get("/metadataschema/:sid", path_params=path_params, query_params=query_params, options=options)

    def get_metadata_schema(self, query_params=None, options=None):
        return self.restHelpers.get("/metadataschema", path_params=None, query_params=query_params, options=options)

    def update_metadata(self, did, wv_pair, body, options=None):
        path_params = {
            "did": did,
            "wv": wv_pair
        }
        return self.restHelpers.post("/metadata/d/:did/[wv]/:wv", path_params=path_params, query_params=None, body=body, options=options)

    def update_standard_content_metadata(self, did, vid, eid, oid, pid, body, query_params=None, options=None):
        path_params = {
            "did": did,
            "vid": vid,
            "eid": eid,
            "oid": oid,
            "pid": pid
        }
        return self.restHelpers.post("/metadata/standardcontent/d/:did/v/:vid/e/:eid/[cu]/:oid/p/:pid", path_params=path_params, query_params=query_params, body=body, options=options)


