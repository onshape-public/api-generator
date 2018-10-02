from apiGroup import ApiGroup

class Documents(ApiGroup):
    def copy_workspace(self, did, wid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid
        }
        return self.restHelpers.post("/documents/:did/workspaces/:wid/copy", path_params=path_params, query_params=None, body=body, options=options)

    def create_document(self, body, options=None):
        return self.restHelpers.post("/documents", path_params=None, query_params=None, body=body, options=options)

    def create_version(self, did, body, options=None):
        path_params = {
            "did": did
        }
        return self.restHelpers.post("/documents/d/:did/versions", path_params=path_params, query_params=None, body=body, options=options)

    def create_version_old(self, did, body, options=None):
        path_params = {
            "did": did
        }
        return self.restHelpers.post("/documents/:did/versions", path_params=path_params, query_params=None, body=body, options=options)

    def create_workspace(self, did, body, options=None):
        path_params = {
            "did": did
        }
        return self.restHelpers.post("/documents/d/:did/workspaces", path_params=path_params, query_params=None, body=body, options=options)

    def create_workspace_old(self, did, body, options=None):
        path_params = {
            "did": did
        }
        return self.restHelpers.post("/documents/:did/workspaces", path_params=path_params, query_params=None, body=body, options=options)

    def delete_document(self, did, options=None):
        path_params = {
            "did": did
        }
        return self.restHelpers.delete("/documents/:did", path_params=path_params, query_params=None, options=options)

    def delete_workspace(self, did, wid, options=None):
        path_params = {
            "did": did,
            "wid": wid
        }
        return self.restHelpers.delete("/documents/d/:did/workspaces/:wid", path_params=path_params, query_params=None, options=options)

    def delete_workspace_old(self, did, wid, options=None):
        path_params = {
            "did": did,
            "wid": wid
        }
        return self.restHelpers.delete("/documents/:did/workspaces/:wid", path_params=path_params, query_params=None, options=options)

    def download_external_data(self, did, fid, options=None):
        path_params = {
            "did": did,
            "fid": fid
        }
        return self.restHelpers.get("/documents/d/:did/externaldata/:fid", path_params=path_params, query_params=None, options=options)

    def get_element_list(self, did, wvm_pair, query_params=None, options=None):
        path_params = {
            "did": did,
            "wvm": wvm_pair
        }
        return self.restHelpers.get("/documents/d/:did/[wvm]/:wvm/elements", path_params=path_params, query_params=query_params, options=options)

    def export_old(self, did, eid, options=None):
        path_params = {
            "did": did,
            "eid": eid
        }
        return self.restHelpers.get("/documents/:did/export/:eid", path_params=path_params, query_params=None, options=options)

    def export_element(self, did, wv_pair, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "wv": wv_pair,
            "eid": eid
        }
        return self.restHelpers.get("/documents/d/:did/[wv]/:wv/e/:eid/export", path_params=path_params, query_params=query_params, options=options)

    def export_element_post_json(self, did, wv_pair, eid, body, query_params=None, options=None):
        path_params = {
            "did": did,
            "wv": wv_pair,
            "eid": eid
        }
        return self.restHelpers.post("/documents/d/:did/[wv]/:wv/e/:eid/export", path_params=path_params, query_params=query_params, body=body, options=options)

    def get_acl(self, did, options=None):
        path_params = {
            "did": did
        }
        return self.restHelpers.get("/documents/:did/acl", path_params=path_params, query_params=None, options=options)

    def get_current_microversion(self, did, wv_pair, options=None):
        path_params = {
            "did": did,
            "wv": wv_pair
        }
        return self.restHelpers.get("/documents/d/:did/[wv]/:wv/currentmicroversion", path_params=path_params, query_params=None, options=options)

    def get_document(self, did, options=None):
        path_params = {
            "did": did
        }
        return self.restHelpers.get("/documents/:did", path_params=path_params, query_params=None, options=options)

    def get_document_permission_set(self, did, options=None):
        path_params = {
            "did": did
        }
        return self.restHelpers.get("/documents/:did/permissionset", path_params=path_params, query_params=None, options=options)

    def get_documents(self, query_params=None, options=None):
        return self.restHelpers.get("/documents", path_params=None, query_params=query_params, options=options)

    def get_elements(self, did, options=None):
        path_params = {
            "did": did
        }
        return self.restHelpers.get("/documents/:did/elements", path_params=path_params, query_params=None, options=options)

    def get_version(self, did, vid, query_params=None, options=None):
        path_params = {
            "did": did,
            "vid": vid
        }
        return self.restHelpers.get("/documents/d/:did/versions/:vid", path_params=path_params, query_params=query_params, options=options)

    def get_version_old(self, did, vid, options=None):
        path_params = {
            "did": did,
            "vid": vid
        }
        return self.restHelpers.get("/documents/:did/versions/:vid", path_params=path_params, query_params=None, options=options)

    def get_versions(self, did, query_params=None, options=None):
        path_params = {
            "did": did
        }
        return self.restHelpers.get("/documents/d/:did/versions", path_params=path_params, query_params=query_params, options=options)

    def get_versions_old(self, did, query_params=None, options=None):
        path_params = {
            "did": did
        }
        return self.restHelpers.get("/documents/:did/versions", path_params=path_params, query_params=query_params, options=options)

    def get_workspace(self, did, wid, options=None):
        path_params = {
            "did": did,
            "wid": wid
        }
        return self.restHelpers.get("/documents/d/:did/workspaces/:wid", path_params=path_params, query_params=None, options=options)

    def get_workspace_old(self, did, wid, options=None):
        path_params = {
            "did": did,
            "wid": wid
        }
        return self.restHelpers.get("/documents/:did/workspaces/:wid", path_params=path_params, query_params=None, options=options)

    def get_workspaces(self, did, query_params=None, options=None):
        path_params = {
            "did": did
        }
        return self.restHelpers.get("/documents/d/:did/workspaces", path_params=path_params, query_params=query_params, options=options)

    def get_workspaces_old(self, did, options=None):
        path_params = {
            "did": did
        }
        return self.restHelpers.get("/documents/:did/workspaces", path_params=path_params, query_params=None, options=options)

    def get_insertables(self, did, vid, query_params=None, options=None):
        path_params = {
            "did": did,
            "vid": vid
        }
        return self.restHelpers.get("/documents/d/:did/v/:vid/insertables", path_params=path_params, query_params=query_params, options=options)

    def move_elements_to_document(self, did, wid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid
        }
        return self.restHelpers.post("/documents/d/:did/w/:wid/moveelement", path_params=path_params, query_params=None, body=body, options=options)

    def share_document(self, did, body, options=None):
        path_params = {
            "did": did
        }
        return self.restHelpers.post("/documents/:did/share", path_params=path_params, query_params=None, body=body, options=options)

    def un_share(self, did, eid, query_params=None, options=None):
        path_params = {
            "did": did,
            "eid": eid
        }
        return self.restHelpers.delete("/documents/:did/share/:eid", path_params=path_params, query_params=query_params, options=options)

    def update_document_attributes(self, did, body, options=None):
        path_params = {
            "did": did
        }
        return self.restHelpers.post("/documents/:did", path_params=path_params, query_params=None, body=body, options=options)

    def update_external_references_to_latest_documents(self, did, wid, eid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid
        }
        return self.restHelpers.post("/documents/d/:did/w/:wid/e/:eid/latestdocumentreferences", path_params=path_params, query_params=None, body=body, options=options)

    def update_version_old(self, did, vid, body, options=None):
        path_params = {
            "did": did,
            "vid": vid
        }
        return self.restHelpers.post("/documents/:did/versions/:vid", path_params=path_params, query_params=None, body=body, options=options)


