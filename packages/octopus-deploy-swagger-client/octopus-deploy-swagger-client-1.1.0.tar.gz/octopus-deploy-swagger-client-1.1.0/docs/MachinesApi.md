# octopus_deploy_swagger_client.MachinesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource**](MachinesApi.md#create_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource) | **POST** /api/machines | Create a DeploymentTargetResource
[**create_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces**](MachinesApi.md#create_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces) | **POST** /api/{baseSpaceId}/machines | Create a DeploymentTargetResource
[**custom_action_response_descriptor_octopus_server_web_api_actions_deployment_target_connection_status_responder**](MachinesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_deployment_target_connection_status_responder) | **GET** /api/machines/{id}/connection | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_deployment_target_connection_status_responder_spaces**](MachinesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_deployment_target_connection_status_responder_spaces) | **GET** /api/{baseSpaceId}/machines/{id}/connection | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_discover_deployment_target_responder**](MachinesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_discover_deployment_target_responder) | **GET** /api/machines/discover | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_discover_deployment_target_responder_spaces**](MachinesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_discover_deployment_target_responder_spaces) | **GET** /api/{baseSpaceId}/machines/discover | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_list_deployment_target_responder**](MachinesApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_list_deployment_target_responder) | **GET** /api/machines | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_list_deployment_target_responder_spaces**](MachinesApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_list_deployment_target_responder_spaces) | **GET** /api/{baseSpaceId}/machines | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_machine_task_responder**](MachinesApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_machine_task_responder) | **GET** /api/machines/{id}/tasks | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_machine_task_responder_spaces**](MachinesApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_machine_task_responder_spaces) | **GET** /api/{baseSpaceId}/machines/{id}/tasks | 
[**delete_on_background_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource**](MachinesApi.md#delete_on_background_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource) | **DELETE** /api/machines/{id} | Delete a DeploymentTargetResource by ID
[**delete_on_background_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces**](MachinesApi.md#delete_on_background_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces) | **DELETE** /api/{baseSpaceId}/machines/{id} | Delete a DeploymentTargetResource by ID
[**list_all_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource**](MachinesApi.md#list_all_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource) | **GET** /api/machines/all | Get a list of DeploymentTargetResources
[**list_all_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces**](MachinesApi.md#list_all_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces) | **GET** /api/{baseSpaceId}/machines/all | Get a list of DeploymentTargetResources
[**load_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource**](MachinesApi.md#load_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource) | **GET** /api/machines/{id} | Get a DeploymentTargetResource by ID
[**load_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces**](MachinesApi.md#load_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces) | **GET** /api/{baseSpaceId}/machines/{id} | Get a DeploymentTargetResource by ID
[**modify_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource**](MachinesApi.md#modify_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource) | **PUT** /api/machines/{id} | Modify a DeploymentTargetResource by ID
[**modify_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces**](MachinesApi.md#modify_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces) | **PUT** /api/{baseSpaceId}/machines/{id} | Modify a DeploymentTargetResource by ID


# **create_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource**
> DeploymentTargetResource create_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource(deployment_target_resource=deployment_target_resource)

Create a DeploymentTargetResource

Creates a new machine.

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
api_instance = octopus_deploy_swagger_client.MachinesApi(octopus_deploy_swagger_client.ApiClient(configuration))
deployment_target_resource = octopus_deploy_swagger_client.DeploymentTargetResource() # DeploymentTargetResource | The DeploymentTargetResource resource to create (optional)

try:
    # Create a DeploymentTargetResource
    api_response = api_instance.create_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource(deployment_target_resource=deployment_target_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->create_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_target_resource** | [**DeploymentTargetResource**](DeploymentTargetResource.md)| The DeploymentTargetResource resource to create | [optional] 

### Return type

[**DeploymentTargetResource**](DeploymentTargetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces**
> DeploymentTargetResource create_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces(base_space_id, deployment_target_resource=deployment_target_resource)

Create a DeploymentTargetResource

Creates a new machine.

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
api_instance = octopus_deploy_swagger_client.MachinesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
deployment_target_resource = octopus_deploy_swagger_client.DeploymentTargetResource() # DeploymentTargetResource | The DeploymentTargetResource resource to create (optional)

try:
    # Create a DeploymentTargetResource
    api_response = api_instance.create_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces(base_space_id, deployment_target_resource=deployment_target_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->create_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **deployment_target_resource** | [**DeploymentTargetResource**](DeploymentTargetResource.md)| The DeploymentTargetResource resource to create | [optional] 

### Return type

[**DeploymentTargetResource**](DeploymentTargetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_deployment_target_connection_status_responder**
> MachineConnectionStatus custom_action_response_descriptor_octopus_server_web_api_actions_deployment_target_connection_status_responder(id)



Get the status of the network connection between the Octopus server and a machine.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.MachinesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_deployment_target_connection_status_responder(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->custom_action_response_descriptor_octopus_server_web_api_actions_deployment_target_connection_status_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**MachineConnectionStatus**](MachineConnectionStatus.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_deployment_target_connection_status_responder_spaces**
> MachineConnectionStatus custom_action_response_descriptor_octopus_server_web_api_actions_deployment_target_connection_status_responder_spaces(base_space_id, id)



Get the status of the network connection between the Octopus server and a machine.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.MachinesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_deployment_target_connection_status_responder_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->custom_action_response_descriptor_octopus_server_web_api_actions_deployment_target_connection_status_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

[**MachineConnectionStatus**](MachineConnectionStatus.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_discover_deployment_target_responder**
> MachineResource custom_action_response_descriptor_octopus_server_web_api_actions_discover_deployment_target_responder()



Interrogate a machine for communication details so that it may be added to the installation.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.MachinesApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_discover_deployment_target_responder()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->custom_action_response_descriptor_octopus_server_web_api_actions_discover_deployment_target_responder: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MachineResource**](MachineResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_discover_deployment_target_responder_spaces**
> MachineResource custom_action_response_descriptor_octopus_server_web_api_actions_discover_deployment_target_responder_spaces(base_space_id)



Interrogate a machine for communication details so that it may be added to the installation.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.MachinesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_discover_deployment_target_responder_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->custom_action_response_descriptor_octopus_server_web_api_actions_discover_deployment_target_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**MachineResource**](MachineResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_list_deployment_target_responder**
> custom_query_response_descriptor_octopus_server_web_api_actions_list_deployment_target_responder()



Lists all of the registered machines in the supplied Octopus Deploy Space, from all environments. The results will be sorted alphabetically by name.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.MachinesApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_list_deployment_target_responder()
except ApiException as e:
    print("Exception when calling MachinesApi->custom_query_response_descriptor_octopus_server_web_api_actions_list_deployment_target_responder: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_list_deployment_target_responder_spaces**
> custom_query_response_descriptor_octopus_server_web_api_actions_list_deployment_target_responder_spaces(base_space_id)



Lists all of the registered machines in the supplied Octopus Deploy Space, from all environments. The results will be sorted alphabetically by name.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.MachinesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_list_deployment_target_responder_spaces(base_space_id)
except ApiException as e:
    print("Exception when calling MachinesApi->custom_query_response_descriptor_octopus_server_web_api_actions_list_deployment_target_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_machine_task_responder**
> ResourceCollectionTaskResource custom_query_response_descriptor_octopus_server_web_api_actions_machine_task_responder(id)



Get the history of related tasks for a machine.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.MachinesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the machine

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_machine_task_responder(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->custom_query_response_descriptor_octopus_server_web_api_actions_machine_task_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the machine | 

### Return type

[**ResourceCollectionTaskResource**](ResourceCollectionTaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_machine_task_responder_spaces**
> ResourceCollectionTaskResource custom_query_response_descriptor_octopus_server_web_api_actions_machine_task_responder_spaces(base_space_id, id)



Get the history of related tasks for a machine.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.MachinesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the machine

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_machine_task_responder_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->custom_query_response_descriptor_octopus_server_web_api_actions_machine_task_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the machine | 

### Return type

[**ResourceCollectionTaskResource**](ResourceCollectionTaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource**
> TaskResource delete_on_background_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource(id)

Delete a DeploymentTargetResource by ID

Deletes an existing machine.

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
api_instance = octopus_deploy_swagger_client.MachinesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the DeploymentTargetResource to delete

try:
    # Delete a DeploymentTargetResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->delete_on_background_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the DeploymentTargetResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces**
> TaskResource delete_on_background_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces(base_space_id, id)

Delete a DeploymentTargetResource by ID

Deletes an existing machine.

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
api_instance = octopus_deploy_swagger_client.MachinesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the DeploymentTargetResource to delete

try:
    # Delete a DeploymentTargetResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->delete_on_background_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the DeploymentTargetResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource**
> list[DeploymentTargetResource] list_all_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource()

Get a list of DeploymentTargetResources

Lists all of the deployment targets in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.

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
api_instance = octopus_deploy_swagger_client.MachinesApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    # Get a list of DeploymentTargetResources
    api_response = api_instance.list_all_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->list_all_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DeploymentTargetResource]**](DeploymentTargetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces**
> list[DeploymentTargetResource] list_all_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces(base_space_id)

Get a list of DeploymentTargetResources

Lists all of the deployment targets in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.

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
api_instance = octopus_deploy_swagger_client.MachinesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    # Get a list of DeploymentTargetResources
    api_response = api_instance.list_all_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->list_all_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**list[DeploymentTargetResource]**](DeploymentTargetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource**
> DeploymentTargetResource load_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource(id)

Get a DeploymentTargetResource by ID

Gets a single machine by ID.

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
api_instance = octopus_deploy_swagger_client.MachinesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the DeploymentTargetResource to load

try:
    # Get a DeploymentTargetResource by ID
    api_response = api_instance.load_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->load_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the DeploymentTargetResource to load | 

### Return type

[**DeploymentTargetResource**](DeploymentTargetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces**
> DeploymentTargetResource load_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces(base_space_id, id)

Get a DeploymentTargetResource by ID

Gets a single machine by ID.

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
api_instance = octopus_deploy_swagger_client.MachinesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the DeploymentTargetResource to load

try:
    # Get a DeploymentTargetResource by ID
    api_response = api_instance.load_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->load_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the DeploymentTargetResource to load | 

### Return type

[**DeploymentTargetResource**](DeploymentTargetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource**
> DeploymentTargetResource modify_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource(id, deployment_target_resource=deployment_target_resource)

Modify a DeploymentTargetResource by ID

Modifies an existing machine.

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
api_instance = octopus_deploy_swagger_client.MachinesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the DeploymentTargetResource to modify
deployment_target_resource = octopus_deploy_swagger_client.DeploymentTargetResource() # DeploymentTargetResource | The DeploymentTargetResource resource to create (optional)

try:
    # Modify a DeploymentTargetResource by ID
    api_response = api_instance.modify_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource(id, deployment_target_resource=deployment_target_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->modify_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the DeploymentTargetResource to modify | 
 **deployment_target_resource** | [**DeploymentTargetResource**](DeploymentTargetResource.md)| The DeploymentTargetResource resource to create | [optional] 

### Return type

[**DeploymentTargetResource**](DeploymentTargetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces**
> DeploymentTargetResource modify_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces(base_space_id, id, deployment_target_resource=deployment_target_resource)

Modify a DeploymentTargetResource by ID

Modifies an existing machine.

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
api_instance = octopus_deploy_swagger_client.MachinesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the DeploymentTargetResource to modify
deployment_target_resource = octopus_deploy_swagger_client.DeploymentTargetResource() # DeploymentTargetResource | The DeploymentTargetResource resource to create (optional)

try:
    # Modify a DeploymentTargetResource by ID
    api_response = api_instance.modify_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces(base_space_id, id, deployment_target_resource=deployment_target_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->modify_response_descriptor_machines_deployment_targets_deployment_target_deployment_target_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the DeploymentTargetResource to modify | 
 **deployment_target_resource** | [**DeploymentTargetResource**](DeploymentTargetResource.md)| The DeploymentTargetResource resource to create | [optional] 

### Return type

[**DeploymentTargetResource**](DeploymentTargetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

