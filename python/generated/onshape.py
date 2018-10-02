from groups import *
from apiGroup import ApiGroup


class Onshape:
    """"A python wrapper for Onshape's REST API"""
    def __init__(self, oauth_access_token=None, access=None, secret=None, target="https://cad.onshape.com"):
        if oauth_access_token is not None:
            self.oauth_access_token = oauth_access_token
        else:
            self.target = target
            self.access = access
            self.secret = secret
        api_group = ApiGroup(oauth_access_token, access, secret, target)

        self.accounts = accounts.Accounts(api_group)
        self.app_associative_data = appAssociativeData.AppAssociativeData(api_group)
        self.app_elements = appElements.AppElements(api_group)
        self.application_elements = applicationElements.ApplicationElements(api_group)
        self.applications = applications.Applications(api_group)
        self.assemblies = assemblies.Assemblies(api_group)
        self.billing = billing.Billing(api_group)
        self.blob_elements = blobElements.BlobElements(api_group)
        self.companies = companies.Companies(api_group)
        self.documents = documents.Documents(api_group)
        self.elements = elements.Elements(api_group)
        self.endpoints = endpoints.Endpoints(api_group)
        self.feature_studios = featureStudios.FeatureStudios(api_group)
        self.folders = folders.Folders(api_group)
        self.metadata = metadata.Metadata(api_group)
        self.models = models.Models(api_group)
        self.part_studios = partStudios.PartStudios(api_group)
        self.parts = parts.Parts(api_group)
        self.teams = teams.Teams(api_group)
        self.thumbnails = thumbnails.Thumbnails(api_group)
        self.translations = translations.Translations(api_group)
        self.users = users.Users(api_group)
        self.versions = versions.Versions(api_group)
        self.webhooks = webhooks.Webhooks(api_group)
