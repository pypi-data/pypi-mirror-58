# DeploymentActionResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**action_type** | **str** |  | [optional] 
**is_disabled** | **bool** |  | [optional] 
**can_be_used_for_project_versioning** | **bool** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**worker_pool_id** | **str** |  | [optional] 
**environments** | **list[str]** |  | [optional] 
**excluded_environments** | **list[str]** |  | [optional] 
**channels** | **list[str]** |  | [optional] 
**tenant_tags** | **list[str]** |  | [optional] 
**packages** | [**list[PackageReference]**](PackageReference.md) |  | [optional] 
**properties** | [**dict(str, PropertyValueResource)**](PropertyValueResource.md) |  | [optional] 
**last_modified_on** | **datetime** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 
**links** | **dict(str, str)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


