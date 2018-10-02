from apiGroup import ApiGroup

class Thumbnails(ApiGroup):
    def delete_application_thumbnails(self, did, wv_pair, eid, options=None):
        path_params = {
            "did": did,
            "wv": wv_pair,
            "eid": eid
        }
        return self.restHelpers.delete("/thumbnails/d/:did/[wv]/:wv/e/:eid", path_params=path_params, query_params=None, options=options)

    def get_configured_element_thumbnail_with_size(self, did, wid, eid, cid, sz, query_params=None, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid,
            "cid": cid,
            "sz": sz
        }
        return self.restHelpers.get("/thumbnails/d/:did/w/:wid/e/:eid/c/:cid/s/:sz", path_params=path_params, query_params=query_params, options=options)

    def get_thumbnail_for_document(self, did, options=None):
        path_params = {
            "did": did
        }
        return self.restHelpers.get("/thumbnails/d/:did", path_params=path_params, query_params=None, options=options)

    def get_thumbnail_for_document_old(self, did, options=None):
        path_params = {
            "did": did
        }
        return self.restHelpers.get("/thumbnails/document/:did", path_params=path_params, query_params=None, options=options)

    def get_document_thumbnail(self, did, wid, options=None):
        path_params = {
            "did": did,
            "wid": wid
        }
        return self.restHelpers.get("/thumbnails/d/:did/w/:wid", path_params=path_params, query_params=None, options=options)

    def get_element_thumbnail(self, did, wv_pair, eid, options=None):
        path_params = {
            "did": did,
            "wv": wv_pair,
            "eid": eid
        }
        return self.restHelpers.get("/thumbnails/d/:did/[wv]/:wv/e/:eid", path_params=path_params, query_params=None, options=options)

    def get_element_thumbnail_with_size(self, did, wid, eid, sz, query_params=None, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "eid": eid,
            "sz": sz
        }
        return self.restHelpers.get("/thumbnails/d/:did/w/:wid/e/:eid/s/:sz", path_params=path_params, query_params=query_params, options=options)

    def get_thumbnail_for_document_and_version(self, did, vid, query_params=None, options=None):
        path_params = {
            "did": did,
            "vid": vid
        }
        return self.restHelpers.get("/thumbnails/d/:did/v/:vid", path_params=path_params, query_params=query_params, options=options)

    def get_thumbnail_for_document_and_version_old(self, did, vid, options=None):
        path_params = {
            "did": did,
            "vid": vid
        }
        return self.restHelpers.get("/thumbnails/document/:did/version/:vid", path_params=path_params, query_params=None, options=options)

    def get_document_thumbnail_with_size(self, did, wid, sz, options=None):
        path_params = {
            "did": did,
            "wid": wid,
            "sz": sz
        }
        return self.restHelpers.get("/thumbnails/d/:did/w/:wid/s/:sz", path_params=path_params, query_params=None, options=options)

    def set_application_element_thumbnail(self, did, wv_pair, eid, body, query_params=None, options=None):
        path_params = {
            "did": did,
            "wv": wv_pair,
            "eid": eid
        }
        return self.restHelpers.post("/thumbnails/d/:did/[wv]/:wv/e/:eid", path_params=path_params, query_params=query_params, body=body, options=options)


