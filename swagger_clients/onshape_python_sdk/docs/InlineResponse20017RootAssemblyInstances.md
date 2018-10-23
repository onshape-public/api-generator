# InlineResponse20017RootAssemblyInstances

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Instance ID | 
**name** | **str** | Part/feature/assembly name | 
**type** | **str** | Instance type. Current valid values are Part,             Assembly, Feature. Other values may be added in the future. Note that \&quot;Part\&quot; may mean a reference to             a surface or a solid and that \&quot;Feature\&quot; currently means a reference to a Sketch, but support for             other feature types may be added in the future. For Part, a specific bodyType is included in the             parts information and for Feature, a specific featureType is included in the partStudioFeatures             information. | 
**suppressed** | **bool** | Instance suppressed or not | 
**document_id** | **str** | Document ID for the document containing the             included instance | 
**document_microversion** | **str** | Microversion ID of document             containing the included instance | 
**document_version** | **str** | Version ID of document containing the             included instance, if reached through one or more version references | 
**element_id** | **str** | Element ID of the part/assembly instance | 
**part_id** | **str** | Deterministic part ID if type is Part. If the             part cannot be resolved, the value will be the empty string. This can happen if a change in the             source part studio causes the part that was originally referenced to be missing. | 
**is_standard_content** | **bool** | If type is Part this field             indicates whether the part is Standard Content. | 
**configuration** | **str** | Configuration of the Part studio element                    if the instance references a Part studio. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


