# InlineResponse20023BomTable

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format_version** | **str** | The version of the Onshape BOM JSON Standard that this             response complies with | 
**id** | **str** | The id of the BOM | 
**name** | **str** | The name of the BOM | 
**description** | **str** | The description of the BOM. Currently empty. | 
**part_number** | **str** | The partNumber of the BOM. Currently empty. | 
**created_at** | **str** | The UTC date and time the BOM data was exported. | 
**bom_source** | [**InlineResponse20023BomTableBomSource**](InlineResponse20023BomTableBomSource.md) |  | 
**headers** | [**list[InlineResponse20023BomTableHeaders]**](InlineResponse20023BomTableHeaders.md) | BOM table column headers | 
**items** | [**list[InlineResponse20023BomTableItems]**](InlineResponse20023BomTableItems.md) | The non-header rows of the BOM table. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


