import unittest
from onshape import Onshape
from _keys import keys


class SmokeTest(unittest.TestCase):

    def setUp(self):
        self.onshape = Onshape(access=keys["access"],
                               secret=keys["secret"])
        self.session_info = self.onshape.users.get_session_info().json()

    def verify_docs_response(self, docs_response):
        self.assertEqual(docs_response.status_code, 200)
        self.assertEqual(len(docs_response.json()["items"][0]["id"]), 24)

    def test_get_documents(self):
        docs_response = self.onshape.documents.get_documents()
        self.verify_docs_response(docs_response)

    def test_get_documents_with_query(self):
        docs_response = self.onshape.documents.get_documents({"filter": 5})
        self.verify_docs_response(docs_response)

    def test_create_and_delete_document(self):
        create_doc_result = self.onshape.documents.create_document({
            "name": "new doc 100",
            "ownerId": self.session_info["id"],
            "ownerType": "0",
            "betaCapabilityIds": [],
            "isPublic": False
        })
        self.assertEqual(create_doc_result.status_code, 200)
        delete_doc_result = self.onshape.documents.delete_document(create_doc_result.json()["id"])
        self.assertEqual(delete_doc_result.status_code, 200)

    def test_upload_blob_and_delete_element(self):
        doc_result = self.onshape.documents.get_documents({"filter": 1})
        self.assertEqual(doc_result.status_code, 200)
        doc = doc_result.json()["items"][0]
        blob_result = self.onshape.blob_elements.upload_file_create_element(doc["id"],
                                                                   doc["defaultWorkspace"]["id"],
                                                                   body={
                                                                       "file_path": "~/Downloads/sampleupload.txt"
                                                                   })
        self.assertEqual(blob_result.status_code, 200)
        delete_element_result = self.onshape.elements.delete_element(doc["id"],
                                                                     doc["defaultWorkspace"]["id"],
                                                                     blob_result.json()["id"])
        self.assertEqual(delete_element_result.status_code, 200)

    def test_wvm_replacement(self):
        doc_result = self.onshape.documents.get_documents()
        self.assertEqual(doc_result.status_code, 200)
        doc = doc_result.json()["items"][0]
        wvm_result = self.onshape.documents.get_element_list(doc["id"],
                                                             ("w", doc["defaultWorkspace"]["id"]))
        self.assertEqual(wvm_result.status_code, 200)
        self.assertEqual(type(wvm_result.json()[0]["lengthUnits"]), str)


if __name__ == '__main__':
    unittest.main()
