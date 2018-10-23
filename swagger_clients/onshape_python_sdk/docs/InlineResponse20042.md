# InlineResponse20042

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_workspace** | [**InlineResponse20037DefaultWorkspace**](InlineResponse20037DefaultWorkspace.md) |  | 
**beta_capability_ids** | **list[str]** | Onshape internal use | 
**public** | **bool** | Whether document is public | 
**owner** | [**InlineResponse20042Owner**](InlineResponse20042Owner.md) |  | 
**permission_set** | **list[str]** | User&#39;s level of access to the document. Possible values: OWNER,             DELETE, RESHARE, WRITE, READ, COPY, EXPORT, COMMENT | 
**permission** | **str** | User&#39;s level of access to the document; can be ANONYMOUS_ACCESS, READ,             READ_COPY_EXPORT, COMMENT, WRITE, RESHARE, FULL, or OWNER (Deprecated) | 
**trashed_at** | **datetime** | When document has been trashed | 
**trash** | **bool** | Whether document has been trashed | 
**starred** | **str** | Whether document has been starred (Deprecated) | 
**active** | **str** | Whether a shared document is active | 
**created_at** | **datetime** | Creation date | 
**document_thumbnail_element_id** | **str** | The element which the Document Thumbnail should mirror | 
**thumbnail** | [**InlineResponse20036Thumbnail**](InlineResponse20036Thumbnail.md) |  | 
**created_by** | [**InlineResponse20036CreatedBy**](InlineResponse20036CreatedBy.md) |  | 
**modified_at** | **datetime** | Date of last modification | 
**modified_by** | [**InlineResponse20036ModifiedBy**](InlineResponse20036ModifiedBy.md) |  | 
**tags** | **list[str]** | Reserved for future use | 
**size_bytes** | **float** | Size of document in bytes | 
**name** | **str** | Name of document | 
**id** | **str** | Document ID | 
**href** | **str** | Document URL | 
**total_workspaces_updating** | **float** | Number of workspaces that are updating | 
**total_workspaces_scheduled_for_update** | **float** | Number of workspaces that are scheduled for             updating | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


