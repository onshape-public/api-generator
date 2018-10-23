# swagger_client.BillingApi

All URIs are relative to *https://cad.onshape.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_plans_billing**](BillingApi.md#get_client_plans_billing) | **GET** /billing/plans/client/{cid} | Get billing plans for client.


# **get_client_plans_billing**
> InlineResponse20030 get_client_plans_billing(cid)

Get billing plans for client.

Returns billing plans for specified client (associated with application). This API is expected to be     used in a context of OAuth-enabled application.

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
api_instance = swagger_client.BillingApi(swagger_client.ApiClient(configuration))
cid = 'cid_example' # str | Client Id

try:
    # Get billing plans for client.
    api_response = api_instance.get_client_plans_billing(cid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_client_plans_billing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| Client Id | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

