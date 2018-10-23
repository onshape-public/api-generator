# InlineResponse20046

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_public** | **bool** | True if the object is public | 
**is_admin** | **bool** | True if the requesting user has RESHARE privileges on the object.      If set to false, entries that do not relate to the caller are removed from the output. | 
**shared_with_support** | **bool** | True if the object is shared with support | 
**visibility** | **str** | A description string indicating whether the object is public or private | 
**entries** | [**list[InlineResponse20046Entries]**](InlineResponse20046Entries.md) | The current share entries for the object. Each share entry indicates      an entity that the object is shared with and the permissions granted to the entity | 
**object_id** | **str** | The ID of the object | 
**object_type** | **float** | Set to the value 1, indicating the the objectId indicates a document,       or 4, indicating that the objectId indicates a folder | 
**owner** | [**InlineResponse20046Owner**](InlineResponse20046Owner.md) |  | 
**id** | **str** | Not used | 
**name** | **str** | Not used | 
**href** | **str** | A URL referencing the API to get this structure | 
**inherited_acls** | [**list[InlineResponse20046InheritedAcls]**](InlineResponse20046InheritedAcls.md) | A list of parent objects from which this object inherits access       rights. Parent objects are currently always folders | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


