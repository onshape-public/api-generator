# swagger_client.AppElementsApi

All URIs are relative to *https://cad.onshape.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commit_transaction_app_elements**](AppElementsApi.md#commit_transaction_app_elements) | **POST** /appelements/d/{did}/w/{wid}/e/{eid}/transactions/{tid} | Commit Transaction
[**create_element_app_elements**](AppElementsApi.md#create_element_app_elements) | **POST** /appelements/d/{did}/w/{wid} | Create Element
[**create_reference_app_elements**](AppElementsApi.md#create_reference_app_elements) | **POST** /appelements/d/{did}/w/{wid}/e/{eid}/references | Create Reference
[**delete_content_app_elements**](AppElementsApi.md#delete_content_app_elements) | **DELETE** /appelements/d/{did}/{wvm_char}/{wvm}/e/{eid}/content/subelements/{sid} | Delete a Sub-element
[**delete_reference_app_elements**](AppElementsApi.md#delete_reference_app_elements) | **DELETE** /appelements/d/{did}/w/{wid}/e/{eid}/references/{rid} | Delete Reference
[**get_history_by_workspace_app_elements**](AppElementsApi.md#get_history_by_workspace_app_elements) | **GET** /appelements/d/{did}/{wvm_char}/{wvm}/e/{eid}/content/history | Get History
[**get_sub_element_content_app_elements**](AppElementsApi.md#get_sub_element_content_app_elements) | **GET** /appelements/d/{did}/{wvm_char}/{wvm}/e/{eid}/content | Get Content
[**get_sub_element_ids_app_elements**](AppElementsApi.md#get_sub_element_ids_app_elements) | **GET** /appelements/d/{did}/{wvm_char}/{wvm}/e/{eid}/content/ids/ | Get Sub-element IDs
[**resolve_reference_app_elements**](AppElementsApi.md#resolve_reference_app_elements) | **GET** /appelements/d/{did}/{wvm_char}/{wvm}/e/{eid}/references/{rid} | Resolve Reference
[**start_transaction_app_elements**](AppElementsApi.md#start_transaction_app_elements) | **POST** /appelements/d/{did}/w/{wid}/e/{eid}/transactions/ | Start Transaction
[**update_element_app_elements**](AppElementsApi.md#update_element_app_elements) | **POST** /appelements/d/{did}/w/{wid}/e/{eid}/content | Update Element
[**update_reference_app_elements**](AppElementsApi.md#update_reference_app_elements) | **POST** /appelements/d/{did}/w/{wid}/e/{eid}/references/{rid} | Update Reference


# **commit_transaction_app_elements**
> InlineResponse2003 commit_transaction_app_elements(tid, did, wid, eid, body=body)

Commit Transaction

Commits a transaction (merges a microbranch)

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
api_instance = swagger_client.AppElementsApi(swagger_client.ApiClient(configuration))
tid = 'tid_example' # str | Id of the transaction to commit
did = 'did_example' # str | Document ID
wid = 'wid_example' # str | Workspace ID
eid = 'eid_example' # str | Element ID
body = swagger_client.Body() # Body | The JSON request body. (optional)

try:
    # Commit Transaction
    api_response = api_instance.commit_transaction_app_elements(tid, did, wid, eid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppElementsApi->commit_transaction_app_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tid** | **str**| Id of the transaction to commit | 
 **did** | **str**| Document ID | 
 **wid** | **str**| Workspace ID | 
 **eid** | **str**| Element ID | 
 **body** | [**Body**](Body.md)| The JSON request body. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_element_app_elements**
> InlineResponse2004 create_element_app_elements(did, wid, body=body)

Create Element

Create an app element

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
api_instance = swagger_client.AppElementsApi(swagger_client.ApiClient(configuration))
did = 'did_example' # str | Document ID
wid = 'wid_example' # str | Workspace ID
body = swagger_client.Body1() # Body1 | The JSON request body. (optional)

try:
    # Create Element
    api_response = api_instance.create_element_app_elements(did, wid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppElementsApi->create_element_app_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| Document ID | 
 **wid** | **str**| Workspace ID | 
 **body** | [**Body1**](Body1.md)| The JSON request body. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_reference_app_elements**
> InlineResponse2005 create_reference_app_elements(did, wid, eid, body=body)

Create Reference

Create an app element reference

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
api_instance = swagger_client.AppElementsApi(swagger_client.ApiClient(configuration))
did = 'did_example' # str | Document ID
wid = 'wid_example' # str | Workspace ID
eid = 'eid_example' # str | Element ID
body = swagger_client.Body2() # Body2 | The JSON request body. (optional)

try:
    # Create Reference
    api_response = api_instance.create_reference_app_elements(did, wid, eid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppElementsApi->create_reference_app_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| Document ID | 
 **wid** | **str**| Workspace ID | 
 **eid** | **str**| Element ID | 
 **body** | [**Body2**](Body2.md)| The JSON request body. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_content_app_elements**
> InlineResponse2008 delete_content_app_elements(wvm_char, sid, did, wvm, eid, parent_change_id=parent_change_id, transaction_id=transaction_id, description=description)

Delete a Sub-element

Deletes a sub-element of an application element

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
api_instance = swagger_client.AppElementsApi(swagger_client.ApiClient(configuration))
wvm_char = 'wvm_char_example' # str | One of w or v or m corresponding to whether a workspace or version or microversion was entered.
sid = 'sid_example' # str | The id of the subelement to be deleted. URL-encode if needed
did = 'did_example' # str | Document ID
wvm = 'wvm_example' # str | Workspace (w), Version (v) or Microversion (m) ID
eid = 'eid_example' # str | Element ID
parent_change_id = 'parent_change_id_example' # str | Id of the last change made by this application to this element (optional)
transaction_id = 'transaction_id_example' # str | Id of the transaction to commit (optional)
description = 'description_example' # str | Description of the deletion operation for history (optional)

try:
    # Delete a Sub-element
    api_response = api_instance.delete_content_app_elements(wvm_char, sid, did, wvm, eid, parent_change_id=parent_change_id, transaction_id=transaction_id, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppElementsApi->delete_content_app_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wvm_char** | **str**| One of w or v or m corresponding to whether a workspace or version or microversion was entered. | 
 **sid** | **str**| The id of the subelement to be deleted. URL-encode if needed | 
 **did** | **str**| Document ID | 
 **wvm** | **str**| Workspace (w), Version (v) or Microversion (m) ID | 
 **eid** | **str**| Element ID | 
 **parent_change_id** | **str**| Id of the last change made by this application to this element | [optional] 
 **transaction_id** | **str**| Id of the transaction to commit | [optional] 
 **description** | **str**| Description of the deletion operation for history | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reference_app_elements**
> InlineResponse2007 delete_reference_app_elements(rid, did, wid, eid, parent_change_id=parent_change_id, transaction_id=transaction_id, description=description)

Delete Reference

Delete an app element reference

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
api_instance = swagger_client.AppElementsApi(swagger_client.ApiClient(configuration))
rid = 'rid_example' # str | The id of the reference to be deleted
did = 'did_example' # str | Document ID
wid = 'wid_example' # str | Workspace ID
eid = 'eid_example' # str | Element ID
parent_change_id = 'parent_change_id_example' # str | Id of the last change made by this application to this element (optional)
transaction_id = 'transaction_id_example' # str | Id of the transaction to commit (optional)
description = 'description_example' # str | Description of the deletion operation for history (optional)

try:
    # Delete Reference
    api_response = api_instance.delete_reference_app_elements(rid, did, wid, eid, parent_change_id=parent_change_id, transaction_id=transaction_id, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppElementsApi->delete_reference_app_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rid** | **str**| The id of the reference to be deleted | 
 **did** | **str**| Document ID | 
 **wid** | **str**| Workspace ID | 
 **eid** | **str**| Element ID | 
 **parent_change_id** | **str**| Id of the last change made by this application to this element | [optional] 
 **transaction_id** | **str**| Id of the transaction to commit | [optional] 
 **description** | **str**| Description of the deletion operation for history | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_history_by_workspace_app_elements**
> InlineResponse20010 get_history_by_workspace_app_elements(wvm_char, did, wvm, eid)

Get History

Get change history

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
api_instance = swagger_client.AppElementsApi(swagger_client.ApiClient(configuration))
wvm_char = 'wvm_char_example' # str | One of w or v or m corresponding to whether a workspace or version or microversion was entered.
did = 'did_example' # str | Document ID
wvm = 'wvm_example' # str | Workspace (w), Version (v) or Microversion (m) ID
eid = 'eid_example' # str | Element ID

try:
    # Get History
    api_response = api_instance.get_history_by_workspace_app_elements(wvm_char, did, wvm, eid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppElementsApi->get_history_by_workspace_app_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wvm_char** | **str**| One of w or v or m corresponding to whether a workspace or version or microversion was entered. | 
 **did** | **str**| Document ID | 
 **wvm** | **str**| Workspace (w), Version (v) or Microversion (m) ID | 
 **eid** | **str**| Element ID | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sub_element_content_app_elements**
> InlineResponse2009 get_sub_element_content_app_elements(wvm_char, did, wvm, eid, transaction_id=transaction_id, change_id=change_id, base_change_id=base_change_id, subelement_id=subelement_id, link_document_id=link_document_id)

Get Content

Get content of sub-elements in a workspace

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
api_instance = swagger_client.AppElementsApi(swagger_client.ApiClient(configuration))
wvm_char = 'wvm_char_example' # str | One of w or v or m corresponding to whether a workspace or version or microversion was entered.
did = 'did_example' # str | Document ID
wvm = 'wvm_example' # str | Workspace (w), Version (v) or Microversion (m) ID
eid = 'eid_example' # str | Element ID
transaction_id = 'transaction_id_example' # str | Id of the transaction in which the ids should be retrieved.   Valid only when used with a workspaceId (optional)
change_id = 'change_id_example' # str | Id of the change at which the ids should be retrieved.  If not   specified, defaults to the latest change in the workspace, version or microversion.  May be specified only   when used with a workspaceId (optional)
base_change_id = 'base_change_id_example' # str | Id of a change made prior to the specified or implied changeId.   If specified, only changes made after the base changeId are returned. (optional)
subelement_id = 'subelement_id_example' # str | Id of a sub-element to use as a restriction for returned data (optional)
link_document_id = 'link_document_id_example' # str | Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. (optional)

try:
    # Get Content
    api_response = api_instance.get_sub_element_content_app_elements(wvm_char, did, wvm, eid, transaction_id=transaction_id, change_id=change_id, base_change_id=base_change_id, subelement_id=subelement_id, link_document_id=link_document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppElementsApi->get_sub_element_content_app_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wvm_char** | **str**| One of w or v or m corresponding to whether a workspace or version or microversion was entered. | 
 **did** | **str**| Document ID | 
 **wvm** | **str**| Workspace (w), Version (v) or Microversion (m) ID | 
 **eid** | **str**| Element ID | 
 **transaction_id** | **str**| Id of the transaction in which the ids should be retrieved.   Valid only when used with a workspaceId | [optional] 
 **change_id** | **str**| Id of the change at which the ids should be retrieved.  If not   specified, defaults to the latest change in the workspace, version or microversion.  May be specified only   when used with a workspaceId | [optional] 
 **base_change_id** | **str**| Id of a change made prior to the specified or implied changeId.   If specified, only changes made after the base changeId are returned. | [optional] 
 **subelement_id** | **str**| Id of a sub-element to use as a restriction for returned data | [optional] 
 **link_document_id** | **str**| Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sub_element_ids_app_elements**
> InlineResponse20011 get_sub_element_ids_app_elements(wvm_char, did, wvm, eid, transaction_id=transaction_id, change_id=change_id)

Get Sub-element IDs

Gets a list of all sub-element IDs of a workspace/microversion/version

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
api_instance = swagger_client.AppElementsApi(swagger_client.ApiClient(configuration))
wvm_char = 'wvm_char_example' # str | One of w or v or m corresponding to whether a workspace or version or microversion was entered.
did = 'did_example' # str | Document ID
wvm = 'wvm_example' # str | Workspace (w), Version (v) or Microversion (m) ID
eid = 'eid_example' # str | Element ID
transaction_id = 'transaction_id_example' # str | Id of the transaction in which the ids should be retrieved   Valid only when used with a workspaceId (optional)
change_id = 'change_id_example' # str | Id of the change at which the ids should be retrieved   Valid only when used with a workspaceId (optional)

try:
    # Get Sub-element IDs
    api_response = api_instance.get_sub_element_ids_app_elements(wvm_char, did, wvm, eid, transaction_id=transaction_id, change_id=change_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppElementsApi->get_sub_element_ids_app_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wvm_char** | **str**| One of w or v or m corresponding to whether a workspace or version or microversion was entered. | 
 **did** | **str**| Document ID | 
 **wvm** | **str**| Workspace (w), Version (v) or Microversion (m) ID | 
 **eid** | **str**| Element ID | 
 **transaction_id** | **str**| Id of the transaction in which the ids should be retrieved   Valid only when used with a workspaceId | [optional] 
 **change_id** | **str**| Id of the change at which the ids should be retrieved   Valid only when used with a workspaceId | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_reference_app_elements**
> InlineResponse20012 resolve_reference_app_elements(wvm_char, rid, did, wvm, eid, transaction_id=transaction_id, parent_change_id=parent_change_id, link_document_id=link_document_id)

Resolve Reference

Resolve an app element reference

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
api_instance = swagger_client.AppElementsApi(swagger_client.ApiClient(configuration))
wvm_char = 'wvm_char_example' # str | One of w or v or m corresponding to whether a workspace or version or microversion was entered.
rid = 'rid_example' # str | The id of the reference to read
did = 'did_example' # str | Document ID
wvm = 'wvm_example' # str | Workspace (w), Version (v) or Microversion (m) ID
eid = 'eid_example' # str | Element ID
transaction_id = 'transaction_id_example' # str | Id of the transaction in which the reference should be retrieved           Valid only when used with a workspaceId (optional)
parent_change_id = 'parent_change_id_example' # str | Id of the change at which the reference should be retrieved           Valid only when used with a workspaceId (optional)
link_document_id = 'link_document_id_example' # str | Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. (optional)

try:
    # Resolve Reference
    api_response = api_instance.resolve_reference_app_elements(wvm_char, rid, did, wvm, eid, transaction_id=transaction_id, parent_change_id=parent_change_id, link_document_id=link_document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppElementsApi->resolve_reference_app_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wvm_char** | **str**| One of w or v or m corresponding to whether a workspace or version or microversion was entered. | 
 **rid** | **str**| The id of the reference to read | 
 **did** | **str**| Document ID | 
 **wvm** | **str**| Workspace (w), Version (v) or Microversion (m) ID | 
 **eid** | **str**| Element ID | 
 **transaction_id** | **str**| Id of the transaction in which the reference should be retrieved           Valid only when used with a workspaceId | [optional] 
 **parent_change_id** | **str**| Id of the change at which the reference should be retrieved           Valid only when used with a workspaceId | [optional] 
 **link_document_id** | **str**| Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_transaction_app_elements**
> InlineResponse20013 start_transaction_app_elements(did, wid, eid, body=body)

Start Transaction

Start a transaction (creates a microbranch)

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
api_instance = swagger_client.AppElementsApi(swagger_client.ApiClient(configuration))
did = 'did_example' # str | Document ID
wid = 'wid_example' # str | Workspace ID
eid = 'eid_example' # str | Element ID
body = swagger_client.Body4() # Body4 | The JSON request body. (optional)

try:
    # Start Transaction
    api_response = api_instance.start_transaction_app_elements(did, wid, eid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppElementsApi->start_transaction_app_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| Document ID | 
 **wid** | **str**| Workspace ID | 
 **eid** | **str**| Element ID | 
 **body** | [**Body4**](Body4.md)| The JSON request body. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_element_app_elements**
> InlineResponse20014 update_element_app_elements(did, wid, eid, body=body)

Update Element

Update an app element

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
api_instance = swagger_client.AppElementsApi(swagger_client.ApiClient(configuration))
did = 'did_example' # str | Document ID
wid = 'wid_example' # str | Workspace ID
eid = 'eid_example' # str | Element ID
body = swagger_client.Body5() # Body5 | The JSON request body. (optional)

try:
    # Update Element
    api_response = api_instance.update_element_app_elements(did, wid, eid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppElementsApi->update_element_app_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| Document ID | 
 **wid** | **str**| Workspace ID | 
 **eid** | **str**| Element ID | 
 **body** | [**Body5**](Body5.md)| The JSON request body. | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reference_app_elements**
> InlineResponse2006 update_reference_app_elements(rid, did, wid, eid, body=body)

Update Reference

Update an app element reference

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
api_instance = swagger_client.AppElementsApi(swagger_client.ApiClient(configuration))
rid = 'rid_example' # str | The id of a reference to update
did = 'did_example' # str | Document ID
wid = 'wid_example' # str | Workspace ID
eid = 'eid_example' # str | Element ID
body = swagger_client.Body3() # Body3 | The JSON request body. (optional)

try:
    # Update Reference
    api_response = api_instance.update_reference_app_elements(rid, did, wid, eid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppElementsApi->update_reference_app_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rid** | **str**| The id of a reference to update | 
 **did** | **str**| Document ID | 
 **wid** | **str**| Workspace ID | 
 **eid** | **str**| Element ID | 
 **body** | [**Body3**](Body3.md)| The JSON request body. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

