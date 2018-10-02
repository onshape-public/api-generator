from apiGroup import ApiGroup

class Assemblies(ApiGroup):
    def add_feature(self, did, wid, eid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.post("/assemblies/d/:did/w/:wid/e/:eid/features", path_params=path_params, query_params=None, body=body, options=options)

    def get_assembly_definition(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/assemblies/d/:did/[wvm]/:wvm/e/:eid", path_params=path_params, query_params=query_params, options=options)

    def get_bounding_boxes(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/assemblies/d/:did/[wvm]/:wvm/e/:eid/boundingboxes", path_params=path_params, query_params=query_params, options=options)

    def create_assembly(self, did, wid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid
        }
        return self.restHelpers.post("/assemblies/d/:did/w/:wid", path_params=path_params, query_params=None, body=body, options=options)

    def create_translation(self, did, wv_pair, eid, body, options=None):
        path_params = {
            "did": did,
            "wv": wv_pair,
            "eid": eid
        }
        return self.restHelpers.post("/assemblies/d/:did/[wv]/:wv/e/:eid/translations", path_params=path_params, query_params=None, body=body, options=options)

    def insert_transformed_instances(self, did, wid, eid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.post("/assemblies/d/:did/w/:wid/e/:eid/transformedinstances", path_params=path_params, query_params=None, body=body, options=options)

    def create_instance(self, did, wid, eid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.post("/assemblies/d/:did/w/:wid/e/:eid/instances", path_params=path_params, query_params=None, body=body, options=options)

    def delete_feature(self, did, wid, eid, fid, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid,
            "fid": fid
        }
        return self.restHelpers.delete("/assemblies/d/:did/w/:wid/e/:eid/features/featureid/:fid", path_params=path_params, query_params=None, options=options)

    def delete_instance(self, did, wid, eid, nid, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid,
            "nid": nid
        }
        return self.restHelpers.delete("/assemblies/d/:did/w/:wid/e/:eid/instance/nodeid/:nid", path_params=path_params, query_params=None, options=options)

    def get_bill_of_materials(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/assemblies/d/:did/[wvm]/:wvm/e/:eid/bom", path_params=path_params, query_params=query_params, options=options)

    def get_features(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/assemblies/d/:did/[wvm]/:wvm/e/:eid/features", path_params=path_params, query_params=query_params, options=options)

    def get_feature_specs(self, did, wvm_pair, eid, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/assemblies/d/:did/[wvm]/:wvm/e/:eid/featurespecs", path_params=path_params, query_params=None, options=options)

    def get_named_views(self, did, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "eid": eid
        }
        return self.restHelpers.get("/assemblies/d/:did/e/:eid/namedViews", path_params=path_params, query_params=query_params, options=options)

    def get_translation_formats(self, did, wid, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.get("/assemblies/d/:did/w/:wid/e/:eid/translationformats", path_params=path_params, query_params=query_params, options=options)

    def get_or_create_bill_of_materials_element(self, did, wid, eid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.post("/assemblies/d/:did/w/:wid/e/:eid/bomelement", path_params=path_params, query_params=None, body=body, options=options)

    def get_shaded_views(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/assemblies/d/:did/[wvm]/:wvm/e/:eid/shadedviews", path_params=path_params, query_params=query_params, options=options)

    def transform_occurrences(self, did, wid, eid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.post("/assemblies/d/:did/w/:wid/e/:eid/occurrencetransforms", path_params=path_params, query_params=None, body=body, options=options)

    def update_feature(self, did, wid, eid, fid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid,
            "fid": fid
        }
        return self.restHelpers.post("/assemblies/d/:did/w/:wid/e/:eid/features/featureid/:fid", path_params=path_params, query_params=None, body=body, options=options)


