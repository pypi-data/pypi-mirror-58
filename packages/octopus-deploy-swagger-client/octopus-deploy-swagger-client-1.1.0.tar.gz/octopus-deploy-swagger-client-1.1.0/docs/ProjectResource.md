# ProjectResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**variable_set_id** | **str** |  | [optional] 
**deployment_process_id** | **str** |  | [optional] 
**cloned_from_project_id** | **str** |  | [optional] 
**discrete_channel_release** | **bool** |  | [optional] 
**included_library_variable_set_ids** | **list[str]** |  | [optional] 
**default_to_skip_if_already_installed** | **bool** |  | [optional] 
**tenanted_deployment_mode** | **str** |  | [optional] 
**default_guided_failure_mode** | **str** |  | [optional] 
**versioning_strategy** | [**VersioningStrategyResource**](VersioningStrategyResource.md) |  | [optional] 
**release_creation_strategy** | [**ReleaseCreationStrategyResource**](ReleaseCreationStrategyResource.md) |  | [optional] 
**templates** | [**list[ActionTemplateParameterResource]**](ActionTemplateParameterResource.md) |  | [optional] 
**auto_deploy_release_overrides** | [**list[AutoDeployReleaseOverrideResource]**](AutoDeployReleaseOverrideResource.md) |  | [optional] 
**release_notes_template** | **str** |  | [optional] 
**space_id** | **str** |  | [optional] 
**extension_settings** | [**list[ExtensionSettingsValues]**](ExtensionSettingsValues.md) |  | [optional] 
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_disabled** | **bool** |  | [optional] 
**project_group_id** | **str** |  | [optional] 
**lifecycle_id** | **str** |  | [optional] 
**auto_create_release** | **bool** |  | [optional] 
**project_connectivity_policy** | [**ProjectConnectivityPolicy**](ProjectConnectivityPolicy.md) |  | [optional] 
**last_modified_on** | **datetime** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 
**links** | **dict(str, str)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


