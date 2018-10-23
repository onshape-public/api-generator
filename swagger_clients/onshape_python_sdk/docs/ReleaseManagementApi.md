# swagger_client.ReleaseManagementApi

All URIs are relative to *https://cad.onshape.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_obsoletion_package_release_management**](ReleaseManagementApi.md#create_obsoletion_package_release_management) | **POST** /releasepackages/obsoletion/{wfid} | Create obsoletion package
[**create_release_package_release_management**](ReleaseManagementApi.md#create_release_package_release_management) | **POST** /releasepackages/release/{wfid} | Create release package
[**get_company_release_workflow_release_management**](ReleaseManagementApi.md#get_company_release_workflow_release_management) | **GET** /releasepackages/companyreleaseworkflow | release workflow details
[**get_release_package_release_management**](ReleaseManagementApi.md#get_release_package_release_management) | **GET** /releasepackages/{rpid} | Get Release Package by id
[**update_release_package_release_management**](ReleaseManagementApi.md#update_release_package_release_management) | **POST** /releasepackages/{rpid} | Update Release Package


# **create_obsoletion_package_release_management**
> InlineResponse20091 create_obsoletion_package_release_management(wfid, revision_id)

Create obsoletion package

Create an obsoletion package to make an existing revision obsolete. Once a release package has                 been successfully created use the updateReleasePackage to transition it to desired state

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
api_instance = swagger_client.ReleaseManagementApi(swagger_client.ApiClient(configuration))
wfid = 'wfid_example' # str | ID of obsoletion workflow as returned by getCompanyReleaseWorkflow
revision_id = 'revision_id_example' # str | ID of revision to be obsoleted as returned by           getRevisionHistoryInCompany

try:
    # Create obsoletion package
    api_response = api_instance.create_obsoletion_package_release_management(wfid, revision_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleaseManagementApi->create_obsoletion_package_release_management: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wfid** | **str**| ID of obsoletion workflow as returned by getCompanyReleaseWorkflow | 
 **revision_id** | **str**| ID of revision to be obsoleted as returned by           getRevisionHistoryInCompany | 

### Return type

[**InlineResponse20091**](InlineResponse20091.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_release_package_release_management**
> InlineResponse20092 create_release_package_release_management(wfid, body=body)

Create release package

Create a new release package to release one or more items. All revisionable items must be from                 the same document. Once a release package has been successfully created use the                 updateReleasePackage to update all desired item/package properties and transition it to desired                 state.

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
api_instance = swagger_client.ReleaseManagementApi(swagger_client.ApiClient(configuration))
wfid = 'wfid_example' # str | ID of release workflow as returned by getCompanyReleaseWorkflow
body = swagger_client.Body43() # Body43 | The JSON request body. (optional)

try:
    # Create release package
    api_response = api_instance.create_release_package_release_management(wfid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleaseManagementApi->create_release_package_release_management: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wfid** | **str**| ID of release workflow as returned by getCompanyReleaseWorkflow | 
 **body** | [**Body43**](Body43.md)| The JSON request body. | [optional] 

### Return type

[**InlineResponse20092**](InlineResponse20092.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_release_workflow_release_management**
> InlineResponse20094 get_company_release_workflow_release_management(document_id)

release workflow details

Information about the release/obsoletion workflow in use by a company owned document

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
api_instance = swagger_client.ReleaseManagementApi(swagger_client.ApiClient(configuration))
document_id = 'document_id_example' # str | Document ID that is owned by company for which workflow is requested.

try:
    # release workflow details
    api_response = api_instance.get_company_release_workflow_release_management(document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleaseManagementApi->get_company_release_workflow_release_management: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document ID that is owned by company for which workflow is requested. | 

### Return type

[**InlineResponse20094**](InlineResponse20094.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release_package_release_management**
> InlineResponse20093 get_release_package_release_management(rpid, detailed=detailed)

Get Release Package by id

Returns detailed information about a release package with specified id

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
api_instance = swagger_client.ReleaseManagementApi(swagger_client.ApiClient(configuration))
rpid = 'rpid_example' # str | ID of package to get detailed information for
detailed = true # bool | Whether to return detailed property information about all           items. (optional)

try:
    # Get Release Package by id
    api_response = api_instance.get_release_package_release_management(rpid, detailed=detailed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleaseManagementApi->get_release_package_release_management: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpid** | **str**| ID of package to get detailed information for | 
 **detailed** | **bool**| Whether to return detailed property information about all           items. | [optional] 

### Return type

[**InlineResponse20093**](InlineResponse20093.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_release_package_release_management**
> update_release_package_release_management(rpid, wfaction, body=body)

Update Release Package

Update the release/obsoletion package properties and/or item properties and transition it to                 desired state

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
api_instance = swagger_client.ReleaseManagementApi(swagger_client.ApiClient(configuration))
rpid = 'rpid_example' # str | ID of package to transition
wfaction = 'wfaction_example' # str | Workflow action to perform on the package. Allowed values are SUBMIT,           CREATE_AND_RELEASE, RELEASE, REJECT, OBSOLETE, DISCARD or CREATE_AND_OBSOLETE. DISCARD can only be           performed by the creator of the package and is the only transition that can be performed even if items           have errors. CREATE_AND_RELEASE and CREATE_AND_OBSOLETE can only be performed by creator if the Release           management settings for the company allow release without approvers. If Release management settings           restrict the approver list to a subset of company users, Only those users can perform transitions.
body = swagger_client.Body44() # Body44 | The JSON request body. (optional)

try:
    # Update Release Package
    api_instance.update_release_package_release_management(rpid, wfaction, body=body)
except ApiException as e:
    print("Exception when calling ReleaseManagementApi->update_release_package_release_management: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpid** | **str**| ID of package to transition | 
 **wfaction** | **str**| Workflow action to perform on the package. Allowed values are SUBMIT,           CREATE_AND_RELEASE, RELEASE, REJECT, OBSOLETE, DISCARD or CREATE_AND_OBSOLETE. DISCARD can only be           performed by the creator of the package and is the only transition that can be performed even if items           have errors. CREATE_AND_RELEASE and CREATE_AND_OBSOLETE can only be performed by creator if the Release           management settings for the company allow release without approvers. If Release management settings           restrict the approver list to a subset of company users, Only those users can perform transitions. | 
 **body** | [**Body44**](Body44.md)| The JSON request body. | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

