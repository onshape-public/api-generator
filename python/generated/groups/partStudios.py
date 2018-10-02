from apiGroup import ApiGroup

class PartStudios(ApiGroup):
    def add_feature(self, did, wid, eid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.post("/partstudios/d/:did/w/:wid/e/:eid/features", path_params=path_params, query_params=None, body=body, options=options)

    def get_body_details(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/partstudios/d/:did/[wvm]/:wvm/e/:eid/bodydetails", path_params=path_params, query_params=query_params, options=options)

    def get_bounding_boxes(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/partstudios/d/:did/[wvm]/:wvm/e/:eid/boundingboxes", path_params=path_params, query_params=query_params, options=options)

    def compare_part_studio(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/partstudios/d/:did/[wvm]/:wvm/e/:eid/compare", path_params=path_params, query_params=query_params, options=options)

    def create_part_studio(self, did, wid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid
        }
        return self.restHelpers.post("/partstudios/d/:did/w/:wid", path_params=path_params, query_params=None, body=body, options=options)

    def create_translation(self, did, wv_pair, eid, body, options=None):
        path_params = {
            "did": did,
            "wv": wv_pair,
            "eid": eid
        }
        return self.restHelpers.post("/partstudios/d/:did/[wv]/:wv/e/:eid/translations", path_params=path_params, query_params=None, body=body, options=options)

    def delete_feature(self, did, wid, eid, fid, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid,
            "fid": fid
        }
        return self.restHelpers.delete("/partstudios/d/:did/w/:wid/e/:eid/features/featureid/:fid", path_params=path_params, query_params=None, options=options)

    def eval_feature_script(self, did, wvm_pair, eid, body, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.post("/partstudios/d/:did/[wvm]/:wvm/e/:eid/featurescript", path_params=path_params, query_params=None, body=body, options=options)

    def export_parasolid(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/partstudios/d/:did/[wvm]/:wvm/e/:eid/parasolid", path_params=path_params, query_params=query_params, options=options)

    def export_stl(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/partstudios/d/:did/[wvm]/:wvm/e/:eid/stl", path_params=path_params, query_params=query_params, options=options)

    def get_configuration(self, did, wvm_pair, eid, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/partstudios/d/:did/[wvm]/:wvm/e/:eid/configuration", path_params=path_params, query_params=None, options=options)

    def get_features(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/partstudios/d/:did/[wvm]/:wvm/e/:eid/features", path_params=path_params, query_params=query_params, options=options)

    def get_feature_specs(self, did, wvm_pair, eid, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/partstudios/d/:did/[wvm]/:wvm/e/:eid/featurespecs", path_params=path_params, query_params=None, options=options)

    def get_named_views(self, did, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "eid": eid
        }
        return self.restHelpers.get("/partstudios/d/:did/e/:eid/namedViews", path_params=path_params, query_params=query_params, options=options)

    def get_translation_formats(self, did, wid, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.get("/partstudios/d/:did/w/:wid/e/:eid/translationformats", path_params=path_params, query_params=query_params, options=options)

    def id_translations(self, did, wvm_pair, eid, body, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.post("/partstudios/d/:did/[wvm]/:wvm/e/:eid/idtranslations", path_params=path_params, query_params=None, body=body, options=options)

    def get_mass_properties(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/partstudios/d/:did/[wvm]/:wvm/e/:eid/massproperties", path_params=path_params, query_params=query_params, options=options)

    def get_metadata(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/partstudios/d/:did/[wvm]/:wvm/e/:eid/metadata", path_params=path_params, query_params=query_params, options=options)

    def get_shaded_views(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/partstudios/d/:did/[wvm]/:wvm/e/:eid/shadedviews", path_params=path_params, query_params=query_params, options=options)

    def get_bounding_boxes_for_sketch(self, did, wvm_pair, eid, sid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid,
            "sid": sid
        }
        return self.restHelpers.get("/partstudios/d/:did/[wvm]/:wvm/e/:eid/sketches/:sid/boundingboxes", path_params=path_params, query_params=query_params, options=options)

    def get_sketch_info(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/partstudios/d/:did/[wvm]/:wvm/e/:eid/sketches", path_params=path_params, query_params=query_params, options=options)

    def get_edges(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/partstudios/d/:did/[wvm]/:wvm/e/:eid/tessellatededges", path_params=path_params, query_params=query_params, options=options)

    def get_faces(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/partstudios/d/:did/[wvm]/:wvm/e/:eid/tessellatedfaces", path_params=path_params, query_params=query_params, options=options)

    def get_tessellated_entities(self, did, wvm_pair, eid, sid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid,
            "sid": sid
        }
        return self.restHelpers.get("/partstudios/d/:did/[wvm]/:wvm/e/:eid/sketches/:sid/tessellatedentities", path_params=path_params, query_params=query_params, options=options)

    def update_configuration(self, did, wid, eid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.post("/partstudios/d/:did/w/:wid/e/:eid/configuration", path_params=path_params, query_params=None, body=body, options=options)

    def update_feature(self, did, wid, eid, fid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid,
            "fid": fid
        }
        return self.restHelpers.post("/partstudios/d/:did/w/:wid/e/:eid/features/featureid/:fid", path_params=path_params, query_params=None, body=body, options=options)

    def update_rollback(self, did, wid, eid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.post("/partstudios/d/:did/w/:wid/e/:eid/features/rollback", path_params=path_params, query_params=None, body=body, options=options)

    def update_features(self, did, wid, eid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.post("/partstudios/d/:did/w/:wid/e/:eid/features/updates", path_params=path_params, query_params=None, body=body, options=options)


