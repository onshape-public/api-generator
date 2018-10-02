from apiGroup import ApiGroup

class Versions(ApiGroup):
    def test_version_1(self, options=None):
        return self.restHelpers.get("/versions/test", path_params=None, query_params=None, options=options)

    def test_version_2(self, options=None):
        return self.restHelpers.get("/versions/test", path_params=None, query_params=None, options=options)


