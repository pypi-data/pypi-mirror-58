# octopus_deploy_swagger_client.EnvironmentsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_response_descriptor_environments_deployment_environment_environment_resource**](EnvironmentsApi.md#create_response_descriptor_environments_deployment_environment_environment_resource) | **POST** /api/environments | Create a EnvironmentResource
[**create_response_descriptor_environments_deployment_environment_environment_resource_spaces**](EnvironmentsApi.md#create_response_descriptor_environments_deployment_environment_environment_resource_spaces) | **POST** /api/{baseSpaceId}/environments | Create a EnvironmentResource
[**custom_action_response_descriptor_octopus_server_web_api_actions_environments_deployment_environment_settings_metadata_responder**](EnvironmentsApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_environments_deployment_environment_settings_metadata_responder) | **GET** /api/environments/{id}/metadata | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_environments_deployment_environment_settings_metadata_responder_spaces**](EnvironmentsApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_environments_deployment_environment_settings_metadata_responder_spaces) | **GET** /api/{baseSpaceId}/environments/{id}/metadata | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_sort_environments_responder**](EnvironmentsApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_sort_environments_responder) | **PUT** /api/environments/sortorder | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_sort_environments_responder_spaces**](EnvironmentsApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_sort_environments_responder_spaces) | **PUT** /api/{baseSpaceId}/environments/sortorder | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_variables_scoped_to_environment_responder**](EnvironmentsApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_variables_scoped_to_environment_responder) | **GET** /api/environments/{id}/singlyScopedVariableDetails | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_variables_scoped_to_environment_responder_spaces**](EnvironmentsApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_variables_scoped_to_environment_responder_spaces) | **GET** /api/{baseSpaceId}/environments/{id}/singlyScopedVariableDetails | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_environments_machines_responder**](EnvironmentsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_environments_machines_responder) | **GET** /api/environments/{id}/machines | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_environments_machines_responder_spaces**](EnvironmentsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_environments_machines_responder_spaces) | **GET** /api/{baseSpaceId}/environments/{id}/machines | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_environments_summary_responder**](EnvironmentsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_environments_summary_responder) | **GET** /api/environments/summary | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_environments_summary_responder_spaces**](EnvironmentsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_environments_summary_responder_spaces) | **GET** /api/{baseSpaceId}/environments/summary | 
[**delete_on_background_response_descriptor_environments_deployment_environment_environment_resource**](EnvironmentsApi.md#delete_on_background_response_descriptor_environments_deployment_environment_environment_resource) | **DELETE** /api/environments/{id} | Delete a EnvironmentResource by ID
[**delete_on_background_response_descriptor_environments_deployment_environment_environment_resource_spaces**](EnvironmentsApi.md#delete_on_background_response_descriptor_environments_deployment_environment_environment_resource_spaces) | **DELETE** /api/{baseSpaceId}/environments/{id} | Delete a EnvironmentResource by ID
[**index_response_descriptor_environments_deployment_environment_environment_resource**](EnvironmentsApi.md#index_response_descriptor_environments_deployment_environment_environment_resource) | **GET** /api/environments | Get a list of EnvironmentResources
[**index_response_descriptor_environments_deployment_environment_environment_resource_spaces**](EnvironmentsApi.md#index_response_descriptor_environments_deployment_environment_environment_resource_spaces) | **GET** /api/{baseSpaceId}/environments | Get a list of EnvironmentResources
[**list_all_response_descriptor_environments_deployment_environment_environment_resource**](EnvironmentsApi.md#list_all_response_descriptor_environments_deployment_environment_environment_resource) | **GET** /api/environments/all | Get a list of EnvironmentResources
[**list_all_response_descriptor_environments_deployment_environment_environment_resource_spaces**](EnvironmentsApi.md#list_all_response_descriptor_environments_deployment_environment_environment_resource_spaces) | **GET** /api/{baseSpaceId}/environments/all | Get a list of EnvironmentResources
[**load_response_descriptor_environments_deployment_environment_environment_resource**](EnvironmentsApi.md#load_response_descriptor_environments_deployment_environment_environment_resource) | **GET** /api/environments/{id} | Get a EnvironmentResource by ID
[**load_response_descriptor_environments_deployment_environment_environment_resource_spaces**](EnvironmentsApi.md#load_response_descriptor_environments_deployment_environment_environment_resource_spaces) | **GET** /api/{baseSpaceId}/environments/{id} | Get a EnvironmentResource by ID
[**modify_response_descriptor_environments_deployment_environment_environment_resource**](EnvironmentsApi.md#modify_response_descriptor_environments_deployment_environment_environment_resource) | **PUT** /api/environments/{id} | Modify a EnvironmentResource by ID
[**modify_response_descriptor_environments_deployment_environment_environment_resource_spaces**](EnvironmentsApi.md#modify_response_descriptor_environments_deployment_environment_environment_resource_spaces) | **PUT** /api/{baseSpaceId}/environments/{id} | Modify a EnvironmentResource by ID


# **create_response_descriptor_environments_deployment_environment_environment_resource**
> EnvironmentResource create_response_descriptor_environments_deployment_environment_environment_resource(environment_resource=environment_resource)

Create a EnvironmentResource

Creates a new environment.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
environment_resource = octopus_deploy_swagger_client.EnvironmentResource() # EnvironmentResource | The EnvironmentResource resource to create (optional)

try:
    # Create a EnvironmentResource
    api_response = api_instance.create_response_descriptor_environments_deployment_environment_environment_resource(environment_resource=environment_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->create_response_descriptor_environments_deployment_environment_environment_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_resource** | [**EnvironmentResource**](EnvironmentResource.md)| The EnvironmentResource resource to create | [optional] 

### Return type

[**EnvironmentResource**](EnvironmentResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response_descriptor_environments_deployment_environment_environment_resource_spaces**
> EnvironmentResource create_response_descriptor_environments_deployment_environment_environment_resource_spaces(base_space_id, environment_resource=environment_resource)

Create a EnvironmentResource

Creates a new environment.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
environment_resource = octopus_deploy_swagger_client.EnvironmentResource() # EnvironmentResource | The EnvironmentResource resource to create (optional)

try:
    # Create a EnvironmentResource
    api_response = api_instance.create_response_descriptor_environments_deployment_environment_environment_resource_spaces(base_space_id, environment_resource=environment_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->create_response_descriptor_environments_deployment_environment_environment_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **environment_resource** | [**EnvironmentResource**](EnvironmentResource.md)| The EnvironmentResource resource to create | [optional] 

### Return type

[**EnvironmentResource**](EnvironmentResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_environments_deployment_environment_settings_metadata_responder**
> list[DeploymentEnvironmentSettingsMetadata] custom_action_response_descriptor_octopus_server_web_api_actions_environments_deployment_environment_settings_metadata_responder(id)



Gets the custom settings metadata from the extensions.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_environments_deployment_environment_settings_metadata_responder(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->custom_action_response_descriptor_octopus_server_web_api_actions_environments_deployment_environment_settings_metadata_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**list[DeploymentEnvironmentSettingsMetadata]**](DeploymentEnvironmentSettingsMetadata.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_environments_deployment_environment_settings_metadata_responder_spaces**
> list[DeploymentEnvironmentSettingsMetadata] custom_action_response_descriptor_octopus_server_web_api_actions_environments_deployment_environment_settings_metadata_responder_spaces(base_space_id, id)



Gets the custom settings metadata from the extensions.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_environments_deployment_environment_settings_metadata_responder_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->custom_action_response_descriptor_octopus_server_web_api_actions_environments_deployment_environment_settings_metadata_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

[**list[DeploymentEnvironmentSettingsMetadata]**](DeploymentEnvironmentSettingsMetadata.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_sort_environments_responder**
> custom_action_response_descriptor_octopus_server_web_api_actions_sort_environments_responder()



Takes an array of environment IDs as the request body, uses the order of items in the array to sort the environments on the server. The ID of every environment must be specified.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_sort_environments_responder()
except ApiException as e:
    print("Exception when calling EnvironmentsApi->custom_action_response_descriptor_octopus_server_web_api_actions_sort_environments_responder: %s\n" % e)
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

# **custom_action_response_descriptor_octopus_server_web_api_actions_sort_environments_responder_spaces**
> custom_action_response_descriptor_octopus_server_web_api_actions_sort_environments_responder_spaces(base_space_id)



Takes an array of environment IDs as the request body, uses the order of items in the array to sort the environments on the server. The ID of every environment must be specified.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_sort_environments_responder_spaces(base_space_id)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->custom_action_response_descriptor_octopus_server_web_api_actions_sort_environments_responder_spaces: %s\n" % e)
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

# **custom_action_response_descriptor_octopus_server_web_api_actions_variables_scoped_to_environment_responder**
> VariablesScopedToEnvironmentResponse custom_action_response_descriptor_octopus_server_web_api_actions_variables_scoped_to_environment_responder(id)



Lists all the variable set names (projects and library variable sets) that have variables that are scoped to only the given environment  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_variables_scoped_to_environment_responder(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->custom_action_response_descriptor_octopus_server_web_api_actions_variables_scoped_to_environment_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**VariablesScopedToEnvironmentResponse**](VariablesScopedToEnvironmentResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_variables_scoped_to_environment_responder_spaces**
> VariablesScopedToEnvironmentResponse custom_action_response_descriptor_octopus_server_web_api_actions_variables_scoped_to_environment_responder_spaces(base_space_id, id)



Lists all the variable set names (projects and library variable sets) that have variables that are scoped to only the given environment  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_variables_scoped_to_environment_responder_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->custom_action_response_descriptor_octopus_server_web_api_actions_variables_scoped_to_environment_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

[**VariablesScopedToEnvironmentResponse**](VariablesScopedToEnvironmentResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_environments_machines_responder**
> custom_query_response_descriptor_octopus_server_web_api_actions_environments_machines_responder(id)



Lists all of the machines that belong to the given environment.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the environment

try:
    api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_environments_machines_responder(id)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->custom_query_response_descriptor_octopus_server_web_api_actions_environments_machines_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the environment | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_environments_machines_responder_spaces**
> custom_query_response_descriptor_octopus_server_web_api_actions_environments_machines_responder_spaces(base_space_id, id)



Lists all of the machines that belong to the given environment.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the environment

try:
    api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_environments_machines_responder_spaces(base_space_id, id)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->custom_query_response_descriptor_octopus_server_web_api_actions_environments_machines_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the environment | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_environments_summary_responder**
> custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_environments_summary_responder()



Lists all environments, including a summary of machine information  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_environments_summary_responder()
except ApiException as e:
    print("Exception when calling EnvironmentsApi->custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_environments_summary_responder: %s\n" % e)
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

# **custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_environments_summary_responder_spaces**
> custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_environments_summary_responder_spaces(base_space_id)



Lists all environments, including a summary of machine information  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_environments_summary_responder_spaces(base_space_id)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_environments_summary_responder_spaces: %s\n" % e)
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

# **delete_on_background_response_descriptor_environments_deployment_environment_environment_resource**
> TaskResource delete_on_background_response_descriptor_environments_deployment_environment_environment_resource(id)

Delete a EnvironmentResource by ID

Deletes an existing environment.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the EnvironmentResource to delete

try:
    # Delete a EnvironmentResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_environments_deployment_environment_environment_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->delete_on_background_response_descriptor_environments_deployment_environment_environment_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the EnvironmentResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_environments_deployment_environment_environment_resource_spaces**
> TaskResource delete_on_background_response_descriptor_environments_deployment_environment_environment_resource_spaces(base_space_id, id)

Delete a EnvironmentResource by ID

Deletes an existing environment.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the EnvironmentResource to delete

try:
    # Delete a EnvironmentResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_environments_deployment_environment_environment_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->delete_on_background_response_descriptor_environments_deployment_environment_environment_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the EnvironmentResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_environments_deployment_environment_environment_resource**
> ResourceCollectionEnvironmentResource index_response_descriptor_environments_deployment_environment_environment_resource(skip=skip, take=take)

Get a list of EnvironmentResources

Lists all of the environments in the supplied Octopus Deploy Space. The results will be sorted by the `SortOrder` field on each environment.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of EnvironmentResources
    api_response = api_instance.index_response_descriptor_environments_deployment_environment_environment_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->index_response_descriptor_environments_deployment_environment_environment_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionEnvironmentResource**](ResourceCollectionEnvironmentResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_environments_deployment_environment_environment_resource_spaces**
> ResourceCollectionEnvironmentResource index_response_descriptor_environments_deployment_environment_environment_resource_spaces(base_space_id, skip=skip, take=take)

Get a list of EnvironmentResources

Lists all of the environments in the supplied Octopus Deploy Space. The results will be sorted by the `SortOrder` field on each environment.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of EnvironmentResources
    api_response = api_instance.index_response_descriptor_environments_deployment_environment_environment_resource_spaces(base_space_id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->index_response_descriptor_environments_deployment_environment_environment_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionEnvironmentResource**](ResourceCollectionEnvironmentResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_environments_deployment_environment_environment_resource**
> list[EnvironmentResource] list_all_response_descriptor_environments_deployment_environment_environment_resource()

Get a list of EnvironmentResources

Lists the name and ID of all of the environments in the supplied Octopus Deploy Space. The results will be sorted by the `SortOrder` field on each environment.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    # Get a list of EnvironmentResources
    api_response = api_instance.list_all_response_descriptor_environments_deployment_environment_environment_resource()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->list_all_response_descriptor_environments_deployment_environment_environment_resource: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EnvironmentResource]**](EnvironmentResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_environments_deployment_environment_environment_resource_spaces**
> list[EnvironmentResource] list_all_response_descriptor_environments_deployment_environment_environment_resource_spaces(base_space_id)

Get a list of EnvironmentResources

Lists the name and ID of all of the environments in the supplied Octopus Deploy Space. The results will be sorted by the `SortOrder` field on each environment.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    # Get a list of EnvironmentResources
    api_response = api_instance.list_all_response_descriptor_environments_deployment_environment_environment_resource_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->list_all_response_descriptor_environments_deployment_environment_environment_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**list[EnvironmentResource]**](EnvironmentResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_environments_deployment_environment_environment_resource**
> EnvironmentResource load_response_descriptor_environments_deployment_environment_environment_resource(id)

Get a EnvironmentResource by ID

Gets a single environment by ID.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the EnvironmentResource to load

try:
    # Get a EnvironmentResource by ID
    api_response = api_instance.load_response_descriptor_environments_deployment_environment_environment_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->load_response_descriptor_environments_deployment_environment_environment_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the EnvironmentResource to load | 

### Return type

[**EnvironmentResource**](EnvironmentResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_environments_deployment_environment_environment_resource_spaces**
> EnvironmentResource load_response_descriptor_environments_deployment_environment_environment_resource_spaces(base_space_id, id)

Get a EnvironmentResource by ID

Gets a single environment by ID.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the EnvironmentResource to load

try:
    # Get a EnvironmentResource by ID
    api_response = api_instance.load_response_descriptor_environments_deployment_environment_environment_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->load_response_descriptor_environments_deployment_environment_environment_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the EnvironmentResource to load | 

### Return type

[**EnvironmentResource**](EnvironmentResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_environments_deployment_environment_environment_resource**
> EnvironmentResource modify_response_descriptor_environments_deployment_environment_environment_resource(id, environment_resource=environment_resource)

Modify a EnvironmentResource by ID

Modifies an existing environment.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the EnvironmentResource to modify
environment_resource = octopus_deploy_swagger_client.EnvironmentResource() # EnvironmentResource | The EnvironmentResource resource to create (optional)

try:
    # Modify a EnvironmentResource by ID
    api_response = api_instance.modify_response_descriptor_environments_deployment_environment_environment_resource(id, environment_resource=environment_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->modify_response_descriptor_environments_deployment_environment_environment_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the EnvironmentResource to modify | 
 **environment_resource** | [**EnvironmentResource**](EnvironmentResource.md)| The EnvironmentResource resource to create | [optional] 

### Return type

[**EnvironmentResource**](EnvironmentResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_environments_deployment_environment_environment_resource_spaces**
> EnvironmentResource modify_response_descriptor_environments_deployment_environment_environment_resource_spaces(base_space_id, id, environment_resource=environment_resource)

Modify a EnvironmentResource by ID

Modifies an existing environment.

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
api_instance = octopus_deploy_swagger_client.EnvironmentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the EnvironmentResource to modify
environment_resource = octopus_deploy_swagger_client.EnvironmentResource() # EnvironmentResource | The EnvironmentResource resource to create (optional)

try:
    # Modify a EnvironmentResource by ID
    api_response = api_instance.modify_response_descriptor_environments_deployment_environment_environment_resource_spaces(base_space_id, id, environment_resource=environment_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->modify_response_descriptor_environments_deployment_environment_environment_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the EnvironmentResource to modify | 
 **environment_resource** | [**EnvironmentResource**](EnvironmentResource.md)| The EnvironmentResource resource to create | [optional] 

### Return type

[**EnvironmentResource**](EnvironmentResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

