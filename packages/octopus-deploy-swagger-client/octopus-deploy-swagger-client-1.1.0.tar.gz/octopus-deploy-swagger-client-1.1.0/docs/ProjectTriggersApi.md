# octopus_deploy_swagger_client.ProjectTriggersApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**child_index_response_descriptor_projects_project_projects_project_trigger_project_trigger_project_resource_project_trigger_resource**](ProjectTriggersApi.md#child_index_response_descriptor_projects_project_projects_project_trigger_project_trigger_project_resource_project_trigger_resource) | **GET** /api/projects/{id}/triggers | Get a list of ProjectTriggerResources
[**child_index_response_descriptor_projects_project_projects_project_trigger_project_trigger_project_resource_project_trigger_resource_spaces**](ProjectTriggersApi.md#child_index_response_descriptor_projects_project_projects_project_trigger_project_trigger_project_resource_project_trigger_resource_spaces) | **GET** /api/{baseSpaceId}/projects/{id}/triggers | Get a list of ProjectTriggerResources
[**create_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource**](ProjectTriggersApi.md#create_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource) | **POST** /api/projecttriggers | Create a ProjectTriggerResource
[**create_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces**](ProjectTriggersApi.md#create_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces) | **POST** /api/{baseSpaceId}/projecttriggers | Create a ProjectTriggerResource
[**delete_on_background_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource**](ProjectTriggersApi.md#delete_on_background_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource) | **DELETE** /api/projecttriggers/{id} | Delete a ProjectTriggerResource by ID
[**delete_on_background_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces**](ProjectTriggersApi.md#delete_on_background_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces) | **DELETE** /api/{baseSpaceId}/projecttriggers/{id} | Delete a ProjectTriggerResource by ID
[**index_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource**](ProjectTriggersApi.md#index_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource) | **GET** /api/projecttriggers | Get a list of ProjectTriggerResources
[**index_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces**](ProjectTriggersApi.md#index_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces) | **GET** /api/{baseSpaceId}/projecttriggers | Get a list of ProjectTriggerResources
[**load_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource**](ProjectTriggersApi.md#load_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource) | **GET** /api/projecttriggers/{id} | Get a ProjectTriggerResource by ID
[**load_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces**](ProjectTriggersApi.md#load_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces) | **GET** /api/{baseSpaceId}/projecttriggers/{id} | Get a ProjectTriggerResource by ID
[**modify_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource**](ProjectTriggersApi.md#modify_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource) | **PUT** /api/projecttriggers/{id} | Modify a ProjectTriggerResource by ID
[**modify_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces**](ProjectTriggersApi.md#modify_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces) | **PUT** /api/{baseSpaceId}/projecttriggers/{id} | Modify a ProjectTriggerResource by ID


# **child_index_response_descriptor_projects_project_projects_project_trigger_project_trigger_project_resource_project_trigger_resource**
> ResourceCollectionProjectResource child_index_response_descriptor_projects_project_projects_project_trigger_project_trigger_project_resource_project_trigger_resource(skip=skip, take=take)

Get a list of ProjectTriggerResources

Lists all the project triggers for the given project

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
api_instance = octopus_deploy_swagger_client.ProjectTriggersApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of ProjectTriggerResources
    api_response = api_instance.child_index_response_descriptor_projects_project_projects_project_trigger_project_trigger_project_resource_project_trigger_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->child_index_response_descriptor_projects_project_projects_project_trigger_project_trigger_project_resource_project_trigger_resource: %s\n" % e)
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

# **child_index_response_descriptor_projects_project_projects_project_trigger_project_trigger_project_resource_project_trigger_resource_spaces**
> ResourceCollectionProjectResource child_index_response_descriptor_projects_project_projects_project_trigger_project_trigger_project_resource_project_trigger_resource_spaces(base_space_id, skip=skip, take=take)

Get a list of ProjectTriggerResources

Lists all the project triggers for the given project

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
api_instance = octopus_deploy_swagger_client.ProjectTriggersApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of ProjectTriggerResources
    api_response = api_instance.child_index_response_descriptor_projects_project_projects_project_trigger_project_trigger_project_resource_project_trigger_resource_spaces(base_space_id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->child_index_response_descriptor_projects_project_projects_project_trigger_project_trigger_project_resource_project_trigger_resource_spaces: %s\n" % e)
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

# **create_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource**
> ProjectTriggerResource create_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource(project_trigger_resource=project_trigger_resource)

Create a ProjectTriggerResource

Creates a new project trigger

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
api_instance = octopus_deploy_swagger_client.ProjectTriggersApi(octopus_deploy_swagger_client.ApiClient(configuration))
project_trigger_resource = octopus_deploy_swagger_client.ProjectTriggerResource() # ProjectTriggerResource | The ProjectTriggerResource resource to create (optional)

try:
    # Create a ProjectTriggerResource
    api_response = api_instance.create_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource(project_trigger_resource=project_trigger_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->create_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_trigger_resource** | [**ProjectTriggerResource**](ProjectTriggerResource.md)| The ProjectTriggerResource resource to create | [optional] 

### Return type

[**ProjectTriggerResource**](ProjectTriggerResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces**
> ProjectTriggerResource create_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces(base_space_id, project_trigger_resource=project_trigger_resource)

Create a ProjectTriggerResource

Creates a new project trigger

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
api_instance = octopus_deploy_swagger_client.ProjectTriggersApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
project_trigger_resource = octopus_deploy_swagger_client.ProjectTriggerResource() # ProjectTriggerResource | The ProjectTriggerResource resource to create (optional)

try:
    # Create a ProjectTriggerResource
    api_response = api_instance.create_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces(base_space_id, project_trigger_resource=project_trigger_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->create_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **project_trigger_resource** | [**ProjectTriggerResource**](ProjectTriggerResource.md)| The ProjectTriggerResource resource to create | [optional] 

### Return type

[**ProjectTriggerResource**](ProjectTriggerResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource**
> TaskResource delete_on_background_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource(id)

Delete a ProjectTriggerResource by ID

Deletes an existing project trigger.

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
api_instance = octopus_deploy_swagger_client.ProjectTriggersApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ProjectTriggerResource to delete

try:
    # Delete a ProjectTriggerResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->delete_on_background_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ProjectTriggerResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces**
> TaskResource delete_on_background_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces(base_space_id, id)

Delete a ProjectTriggerResource by ID

Deletes an existing project trigger.

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
api_instance = octopus_deploy_swagger_client.ProjectTriggersApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ProjectTriggerResource to delete

try:
    # Delete a ProjectTriggerResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->delete_on_background_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ProjectTriggerResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource**
> ResourceCollectionProjectTriggerResource index_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource(skip=skip, take=take)

Get a list of ProjectTriggerResources

Gets all the project triggers in the supplied Octopus Deploy Space, sorted by Id

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
api_instance = octopus_deploy_swagger_client.ProjectTriggersApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of ProjectTriggerResources
    api_response = api_instance.index_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->index_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionProjectTriggerResource**](ResourceCollectionProjectTriggerResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces**
> ResourceCollectionProjectTriggerResource index_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces(base_space_id, skip=skip, take=take)

Get a list of ProjectTriggerResources

Gets all the project triggers in the supplied Octopus Deploy Space, sorted by Id

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
api_instance = octopus_deploy_swagger_client.ProjectTriggersApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of ProjectTriggerResources
    api_response = api_instance.index_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces(base_space_id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->index_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionProjectTriggerResource**](ResourceCollectionProjectTriggerResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource**
> ProjectTriggerResource load_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource(id)

Get a ProjectTriggerResource by ID

Get a project trigger

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
api_instance = octopus_deploy_swagger_client.ProjectTriggersApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ProjectTriggerResource to load

try:
    # Get a ProjectTriggerResource by ID
    api_response = api_instance.load_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->load_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ProjectTriggerResource to load | 

### Return type

[**ProjectTriggerResource**](ProjectTriggerResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces**
> ProjectTriggerResource load_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces(base_space_id, id)

Get a ProjectTriggerResource by ID

Get a project trigger

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
api_instance = octopus_deploy_swagger_client.ProjectTriggersApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ProjectTriggerResource to load

try:
    # Get a ProjectTriggerResource by ID
    api_response = api_instance.load_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->load_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ProjectTriggerResource to load | 

### Return type

[**ProjectTriggerResource**](ProjectTriggerResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource**
> ProjectTriggerResource modify_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource(id, project_trigger_resource=project_trigger_resource)

Modify a ProjectTriggerResource by ID

Updates an existing project trigger

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
api_instance = octopus_deploy_swagger_client.ProjectTriggersApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ProjectTriggerResource to modify
project_trigger_resource = octopus_deploy_swagger_client.ProjectTriggerResource() # ProjectTriggerResource | The ProjectTriggerResource resource to create (optional)

try:
    # Modify a ProjectTriggerResource by ID
    api_response = api_instance.modify_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource(id, project_trigger_resource=project_trigger_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->modify_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ProjectTriggerResource to modify | 
 **project_trigger_resource** | [**ProjectTriggerResource**](ProjectTriggerResource.md)| The ProjectTriggerResource resource to create | [optional] 

### Return type

[**ProjectTriggerResource**](ProjectTriggerResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces**
> ProjectTriggerResource modify_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces(base_space_id, id, project_trigger_resource=project_trigger_resource)

Modify a ProjectTriggerResource by ID

Updates an existing project trigger

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
api_instance = octopus_deploy_swagger_client.ProjectTriggersApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ProjectTriggerResource to modify
project_trigger_resource = octopus_deploy_swagger_client.ProjectTriggerResource() # ProjectTriggerResource | The ProjectTriggerResource resource to create (optional)

try:
    # Modify a ProjectTriggerResource by ID
    api_response = api_instance.modify_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces(base_space_id, id, project_trigger_resource=project_trigger_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTriggersApi->modify_response_descriptor_projects_project_trigger_project_trigger_project_trigger_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ProjectTriggerResource to modify | 
 **project_trigger_resource** | [**ProjectTriggerResource**](ProjectTriggerResource.md)| The ProjectTriggerResource resource to create | [optional] 

### Return type

[**ProjectTriggerResource**](ProjectTriggerResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

