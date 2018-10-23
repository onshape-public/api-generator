# InlineResponse20093

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the release package. | 
**is_frozen** | **bool** | Whether the release package has reached its terminal tranistion. Frozen             packages cannot be modified. | 
**company_id** | **str** | Company ID to which the release package belongs. | 
**document_id** | **str** | Primary Document ID of items in the release package | 
**version_id** | **str** | Primary Version ID of items in the release package | [optional] 
**workspace_id** | **str** | Primary Workspace ID of items in the release package | [optional] 
**properties** | [**list[InlineResponse20092Properties]**](InlineResponse20092Properties.md) | Array of properties for the package | 
**items** | [**list[InlineResponse20092Items]**](InlineResponse20092Items.md) | Full item list in the package determined by the input items | 
**workflow** | [**InlineResponse20093Workflow**](InlineResponse20093Workflow.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


