from apiGroup import ApiGroup

class Translations(ApiGroup):
    def create_translation(self, did, wid, body, options=None):
        path_params = {
            "did": did,
            "wid": wid
        }
        return self.restHelpers.post("/translations/d/:did/w/:wid", path_params=path_params, query_params=None, body=body, options=options)

    def delete_translation(self, tid, options=None):
        path_params = {
            "tid": tid
        }
        return self.restHelpers.delete("/translations/:tid", path_params=path_params, query_params=None, options=options)

    def get_translator_formats(self, options=None):
        return self.restHelpers.get("/translations/translationformats", path_params=None, query_params=None, options=options)

    def get_translation(self, tid, options=None):
        path_params = {
            "tid": tid
        }
        return self.restHelpers.get("/translations/:tid", path_params=path_params, query_params=None, options=options)

    def get_translations(self, did, query_params=None, options=None):
        path_params = {
            "did": did
        }
        return self.restHelpers.get("/translations/d/:did", path_params=path_params, query_params=query_params, options=options)


