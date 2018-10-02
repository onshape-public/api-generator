import re
import datetime
import copy
import string
import random
import base64
import hmac
import hashlib
import requests
import json
import mimetypes
import os
from requests_toolbelt.multipart.encoder import MultipartEncoder


class MissingArgumentError(Exception):
    pass


class RestHelpers:

    def __init__(self, *args):
        if len(args) == 1:
            self.oauth_access_token = args[0].oauth_access_token
            self.target = args[0].target
            self.access = args[0].access
            self.secret = args[0].secret
        else:
            self.oauth_access_token = args[0]
            self.access = args[1]
            self.secret = args[2]
            self.target = args[3]

    @staticmethod
    def merge_dicts(a, b):
        return dict(list(a.items()) + list(b.items()))

    def build_api_key_headers(self,
                              method,
                              path,
                              query_string,
                              input_headers,
                              access,
                              secret):
        headers = copy.deepcopy(input_headers)
        auth_date = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        nonce = self._make_nonce()
        content_type_string_constant = "Content-Type"
        accept_string_constant = "Accept"
        if content_type_string_constant not in headers:
            headers[content_type_string_constant] = "application/json"
        if accept_string_constant not in headers:
            headers[accept_string_constant] = "application/vnd.onshape.v1+json"
        auth_string = self._build_auth(method=method,
                                       auth_date=auth_date,
                                       nonce=nonce,
                                       path=path,
                                       query_string=query_string,
                                       content_type=headers[content_type_string_constant],
                                       access=access,
                                       secret=secret)
        headers["On-Nonce"] = nonce
        headers["Date"] = auth_date
        headers["Authorization"] = auth_string
        return headers

    @staticmethod
    def _build_auth(method,
                    auth_date,
                    nonce,
                    path,
                    query_string,
                    content_type,
                    access,
                    secret):
        hmac_str = (method + '\n' + nonce + '\n' + auth_date + '\n' + content_type + '\n' + path +
                    '\n' + query_string[1:] + '\n').lower().encode('utf-8')
        signature = base64.b64encode(hmac.new(bytearray(secret, 'utf-8'), hmac_str, digestmod=hashlib.sha256).digest())
        auth = 'On ' + access + ':HmacSHA256:' + signature.decode('utf-8')

        return auth

    @staticmethod
    def _make_nonce():
        chars = string.digits + string.ascii_letters
        nonce = "".join(random.choice(chars) for i in range(25))
        return nonce

    @staticmethod
    def build_path_and_query(path,
                             path_params=None,
                             query_params=None):
        if path_params is None:
            path_params = {}
        if query_params is None:
            query_params = {}
        for field, pathParam in path_params.items():
            if type(pathParam) is tuple:
                path = re.sub(r"\[[a-zA-Z0-9]*\]/:{}".format(field),
                              "{}/{}".format(pathParam[0], pathParam[1]),
                              path)
            else:
                path = path.replace(":" + field, pathParam)
        path_param_regex = re.compile(r":[a-zA-Z0-9]*")
        if path_param_regex.search(path):
            raise MissingArgumentError("Missing argument(s): " +
                                       ", ".join(map(lambda match: match[1:], re.findall(path_param_regex, path))))
        if len(query_params.items()) is not 0:
            query_string = "?" + "&".join(map(lambda pair: "{}={}".format(pair[0], pair[1]), query_params.items()))
        else:
            query_string = ""
        return "/api" + path, query_string

    def get(self, path, path_params, query_params, options):
        if options is None:
            options = {}
        return self._generic_request("GET", path, self.merge_dicts({
            "path_params": path_params,
            "query_params": query_params
        }, options))

    def post(self, path, path_params, query_params, body, options):
        if options is None:
            options = {}
        if "file_path" in body:
            return self._upload(path, path_params, body, body["file_path"], options)
        else:
            return self._generic_request("POST", path, self.merge_dicts({
                "path_params": path_params,
                "body": json.dumps(body),
                "query_params": query_params
            }, options))

    def delete(self, path, path_params, query_params, options):
        if options is None:
            options = {}
        return self._generic_request("DELETE", path, self.merge_dicts({
            "path_params": path_params,
            "query_params": query_params
        }, options))

    def _upload(self, path, path_params, body, file_path, options):
        if "~" in file_path:
            file_path = os.path.expanduser(file_path)
        if options is None:
            options = {}
        headers = {}
        if "headers" in options and options["headers"] is not None:
            headers = options["headers"]
        mimetype = mimetypes.guess_type(file_path)[0]
        encoded_filename = os.path.basename(file_path)
        file_content_length = str(os.path.getsize(file_path))
        blob = open(file_path, 'rb')
        file_body = self._build_file_body(mimetype, encoded_filename, file_content_length, blob, body)
        options["headers"] = self.merge_dicts(headers, {
            "Content-Type": file_body.content_type
        })
        return self._generic_request("POST", path, self.merge_dicts({
            "path_params": path_params,
            "body": file_body,
            "blob_to_close": blob
        }, options))

    def _build_file_body(self, mimetype, encoded_filename, file_content_length, blob, body):
        fields = self.merge_dicts({
                "file": (encoded_filename, blob, mimetype),
                "encodedFileName": encoded_filename,
                "fileContentLength": file_content_length
            }, body)
        payload = MultipartEncoder(
            fields=fields
        )
        return payload

    def _generic_request(self, method, path, options):
        query_params = {}
        path_params = {}
        input_headers = {}
        if "query_params" in options and options["query_params"] is not None:
            query_params = options["query_params"]
        if "path_params" in options and options["path_params"] is not None:
            path_params = options["path_params"]
        if "headers" in options and options["headers"] is not None:
            input_headers = options["headers"]
        path, query = self.build_path_and_query(path, query_params=query_params, path_params=path_params)
        if self.access is not None and self.secret is not None:
            headers = self.build_api_key_headers(method=method,
                                                 path=path,
                                                 query_string=query,
                                                 input_headers=input_headers,
                                                 access=self.access,
                                                 secret=self.secret)
        elif self.oauth_access_token:
            headers = self.merge_dicts({
                "Authorization": "Bearer " + self.oauth_access_token,
                "Content-Type": "application/json"
            }, input_headers)
        else:
            raise MissingArgumentError("No oauth token or API key pair")
        full_path = self.target + path + query
        if method is "GET":
            return requests.get(full_path, headers=headers)
        if method is "POST":
            if "body" not in options:
                raise MissingArgumentError("no body present in post request")
            result = requests.post(full_path, headers=headers, data=options["body"])
            if "blob_to_close" in options:
                options["blob_to_close"].close()
            return result
        if method is "DELETE":
            return requests.delete(full_path, headers=headers)
