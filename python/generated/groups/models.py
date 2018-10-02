from apiGroup import ApiGroup

class Models(ApiGroup):
    def get_assembly_definition(self, did, wid, eid, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.get("/models/assembly/definition/:did/workspace/:wid/element/:eid", path_params=path_params, query_params=None, options=options)

    def get_body_details(self, body, options=None):
        return self.restHelpers.post("/models/bodies/details", path_params=None, query_params=None, body=body, options=options)

    def get_bounding_box(self, body, options=None):
        return self.restHelpers.post("/models/boundingbox", path_params=None, query_params=None, body=body, options=options)

    def get_edges(self, body, options=None):
        return self.restHelpers.post("/models/tessellatededges", path_params=None, query_params=None, body=body, options=options)

    def get_faces(self, body, options=None):
        return self.restHelpers.post("/models/tessellatedfaces", path_params=None, query_params=None, body=body, options=options)


