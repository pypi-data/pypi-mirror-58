# octopus_deploy_swagger_client.ReleasesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**child_index_response_descriptor_projects_project_projects_release_project_resource_release_resource**](ReleasesApi.md#child_index_response_descriptor_projects_project_projects_release_project_resource_release_resource) | **GET** /api/projects/{id}/releases | Get a list of ReleaseResources
[**child_index_response_descriptor_projects_project_projects_release_project_resource_release_resource_spaces**](ReleasesApi.md#child_index_response_descriptor_projects_project_projects_release_project_resource_release_resource_spaces) | **GET** /api/{baseSpaceId}/projects/{id}/releases | Get a list of ReleaseResources
[**child_index_response_descriptor_projects_release_projects_deployment_release_resource_deployment_resource**](ReleasesApi.md#child_index_response_descriptor_projects_release_projects_deployment_release_resource_deployment_resource) | **GET** /api/releases/{id}/deployments | Get a list of DeploymentResources
[**child_index_response_descriptor_projects_release_projects_deployment_release_resource_deployment_resource_spaces**](ReleasesApi.md#child_index_response_descriptor_projects_release_projects_deployment_release_resource_deployment_resource_spaces) | **GET** /api/{baseSpaceId}/releases/{id}/deployments | Get a list of DeploymentResources
[**create_response_descriptor_projects_release_release_resource**](ReleasesApi.md#create_response_descriptor_projects_release_release_resource) | **POST** /api/releases | Create a ReleaseResource
[**create_response_descriptor_projects_release_release_resource_spaces**](ReleasesApi.md#create_response_descriptor_projects_release_release_resource_spaces) | **POST** /api/{baseSpaceId}/releases | Create a ReleaseResource
[**custom_action_response_descriptor_octopus_server_web_api_actions_defect_reported_responder**](ReleasesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_defect_reported_responder) | **POST** /api/releases/{id}/defects | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_defect_reported_responder_spaces**](ReleasesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_defect_reported_responder_spaces) | **POST** /api/{baseSpaceId}/releases/{id}/defects | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_defect_resolved_responder**](ReleasesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_defect_resolved_responder) | **POST** /api/releases/{id}/defects/resolve | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_defect_resolved_responder_spaces**](ReleasesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_defect_resolved_responder_spaces) | **POST** /api/{baseSpaceId}/releases/{id}/defects/resolve | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action**](ReleasesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action) | **GET** /api/releases/{id}/deployments/preview/{environment} | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action_0**](ReleasesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action_0) | **GET** /api/releases/{id}/deployments/preview/{environment}/{tenant} | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action_spaces**](ReleasesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action_spaces) | **GET** /api/{baseSpaceId}/releases/{id}/deployments/preview/{environment} | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action_spaces_0**](ReleasesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action_spaces_0) | **GET** /api/{baseSpaceId}/releases/{id}/deployments/preview/{environment}/{tenant} | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_deployment_template_action**](ReleasesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_deployment_template_action) | **GET** /api/releases/{id}/deployments/template | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_deployment_template_action_spaces**](ReleasesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_deployment_template_action_spaces) | **GET** /api/{baseSpaceId}/releases/{id}/deployments/template | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_release_by_project_and_version_responder**](ReleasesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_release_by_project_and_version_responder) | **GET** /api/projects/{id}/releases/{version} | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_release_by_project_and_version_responder_spaces**](ReleasesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_release_by_project_and_version_responder_spaces) | **GET** /api/{baseSpaceId}/projects/{id}/releases/{version} | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_release_lifecycle_progression_action**](ReleasesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_release_lifecycle_progression_action) | **GET** /api/releases/{id}/progression | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_release_lifecycle_progression_action_spaces**](ReleasesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_release_lifecycle_progression_action_spaces) | **GET** /api/{baseSpaceId}/releases/{id}/progression | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_release_snapshot_variables_action**](ReleasesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_release_snapshot_variables_action) | **POST** /api/releases/{id}/snapshot-variables | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_release_snapshot_variables_action_spaces**](ReleasesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_release_snapshot_variables_action_spaces) | **POST** /api/{baseSpaceId}/releases/{id}/snapshot-variables | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_list_defects_responder**](ReleasesApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_list_defects_responder) | **GET** /api/releases/{id}/defects | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_list_defects_responder_spaces**](ReleasesApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_list_defects_responder_spaces) | **GET** /api/{baseSpaceId}/releases/{id}/defects | 
[**delete_on_background_response_descriptor_projects_release_release_resource**](ReleasesApi.md#delete_on_background_response_descriptor_projects_release_release_resource) | **DELETE** /api/releases/{id} | Delete a ReleaseResource by ID
[**delete_on_background_response_descriptor_projects_release_release_resource_spaces**](ReleasesApi.md#delete_on_background_response_descriptor_projects_release_release_resource_spaces) | **DELETE** /api/{baseSpaceId}/releases/{id} | Delete a ReleaseResource by ID
[**index_response_descriptor_projects_release_release_resource**](ReleasesApi.md#index_response_descriptor_projects_release_release_resource) | **GET** /api/releases | Get a list of ReleaseResources
[**index_response_descriptor_projects_release_release_resource_spaces**](ReleasesApi.md#index_response_descriptor_projects_release_release_resource_spaces) | **GET** /api/{baseSpaceId}/releases | Get a list of ReleaseResources
[**load_response_descriptor_projects_release_release_resource**](ReleasesApi.md#load_response_descriptor_projects_release_release_resource) | **GET** /api/releases/{id} | Get a ReleaseResource by ID
[**load_response_descriptor_projects_release_release_resource_spaces**](ReleasesApi.md#load_response_descriptor_projects_release_release_resource_spaces) | **GET** /api/{baseSpaceId}/releases/{id} | Get a ReleaseResource by ID
[**modify_response_descriptor_projects_release_release_resource**](ReleasesApi.md#modify_response_descriptor_projects_release_release_resource) | **PUT** /api/releases/{id} | Modify a ReleaseResource by ID
[**modify_response_descriptor_projects_release_release_resource_spaces**](ReleasesApi.md#modify_response_descriptor_projects_release_release_resource_spaces) | **PUT** /api/{baseSpaceId}/releases/{id} | Modify a ReleaseResource by ID


# **child_index_response_descriptor_projects_project_projects_release_project_resource_release_resource**
> ResourceCollectionProjectResource child_index_response_descriptor_projects_project_projects_release_project_resource_release_resource(skip=skip, take=take)

Get a list of ReleaseResources

Lists all of the releases that belong to the given project. Releases will be ordered from most recent to least recent.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of ReleaseResources
    api_response = api_instance.child_index_response_descriptor_projects_project_projects_release_project_resource_release_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->child_index_response_descriptor_projects_project_projects_release_project_resource_release_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionProjectResource**](ResourceCollectionProjectResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **child_index_response_descriptor_projects_project_projects_release_project_resource_release_resource_spaces**
> ResourceCollectionProjectResource child_index_response_descriptor_projects_project_projects_release_project_resource_release_resource_spaces(base_space_id, skip=skip, take=take)

Get a list of ReleaseResources

Lists all of the releases that belong to the given project. Releases will be ordered from most recent to least recent.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of ReleaseResources
    api_response = api_instance.child_index_response_descriptor_projects_project_projects_release_project_resource_release_resource_spaces(base_space_id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->child_index_response_descriptor_projects_project_projects_release_project_resource_release_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionProjectResource**](ResourceCollectionProjectResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **child_index_response_descriptor_projects_release_projects_deployment_release_resource_deployment_resource**
> ResourceCollectionReleaseResource child_index_response_descriptor_projects_release_projects_deployment_release_resource_deployment_resource(skip=skip, take=take)

Get a list of DeploymentResources

Lists all of the deployments that belong to the given release. Deployments will be ordered from most recent to least recent.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of DeploymentResources
    api_response = api_instance.child_index_response_descriptor_projects_release_projects_deployment_release_resource_deployment_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->child_index_response_descriptor_projects_release_projects_deployment_release_resource_deployment_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionReleaseResource**](ResourceCollectionReleaseResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **child_index_response_descriptor_projects_release_projects_deployment_release_resource_deployment_resource_spaces**
> ResourceCollectionReleaseResource child_index_response_descriptor_projects_release_projects_deployment_release_resource_deployment_resource_spaces(base_space_id, skip=skip, take=take)

Get a list of DeploymentResources

Lists all of the deployments that belong to the given release. Deployments will be ordered from most recent to least recent.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of DeploymentResources
    api_response = api_instance.child_index_response_descriptor_projects_release_projects_deployment_release_resource_deployment_resource_spaces(base_space_id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->child_index_response_descriptor_projects_release_projects_deployment_release_resource_deployment_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionReleaseResource**](ResourceCollectionReleaseResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response_descriptor_projects_release_release_resource**
> ReleaseResource create_response_descriptor_projects_release_release_resource(release_resource=release_resource)

Create a ReleaseResource

Creates a new release.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
release_resource = octopus_deploy_swagger_client.ReleaseResource() # ReleaseResource | The ReleaseResource resource to create (optional)

try:
    # Create a ReleaseResource
    api_response = api_instance.create_response_descriptor_projects_release_release_resource(release_resource=release_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->create_response_descriptor_projects_release_release_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_resource** | [**ReleaseResource**](ReleaseResource.md)| The ReleaseResource resource to create | [optional] 

### Return type

[**ReleaseResource**](ReleaseResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response_descriptor_projects_release_release_resource_spaces**
> ReleaseResource create_response_descriptor_projects_release_release_resource_spaces(base_space_id, release_resource=release_resource)

Create a ReleaseResource

Creates a new release.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
release_resource = octopus_deploy_swagger_client.ReleaseResource() # ReleaseResource | The ReleaseResource resource to create (optional)

try:
    # Create a ReleaseResource
    api_response = api_instance.create_response_descriptor_projects_release_release_resource_spaces(base_space_id, release_resource=release_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->create_response_descriptor_projects_release_release_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **release_resource** | [**ReleaseResource**](ReleaseResource.md)| The ReleaseResource resource to create | [optional] 

### Return type

[**ReleaseResource**](ReleaseResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_defect_reported_responder**
> DefectResource custom_action_response_descriptor_octopus_server_web_api_actions_defect_reported_responder(id)



Record defect in a release.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_defect_reported_responder(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->custom_action_response_descriptor_octopus_server_web_api_actions_defect_reported_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**DefectResource**](DefectResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_defect_reported_responder_spaces**
> DefectResource custom_action_response_descriptor_octopus_server_web_api_actions_defect_reported_responder_spaces(base_space_id, id)



Record defect in a release.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_defect_reported_responder_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->custom_action_response_descriptor_octopus_server_web_api_actions_defect_reported_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

[**DefectResource**](DefectResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_defect_resolved_responder**
> DefectResource custom_action_response_descriptor_octopus_server_web_api_actions_defect_resolved_responder(id)



Update or resolve defect in a release.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_defect_resolved_responder(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->custom_action_response_descriptor_octopus_server_web_api_actions_defect_resolved_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**DefectResource**](DefectResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_defect_resolved_responder_spaces**
> DefectResource custom_action_response_descriptor_octopus_server_web_api_actions_defect_resolved_responder_spaces(base_space_id, id)



Update or resolve defect in a release.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_defect_resolved_responder_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->custom_action_response_descriptor_octopus_server_web_api_actions_defect_resolved_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

[**DefectResource**](DefectResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action**
> DeploymentPreviewResource custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action(environment, tenant, id)



Gets a document that describes what steps will/won't be run during a deployment to a given environment.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
environment = 'environment_example' # str | ID of the environment
tenant = 'tenant_example' # str | ID of the tenant
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action(environment, tenant, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| ID of the environment | 
 **tenant** | **str**| ID of the tenant | 
 **id** | **str**| ID of the resource | 

### Return type

[**DeploymentPreviewResource**](DeploymentPreviewResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action_0**
> DeploymentPreviewResource custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action_0(environment, tenant, id)



Gets a document that describes what steps will/won't be run during a deployment to a given environment for the given tenant.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
environment = 'environment_example' # str | ID of the environment
tenant = 'tenant_example' # str | ID of the tenant
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action_0(environment, tenant, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| ID of the environment | 
 **tenant** | **str**| ID of the tenant | 
 **id** | **str**| ID of the resource | 

### Return type

[**DeploymentPreviewResource**](DeploymentPreviewResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action_spaces**
> DeploymentPreviewResource custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action_spaces(base_space_id, environment, tenant, id)



Gets a document that describes what steps will/won't be run during a deployment to a given environment.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
environment = 'environment_example' # str | ID of the environment
tenant = 'tenant_example' # str | ID of the tenant
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action_spaces(base_space_id, environment, tenant, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **environment** | **str**| ID of the environment | 
 **tenant** | **str**| ID of the tenant | 
 **id** | **str**| ID of the resource | 

### Return type

[**DeploymentPreviewResource**](DeploymentPreviewResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action_spaces_0**
> DeploymentPreviewResource custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action_spaces_0(base_space_id, environment, tenant, id)



Gets a document that describes what steps will/won't be run during a deployment to a given environment for the given tenant.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
environment = 'environment_example' # str | ID of the environment
tenant = 'tenant_example' # str | ID of the tenant
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action_spaces_0(base_space_id, environment, tenant, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->custom_action_response_descriptor_octopus_server_web_api_actions_deployment_preview_action_spaces_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **environment** | **str**| ID of the environment | 
 **tenant** | **str**| ID of the tenant | 
 **id** | **str**| ID of the resource | 

### Return type

[**DeploymentPreviewResource**](DeploymentPreviewResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_deployment_template_action**
> DeploymentTemplateResource custom_action_response_descriptor_octopus_server_web_api_actions_deployment_template_action(id)



Gets all of the information necessary for creating or editing a deployment for this release.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_deployment_template_action(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->custom_action_response_descriptor_octopus_server_web_api_actions_deployment_template_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**DeploymentTemplateResource**](DeploymentTemplateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_deployment_template_action_spaces**
> DeploymentTemplateResource custom_action_response_descriptor_octopus_server_web_api_actions_deployment_template_action_spaces(base_space_id, id)



Gets all of the information necessary for creating or editing a deployment for this release.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_deployment_template_action_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->custom_action_response_descriptor_octopus_server_web_api_actions_deployment_template_action_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

[**DeploymentTemplateResource**](DeploymentTemplateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_release_by_project_and_version_responder**
> ReleaseResource custom_action_response_descriptor_octopus_server_web_api_actions_release_by_project_and_version_responder(version, id)



Gets a single release by project ID and version number.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
version = 'version_example' # str | ERROR - NOT DEFINED
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_release_by_project_and_version_responder(version, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->custom_action_response_descriptor_octopus_server_web_api_actions_release_by_project_and_version_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| ERROR - NOT DEFINED | 
 **id** | **str**| ID of the resource | 

### Return type

[**ReleaseResource**](ReleaseResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_release_by_project_and_version_responder_spaces**
> ReleaseResource custom_action_response_descriptor_octopus_server_web_api_actions_release_by_project_and_version_responder_spaces(base_space_id, version, id)



Gets a single release by project ID and version number.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
version = 'version_example' # str | ERROR - NOT DEFINED
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_release_by_project_and_version_responder_spaces(base_space_id, version, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->custom_action_response_descriptor_octopus_server_web_api_actions_release_by_project_and_version_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **version** | **str**| ERROR - NOT DEFINED | 
 **id** | **str**| ID of the resource | 

### Return type

[**ReleaseResource**](ReleaseResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_release_lifecycle_progression_action**
> LifecycleProgressionResource custom_action_response_descriptor_octopus_server_web_api_actions_release_lifecycle_progression_action(id)



Gets all of the information necessary for creating or editing a deployment for this release.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_release_lifecycle_progression_action(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->custom_action_response_descriptor_octopus_server_web_api_actions_release_lifecycle_progression_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**LifecycleProgressionResource**](LifecycleProgressionResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_release_lifecycle_progression_action_spaces**
> LifecycleProgressionResource custom_action_response_descriptor_octopus_server_web_api_actions_release_lifecycle_progression_action_spaces(base_space_id, id)



Gets all of the information necessary for creating or editing a deployment for this release.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_release_lifecycle_progression_action_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->custom_action_response_descriptor_octopus_server_web_api_actions_release_lifecycle_progression_action_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

[**LifecycleProgressionResource**](LifecycleProgressionResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_release_snapshot_variables_action**
> ReleaseResource custom_action_response_descriptor_octopus_server_web_api_actions_release_snapshot_variables_action(id)



Refresh the variable snapshots associated with the release. The project's deployment process must not have changed since the release was created.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_release_snapshot_variables_action(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->custom_action_response_descriptor_octopus_server_web_api_actions_release_snapshot_variables_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**ReleaseResource**](ReleaseResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_release_snapshot_variables_action_spaces**
> ReleaseResource custom_action_response_descriptor_octopus_server_web_api_actions_release_snapshot_variables_action_spaces(base_space_id, id)



Refresh the variable snapshots associated with the release. The project's deployment process must not have changed since the release was created.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_release_snapshot_variables_action_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->custom_action_response_descriptor_octopus_server_web_api_actions_release_snapshot_variables_action_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

[**ReleaseResource**](ReleaseResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_list_defects_responder**
> ResourceCollectionDefectResource custom_query_response_descriptor_octopus_server_web_api_actions_list_defects_responder(id)



Gets all defects for a release.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the defect

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_list_defects_responder(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->custom_query_response_descriptor_octopus_server_web_api_actions_list_defects_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the defect | 

### Return type

[**ResourceCollectionDefectResource**](ResourceCollectionDefectResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_list_defects_responder_spaces**
> ResourceCollectionDefectResource custom_query_response_descriptor_octopus_server_web_api_actions_list_defects_responder_spaces(base_space_id, id)



Gets all defects for a release.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the defect

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_list_defects_responder_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->custom_query_response_descriptor_octopus_server_web_api_actions_list_defects_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the defect | 

### Return type

[**ResourceCollectionDefectResource**](ResourceCollectionDefectResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_projects_release_release_resource**
> TaskResource delete_on_background_response_descriptor_projects_release_release_resource(id)

Delete a ReleaseResource by ID

Deletes an existing release, along with all of the deployments, tasks and other associated resources belonging to the release.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ReleaseResource to delete

try:
    # Delete a ReleaseResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_projects_release_release_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->delete_on_background_response_descriptor_projects_release_release_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ReleaseResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_projects_release_release_resource_spaces**
> TaskResource delete_on_background_response_descriptor_projects_release_release_resource_spaces(base_space_id, id)

Delete a ReleaseResource by ID

Deletes an existing release, along with all of the deployments, tasks and other associated resources belonging to the release.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ReleaseResource to delete

try:
    # Delete a ReleaseResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_projects_release_release_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->delete_on_background_response_descriptor_projects_release_release_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ReleaseResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_projects_release_release_resource**
> ResourceCollectionReleaseResource index_response_descriptor_projects_release_release_resource(skip=skip, take=take)

Get a list of ReleaseResources

Lists all of the releases in the supplied Octopus Deploy Space, from all projects. The results will be sorted from most recent to least recent release.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of ReleaseResources
    api_response = api_instance.index_response_descriptor_projects_release_release_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->index_response_descriptor_projects_release_release_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionReleaseResource**](ResourceCollectionReleaseResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_projects_release_release_resource_spaces**
> ResourceCollectionReleaseResource index_response_descriptor_projects_release_release_resource_spaces(base_space_id, skip=skip, take=take)

Get a list of ReleaseResources

Lists all of the releases in the supplied Octopus Deploy Space, from all projects. The results will be sorted from most recent to least recent release.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of ReleaseResources
    api_response = api_instance.index_response_descriptor_projects_release_release_resource_spaces(base_space_id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->index_response_descriptor_projects_release_release_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionReleaseResource**](ResourceCollectionReleaseResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_projects_release_release_resource**
> ReleaseResource load_response_descriptor_projects_release_release_resource(id)

Get a ReleaseResource by ID

Gets a release by ID.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ReleaseResource to load

try:
    # Get a ReleaseResource by ID
    api_response = api_instance.load_response_descriptor_projects_release_release_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->load_response_descriptor_projects_release_release_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ReleaseResource to load | 

### Return type

[**ReleaseResource**](ReleaseResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_projects_release_release_resource_spaces**
> ReleaseResource load_response_descriptor_projects_release_release_resource_spaces(base_space_id, id)

Get a ReleaseResource by ID

Gets a release by ID.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ReleaseResource to load

try:
    # Get a ReleaseResource by ID
    api_response = api_instance.load_response_descriptor_projects_release_release_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->load_response_descriptor_projects_release_release_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ReleaseResource to load | 

### Return type

[**ReleaseResource**](ReleaseResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_projects_release_release_resource**
> ReleaseResource modify_response_descriptor_projects_release_release_resource(id, release_resource=release_resource)

Modify a ReleaseResource by ID

Updates an existing release.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ReleaseResource to modify
release_resource = octopus_deploy_swagger_client.ReleaseResource() # ReleaseResource | The ReleaseResource resource to create (optional)

try:
    # Modify a ReleaseResource by ID
    api_response = api_instance.modify_response_descriptor_projects_release_release_resource(id, release_resource=release_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->modify_response_descriptor_projects_release_release_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ReleaseResource to modify | 
 **release_resource** | [**ReleaseResource**](ReleaseResource.md)| The ReleaseResource resource to create | [optional] 

### Return type

[**ReleaseResource**](ReleaseResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_projects_release_release_resource_spaces**
> ReleaseResource modify_response_descriptor_projects_release_release_resource_spaces(base_space_id, id, release_resource=release_resource)

Modify a ReleaseResource by ID

Updates an existing release.

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
api_instance = octopus_deploy_swagger_client.ReleasesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ReleaseResource to modify
release_resource = octopus_deploy_swagger_client.ReleaseResource() # ReleaseResource | The ReleaseResource resource to create (optional)

try:
    # Modify a ReleaseResource by ID
    api_response = api_instance.modify_response_descriptor_projects_release_release_resource_spaces(base_space_id, id, release_resource=release_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->modify_response_descriptor_projects_release_release_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ReleaseResource to modify | 
 **release_resource** | [**ReleaseResource**](ReleaseResource.md)| The ReleaseResource resource to create | [optional] 

### Return type

[**ReleaseResource**](ReleaseResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

