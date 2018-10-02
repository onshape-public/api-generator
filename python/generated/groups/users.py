from apiGroup import ApiGroup

class Users(ApiGroup):
    def get_session(self, options=None):
        return self.restHelpers.get("/users/session", path_params=None, query_params=None, options=options)

    def get_session_info(self, options=None):
        return self.restHelpers.get("/users/sessioninfo", path_params=None, query_params=None, options=options)

    def get_user_settings(self, uid, options=None):
        path_params = {
            "uid": uid
        }
        return self.restHelpers.get("/users/:uid/settings", path_params=path_params, query_params=None, options=options)

    def get_user_settings_current_logged_in_user(self, options=None):
        return self.restHelpers.get("/users/settings", path_params=None, query_params=None, options=options)


