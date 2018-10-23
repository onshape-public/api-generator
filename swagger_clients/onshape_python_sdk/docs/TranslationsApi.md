# swagger_client.TranslationsApi

All URIs are relative to *https://cad.onshape.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_translation_translations**](TranslationsApi.md#create_translation_translations) | **POST** /translations/d/{did}/w/{wid} | Create translation from upload
[**delete_translation_translations**](TranslationsApi.md#delete_translation_translations) | **DELETE** /translations/{tid} | Delete Translation Status entry
[**get_translation_translations**](TranslationsApi.md#get_translation_translations) | **GET** /translations/{tid} | Get Translation Status
[**get_translations_translations**](TranslationsApi.md#get_translations_translations) | **GET** /translations/d/{did} | Get Translation Status for a document
[**get_translator_formats_translations**](TranslationsApi.md#get_translator_formats_translations) | **GET** /translations/translationformats | Get Translation Formats


# **create_translation_translations**
> InlineResponse20020 create_translation_translations(file, format_name, flatten_assemblies, y_axis_is_up, store_in_document, did, wid, version_string=version_string, notify_user=notify_user, import_in_background=import_in_background, allow_faulty_parts=allow_faulty_parts)

Create translation from upload

Create a translation of the input data. The translation may be incomplete at the time that the                 call completes. If the requestState is ACTIVE, the translation can be polled until the state                 becomes either DONE or FAILED. Alternatively, a webhook callback can be registered for                 notification of translation completion.

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
api_instance = swagger_client.TranslationsApi(swagger_client.ApiClient(configuration))
file = '/path/to/file.txt' # file | File to upload
format_name = 'format_name_example' # str | Name of format into which this element should be translated. ONSHAPE        indicates that the model file should be translated into a Part Studio or Assembly.
flatten_assemblies = true # bool | If true, remove assembly structure and create only a        Part Studio
y_axis_is_up = true # bool | If true, treat the model's Y axis as the vertical axis.  Otherwise,        Z is treated as the vertical axis.
store_in_document = true # bool | controls whether the translation is stored as a new element or        whether the data is stored as external data (storeInDocument=false).
did = 'did_example' # str | Document ID
wid = 'wid_example' # str | Workspace ID
version_string = 'version_string_example' # str | Version of output format to use (format-dependent) (optional)
notify_user = true # bool | Whether a user notification should be generated on completion (optional)
import_in_background = true # bool | If storeInDocument is true and formatName is ONSHAPE and        the source is a Parasolid file, this specifies the preference as to whether the import should be completed        prior to the completion of the request (importInBackground=false) or whether it should be performed        asynchronously (importInBackground=true). Historically, this parameter was implicitly set to false, but large        imports can take long enough that the request could result in a timeout. Applications are encouraged to set        this parameter to true for reliable operation. (optional)
allow_faulty_parts = true # bool | If not specified or if specified as false, bodies to be imported        are examined for validity and any found to be faulty are removed from the import. If all bodies are found to        be faulty, the import fails. If the value is specified as true, we attempt to import the bodies that appear to        have faults. (optional)

try:
    # Create translation from upload
    api_response = api_instance.create_translation_translations(file, format_name, flatten_assemblies, y_axis_is_up, store_in_document, did, wid, version_string=version_string, notify_user=notify_user, import_in_background=import_in_background, allow_faulty_parts=allow_faulty_parts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationsApi->create_translation_translations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to upload | 
 **format_name** | **str**| Name of format into which this element should be translated. ONSHAPE        indicates that the model file should be translated into a Part Studio or Assembly. | 
 **flatten_assemblies** | **bool**| If true, remove assembly structure and create only a        Part Studio | 
 **y_axis_is_up** | **bool**| If true, treat the model&#39;s Y axis as the vertical axis.  Otherwise,        Z is treated as the vertical axis. | 
 **store_in_document** | **bool**| controls whether the translation is stored as a new element or        whether the data is stored as external data (storeInDocument&#x3D;false). | 
 **did** | **str**| Document ID | 
 **wid** | **str**| Workspace ID | 
 **version_string** | **str**| Version of output format to use (format-dependent) | [optional] 
 **notify_user** | **bool**| Whether a user notification should be generated on completion | [optional] 
 **import_in_background** | **bool**| If storeInDocument is true and formatName is ONSHAPE and        the source is a Parasolid file, this specifies the preference as to whether the import should be completed        prior to the completion of the request (importInBackground&#x3D;false) or whether it should be performed        asynchronously (importInBackground&#x3D;true). Historically, this parameter was implicitly set to false, but large        imports can take long enough that the request could result in a timeout. Applications are encouraged to set        this parameter to true for reliable operation. | [optional] 
 **allow_faulty_parts** | **bool**| If not specified or if specified as false, bodies to be imported        are examined for validity and any found to be faulty are removed from the import. If all bodies are found to        be faulty, the import fails. If the value is specified as true, we attempt to import the bodies that appear to        have faults. | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_translation_translations**
> delete_translation_translations(tid)

Delete Translation Status entry

Delete translation status

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
api_instance = swagger_client.TranslationsApi(swagger_client.ApiClient(configuration))
tid = 'tid_example' # str | Translation ID

try:
    # Delete Translation Status entry
    api_instance.delete_translation_translations(tid)
except ApiException as e:
    print("Exception when calling TranslationsApi->delete_translation_translations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tid** | **str**| Translation ID | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_translation_translations**
> InlineResponse20020 get_translation_translations(tid)

Get Translation Status

Get element translation status

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
api_instance = swagger_client.TranslationsApi(swagger_client.ApiClient(configuration))
tid = 'tid_example' # str | Translation ID

try:
    # Get Translation Status
    api_response = api_instance.get_translation_translations(tid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationsApi->get_translation_translations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tid** | **str**| Translation ID | 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_translations_translations**
> InlineResponse200101 get_translations_translations(did, offset, limit)

Get Translation Status for a document

Get list of translation status entries for a document

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
api_instance = swagger_client.TranslationsApi(swagger_client.ApiClient(configuration))
did = 'did_example' # str | Document ID
offset = 8.14 # float | Offset into list of items
limit = 8.14 # float | Maximum number to retrieve (Must be <= 20)

try:
    # Get Translation Status for a document
    api_response = api_instance.get_translations_translations(did, offset, limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationsApi->get_translations_translations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| Document ID | 
 **offset** | **float**| Offset into list of items | 
 **limit** | **float**| Maximum number to retrieve (Must be &lt;&#x3D; 20) | 

### Return type

[**InlineResponse200101**](InlineResponse200101.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_translator_formats_translations**
> InlineResponse200100 get_translator_formats_translations()

Get Translation Formats

Get a list of all translator formats. Some are valid only as input formats and cannot be used as                 an output format.

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
api_instance = swagger_client.TranslationsApi(swagger_client.ApiClient(configuration))

try:
    # Get Translation Formats
    api_response = api_instance.get_translator_formats_translations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationsApi->get_translator_formats_translations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200100**](InlineResponse200100.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

