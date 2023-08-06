# octopus_deploy_swagger_client.ProjectGroupsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**child_index_response_descriptor_projects_project_group_projects_project_project_group_resource_project_resource**](ProjectGroupsApi.md#child_index_response_descriptor_projects_project_group_projects_project_project_group_resource_project_resource) | **GET** /api/projectgroups/{id}/projects | Get a list of ProjectResources
[**child_index_response_descriptor_projects_project_group_projects_project_project_group_resource_project_resource_spaces**](ProjectGroupsApi.md#child_index_response_descriptor_projects_project_group_projects_project_project_group_resource_project_resource_spaces) | **GET** /api/{baseSpaceId}/projectgroups/{id}/projects | Get a list of ProjectResources
[**create_response_descriptor_projects_project_group_project_group_resource**](ProjectGroupsApi.md#create_response_descriptor_projects_project_group_project_group_resource) | **POST** /api/projectgroups | Create a ProjectGroupResource
[**create_response_descriptor_projects_project_group_project_group_resource_spaces**](ProjectGroupsApi.md#create_response_descriptor_projects_project_group_project_group_resource_spaces) | **POST** /api/{baseSpaceId}/projectgroups | Create a ProjectGroupResource
[**delete_on_background_response_descriptor_projects_project_group_project_group_resource**](ProjectGroupsApi.md#delete_on_background_response_descriptor_projects_project_group_project_group_resource) | **DELETE** /api/projectgroups/{id} | Delete a ProjectGroupResource by ID
[**delete_on_background_response_descriptor_projects_project_group_project_group_resource_spaces**](ProjectGroupsApi.md#delete_on_background_response_descriptor_projects_project_group_project_group_resource_spaces) | **DELETE** /api/{baseSpaceId}/projectgroups/{id} | Delete a ProjectGroupResource by ID
[**index_response_descriptor_projects_project_group_project_group_resource**](ProjectGroupsApi.md#index_response_descriptor_projects_project_group_project_group_resource) | **GET** /api/projectgroups | Get a list of ProjectGroupResources
[**index_response_descriptor_projects_project_group_project_group_resource_spaces**](ProjectGroupsApi.md#index_response_descriptor_projects_project_group_project_group_resource_spaces) | **GET** /api/{baseSpaceId}/projectgroups | Get a list of ProjectGroupResources
[**list_all_response_descriptor_projects_project_group_project_group_resource**](ProjectGroupsApi.md#list_all_response_descriptor_projects_project_group_project_group_resource) | **GET** /api/projectgroups/all | Get a list of ProjectGroupResources
[**list_all_response_descriptor_projects_project_group_project_group_resource_spaces**](ProjectGroupsApi.md#list_all_response_descriptor_projects_project_group_project_group_resource_spaces) | **GET** /api/{baseSpaceId}/projectgroups/all | Get a list of ProjectGroupResources
[**load_response_descriptor_projects_project_group_project_group_resource**](ProjectGroupsApi.md#load_response_descriptor_projects_project_group_project_group_resource) | **GET** /api/projectgroups/{id} | Get a ProjectGroupResource by ID
[**load_response_descriptor_projects_project_group_project_group_resource_spaces**](ProjectGroupsApi.md#load_response_descriptor_projects_project_group_project_group_resource_spaces) | **GET** /api/{baseSpaceId}/projectgroups/{id} | Get a ProjectGroupResource by ID
[**modify_response_descriptor_projects_project_group_project_group_resource**](ProjectGroupsApi.md#modify_response_descriptor_projects_project_group_project_group_resource) | **PUT** /api/projectgroups/{id} | Modify a ProjectGroupResource by ID
[**modify_response_descriptor_projects_project_group_project_group_resource_spaces**](ProjectGroupsApi.md#modify_response_descriptor_projects_project_group_project_group_resource_spaces) | **PUT** /api/{baseSpaceId}/projectgroups/{id} | Modify a ProjectGroupResource by ID


# **child_index_response_descriptor_projects_project_group_projects_project_project_group_resource_project_resource**
> ResourceCollectionProjectGroupResource child_index_response_descriptor_projects_project_group_projects_project_project_group_resource_project_resource(skip=skip, take=take)

Get a list of ProjectResources

Lists all of the projects that belong to the given project group.

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
api_instance = octopus_deploy_swagger_client.ProjectGroupsApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of ProjectResources
    api_response = api_instance.child_index_response_descriptor_projects_project_group_projects_project_project_group_resource_project_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectGroupsApi->child_index_response_descriptor_projects_project_group_projects_project_project_group_resource_project_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionProjectGroupResource**](ResourceCollectionProjectGroupResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **child_index_response_descriptor_projects_project_group_projects_project_project_group_resource_project_resource_spaces**
> ResourceCollectionProjectGroupResource child_index_response_descriptor_projects_project_group_projects_project_project_group_resource_project_resource_spaces(base_space_id, skip=skip, take=take)

Get a list of ProjectResources

Lists all of the projects that belong to the given project group.

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
api_instance = octopus_deploy_swagger_client.ProjectGroupsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of ProjectResources
    api_response = api_instance.child_index_response_descriptor_projects_project_group_projects_project_project_group_resource_project_resource_spaces(base_space_id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectGroupsApi->child_index_response_descriptor_projects_project_group_projects_project_project_group_resource_project_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionProjectGroupResource**](ResourceCollectionProjectGroupResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response_descriptor_projects_project_group_project_group_resource**
> ProjectGroupResource create_response_descriptor_projects_project_group_project_group_resource(project_group_resource=project_group_resource)

Create a ProjectGroupResource

Creates a new project group.

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
api_instance = octopus_deploy_swagger_client.ProjectGroupsApi(octopus_deploy_swagger_client.ApiClient(configuration))
project_group_resource = octopus_deploy_swagger_client.ProjectGroupResource() # ProjectGroupResource | The ProjectGroupResource resource to create (optional)

try:
    # Create a ProjectGroupResource
    api_response = api_instance.create_response_descriptor_projects_project_group_project_group_resource(project_group_resource=project_group_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectGroupsApi->create_response_descriptor_projects_project_group_project_group_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_group_resource** | [**ProjectGroupResource**](ProjectGroupResource.md)| The ProjectGroupResource resource to create | [optional] 

### Return type

[**ProjectGroupResource**](ProjectGroupResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response_descriptor_projects_project_group_project_group_resource_spaces**
> ProjectGroupResource create_response_descriptor_projects_project_group_project_group_resource_spaces(base_space_id, project_group_resource=project_group_resource)

Create a ProjectGroupResource

Creates a new project group.

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
api_instance = octopus_deploy_swagger_client.ProjectGroupsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
project_group_resource = octopus_deploy_swagger_client.ProjectGroupResource() # ProjectGroupResource | The ProjectGroupResource resource to create (optional)

try:
    # Create a ProjectGroupResource
    api_response = api_instance.create_response_descriptor_projects_project_group_project_group_resource_spaces(base_space_id, project_group_resource=project_group_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectGroupsApi->create_response_descriptor_projects_project_group_project_group_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **project_group_resource** | [**ProjectGroupResource**](ProjectGroupResource.md)| The ProjectGroupResource resource to create | [optional] 

### Return type

[**ProjectGroupResource**](ProjectGroupResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_projects_project_group_project_group_resource**
> TaskResource delete_on_background_response_descriptor_projects_project_group_project_group_resource(id)

Delete a ProjectGroupResource by ID

Deletes an existing project group.

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
api_instance = octopus_deploy_swagger_client.ProjectGroupsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ProjectGroupResource to delete

try:
    # Delete a ProjectGroupResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_projects_project_group_project_group_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectGroupsApi->delete_on_background_response_descriptor_projects_project_group_project_group_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ProjectGroupResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_projects_project_group_project_group_resource_spaces**
> TaskResource delete_on_background_response_descriptor_projects_project_group_project_group_resource_spaces(base_space_id, id)

Delete a ProjectGroupResource by ID

Deletes an existing project group.

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
api_instance = octopus_deploy_swagger_client.ProjectGroupsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ProjectGroupResource to delete

try:
    # Delete a ProjectGroupResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_projects_project_group_project_group_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectGroupsApi->delete_on_background_response_descriptor_projects_project_group_project_group_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ProjectGroupResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_projects_project_group_project_group_resource**
> ResourceCollectionProjectGroupResource index_response_descriptor_projects_project_group_project_group_resource(skip=skip, take=take)

Get a list of ProjectGroupResources

Lists all of the project groups in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.

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
api_instance = octopus_deploy_swagger_client.ProjectGroupsApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of ProjectGroupResources
    api_response = api_instance.index_response_descriptor_projects_project_group_project_group_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectGroupsApi->index_response_descriptor_projects_project_group_project_group_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionProjectGroupResource**](ResourceCollectionProjectGroupResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_projects_project_group_project_group_resource_spaces**
> ResourceCollectionProjectGroupResource index_response_descriptor_projects_project_group_project_group_resource_spaces(base_space_id, skip=skip, take=take)

Get a list of ProjectGroupResources

Lists all of the project groups in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.

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
api_instance = octopus_deploy_swagger_client.ProjectGroupsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of ProjectGroupResources
    api_response = api_instance.index_response_descriptor_projects_project_group_project_group_resource_spaces(base_space_id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectGroupsApi->index_response_descriptor_projects_project_group_project_group_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionProjectGroupResource**](ResourceCollectionProjectGroupResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_projects_project_group_project_group_resource**
> list[ProjectGroupResource] list_all_response_descriptor_projects_project_group_project_group_resource()

Get a list of ProjectGroupResources

Lists the name and ID of all of the project groups in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.

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
api_instance = octopus_deploy_swagger_client.ProjectGroupsApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    # Get a list of ProjectGroupResources
    api_response = api_instance.list_all_response_descriptor_projects_project_group_project_group_resource()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectGroupsApi->list_all_response_descriptor_projects_project_group_project_group_resource: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ProjectGroupResource]**](ProjectGroupResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_projects_project_group_project_group_resource_spaces**
> list[ProjectGroupResource] list_all_response_descriptor_projects_project_group_project_group_resource_spaces(base_space_id)

Get a list of ProjectGroupResources

Lists the name and ID of all of the project groups in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.

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
api_instance = octopus_deploy_swagger_client.ProjectGroupsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    # Get a list of ProjectGroupResources
    api_response = api_instance.list_all_response_descriptor_projects_project_group_project_group_resource_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectGroupsApi->list_all_response_descriptor_projects_project_group_project_group_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**list[ProjectGroupResource]**](ProjectGroupResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_projects_project_group_project_group_resource**
> ProjectGroupResource load_response_descriptor_projects_project_group_project_group_resource(id)

Get a ProjectGroupResource by ID

Gets a single project group by ID.

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
api_instance = octopus_deploy_swagger_client.ProjectGroupsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ProjectGroupResource to load

try:
    # Get a ProjectGroupResource by ID
    api_response = api_instance.load_response_descriptor_projects_project_group_project_group_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectGroupsApi->load_response_descriptor_projects_project_group_project_group_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ProjectGroupResource to load | 

### Return type

[**ProjectGroupResource**](ProjectGroupResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_projects_project_group_project_group_resource_spaces**
> ProjectGroupResource load_response_descriptor_projects_project_group_project_group_resource_spaces(base_space_id, id)

Get a ProjectGroupResource by ID

Gets a single project group by ID.

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
api_instance = octopus_deploy_swagger_client.ProjectGroupsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ProjectGroupResource to load

try:
    # Get a ProjectGroupResource by ID
    api_response = api_instance.load_response_descriptor_projects_project_group_project_group_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectGroupsApi->load_response_descriptor_projects_project_group_project_group_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ProjectGroupResource to load | 

### Return type

[**ProjectGroupResource**](ProjectGroupResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_projects_project_group_project_group_resource**
> ProjectGroupResource modify_response_descriptor_projects_project_group_project_group_resource(id, project_group_resource=project_group_resource)

Modify a ProjectGroupResource by ID

Modifies an existing project group.

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
api_instance = octopus_deploy_swagger_client.ProjectGroupsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ProjectGroupResource to modify
project_group_resource = octopus_deploy_swagger_client.ProjectGroupResource() # ProjectGroupResource | The ProjectGroupResource resource to create (optional)

try:
    # Modify a ProjectGroupResource by ID
    api_response = api_instance.modify_response_descriptor_projects_project_group_project_group_resource(id, project_group_resource=project_group_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectGroupsApi->modify_response_descriptor_projects_project_group_project_group_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ProjectGroupResource to modify | 
 **project_group_resource** | [**ProjectGroupResource**](ProjectGroupResource.md)| The ProjectGroupResource resource to create | [optional] 

### Return type

[**ProjectGroupResource**](ProjectGroupResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_projects_project_group_project_group_resource_spaces**
> ProjectGroupResource modify_response_descriptor_projects_project_group_project_group_resource_spaces(base_space_id, id, project_group_resource=project_group_resource)

Modify a ProjectGroupResource by ID

Modifies an existing project group.

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
api_instance = octopus_deploy_swagger_client.ProjectGroupsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ProjectGroupResource to modify
project_group_resource = octopus_deploy_swagger_client.ProjectGroupResource() # ProjectGroupResource | The ProjectGroupResource resource to create (optional)

try:
    # Modify a ProjectGroupResource by ID
    api_response = api_instance.modify_response_descriptor_projects_project_group_project_group_resource_spaces(base_space_id, id, project_group_resource=project_group_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectGroupsApi->modify_response_descriptor_projects_project_group_project_group_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ProjectGroupResource to modify | 
 **project_group_resource** | [**ProjectGroupResource**](ProjectGroupResource.md)| The ProjectGroupResource resource to create | [optional] 

### Return type

[**ProjectGroupResource**](ProjectGroupResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

