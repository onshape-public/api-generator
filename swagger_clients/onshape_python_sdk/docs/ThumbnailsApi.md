# swagger_client.ThumbnailsApi

All URIs are relative to *https://cad.onshape.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_application_thumbnails_thumbnails**](ThumbnailsApi.md#delete_application_thumbnails_thumbnails) | **DELETE** /thumbnails/d/{did}/{wv_char}/{wv}/e/{eid} | Delete Application Element Thumbnail
[**get_configured_element_thumbnail_with_size_thumbnails**](ThumbnailsApi.md#get_configured_element_thumbnail_with_size_thumbnails) | **GET** /thumbnails/d/{did}/w/{wid}/e/{eid}/c/{cid}/s/{sz} | Get Configured Element Thumbnail With Size
[**get_document_thumbnail_thumbnails**](ThumbnailsApi.md#get_document_thumbnail_thumbnails) | **GET** /thumbnails/d/{did}/w/{wid} | Get Document Thumbnail Info
[**get_document_thumbnail_with_size_thumbnails**](ThumbnailsApi.md#get_document_thumbnail_with_size_thumbnails) | **GET** /thumbnails/d/{did}/w/{wid}/s/{sz} | Get Thumbnail With Size
[**get_element_thumbnail_thumbnails**](ThumbnailsApi.md#get_element_thumbnail_thumbnails) | **GET** /thumbnails/d/{did}/{wv_char}/{wv}/e/{eid} | Get Element Thumbnail Info
[**get_element_thumbnail_with_size_thumbnails**](ThumbnailsApi.md#get_element_thumbnail_with_size_thumbnails) | **GET** /thumbnails/d/{did}/w/{wid}/e/{eid}/s/{sz} | Get Element Thumbnail With Size
[**get_thumbnail_for_document_and_version_thumbnails**](ThumbnailsApi.md#get_thumbnail_for_document_and_version_thumbnails) | **GET** /thumbnails/d/{did}/v/{vid} | Get Thumbnail Info For Document Version
[**get_thumbnail_for_document_thumbnails**](ThumbnailsApi.md#get_thumbnail_for_document_thumbnails) | **GET** /thumbnails/d/{did} | Get Default Workspace Thumbnail Info
[**set_application_element_thumbnail_thumbnails**](ThumbnailsApi.md#set_application_element_thumbnail_thumbnails) | **POST** /thumbnails/d/{did}/{wv_char}/{wv}/e/{eid} | Set Application Element Thumbnail


# **delete_application_thumbnails_thumbnails**
> delete_application_thumbnails_thumbnails(wv_char, did, wv, eid)

Delete Application Element Thumbnail

Delete element thumbnails for an application element

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: apiAccessKey
configuration = swagger_client.Configuration()
configuration.api_key['ACCESS_KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ACCESS_KEY'] = 'Bearer'
# Configure API key authorization: apiSecretKey
configuration = swagger_client.Configuration()
configuration.api_key['SECRET_KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SECRET_KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ThumbnailsApi(swagger_client.ApiClient(configuration))
wv_char = 'wv_char_example' # str | One of w or v corresponding to whether a workspace or version was entered.
did = 'did_example' # str | Document ID
wv = 'wv_example' # str | Workspace (w) or Version (v) ID
eid = 'eid_example' # str | Element ID

try:
    # Delete Application Element Thumbnail
    api_instance.delete_application_thumbnails_thumbnails(wv_char, did, wv, eid)
except ApiException as e:
    print("Exception when calling ThumbnailsApi->delete_application_thumbnails_thumbnails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wv_char** | **str**| One of w or v corresponding to whether a workspace or version was entered. | 
 **did** | **str**| Document ID | 
 **wv** | **str**| Workspace (w) or Version (v) ID | 
 **eid** | **str**| Element ID | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configured_element_thumbnail_with_size_thumbnails**
> InlineResponse20099 get_configured_element_thumbnail_with_size_thumbnails(cid, sz, did, wid, eid, reject_empty)

Get Configured Element Thumbnail With Size

Return thumbnail for a configured element, with specified size in pixels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: apiAccessKey
configuration = swagger_client.Configuration()
configuration.api_key['ACCESS_KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ACCESS_KEY'] = 'Bearer'
# Configure API key authorization: apiSecretKey
configuration = swagger_client.Configuration()
configuration.api_key['SECRET_KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SECRET_KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ThumbnailsApi(swagger_client.ApiClient(configuration))
cid = 'cid_example' # str | The cache key for the requested configuration, as generated by                      BTMicroversionIdAndConfiguration.configurationToCacheKeyString
sz = 'sz_example' # str | Requested thumbnail size, such as 300x300
did = 'did_example' # str | Document ID
wid = 'wid_example' # str | Workspace ID
eid = 'eid_example' # str | Element ID
reject_empty = true # bool | If true, a 404 will be returned for thumbnails that are made for                       empty elements. Clients can use this parameter to skip the display of empty thumbnails and                       display a default icon instead. Defaults to false.

try:
    # Get Configured Element Thumbnail With Size
    api_response = api_instance.get_configured_element_thumbnail_with_size_thumbnails(cid, sz, did, wid, eid, reject_empty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThumbnailsApi->get_configured_element_thumbnail_with_size_thumbnails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| The cache key for the requested configuration, as generated by                      BTMicroversionIdAndConfiguration.configurationToCacheKeyString | 
 **sz** | **str**| Requested thumbnail size, such as 300x300 | 
 **did** | **str**| Document ID | 
 **wid** | **str**| Workspace ID | 
 **eid** | **str**| Element ID | 
 **reject_empty** | **bool**| If true, a 404 will be returned for thumbnails that are made for                       empty elements. Clients can use this parameter to skip the display of empty thumbnails and                       display a default icon instead. Defaults to false. | 

### Return type

[**InlineResponse20099**](InlineResponse20099.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_thumbnail_thumbnails**
> InlineResponse20098 get_document_thumbnail_thumbnails(did, wid)

Get Document Thumbnail Info

Get the thumbnail for a document in a specific workspace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: apiAccessKey
configuration = swagger_client.Configuration()
configuration.api_key['ACCESS_KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ACCESS_KEY'] = 'Bearer'
# Configure API key authorization: apiSecretKey
configuration = swagger_client.Configuration()
configuration.api_key['SECRET_KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SECRET_KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ThumbnailsApi(swagger_client.ApiClient(configuration))
did = 'did_example' # str | Document ID
wid = 'wid_example' # str | Workspace ID

try:
    # Get Document Thumbnail Info
    api_response = api_instance.get_document_thumbnail_thumbnails(did, wid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThumbnailsApi->get_document_thumbnail_thumbnails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| Document ID | 
 **wid** | **str**| Workspace ID | 

### Return type

[**InlineResponse20098**](InlineResponse20098.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_thumbnail_with_size_thumbnails**
> InlineResponse20099 get_document_thumbnail_with_size_thumbnails(sz, did, wid)

Get Thumbnail With Size

Return thumbnail for document, with specified size in pixels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: apiAccessKey
configuration = swagger_client.Configuration()
configuration.api_key['ACCESS_KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ACCESS_KEY'] = 'Bearer'
# Configure API key authorization: apiSecretKey
configuration = swagger_client.Configuration()
configuration.api_key['SECRET_KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SECRET_KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ThumbnailsApi(swagger_client.ApiClient(configuration))
sz = 'sz_example' # str | Requested thumbnail size, such as 300x300
did = 'did_example' # str | Document ID
wid = 'wid_example' # str | Workspace ID

try:
    # Get Thumbnail With Size
    api_response = api_instance.get_document_thumbnail_with_size_thumbnails(sz, did, wid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThumbnailsApi->get_document_thumbnail_with_size_thumbnails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sz** | **str**| Requested thumbnail size, such as 300x300 | 
 **did** | **str**| Document ID | 
 **wid** | **str**| Workspace ID | 

### Return type

[**InlineResponse20099**](InlineResponse20099.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_thumbnail_thumbnails**
> InlineResponse20098 get_element_thumbnail_thumbnails(wv_char, did, wv, eid)

Get Element Thumbnail Info

Return thumbnail info for an element tab

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: apiAccessKey
configuration = swagger_client.Configuration()
configuration.api_key['ACCESS_KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ACCESS_KEY'] = 'Bearer'
# Configure API key authorization: apiSecretKey
configuration = swagger_client.Configuration()
configuration.api_key['SECRET_KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SECRET_KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ThumbnailsApi(swagger_client.ApiClient(configuration))
wv_char = 'wv_char_example' # str | One of w or v corresponding to whether a workspace or version was entered.
did = 'did_example' # str | Document ID
wv = 'wv_example' # str | Workspace (w) or Version (v) ID
eid = 'eid_example' # str | Element ID

try:
    # Get Element Thumbnail Info
    api_response = api_instance.get_element_thumbnail_thumbnails(wv_char, did, wv, eid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThumbnailsApi->get_element_thumbnail_thumbnails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wv_char** | **str**| One of w or v corresponding to whether a workspace or version was entered. | 
 **did** | **str**| Document ID | 
 **wv** | **str**| Workspace (w) or Version (v) ID | 
 **eid** | **str**| Element ID | 

### Return type

[**InlineResponse20098**](InlineResponse20098.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_thumbnail_with_size_thumbnails**
> InlineResponse20099 get_element_thumbnail_with_size_thumbnails(sz, did, wid, eid, reject_empty)

Get Element Thumbnail With Size

Return thumbnail for element, with specified size in pixels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: apiAccessKey
configuration = swagger_client.Configuration()
configuration.api_key['ACCESS_KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ACCESS_KEY'] = 'Bearer'
# Configure API key authorization: apiSecretKey
configuration = swagger_client.Configuration()
configuration.api_key['SECRET_KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SECRET_KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ThumbnailsApi(swagger_client.ApiClient(configuration))
sz = 'sz_example' # str | Requested thumbnail size, such as 300x300
did = 'did_example' # str | Document ID
wid = 'wid_example' # str | Workspace ID
eid = 'eid_example' # str | Element ID
reject_empty = true # bool | If true, a 404 will be returned for thumbnails that are made for                       empty elements. Clients can use this parameter to skip the display of empty thumbnails and                       display a default icon instead. Defaults to false.

try:
    # Get Element Thumbnail With Size
    api_response = api_instance.get_element_thumbnail_with_size_thumbnails(sz, did, wid, eid, reject_empty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThumbnailsApi->get_element_thumbnail_with_size_thumbnails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sz** | **str**| Requested thumbnail size, such as 300x300 | 
 **did** | **str**| Document ID | 
 **wid** | **str**| Workspace ID | 
 **eid** | **str**| Element ID | 
 **reject_empty** | **bool**| If true, a 404 will be returned for thumbnails that are made for                       empty elements. Clients can use this parameter to skip the display of empty thumbnails and                       display a default icon instead. Defaults to false. | 

### Return type

[**InlineResponse20099**](InlineResponse20099.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thumbnail_for_document_and_version_thumbnails**
> InlineResponse20098 get_thumbnail_for_document_and_version_thumbnails(did, vid, link_document_id=link_document_id)

Get Thumbnail Info For Document Version

Return thumbnail info for document at specified version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: apiAccessKey
configuration = swagger_client.Configuration()
configuration.api_key['ACCESS_KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ACCESS_KEY'] = 'Bearer'
# Configure API key authorization: apiSecretKey
configuration = swagger_client.Configuration()
configuration.api_key['SECRET_KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SECRET_KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ThumbnailsApi(swagger_client.ApiClient(configuration))
did = 'did_example' # str | Document ID
vid = 'vid_example' # str | Version ID
link_document_id = 'link_document_id_example' # str | Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. (optional)

try:
    # Get Thumbnail Info For Document Version
    api_response = api_instance.get_thumbnail_for_document_and_version_thumbnails(did, vid, link_document_id=link_document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThumbnailsApi->get_thumbnail_for_document_and_version_thumbnails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| Document ID | 
 **vid** | **str**| Version ID | 
 **link_document_id** | **str**| Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. | [optional] 

### Return type

[**InlineResponse20098**](InlineResponse20098.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thumbnail_for_document_thumbnails**
> InlineResponse20098 get_thumbnail_for_document_thumbnails(did)

Get Default Workspace Thumbnail Info

Get thumbnail info for document in default workspace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: apiAccessKey
configuration = swagger_client.Configuration()
configuration.api_key['ACCESS_KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ACCESS_KEY'] = 'Bearer'
# Configure API key authorization: apiSecretKey
configuration = swagger_client.Configuration()
configuration.api_key['SECRET_KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SECRET_KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ThumbnailsApi(swagger_client.ApiClient(configuration))
did = 'did_example' # str | Document ID

try:
    # Get Default Workspace Thumbnail Info
    api_response = api_instance.get_thumbnail_for_document_thumbnails(did)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThumbnailsApi->get_thumbnail_for_document_thumbnails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| Document ID | 

### Return type

[**InlineResponse20098**](InlineResponse20098.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_application_element_thumbnail_thumbnails**
> set_application_element_thumbnail_thumbnails(wv_char, did, wv, eid, overwrite=overwrite, body=body)

Set Application Element Thumbnail

Set element thumbnails for an application element

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: apiAccessKey
configuration = swagger_client.Configuration()
configuration.api_key['ACCESS_KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ACCESS_KEY'] = 'Bearer'
# Configure API key authorization: apiSecretKey
configuration = swagger_client.Configuration()
configuration.api_key['SECRET_KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SECRET_KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ThumbnailsApi(swagger_client.ApiClient(configuration))
wv_char = 'wv_char_example' # str | One of w or v corresponding to whether a workspace or version was entered.
did = 'did_example' # str | Document ID
wv = 'wv_example' # str | Workspace (w) or Version (v) ID
eid = 'eid_example' # str | Element ID
overwrite = true # bool | Set to true when a different thumbnail needs to be made the primary thumbnail or secondary thumbnails need to be updated. This deletes all associated thumbnails and then sets the new thumbnails.                                                     Ensure that the primary and all non-primary thumbnails information are specified. (optional)
body = swagger_client.Body45() # Body45 | The JSON request body. (optional)

try:
    # Set Application Element Thumbnail
    api_instance.set_application_element_thumbnail_thumbnails(wv_char, did, wv, eid, overwrite=overwrite, body=body)
except ApiException as e:
    print("Exception when calling ThumbnailsApi->set_application_element_thumbnail_thumbnails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wv_char** | **str**| One of w or v corresponding to whether a workspace or version was entered. | 
 **did** | **str**| Document ID | 
 **wv** | **str**| Workspace (w) or Version (v) ID | 
 **eid** | **str**| Element ID | 
 **overwrite** | **bool**| Set to true when a different thumbnail needs to be made the primary thumbnail or secondary thumbnails need to be updated. This deletes all associated thumbnails and then sets the new thumbnails.                                                     Ensure that the primary and all non-primary thumbnails information are specified. | [optional] 
 **body** | [**Body45**](Body45.md)| The JSON request body. | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

