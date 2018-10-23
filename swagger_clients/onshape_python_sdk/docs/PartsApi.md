# swagger_client.PartsApi

All URIs are relative to *https://cad.onshape.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_update_part_metadata_parts**](PartsApi.md#batch_update_part_metadata_parts) | **POST** /parts/d/{did}/{wvm_char}/{wvm} | Update Part metadata
[**export_parasolid_parts**](PartsApi.md#export_parasolid_parts) | **GET** /parts/d/{did}/{wvm_char}/{wvm}/e/{eid}/partid/{partid}/parasolid | Export Part to Parasolid
[**export_stl_parts**](PartsApi.md#export_stl_parts) | **GET** /parts/d/{did}/{wvm_char}/{wvm}/e/{eid}/partid/{partid}/stl | Export Part to STL
[**get_bend_table_parts**](PartsApi.md#get_bend_table_parts) | **GET** /parts/d/{did}/{wvm_char}/{wvm}/e/{eid}/partid/{partid}/sheetmetal/bendtable | Get Sheet Metal Bend Table
[**get_body_details_parts**](PartsApi.md#get_body_details_parts) | **GET** /parts/d/{did}/{wvm_char}/{wvm}/e/{eid}/partid/{partid}/bodydetails | Body Details
[**get_bounding_boxes_parts**](PartsApi.md#get_bounding_boxes_parts) | **GET** /parts/d/{did}/{wvm_char}/{wvm}/e/{eid}/partid/{partid}/boundingboxes | Bounding Boxes
[**get_edges_parts**](PartsApi.md#get_edges_parts) | **GET** /parts/d/{did}/{wvm_char}/{wvm}/e/{eid}/partid/{partid}/tessellatededges | Tessellated Edges
[**get_faces_parts**](PartsApi.md#get_faces_parts) | **GET** /parts/d/{did}/{wvm_char}/{wvm}/e/{eid}/partid/{partid}/tessellatedfaces | Tessellated Faces
[**get_mass_properties_parts**](PartsApi.md#get_mass_properties_parts) | **GET** /parts/d/{did}/{wvm_char}/{wvm}/e/{eid}/partid/{partid}/massproperties | Mass Properties
[**get_part_metadata_parts**](PartsApi.md#get_part_metadata_parts) | **GET** /parts/d/{did}/{wvm_char}/{wvm}/e/{eid}/partid/{partid}/metadata | Get Metadata
[**get_parts_in_partstudio_parts**](PartsApi.md#get_parts_in_partstudio_parts) | **GET** /parts/d/{did}/{wvm_char}/{wvm}/e/{eid} | Get Parts In Part Studio
[**get_parts_parts**](PartsApi.md#get_parts_parts) | **GET** /parts/d/{did}/{wvm_char}/{wvm} | Get Parts
[**get_shaded_views_parts**](PartsApi.md#get_shaded_views_parts) | **GET** /parts/d/{did}/{wvm_char}/{wvm}/e/{eid}/partid/{partid}/shadedviews | Shaded views
[**get_standard_content_part_metadata_parts**](PartsApi.md#get_standard_content_part_metadata_parts) | **GET** /parts/standardcontent/d/{did}/v/{vid}/e/{eid}/{cu_char}/{oid}/partid/{partid}/metadata | Get Standard Content Metadata
[**update_part_metadata_parts**](PartsApi.md#update_part_metadata_parts) | **POST** /parts/d/{did}/{wvm_char}/{wvm}/e/{eid}/partid/{partid}/metadata | Update Metadata
[**update_standard_content_part_metadata_parts**](PartsApi.md#update_standard_content_part_metadata_parts) | **POST** /parts/standardcontent/d/{did}/v/{vid}/e/{eid}/{cu_char}/{oid}/partid/{partid}/metadata | Update Standard Content Metadata


# **batch_update_part_metadata_parts**
> batch_update_part_metadata_parts(wvm_char, did, wvm, edit_description=edit_description, body=body)

Update Part metadata

Part metadata batch update

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
api_instance = swagger_client.PartsApi(swagger_client.ApiClient(configuration))
wvm_char = 'wvm_char_example' # str | One of w or v or m corresponding to whether a workspace or version or microversion was entered.
did = 'did_example' # str | Document ID
wvm = 'wvm_example' # str | Workspace (w), Version (v) or Microversion (m) ID
edit_description = 'edit_description_example' # str | Description of the update (as appear in document history) (optional)
body = swagger_client.Body41() # Body41 | The JSON request body. (optional)

try:
    # Update Part metadata
    api_instance.batch_update_part_metadata_parts(wvm_char, did, wvm, edit_description=edit_description, body=body)
except ApiException as e:
    print("Exception when calling PartsApi->batch_update_part_metadata_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wvm_char** | **str**| One of w or v or m corresponding to whether a workspace or version or microversion was entered. | 
 **did** | **str**| Document ID | 
 **wvm** | **str**| Workspace (w), Version (v) or Microversion (m) ID | 
 **edit_description** | **str**| Description of the update (as appear in document history) | [optional] 
 **body** | [**Body41**](Body41.md)| The JSON request body. | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_parasolid_parts**
> file export_parasolid_parts(wvm_char, did, wvm, eid, partid, version=version, link_document_id=link_document_id, configuration=configuration)

Export Part to Parasolid

Export the part in text Parasolid format; returns a 307 redirect.

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
api_instance = swagger_client.PartsApi(swagger_client.ApiClient(configuration))
wvm_char = 'wvm_char_example' # str | One of w or v or m corresponding to whether a workspace or version or microversion was entered.
did = 'did_example' # str | Document ID
wvm = 'wvm_example' # str | Workspace (w), Version (v) or Microversion (m) ID
eid = 'eid_example' # str | Part studio element ID
partid = 'partid_example' # str | Part ID
version = 8.14 # float | Parasolid version (optional)
link_document_id = 'link_document_id_example' # str | Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. (optional)
configuration = 'configuration_example' # str | Configuration string (optional)

try:
    # Export Part to Parasolid
    api_response = api_instance.export_parasolid_parts(wvm_char, did, wvm, eid, partid, version=version, link_document_id=link_document_id, configuration=configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartsApi->export_parasolid_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wvm_char** | **str**| One of w or v or m corresponding to whether a workspace or version or microversion was entered. | 
 **did** | **str**| Document ID | 
 **wvm** | **str**| Workspace (w), Version (v) or Microversion (m) ID | 
 **eid** | **str**| Part studio element ID | 
 **partid** | **str**| Part ID | 
 **version** | **float**| Parasolid version | [optional] 
 **link_document_id** | **str**| Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. | [optional] 
 **configuration** | **str**| Configuration string | [optional] 

### Return type

[**file**](file.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_stl_parts**
> file export_stl_parts(wvm_char, did, wvm, eid, partid, grouping=grouping, scale=scale, units=units, angle_tolerance=angle_tolerance, chord_tolerance=chord_tolerance, max_facet_width=max_facet_width, min_facet_width=min_facet_width, mode=mode, link_document_id=link_document_id, configuration=configuration)

Export Part to STL

Export the part in text or binary STL format; returns a 307 redirect.

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
api_instance = swagger_client.PartsApi(swagger_client.ApiClient(configuration))
wvm_char = 'wvm_char_example' # str | One of w or v or m corresponding to whether a workspace or version or microversion was entered.
did = 'did_example' # str | Document ID
wvm = 'wvm_example' # str | Workspace (w), Version (v) or Microversion (m) ID
eid = 'eid_example' # str | Part studio element ID
partid = 'partid_example' # str | Part ID
grouping = true # bool | Whether parts should be exported as a group or individually in a           .zip file (optional)
scale = 8.14 # float | Scale for measurements (optional)
units = 'units_example' # str | Name of base unit (meter, centimeter, millimeter, inch, foot, or           yard) (optional)
angle_tolerance = 8.14 # float | Angle tolerance (in radians; must be < pi/2) (optional)
chord_tolerance = 8.14 # float | Chord tolerance (in selected units) (optional)
max_facet_width = 8.14 # float | Maximum facet width (in selected units) (optional)
min_facet_width = 8.14 # float | Minimum facet width (in selected units - must be <           maximumFacetWidth) (optional)
mode = 'mode_example' # str | Type of file: text, binary (optional)
link_document_id = 'link_document_id_example' # str | Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. (optional)
configuration = 'configuration_example' # str | Configuration string (optional)

try:
    # Export Part to STL
    api_response = api_instance.export_stl_parts(wvm_char, did, wvm, eid, partid, grouping=grouping, scale=scale, units=units, angle_tolerance=angle_tolerance, chord_tolerance=chord_tolerance, max_facet_width=max_facet_width, min_facet_width=min_facet_width, mode=mode, link_document_id=link_document_id, configuration=configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartsApi->export_stl_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wvm_char** | **str**| One of w or v or m corresponding to whether a workspace or version or microversion was entered. | 
 **did** | **str**| Document ID | 
 **wvm** | **str**| Workspace (w), Version (v) or Microversion (m) ID | 
 **eid** | **str**| Part studio element ID | 
 **partid** | **str**| Part ID | 
 **grouping** | **bool**| Whether parts should be exported as a group or individually in a           .zip file | [optional] 
 **scale** | **float**| Scale for measurements | [optional] 
 **units** | **str**| Name of base unit (meter, centimeter, millimeter, inch, foot, or           yard) | [optional] 
 **angle_tolerance** | **float**| Angle tolerance (in radians; must be &lt; pi/2) | [optional] 
 **chord_tolerance** | **float**| Chord tolerance (in selected units) | [optional] 
 **max_facet_width** | **float**| Maximum facet width (in selected units) | [optional] 
 **min_facet_width** | **float**| Minimum facet width (in selected units - must be &lt;           maximumFacetWidth) | [optional] 
 **mode** | **str**| Type of file: text, binary | [optional] 
 **link_document_id** | **str**| Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. | [optional] 
 **configuration** | **str**| Configuration string | [optional] 

### Return type

[**file**](file.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bend_table_parts**
> InlineResponse20086 get_bend_table_parts(wvm_char, did, wvm, eid, partid, link_document_id=link_document_id)

Get Sheet Metal Bend Table

Get the bend table a sheet metal part.

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
api_instance = swagger_client.PartsApi(swagger_client.ApiClient(configuration))
wvm_char = 'wvm_char_example' # str | One of w or v or m corresponding to whether a workspace or version or microversion was entered.
did = 'did_example' # str | Document ID
wvm = 'wvm_example' # str | Workspace (w), Version (v) or Microversion (m) ID
eid = 'eid_example' # str | Element ID
partid = 'partid_example' # str | Part ID
link_document_id = 'link_document_id_example' # str | Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. (optional)

try:
    # Get Sheet Metal Bend Table
    api_response = api_instance.get_bend_table_parts(wvm_char, did, wvm, eid, partid, link_document_id=link_document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartsApi->get_bend_table_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wvm_char** | **str**| One of w or v or m corresponding to whether a workspace or version or microversion was entered. | 
 **did** | **str**| Document ID | 
 **wvm** | **str**| Workspace (w), Version (v) or Microversion (m) ID | 
 **eid** | **str**| Element ID | 
 **partid** | **str**| Part ID | 
 **link_document_id** | **str**| Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. | [optional] 

### Return type

[**InlineResponse20086**](InlineResponse20086.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_body_details_parts**
> InlineResponse20082 get_body_details_parts(wvm_char, did, wvm, eid, partid, link_document_id=link_document_id, configuration=configuration)

Body Details

Get the body details of a part. All coordinates are in meters.

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
api_instance = swagger_client.PartsApi(swagger_client.ApiClient(configuration))
wvm_char = 'wvm_char_example' # str | One of w or v or m corresponding to whether a workspace or version or microversion was entered.
did = 'did_example' # str | Document ID
wvm = 'wvm_example' # str | Workspace (w), Version (v) or Microversion (m) ID
eid = 'eid_example' # str | Element ID
partid = 'partid_example' # str | Part ID
link_document_id = 'link_document_id_example' # str | Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. (optional)
configuration = 'configuration_example' # str | Configuration string (optional)

try:
    # Body Details
    api_response = api_instance.get_body_details_parts(wvm_char, did, wvm, eid, partid, link_document_id=link_document_id, configuration=configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartsApi->get_body_details_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wvm_char** | **str**| One of w or v or m corresponding to whether a workspace or version or microversion was entered. | 
 **did** | **str**| Document ID | 
 **wvm** | **str**| Workspace (w), Version (v) or Microversion (m) ID | 
 **eid** | **str**| Element ID | 
 **partid** | **str**| Part ID | 
 **link_document_id** | **str**| Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. | [optional] 
 **configuration** | **str**| Configuration string | [optional] 

### Return type

[**InlineResponse20082**](InlineResponse20082.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bounding_boxes_parts**
> InlineResponse20018 get_bounding_boxes_parts(wvm_char, did, wvm, eid, partid, include_hidden=include_hidden, link_document_id=link_document_id, configuration=configuration)

Bounding Boxes

Get the bounding box of a part. All coordinates are in meters.

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
api_instance = swagger_client.PartsApi(swagger_client.ApiClient(configuration))
wvm_char = 'wvm_char_example' # str | One of w or v or m corresponding to whether a workspace or version or microversion was entered.
did = 'did_example' # str | Document ID
wvm = 'wvm_example' # str | Workspace (w), Version (v) or Microversion (m) ID
eid = 'eid_example' # str | Element ID
partid = 'partid_example' # str | Part ID
include_hidden = true # bool | Whether or not to include bounding boxes for hidden parts (optional)
link_document_id = 'link_document_id_example' # str | Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. (optional)
configuration = 'configuration_example' # str | Configuration string (optional)

try:
    # Bounding Boxes
    api_response = api_instance.get_bounding_boxes_parts(wvm_char, did, wvm, eid, partid, include_hidden=include_hidden, link_document_id=link_document_id, configuration=configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartsApi->get_bounding_boxes_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wvm_char** | **str**| One of w or v or m corresponding to whether a workspace or version or microversion was entered. | 
 **did** | **str**| Document ID | 
 **wvm** | **str**| Workspace (w), Version (v) or Microversion (m) ID | 
 **eid** | **str**| Element ID | 
 **partid** | **str**| Part ID | 
 **include_hidden** | **bool**| Whether or not to include bounding boxes for hidden parts | [optional] 
 **link_document_id** | **str**| Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. | [optional] 
 **configuration** | **str**| Configuration string | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edges_parts**
> InlineResponse20090 get_edges_parts(wvm_char, did, wvm, eid, partid, angle_tolerance=angle_tolerance, chord_tolerance=chord_tolerance, edge_id=edge_id, link_document_id=link_document_id, configuration=configuration)

Tessellated Edges

Get the tessellated edges of a part. The accuracy of the tessellation approximation to exact                 geometry is controlled by the angleTolerance and chordTolerance parameters. The tessellation                 points are computed close enough so that neither the angle tolerance nor the chord tolerance are                 exceeded. All coordinates are in meters.

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
api_instance = swagger_client.PartsApi(swagger_client.ApiClient(configuration))
wvm_char = 'wvm_char_example' # str | One of w or v or m corresponding to whether a workspace or version or microversion was entered.
did = 'did_example' # str | Document ID
wvm = 'wvm_example' # str | Workspace (w), Version (v) or Microversion (m) ID
eid = 'eid_example' # str | Element ID
partid = 'partid_example' # str | Part ID
angle_tolerance = 8.14 # float | Angle tolerance (in radians). This specifies the limit on the           sum of the angular deviations of a tessellation chord from the tangent vectors at two chord endpoints.           The specified value must be less than PI/2. This parameter currently has a default value chosen based           on the complexity of the parts being tessellated. (optional)
chord_tolerance = 8.14 # float | Chord tolerance (in meters). This specifies the limit on the           maximum deviation of a tessellation chord from the true edge. This parameter currently has a default           value chosen based on the size and complexity of the part being tessellated. (optional)
edge_id = 'edge_id_example' # str | Edges to tessellate (repeat query param to add more than one, i.e.           edgeId=JHK&edgeId=JHD) (optional)
link_document_id = 'link_document_id_example' # str | Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. (optional)
configuration = 'configuration_example' # str | Configuration string (optional)

try:
    # Tessellated Edges
    api_response = api_instance.get_edges_parts(wvm_char, did, wvm, eid, partid, angle_tolerance=angle_tolerance, chord_tolerance=chord_tolerance, edge_id=edge_id, link_document_id=link_document_id, configuration=configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartsApi->get_edges_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wvm_char** | **str**| One of w or v or m corresponding to whether a workspace or version or microversion was entered. | 
 **did** | **str**| Document ID | 
 **wvm** | **str**| Workspace (w), Version (v) or Microversion (m) ID | 
 **eid** | **str**| Element ID | 
 **partid** | **str**| Part ID | 
 **angle_tolerance** | **float**| Angle tolerance (in radians). This specifies the limit on the           sum of the angular deviations of a tessellation chord from the tangent vectors at two chord endpoints.           The specified value must be less than PI/2. This parameter currently has a default value chosen based           on the complexity of the parts being tessellated. | [optional] 
 **chord_tolerance** | **float**| Chord tolerance (in meters). This specifies the limit on the           maximum deviation of a tessellation chord from the true edge. This parameter currently has a default           value chosen based on the size and complexity of the part being tessellated. | [optional] 
 **edge_id** | **str**| Edges to tessellate (repeat query param to add more than one, i.e.           edgeId&#x3D;JHK&amp;edgeId&#x3D;JHD) | [optional] 
 **link_document_id** | **str**| Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. | [optional] 
 **configuration** | **str**| Configuration string | [optional] 

### Return type

[**InlineResponse20090**](InlineResponse20090.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_faces_parts**
> InlineResponse20077 get_faces_parts(wvm_char, did, wvm, eid, partid, angle_tolerance=angle_tolerance, chord_tolerance=chord_tolerance, max_facet_width=max_facet_width, output_vertex_normals=output_vertex_normals, output_facet_normals=output_facet_normals, output_texture_coordinates=output_texture_coordinates, output_index_table=output_index_table, face_id=face_id, output_error_faces=output_error_faces, link_document_id=link_document_id, configuration=configuration)

Tessellated Faces

Get the tessellated faces of a part. The accuracy of the tessellation approximation to exact                 geometry is controlled by the angleTolerance, chordTolerance and maxFacetWidth parameters. The                 tessellation points are computed close enough so that none of these parameters are exceeded. All                 coordinates are in meters.

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
api_instance = swagger_client.PartsApi(swagger_client.ApiClient(configuration))
wvm_char = 'wvm_char_example' # str | One of w or v or m corresponding to whether a workspace or version or microversion was entered.
did = 'did_example' # str | Document ID
wvm = 'wvm_example' # str | Workspace (w), Version (v) or Microversion (m) ID
eid = 'eid_example' # str | Element ID
partid = 'partid_example' # str | Part ID
angle_tolerance = 8.14 # float | Angle tolerance (in radians). This specifies the limit on the           sum of the angular deviations of a tessellation chord from the tangent vectors at two chord endpoints.           The specified value must be less than PI/2. This parameter currently has a default value chosen based           on the complexity of the part being tessellated. (optional)
chord_tolerance = 8.14 # float | Chord tolerance (in meters). This specifies the limit on the           maximum deviation of a tessellation chord from the true surface/edge. This parameter currently has a           default value chosen based on the size and complexity of the parts being tessellated. (optional)
max_facet_width = 8.14 # float | Max facet width. This specifies the limit on the size of any side           of a tessellation facet. (optional)
output_vertex_normals = true # bool | Output vertex normals (optional)
output_facet_normals = true # bool | Output facet normals (optional)
output_texture_coordinates = true # bool | Output texture coordinates (optional)
output_index_table = true # bool | Output index table (optional)
face_id = 'face_id_example' # str | IDs of the faces to tessellate (repeat query param to add more than one,           i.e. faceId=JHK&faceId=JHD) (optional)
output_error_faces = true # bool | Whether or not to output faces that cause an error (optional)
link_document_id = 'link_document_id_example' # str | Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. (optional)
configuration = 'configuration_example' # str | Configuration string (optional)

try:
    # Tessellated Faces
    api_response = api_instance.get_faces_parts(wvm_char, did, wvm, eid, partid, angle_tolerance=angle_tolerance, chord_tolerance=chord_tolerance, max_facet_width=max_facet_width, output_vertex_normals=output_vertex_normals, output_facet_normals=output_facet_normals, output_texture_coordinates=output_texture_coordinates, output_index_table=output_index_table, face_id=face_id, output_error_faces=output_error_faces, link_document_id=link_document_id, configuration=configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartsApi->get_faces_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wvm_char** | **str**| One of w or v or m corresponding to whether a workspace or version or microversion was entered. | 
 **did** | **str**| Document ID | 
 **wvm** | **str**| Workspace (w), Version (v) or Microversion (m) ID | 
 **eid** | **str**| Element ID | 
 **partid** | **str**| Part ID | 
 **angle_tolerance** | **float**| Angle tolerance (in radians). This specifies the limit on the           sum of the angular deviations of a tessellation chord from the tangent vectors at two chord endpoints.           The specified value must be less than PI/2. This parameter currently has a default value chosen based           on the complexity of the part being tessellated. | [optional] 
 **chord_tolerance** | **float**| Chord tolerance (in meters). This specifies the limit on the           maximum deviation of a tessellation chord from the true surface/edge. This parameter currently has a           default value chosen based on the size and complexity of the parts being tessellated. | [optional] 
 **max_facet_width** | **float**| Max facet width. This specifies the limit on the size of any side           of a tessellation facet. | [optional] 
 **output_vertex_normals** | **bool**| Output vertex normals | [optional] 
 **output_facet_normals** | **bool**| Output facet normals | [optional] 
 **output_texture_coordinates** | **bool**| Output texture coordinates | [optional] 
 **output_index_table** | **bool**| Output index table | [optional] 
 **face_id** | **str**| IDs of the faces to tessellate (repeat query param to add more than one,           i.e. faceId&#x3D;JHK&amp;faceId&#x3D;JHD) | [optional] 
 **output_error_faces** | **bool**| Whether or not to output faces that cause an error | [optional] 
 **link_document_id** | **str**| Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. | [optional] 
 **configuration** | **str**| Configuration string | [optional] 

### Return type

[**InlineResponse20077**](InlineResponse20077.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mass_properties_parts**
> InlineResponse20089 get_mass_properties_parts(wvm_char, did, wvm, eid, partid, infer_metadata_owner=infer_metadata_owner, link_document_id=link_document_id, configuration=configuration)

Mass Properties

Get the mass properties of a part; parts must have density in order to have mass. For properties                 that come in sets of three, the first set is the calculated value, and the second and third are                 minimum and maximum possible values considering tolerance.

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
api_instance = swagger_client.PartsApi(swagger_client.ApiClient(configuration))
wvm_char = 'wvm_char_example' # str | One of w or v or m corresponding to whether a workspace or version or microversion was entered.
did = 'did_example' # str | Document ID
wvm = 'wvm_example' # str | Workspace (w), Version (v) or Microversion (m) ID
eid = 'eid_example' # str | Element ID
partid = 'partid_example' # str | Part ID
infer_metadata_owner = true # bool | If the referenced part is a Standard Content part,           specifying a value of true causes the API to look for metadata owned by the owner of the referencing           linkDocument prior to calculating mass properties. If Standard Content metadata is found and it           contains a material assignment, the density from that material is applied to the mass properties           calculation. (optional)
link_document_id = 'link_document_id_example' # str | Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. (optional)
configuration = 'configuration_example' # str | Configuration string (optional)

try:
    # Mass Properties
    api_response = api_instance.get_mass_properties_parts(wvm_char, did, wvm, eid, partid, infer_metadata_owner=infer_metadata_owner, link_document_id=link_document_id, configuration=configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartsApi->get_mass_properties_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wvm_char** | **str**| One of w or v or m corresponding to whether a workspace or version or microversion was entered. | 
 **did** | **str**| Document ID | 
 **wvm** | **str**| Workspace (w), Version (v) or Microversion (m) ID | 
 **eid** | **str**| Element ID | 
 **partid** | **str**| Part ID | 
 **infer_metadata_owner** | **bool**| If the referenced part is a Standard Content part,           specifying a value of true causes the API to look for metadata owned by the owner of the referencing           linkDocument prior to calculating mass properties. If Standard Content metadata is found and it           contains a material assignment, the density from that material is applied to the mass properties           calculation. | [optional] 
 **link_document_id** | **str**| Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. | [optional] 
 **configuration** | **str**| Configuration string | [optional] 

### Return type

[**InlineResponse20089**](InlineResponse20089.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_part_metadata_parts**
> InlineResponse20083 get_part_metadata_parts(wvm_char, did, wvm, eid, partid, link_document_id=link_document_id, configuration=configuration, infer_metadata_owner=infer_metadata_owner, include_property_defaults=include_property_defaults)

Get Metadata

Get a part's metadata

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
api_instance = swagger_client.PartsApi(swagger_client.ApiClient(configuration))
wvm_char = 'wvm_char_example' # str | One of w or v or m corresponding to whether a workspace or version or microversion was entered.
did = 'did_example' # str | Document ID
wvm = 'wvm_example' # str | Workspace (w), Version (v) or Microversion (m) ID
eid = 'eid_example' # str | Element ID
partid = 'partid_example' # str | Part ID
link_document_id = 'link_document_id_example' # str | Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. (optional)
configuration = 'configuration_example' # str | Configuration string (optional)
infer_metadata_owner = true # bool | If the URL references a Standard Content part,       specifying a value of true causes the API to use the owner of the referencing linkDocument as the       metadata scope and the href of the returned part is modified to reflect this metadata scope. If not       explictly set or if set to false, the part metadata returned is the metadata defined internal to the       Standard Content document. (optional)
include_property_defaults = true # bool | If true, include metadata schema property       defaults in response (optional)

try:
    # Get Metadata
    api_response = api_instance.get_part_metadata_parts(wvm_char, did, wvm, eid, partid, link_document_id=link_document_id, configuration=configuration, infer_metadata_owner=infer_metadata_owner, include_property_defaults=include_property_defaults)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartsApi->get_part_metadata_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wvm_char** | **str**| One of w or v or m corresponding to whether a workspace or version or microversion was entered. | 
 **did** | **str**| Document ID | 
 **wvm** | **str**| Workspace (w), Version (v) or Microversion (m) ID | 
 **eid** | **str**| Element ID | 
 **partid** | **str**| Part ID | 
 **link_document_id** | **str**| Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. | [optional] 
 **configuration** | **str**| Configuration string | [optional] 
 **infer_metadata_owner** | **bool**| If the URL references a Standard Content part,       specifying a value of true causes the API to use the owner of the referencing linkDocument as the       metadata scope and the href of the returned part is modified to reflect this metadata scope. If not       explictly set or if set to false, the part metadata returned is the metadata defined internal to the       Standard Content document. | [optional] 
 **include_property_defaults** | **bool**| If true, include metadata schema property       defaults in response | [optional] 

### Return type

[**InlineResponse20083**](InlineResponse20083.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parts_in_partstudio_parts**
> InlineResponse20085 get_parts_in_partstudio_parts(wvm_char, did, wvm, eid, with_thumbnails=with_thumbnails, link_document_id=link_document_id, include_property_defaults=include_property_defaults)

Get Parts In Part Studio

Get list of parts in a part studio. An error is returned if the specified element is not a part                 studio. Surface, wire, and mesh parts are not returned for a version but are included for a                 workspace or microversion.

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
api_instance = swagger_client.PartsApi(swagger_client.ApiClient(configuration))
wvm_char = 'wvm_char_example' # str | One of w or v or m corresponding to whether a workspace or version or microversion was entered.
did = 'did_example' # str | Document ID
wvm = 'wvm_example' # str | Workspace (w), Version (v) or Microversion (m) ID
eid = 'eid_example' # str | Part studio element ID
with_thumbnails = true # bool | Whether or not to include thumbnails (not supported for           microversion) (optional)
link_document_id = 'link_document_id_example' # str | Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. (optional)
include_property_defaults = true # bool | If true, include metadata schema property       defaults in response (optional)

try:
    # Get Parts In Part Studio
    api_response = api_instance.get_parts_in_partstudio_parts(wvm_char, did, wvm, eid, with_thumbnails=with_thumbnails, link_document_id=link_document_id, include_property_defaults=include_property_defaults)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartsApi->get_parts_in_partstudio_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wvm_char** | **str**| One of w or v or m corresponding to whether a workspace or version or microversion was entered. | 
 **did** | **str**| Document ID | 
 **wvm** | **str**| Workspace (w), Version (v) or Microversion (m) ID | 
 **eid** | **str**| Part studio element ID | 
 **with_thumbnails** | **bool**| Whether or not to include thumbnails (not supported for           microversion) | [optional] 
 **link_document_id** | **str**| Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. | [optional] 
 **include_property_defaults** | **bool**| If true, include metadata schema property       defaults in response | [optional] 

### Return type

[**InlineResponse20085**](InlineResponse20085.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parts_parts**
> InlineResponse20085 get_parts_parts(wvm_char, did, wvm, with_thumbnails=with_thumbnails, link_document_id=link_document_id, include_property_defaults=include_property_defaults)

Get Parts

Get list of parts

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
api_instance = swagger_client.PartsApi(swagger_client.ApiClient(configuration))
wvm_char = 'wvm_char_example' # str | One of w or v or m corresponding to whether a workspace or version or microversion was entered.
did = 'did_example' # str | Document ID
wvm = 'wvm_example' # str | Workspace (w), Version (v) or Microversion (m) ID
with_thumbnails = true # bool | Whether or not to include thumbnails (not supported for           microversion) (optional)
link_document_id = 'link_document_id_example' # str | Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. (optional)
include_property_defaults = true # bool | If true, include metadata schema property       defaults in response (optional)

try:
    # Get Parts
    api_response = api_instance.get_parts_parts(wvm_char, did, wvm, with_thumbnails=with_thumbnails, link_document_id=link_document_id, include_property_defaults=include_property_defaults)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartsApi->get_parts_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wvm_char** | **str**| One of w or v or m corresponding to whether a workspace or version or microversion was entered. | 
 **did** | **str**| Document ID | 
 **wvm** | **str**| Workspace (w), Version (v) or Microversion (m) ID | 
 **with_thumbnails** | **bool**| Whether or not to include thumbnails (not supported for           microversion) | [optional] 
 **link_document_id** | **str**| Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. | [optional] 
 **include_property_defaults** | **bool**| If true, include metadata schema property       defaults in response | [optional] 

### Return type

[**InlineResponse20085**](InlineResponse20085.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shaded_views_parts**
> InlineResponse20074 get_shaded_views_parts(wvm_char, did, wvm, eid, partid, output_height=output_height, output_width=output_width, pixel_size=pixel_size, edges=edges, use_anti_aliasing=use_anti_aliasing, link_document_id=link_document_id, configuration=configuration, view_matrix=view_matrix)

Shaded views

Get a shaded image rendering of a part

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
api_instance = swagger_client.PartsApi(swagger_client.ApiClient(configuration))
wvm_char = 'wvm_char_example' # str | One of w or v or m corresponding to whether a workspace or version or microversion was entered.
did = 'did_example' # str | Document ID
wvm = 'wvm_example' # str | Workspace (w), Version (v) or Microversion (m) ID
eid = 'eid_example' # str | Element ID
partid = 'partid_example' # str | Part ID
output_height = 8.14 # float | Output image height (in pixels) (optional)
output_width = 8.14 # float | Output image width (in pixels) (optional)
pixel_size = 8.14 # float | Height and width represented by each pixel (in meters). If the           value is 0, the display will be sized to fit the output image dimensions. (optional)
edges = 'edges_example' # str | The treatment to be applied to edges in the display. Options are           show: show visible edges, hide: hide visible edges (optional)
use_anti_aliasing = true # bool | If true, an anti-aliasing factor will be used to smooth           model boundaries in the final image result. If false, the image will be rasterized at the given           resolution. Setting to true can have negative performance implications with respect to rendering time           and memory usage. If a high-resolution image is requested and anti-aliasing is turned on, the server           may not be able to fulfill the request. (optional)
link_document_id = 'link_document_id_example' # str | Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. (optional)
configuration = 'configuration_example' # str | Configuration string (optional)
view_matrix = 'view_matrix_example' # str | 12-number view matrix (comma-separated), or one of the following named views: top, bottom, front, back, left, right The 12 entries in the view matrix form three rows and four columns, which is a linear transformation applied to the model itself. The matrix's first three columns maps the coordinate axes of the model to the coordinate axes of the view, and the fourth column translates the origin (in meters). The view coordinates have x pointing right, y pointing up, and z pointing towards the viewer, while a front view of the model has x pointing right, y pointing away from the viewer, and z pointing up. For example, the identity matrix viewMatrix=1,0,0,0,0,1,0,0,0,0,1,0 corresponds to the top view, and viewMatrix=0.612,0.612,0,0,-0.354,0.354,0.707,0,0.707,-0.707,0.707,0 corresponds (approximately) to the isometric view. The first three columns of the view matrix should be orthonormal and have a positive determinant.  If this is not the case, view behavior may be undefined. (optional)

try:
    # Shaded views
    api_response = api_instance.get_shaded_views_parts(wvm_char, did, wvm, eid, partid, output_height=output_height, output_width=output_width, pixel_size=pixel_size, edges=edges, use_anti_aliasing=use_anti_aliasing, link_document_id=link_document_id, configuration=configuration, view_matrix=view_matrix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartsApi->get_shaded_views_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wvm_char** | **str**| One of w or v or m corresponding to whether a workspace or version or microversion was entered. | 
 **did** | **str**| Document ID | 
 **wvm** | **str**| Workspace (w), Version (v) or Microversion (m) ID | 
 **eid** | **str**| Element ID | 
 **partid** | **str**| Part ID | 
 **output_height** | **float**| Output image height (in pixels) | [optional] 
 **output_width** | **float**| Output image width (in pixels) | [optional] 
 **pixel_size** | **float**| Height and width represented by each pixel (in meters). If the           value is 0, the display will be sized to fit the output image dimensions. | [optional] 
 **edges** | **str**| The treatment to be applied to edges in the display. Options are           show: show visible edges, hide: hide visible edges | [optional] 
 **use_anti_aliasing** | **bool**| If true, an anti-aliasing factor will be used to smooth           model boundaries in the final image result. If false, the image will be rasterized at the given           resolution. Setting to true can have negative performance implications with respect to rendering time           and memory usage. If a high-resolution image is requested and anti-aliasing is turned on, the server           may not be able to fulfill the request. | [optional] 
 **link_document_id** | **str**| Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. | [optional] 
 **configuration** | **str**| Configuration string | [optional] 
 **view_matrix** | **str**| 12-number view matrix (comma-separated), or one of the following named views: top, bottom, front, back, left, right The 12 entries in the view matrix form three rows and four columns, which is a linear transformation applied to the model itself. The matrix&#39;s first three columns maps the coordinate axes of the model to the coordinate axes of the view, and the fourth column translates the origin (in meters). The view coordinates have x pointing right, y pointing up, and z pointing towards the viewer, while a front view of the model has x pointing right, y pointing away from the viewer, and z pointing up. For example, the identity matrix viewMatrix&#x3D;1,0,0,0,0,1,0,0,0,0,1,0 corresponds to the top view, and viewMatrix&#x3D;0.612,0.612,0,0,-0.354,0.354,0.707,0,0.707,-0.707,0.707,0 corresponds (approximately) to the isometric view. The first three columns of the view matrix should be orthonormal and have a positive determinant.  If this is not the case, view behavior may be undefined. | [optional] 

### Return type

[**InlineResponse20074**](InlineResponse20074.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_standard_content_part_metadata_parts**
> InlineResponse20087 get_standard_content_part_metadata_parts(cu_char, partid, did, vid, eid, oid, link_document_id=link_document_id, configuration=configuration, include_property_defaults=include_property_defaults)

Get Standard Content Metadata

Get metadata for a standard content part in the context of a user or company

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
api_instance = swagger_client.PartsApi(swagger_client.ApiClient(configuration))
cu_char = 'cu_char_example' # str | One of c or u corresponding to whether a company or user was entered.
partid = 'partid_example' # str | Part ID
did = 'did_example' # str | Document ID
vid = 'vid_example' # str | Version ID
eid = 'eid_example' # str | Element ID
oid = 'oid_example' # str | Company (c) or User (u) ID of metadata owner
link_document_id = 'link_document_id_example' # str | Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. (optional)
configuration = 'configuration_example' # str | Configuration string (optional)
include_property_defaults = true # bool | If true, include metadata schema property       defaults in response (optional)

try:
    # Get Standard Content Metadata
    api_response = api_instance.get_standard_content_part_metadata_parts(cu_char, partid, did, vid, eid, oid, link_document_id=link_document_id, configuration=configuration, include_property_defaults=include_property_defaults)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartsApi->get_standard_content_part_metadata_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cu_char** | **str**| One of c or u corresponding to whether a company or user was entered. | 
 **partid** | **str**| Part ID | 
 **did** | **str**| Document ID | 
 **vid** | **str**| Version ID | 
 **eid** | **str**| Element ID | 
 **oid** | **str**| Company (c) or User (u) ID of metadata owner | 
 **link_document_id** | **str**| Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. | [optional] 
 **configuration** | **str**| Configuration string | [optional] 
 **include_property_defaults** | **bool**| If true, include metadata schema property       defaults in response | [optional] 

### Return type

[**InlineResponse20087**](InlineResponse20087.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_part_metadata_parts**
> InlineResponse20084 update_part_metadata_parts(wvm_char, did, wvm, eid, partid, body=body)

Update Metadata

Update a part's metadata

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
api_instance = swagger_client.PartsApi(swagger_client.ApiClient(configuration))
wvm_char = 'wvm_char_example' # str | One of w or v or m corresponding to whether a workspace or version or microversion was entered.
did = 'did_example' # str | Document ID
wvm = 'wvm_example' # str | Workspace (w), Version (v) or Microversion (m) ID
eid = 'eid_example' # str | Element ID
partid = 'partid_example' # str | Part ID
body = swagger_client.Body40() # Body40 | The JSON request body. (optional)

try:
    # Update Metadata
    api_response = api_instance.update_part_metadata_parts(wvm_char, did, wvm, eid, partid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartsApi->update_part_metadata_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wvm_char** | **str**| One of w or v or m corresponding to whether a workspace or version or microversion was entered. | 
 **did** | **str**| Document ID | 
 **wvm** | **str**| Workspace (w), Version (v) or Microversion (m) ID | 
 **eid** | **str**| Element ID | 
 **partid** | **str**| Part ID | 
 **body** | [**Body40**](Body40.md)| The JSON request body. | [optional] 

### Return type

[**InlineResponse20084**](InlineResponse20084.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_standard_content_part_metadata_parts**
> InlineResponse20088 update_standard_content_part_metadata_parts(cu_char, partid, did, vid, eid, oid, body=body, link_document_id=link_document_id, include_property_defaults=include_property_defaults)

Update Standard Content Metadata

Update metadata for a standard content part in the context of a company or user

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
api_instance = swagger_client.PartsApi(swagger_client.ApiClient(configuration))
cu_char = 'cu_char_example' # str | One of c or u corresponding to whether a company or user was entered.
partid = 'partid_example' # str | Part ID
did = 'did_example' # str | Document ID
vid = 'vid_example' # str | Version ID
eid = 'eid_example' # str | Element ID
oid = 'oid_example' # str | Company (c) or User (u) ID of metadata owner
body = swagger_client.Body42() # Body42 | The JSON request body. (optional)
link_document_id = 'link_document_id_example' # str | Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. (optional)
include_property_defaults = true # bool | If true, include metadata schema property       defaults in response (optional)

try:
    # Update Standard Content Metadata
    api_response = api_instance.update_standard_content_part_metadata_parts(cu_char, partid, did, vid, eid, oid, body=body, link_document_id=link_document_id, include_property_defaults=include_property_defaults)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartsApi->update_standard_content_part_metadata_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cu_char** | **str**| One of c or u corresponding to whether a company or user was entered. | 
 **partid** | **str**| Part ID | 
 **did** | **str**| Document ID | 
 **vid** | **str**| Version ID | 
 **eid** | **str**| Element ID | 
 **oid** | **str**| Company (c) or User (u) ID of metadata owner | 
 **body** | [**Body42**](Body42.md)| The JSON request body. | [optional] 
 **link_document_id** | **str**| Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter. | [optional] 
 **include_property_defaults** | **bool**| If true, include metadata schema property       defaults in response | [optional] 

### Return type

[**InlineResponse20088**](InlineResponse20088.md)

### Authorization

[OAuth2](../README.md#OAuth2), [apiAccessKey](../README.md#apiAccessKey), [apiSecretKey](../README.md#apiSecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

