from apiGroup import ApiGroup

class Webhooks(ApiGroup):
    def create_webhook(self, body, options=None):
        return self.restHelpers.post("/webhooks", path_params=None, query_params=None, body=body, options=options)

    def get_webhook(self, webhookid, options=None):
        path_params = {
            "webhookid": webhookid
        }
        return self.restHelpers.get("/webhooks/:webhookid", path_params=path_params, query_params=None, options=options)

    def ping_webhook(self, webhookid, body, options=None):
        path_params = {
            "webhookid": webhookid
        }
        return self.restHelpers.post("/webhooks/:webhookid/ping", path_params=path_params, query_params=None, body=body, options=options)

    def unregister_webhook(self, webhookid, options=None):
        path_params = {
            "webhookid": webhookid
        }
        return self.restHelpers.delete("/webhooks/:webhookid", path_params=path_params, query_params=None, options=options)

    def update_webhook(self, webhookid, body, options=None):
        path_params = {
            "webhookid": webhookid
        }
        return self.restHelpers.post("/webhooks/:webhookid", path_params=path_params, query_params=None, body=body, options=options)


