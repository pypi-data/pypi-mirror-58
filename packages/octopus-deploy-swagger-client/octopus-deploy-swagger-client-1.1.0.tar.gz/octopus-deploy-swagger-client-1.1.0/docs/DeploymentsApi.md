# octopus_deploy_swagger_client.DeploymentsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_action_response_descriptor_octopus_server_web_api_actions_deployment_create_action**](DeploymentsApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_deployment_create_action) | **POST** /api/deployments | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_deployment_create_action_spaces**](DeploymentsApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_deployment_create_action_spaces) | **POST** /api/{baseSpaceId}/deployments | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_deployments_query_responder**](DeploymentsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_deployments_query_responder) | **GET** /api/deployments | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_deployments_query_responder_spaces**](DeploymentsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_deployments_query_responder_spaces) | **GET** /api/{baseSpaceId}/deployments | 
[**delete_on_background_response_descriptor_projects_deployment_deployment_resource**](DeploymentsApi.md#delete_on_background_response_descriptor_projects_deployment_deployment_resource) | **DELETE** /api/deployments/{id} | Delete a DeploymentResource by ID
[**delete_on_background_response_descriptor_projects_deployment_deployment_resource_spaces**](DeploymentsApi.md#delete_on_background_response_descriptor_projects_deployment_deployment_resource_spaces) | **DELETE** /api/{baseSpaceId}/deployments/{id} | Delete a DeploymentResource by ID
[**load_response_descriptor_projects_deployment_deployment_resource**](DeploymentsApi.md#load_response_descriptor_projects_deployment_deployment_resource) | **GET** /api/deployments/{id} | Get a DeploymentResource by ID
[**load_response_descriptor_projects_deployment_deployment_resource_spaces**](DeploymentsApi.md#load_response_descriptor_projects_deployment_deployment_resource_spaces) | **GET** /api/{baseSpaceId}/deployments/{id} | Get a DeploymentResource by ID


# **custom_action_response_descriptor_octopus_server_web_api_actions_deployment_create_action**
> DeploymentResource custom_action_response_descriptor_octopus_server_web_api_actions_deployment_create_action()



Creates a new deployment.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.DeploymentsApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_deployment_create_action()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->custom_action_response_descriptor_octopus_server_web_api_actions_deployment_create_action: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeploymentResource**](DeploymentResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_deployment_create_action_spaces**
> DeploymentResource custom_action_response_descriptor_octopus_server_web_api_actions_deployment_create_action_spaces(base_space_id)



Creates a new deployment.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.DeploymentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_deployment_create_action_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->custom_action_response_descriptor_octopus_server_web_api_actions_deployment_create_action_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**DeploymentResource**](DeploymentResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_deployments_query_responder**
> ResourceCollectionDeploymentResource custom_query_response_descriptor_octopus_server_web_api_actions_deployments_query_responder()



Lists all of the deployments in the supplied Octopus Deploy Space, from projects, releases and environments accessible by the current user. The results will be sorted from most recent to least recent deployment.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.DeploymentsApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_deployments_query_responder()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->custom_query_response_descriptor_octopus_server_web_api_actions_deployments_query_responder: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceCollectionDeploymentResource**](ResourceCollectionDeploymentResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_deployments_query_responder_spaces**
> ResourceCollectionDeploymentResource custom_query_response_descriptor_octopus_server_web_api_actions_deployments_query_responder_spaces(base_space_id)



Lists all of the deployments in the supplied Octopus Deploy Space, from projects, releases and environments accessible by the current user. The results will be sorted from most recent to least recent deployment.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.DeploymentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_deployments_query_responder_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->custom_query_response_descriptor_octopus_server_web_api_actions_deployments_query_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**ResourceCollectionDeploymentResource**](ResourceCollectionDeploymentResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_projects_deployment_deployment_resource**
> TaskResource delete_on_background_response_descriptor_projects_deployment_deployment_resource(id)

Delete a DeploymentResource by ID

Deletes a deployment.

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
api_instance = octopus_deploy_swagger_client.DeploymentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the DeploymentResource to delete

try:
    # Delete a DeploymentResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_projects_deployment_deployment_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->delete_on_background_response_descriptor_projects_deployment_deployment_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the DeploymentResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_projects_deployment_deployment_resource_spaces**
> TaskResource delete_on_background_response_descriptor_projects_deployment_deployment_resource_spaces(base_space_id, id)

Delete a DeploymentResource by ID

Deletes a deployment.

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
api_instance = octopus_deploy_swagger_client.DeploymentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the DeploymentResource to delete

try:
    # Delete a DeploymentResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_projects_deployment_deployment_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->delete_on_background_response_descriptor_projects_deployment_deployment_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the DeploymentResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_projects_deployment_deployment_resource**
> DeploymentResource load_response_descriptor_projects_deployment_deployment_resource(id)

Get a DeploymentResource by ID

Gets a deployment by ID.

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
api_instance = octopus_deploy_swagger_client.DeploymentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the DeploymentResource to load

try:
    # Get a DeploymentResource by ID
    api_response = api_instance.load_response_descriptor_projects_deployment_deployment_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->load_response_descriptor_projects_deployment_deployment_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the DeploymentResource to load | 

### Return type

[**DeploymentResource**](DeploymentResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_projects_deployment_deployment_resource_spaces**
> DeploymentResource load_response_descriptor_projects_deployment_deployment_resource_spaces(base_space_id, id)

Get a DeploymentResource by ID

Gets a deployment by ID.

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
api_instance = octopus_deploy_swagger_client.DeploymentsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the DeploymentResource to load

try:
    # Get a DeploymentResource by ID
    api_response = api_instance.load_response_descriptor_projects_deployment_deployment_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->load_response_descriptor_projects_deployment_deployment_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the DeploymentResource to load | 

### Return type

[**DeploymentResource**](DeploymentResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

