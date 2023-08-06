# CertificateResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**certificate_data** | [**SensitiveValue**](SensitiveValue.md) |  | [optional] 
**password** | [**SensitiveValue**](SensitiveValue.md) |  | [optional] 
**environment_ids** | **list[str]** |  | [optional] 
**tenanted_deployment_participation** | **str** |  | [optional] 
**tenant_ids** | **list[str]** |  | [optional] 
**tenant_tags** | **list[str]** |  | [optional] 
**certificate_data_format** | **str** |  | [optional] 
**archived** | **datetime** |  | [optional] 
**replaced_by** | **str** |  | [optional] 
**subject_distinguished_name** | **str** |  | [optional] 
**subject_common_name** | **str** |  | [optional] 
**subject_organization** | **str** |  | [optional] 
**issuer_distinguished_name** | **str** |  | [optional] 
**issuer_common_name** | **str** |  | [optional] 
**issuer_organization** | **str** |  | [optional] 
**self_signed** | **bool** |  | [optional] 
**thumbprint** | **str** |  | [optional] 
**not_after** | **datetime** |  | [optional] 
**not_before** | **datetime** |  | [optional] 
**is_expired** | **bool** |  | [optional] 
**has_private_key** | **bool** |  | [optional] 
**version** | **int** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**signature_algorithm_name** | **str** |  | [optional] 
**subject_alternative_names** | **list[str]** |  | [optional] 
**certificate_chain** | [**list[X509Certificate]**](X509Certificate.md) |  | [optional] 
**space_id** | **str** |  | [optional] 
**last_modified_on** | **datetime** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 
**links** | **dict(str, str)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


