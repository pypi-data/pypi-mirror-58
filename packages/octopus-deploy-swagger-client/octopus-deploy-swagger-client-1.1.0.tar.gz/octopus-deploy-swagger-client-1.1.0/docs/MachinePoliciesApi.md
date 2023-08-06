# octopus_deploy_swagger_client.MachinePoliciesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**child_index_response_descriptor_policies_machine_policy_machines_deployment_targets_deployment_target_machine_policy_resource_deployment_target_resource**](MachinePoliciesApi.md#child_index_response_descriptor_policies_machine_policy_machines_deployment_targets_deployment_target_machine_policy_resource_deployment_target_resource) | **GET** /api/machinepolicies/{id}/machines | Get a list of DeploymentTargetResources
[**child_index_response_descriptor_policies_machine_policy_machines_deployment_targets_deployment_target_machine_policy_resource_deployment_target_resource_spaces**](MachinePoliciesApi.md#child_index_response_descriptor_policies_machine_policy_machines_deployment_targets_deployment_target_machine_policy_resource_deployment_target_resource_spaces) | **GET** /api/{baseSpaceId}/machinepolicies/{id}/machines | Get a list of DeploymentTargetResources
[**child_index_response_descriptor_policies_machine_policy_machines_workers_worker_machine_policy_resource_worker_resource**](MachinePoliciesApi.md#child_index_response_descriptor_policies_machine_policy_machines_workers_worker_machine_policy_resource_worker_resource) | **GET** /api/machinepolicies/{id}/workers | Get a list of WorkerResources
[**child_index_response_descriptor_policies_machine_policy_machines_workers_worker_machine_policy_resource_worker_resource_spaces**](MachinePoliciesApi.md#child_index_response_descriptor_policies_machine_policy_machines_workers_worker_machine_policy_resource_worker_resource_spaces) | **GET** /api/{baseSpaceId}/machinepolicies/{id}/workers | Get a list of WorkerResources
[**create_response_descriptor_policies_machine_policy_machine_policy_resource**](MachinePoliciesApi.md#create_response_descriptor_policies_machine_policy_machine_policy_resource) | **POST** /api/machinepolicies | Create a MachinePolicyResource
[**create_response_descriptor_policies_machine_policy_machine_policy_resource_spaces**](MachinePoliciesApi.md#create_response_descriptor_policies_machine_policy_machine_policy_resource_spaces) | **POST** /api/{baseSpaceId}/machinepolicies | Create a MachinePolicyResource
[**custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_delete_action**](MachinePoliciesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_delete_action) | **DELETE** /api/machinepolicies/{id} | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_delete_action_spaces**](MachinePoliciesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_delete_action_spaces) | **DELETE** /api/{baseSpaceId}/machinepolicies/{id} | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_template_action**](MachinePoliciesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_template_action) | **GET** /api/machinepolicies/template | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_template_action_spaces**](MachinePoliciesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_template_action_spaces) | **GET** /api/{baseSpaceId}/machinepolicies/template | 
[**index_response_descriptor_policies_machine_policy_machine_policy_resource**](MachinePoliciesApi.md#index_response_descriptor_policies_machine_policy_machine_policy_resource) | **GET** /api/machinepolicies | Get a list of MachinePolicyResources
[**index_response_descriptor_policies_machine_policy_machine_policy_resource_spaces**](MachinePoliciesApi.md#index_response_descriptor_policies_machine_policy_machine_policy_resource_spaces) | **GET** /api/{baseSpaceId}/machinepolicies | Get a list of MachinePolicyResources
[**list_all_response_descriptor_policies_machine_policy_machine_policy_resource**](MachinePoliciesApi.md#list_all_response_descriptor_policies_machine_policy_machine_policy_resource) | **GET** /api/machinepolicies/all | Get a list of MachinePolicyResources
[**list_all_response_descriptor_policies_machine_policy_machine_policy_resource_spaces**](MachinePoliciesApi.md#list_all_response_descriptor_policies_machine_policy_machine_policy_resource_spaces) | **GET** /api/{baseSpaceId}/machinepolicies/all | Get a list of MachinePolicyResources
[**load_response_descriptor_policies_machine_policy_machine_policy_resource**](MachinePoliciesApi.md#load_response_descriptor_policies_machine_policy_machine_policy_resource) | **GET** /api/machinepolicies/{id} | Get a MachinePolicyResource by ID
[**load_response_descriptor_policies_machine_policy_machine_policy_resource_spaces**](MachinePoliciesApi.md#load_response_descriptor_policies_machine_policy_machine_policy_resource_spaces) | **GET** /api/{baseSpaceId}/machinepolicies/{id} | Get a MachinePolicyResource by ID
[**modify_response_descriptor_policies_machine_policy_machine_policy_resource**](MachinePoliciesApi.md#modify_response_descriptor_policies_machine_policy_machine_policy_resource) | **PUT** /api/machinepolicies/{id} | Modify a MachinePolicyResource by ID
[**modify_response_descriptor_policies_machine_policy_machine_policy_resource_spaces**](MachinePoliciesApi.md#modify_response_descriptor_policies_machine_policy_machine_policy_resource_spaces) | **PUT** /api/{baseSpaceId}/machinepolicies/{id} | Modify a MachinePolicyResource by ID


# **child_index_response_descriptor_policies_machine_policy_machines_deployment_targets_deployment_target_machine_policy_resource_deployment_target_resource**
> ResourceCollectionMachinePolicyResource child_index_response_descriptor_policies_machine_policy_machines_deployment_targets_deployment_target_machine_policy_resource_deployment_target_resource(skip=skip, take=take)

Get a list of DeploymentTargetResources

Lists all of the machines that belong to the given machine policy.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.MachinePoliciesApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of DeploymentTargetResources
    api_response = api_instance.child_index_response_descriptor_policies_machine_policy_machines_deployment_targets_deployment_target_machine_policy_resource_deployment_target_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinePoliciesApi->child_index_response_descriptor_policies_machine_policy_machines_deployment_targets_deployment_target_machine_policy_resource_deployment_target_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionMachinePolicyResource**](ResourceCollectionMachinePolicyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **child_index_response_descriptor_policies_machine_policy_machines_deployment_targets_deployment_target_machine_policy_resource_deployment_target_resource_spaces**
> ResourceCollectionMachinePolicyResource child_index_response_descriptor_policies_machine_policy_machines_deployment_targets_deployment_target_machine_policy_resource_deployment_target_resource_spaces(base_space_id, skip=skip, take=take)

Get a list of DeploymentTargetResources

Lists all of the machines that belong to the given machine policy.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.MachinePoliciesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of DeploymentTargetResources
    api_response = api_instance.child_index_response_descriptor_policies_machine_policy_machines_deployment_targets_deployment_target_machine_policy_resource_deployment_target_resource_spaces(base_space_id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinePoliciesApi->child_index_response_descriptor_policies_machine_policy_machines_deployment_targets_deployment_target_machine_policy_resource_deployment_target_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionMachinePolicyResource**](ResourceCollectionMachinePolicyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **child_index_response_descriptor_policies_machine_policy_machines_workers_worker_machine_policy_resource_worker_resource**
> ResourceCollectionMachinePolicyResource child_index_response_descriptor_policies_machine_policy_machines_workers_worker_machine_policy_resource_worker_resource(skip=skip, take=take)

Get a list of WorkerResources

Lists all of the workers that belong to the given machine policy.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.MachinePoliciesApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of WorkerResources
    api_response = api_instance.child_index_response_descriptor_policies_machine_policy_machines_workers_worker_machine_policy_resource_worker_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinePoliciesApi->child_index_response_descriptor_policies_machine_policy_machines_workers_worker_machine_policy_resource_worker_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionMachinePolicyResource**](ResourceCollectionMachinePolicyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **child_index_response_descriptor_policies_machine_policy_machines_workers_worker_machine_policy_resource_worker_resource_spaces**
> ResourceCollectionMachinePolicyResource child_index_response_descriptor_policies_machine_policy_machines_workers_worker_machine_policy_resource_worker_resource_spaces(base_space_id, skip=skip, take=take)

Get a list of WorkerResources

Lists all of the workers that belong to the given machine policy.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.MachinePoliciesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of WorkerResources
    api_response = api_instance.child_index_response_descriptor_policies_machine_policy_machines_workers_worker_machine_policy_resource_worker_resource_spaces(base_space_id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinePoliciesApi->child_index_response_descriptor_policies_machine_policy_machines_workers_worker_machine_policy_resource_worker_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionMachinePolicyResource**](ResourceCollectionMachinePolicyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response_descriptor_policies_machine_policy_machine_policy_resource**
> MachinePolicyResource create_response_descriptor_policies_machine_policy_machine_policy_resource(machine_policy_resource=machine_policy_resource)

Create a MachinePolicyResource

Creates a new machine policy.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.MachinePoliciesApi(octopus_deploy_swagger_client.ApiClient(configuration))
machine_policy_resource = octopus_deploy_swagger_client.MachinePolicyResource() # MachinePolicyResource | The MachinePolicyResource resource to create (optional)

try:
    # Create a MachinePolicyResource
    api_response = api_instance.create_response_descriptor_policies_machine_policy_machine_policy_resource(machine_policy_resource=machine_policy_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinePoliciesApi->create_response_descriptor_policies_machine_policy_machine_policy_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **machine_policy_resource** | [**MachinePolicyResource**](MachinePolicyResource.md)| The MachinePolicyResource resource to create | [optional] 

### Return type

[**MachinePolicyResource**](MachinePolicyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response_descriptor_policies_machine_policy_machine_policy_resource_spaces**
> MachinePolicyResource create_response_descriptor_policies_machine_policy_machine_policy_resource_spaces(base_space_id, machine_policy_resource=machine_policy_resource)

Create a MachinePolicyResource

Creates a new machine policy.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.MachinePoliciesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
machine_policy_resource = octopus_deploy_swagger_client.MachinePolicyResource() # MachinePolicyResource | The MachinePolicyResource resource to create (optional)

try:
    # Create a MachinePolicyResource
    api_response = api_instance.create_response_descriptor_policies_machine_policy_machine_policy_resource_spaces(base_space_id, machine_policy_resource=machine_policy_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinePoliciesApi->create_response_descriptor_policies_machine_policy_machine_policy_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **machine_policy_resource** | [**MachinePolicyResource**](MachinePolicyResource.md)| The MachinePolicyResource resource to create | [optional] 

### Return type

[**MachinePolicyResource**](MachinePolicyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_delete_action**
> custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_delete_action(id)



Deletes an existing machine policy.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.MachinePoliciesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_delete_action(id)
except ApiException as e:
    print("Exception when calling MachinePoliciesApi->custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_delete_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_delete_action_spaces**
> custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_delete_action_spaces(base_space_id, id)



Deletes an existing machine policy.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.MachinePoliciesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_delete_action_spaces(base_space_id, id)
except ApiException as e:
    print("Exception when calling MachinePoliciesApi->custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_delete_action_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_template_action**
> MachinePolicyResource custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_template_action()



Gets a template for a new Machine Policy, which includes any defaults.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.MachinePoliciesApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_template_action()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinePoliciesApi->custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_template_action: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MachinePolicyResource**](MachinePolicyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_template_action_spaces**
> MachinePolicyResource custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_template_action_spaces(base_space_id)



Gets a template for a new Machine Policy, which includes any defaults.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.MachinePoliciesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_template_action_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinePoliciesApi->custom_action_response_descriptor_octopus_server_web_api_actions_machine_policy_template_action_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**MachinePolicyResource**](MachinePolicyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_policies_machine_policy_machine_policy_resource**
> ResourceCollectionMachinePolicyResource index_response_descriptor_policies_machine_policy_machine_policy_resource(skip=skip, take=take)

Get a list of MachinePolicyResources

Lists all of the machine policies in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.MachinePoliciesApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of MachinePolicyResources
    api_response = api_instance.index_response_descriptor_policies_machine_policy_machine_policy_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinePoliciesApi->index_response_descriptor_policies_machine_policy_machine_policy_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionMachinePolicyResource**](ResourceCollectionMachinePolicyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_policies_machine_policy_machine_policy_resource_spaces**
> ResourceCollectionMachinePolicyResource index_response_descriptor_policies_machine_policy_machine_policy_resource_spaces(base_space_id, skip=skip, take=take)

Get a list of MachinePolicyResources

Lists all of the machine policies in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.MachinePoliciesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of MachinePolicyResources
    api_response = api_instance.index_response_descriptor_policies_machine_policy_machine_policy_resource_spaces(base_space_id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinePoliciesApi->index_response_descriptor_policies_machine_policy_machine_policy_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionMachinePolicyResource**](ResourceCollectionMachinePolicyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_policies_machine_policy_machine_policy_resource**
> list[MachinePolicyResource] list_all_response_descriptor_policies_machine_policy_machine_policy_resource()

Get a list of MachinePolicyResources

Lists all the machine policies in the supplied Octopus Deploy Space.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.MachinePoliciesApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    # Get a list of MachinePolicyResources
    api_response = api_instance.list_all_response_descriptor_policies_machine_policy_machine_policy_resource()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinePoliciesApi->list_all_response_descriptor_policies_machine_policy_machine_policy_resource: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MachinePolicyResource]**](MachinePolicyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_policies_machine_policy_machine_policy_resource_spaces**
> list[MachinePolicyResource] list_all_response_descriptor_policies_machine_policy_machine_policy_resource_spaces(base_space_id)

Get a list of MachinePolicyResources

Lists all the machine policies in the supplied Octopus Deploy Space.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.MachinePoliciesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    # Get a list of MachinePolicyResources
    api_response = api_instance.list_all_response_descriptor_policies_machine_policy_machine_policy_resource_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinePoliciesApi->list_all_response_descriptor_policies_machine_policy_machine_policy_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**list[MachinePolicyResource]**](MachinePolicyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_policies_machine_policy_machine_policy_resource**
> MachinePolicyResource load_response_descriptor_policies_machine_policy_machine_policy_resource(id)

Get a MachinePolicyResource by ID

Gets a single machine policy by ID.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.MachinePoliciesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the MachinePolicyResource to load

try:
    # Get a MachinePolicyResource by ID
    api_response = api_instance.load_response_descriptor_policies_machine_policy_machine_policy_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinePoliciesApi->load_response_descriptor_policies_machine_policy_machine_policy_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the MachinePolicyResource to load | 

### Return type

[**MachinePolicyResource**](MachinePolicyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_policies_machine_policy_machine_policy_resource_spaces**
> MachinePolicyResource load_response_descriptor_policies_machine_policy_machine_policy_resource_spaces(base_space_id, id)

Get a MachinePolicyResource by ID

Gets a single machine policy by ID.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.MachinePoliciesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the MachinePolicyResource to load

try:
    # Get a MachinePolicyResource by ID
    api_response = api_instance.load_response_descriptor_policies_machine_policy_machine_policy_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinePoliciesApi->load_response_descriptor_policies_machine_policy_machine_policy_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the MachinePolicyResource to load | 

### Return type

[**MachinePolicyResource**](MachinePolicyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_policies_machine_policy_machine_policy_resource**
> MachinePolicyResource modify_response_descriptor_policies_machine_policy_machine_policy_resource(id, machine_policy_resource=machine_policy_resource)

Modify a MachinePolicyResource by ID

Modifies an existing machine policy.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.MachinePoliciesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the MachinePolicyResource to modify
machine_policy_resource = octopus_deploy_swagger_client.MachinePolicyResource() # MachinePolicyResource | The MachinePolicyResource resource to create (optional)

try:
    # Modify a MachinePolicyResource by ID
    api_response = api_instance.modify_response_descriptor_policies_machine_policy_machine_policy_resource(id, machine_policy_resource=machine_policy_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinePoliciesApi->modify_response_descriptor_policies_machine_policy_machine_policy_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the MachinePolicyResource to modify | 
 **machine_policy_resource** | [**MachinePolicyResource**](MachinePolicyResource.md)| The MachinePolicyResource resource to create | [optional] 

### Return type

[**MachinePolicyResource**](MachinePolicyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_policies_machine_policy_machine_policy_resource_spaces**
> MachinePolicyResource modify_response_descriptor_policies_machine_policy_machine_policy_resource_spaces(base_space_id, id, machine_policy_resource=machine_policy_resource)

Modify a MachinePolicyResource by ID

Modifies an existing machine policy.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-Octopus-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Octopus-ApiKey'] = 'Bearer'
# Configure API key authorization: APIKeyQuery
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: NugetApiKeyHeader
configuration = octopus_deploy_swagger_client.Configuration()
configuration.api_key['X-NuGet-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-NuGet-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.MachinePoliciesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the MachinePolicyResource to modify
machine_policy_resource = octopus_deploy_swagger_client.MachinePolicyResource() # MachinePolicyResource | The MachinePolicyResource resource to create (optional)

try:
    # Modify a MachinePolicyResource by ID
    api_response = api_instance.modify_response_descriptor_policies_machine_policy_machine_policy_resource_spaces(base_space_id, id, machine_policy_resource=machine_policy_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinePoliciesApi->modify_response_descriptor_policies_machine_policy_machine_policy_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the MachinePolicyResource to modify | 
 **machine_policy_resource** | [**MachinePolicyResource**](MachinePolicyResource.md)| The MachinePolicyResource resource to create | [optional] 

### Return type

[**MachinePolicyResource**](MachinePolicyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

