from apiGroup import ApiGroup

class Parts(ApiGroup):
    def get_body_details(self, did, wvm_pair, eid, partid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid,
            "partid": partid
        }
        return self.restHelpers.get("/parts/d/:did/[wvm]/:wvm/e/:eid/partid/:partid/bodydetails", path_params=path_params, query_params=query_params, options=options)

    def get_bounding_boxes(self, did, wvm_pair, eid, partid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid,
            "partid": partid
        }
        return self.restHelpers.get("/parts/d/:did/[wvm]/:wvm/e/:eid/partid/:partid/boundingboxes", path_params=path_params, query_params=query_params, options=options)

    def export_parasolid(self, did, wvm_pair, eid, partid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid,
            "partid": partid
        }
        return self.restHelpers.get("/parts/d/:did/[wvm]/:wvm/e/:eid/partid/:partid/parasolid", path_params=path_params, query_params=query_params, options=options)

    def export_stl(self, did, wvm_pair, eid, partid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid,
            "partid": partid
        }
        return self.restHelpers.get("/parts/d/:did/[wvm]/:wvm/e/:eid/partid/:partid/stl", path_params=path_params, query_params=query_params, options=options)

    def get_element_parts_old(self, did, wid, eid, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.get("/parts/:did/workspace/:wid/element/:eid", path_params=path_params, query_params=None, options=options)

    def get_part_metadata(self, did, wvm_pair, eid, partid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid,
            "partid": partid
        }
        return self.restHelpers.get("/parts/d/:did/[wvm]/:wvm/e/:eid/partid/:partid/metadata", path_params=path_params, query_params=query_params, options=options)

    def get_parts(self, did, wvm_pair, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair
        }
        return self.restHelpers.get("/parts/d/:did/[wvm]/:wvm", path_params=path_params, query_params=query_params, options=options)

    def get_by_version_old(self, did, vid, options=None):
        path_params = {
            "did": did,
            "vid": vid
        }
        return self.restHelpers.get("/parts/:did/version/:vid", path_params=path_params, query_params=None, options=options)

    def get_parts_in_partstudio(self, did, wvm_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid
        }
        return self.restHelpers.get("/parts/d/:did/[wvm]/:wvm/e/:eid", path_params=path_params, query_params=query_params, options=options)

    def get_bend_table(self, did, wvm_pair, eid, partid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid,
            "partid": partid
        }
        return self.restHelpers.get("/parts/d/:did/[wvm]/:wvm/e/:eid/partid/:partid/sheetmetal/bendtable", path_params=path_params, query_params=query_params, options=options)

    def get_standard_content_part_metadata(self, did, vid, eid, oid, partid, query_params=None, options=None):
        path_params = {
            "did": did,
            "vid": vid,
            "eid": eid,
            "oid": oid,
            "partid": partid
        }
        return self.restHelpers.get("/parts/standardcontent/d/:did/v/:vid/e/:eid/[cu]/:oid/partid/:partid/metadata", path_params=path_params, query_params=query_params, options=options)

    def get_workspace_parts_old(self, did, wid, options=None):
        path_params = {
            "did": did,
            "wid": wid
        }
        return self.restHelpers.get("/parts/:did/workspace/:wid", path_params=path_params, query_params=None, options=options)

    def get_mass_properties(self, did, wvm_pair, eid, partid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid,
            "partid": partid
        }
        return self.restHelpers.get("/parts/d/:did/[wvm]/:wvm/e/:eid/partid/:partid/massproperties", path_params=path_params, query_params=query_params, options=options)

    def get_shaded_views(self, did, wvm_pair, eid, partid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid,
            "partid": partid
        }
        return self.restHelpers.get("/parts/d/:did/[wvm]/:wvm/e/:eid/partid/:partid/shadedviews", path_params=path_params, query_params=query_params, options=options)

    def get_edges(self, did, wvm_pair, eid, partid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid,
            "partid": partid
        }
        return self.restHelpers.get("/parts/d/:did/[wvm]/:wvm/e/:eid/partid/:partid/tessellatededges", path_params=path_params, query_params=query_params, options=options)

    def get_faces(self, did, wvm_pair, eid, partid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid,
            "partid": partid
        }
        return self.restHelpers.get("/parts/d/:did/[wvm]/:wvm/e/:eid/partid/:partid/tessellatedfaces", path_params=path_params, query_params=query_params, options=options)

    def update_part_metadata(self, did, wvm_pair, eid, partid, body, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair,
            "eid": eid,
            "partid": partid
        }
        return self.restHelpers.post("/parts/d/:did/[wvm]/:wvm/e/:eid/partid/:partid/metadata", path_params=path_params, query_params=None, body=body, options=options)

    def batch_update_part_metadata(self, did, wvm_pair, body, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair
        }
        return self.restHelpers.post("/parts/d/:did/[wvm]/:wvm", path_params=path_params, query_params=query_params, body=body, options=options)

    def update_standard_content_part_metadata(self, did, vid, eid, oid, partid, body, query_params=None, options=None):
        path_params = {
            "did": did,
            "vid": vid,
            "eid": eid,
            "oid": oid,
            "partid": partid
        }
        return self.restHelpers.post("/parts/standardcontent/d/:did/v/:vid/e/:eid/[cu]/:oid/partid/:partid/metadata", path_params=path_params, query_params=query_params, body=body, options=options)


