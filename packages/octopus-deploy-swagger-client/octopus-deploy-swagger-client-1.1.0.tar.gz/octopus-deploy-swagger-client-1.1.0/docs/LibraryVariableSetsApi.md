# octopus_deploy_swagger_client.LibraryVariableSetsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_response_descriptor_variables_library_variable_set_library_variable_set_resource**](LibraryVariableSetsApi.md#create_response_descriptor_variables_library_variable_set_library_variable_set_resource) | **POST** /api/libraryvariablesets | Create a LibraryVariableSetResource
[**create_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces**](LibraryVariableSetsApi.md#create_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces) | **POST** /api/{baseSpaceId}/libraryvariablesets | Create a LibraryVariableSetResource
[**custom_action_response_descriptor_octopus_server_web_api_actions_library_variable_set_usage_list_action**](LibraryVariableSetsApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_library_variable_set_usage_list_action) | **GET** /api/libraryvariablesets/{id}/usages | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_library_variable_set_usage_list_action_spaces**](LibraryVariableSetsApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_library_variable_set_usage_list_action_spaces) | **GET** /api/{baseSpaceId}/libraryvariablesets/{id}/usages | 
[**delete_on_background_response_descriptor_variables_library_variable_set_library_variable_set_resource**](LibraryVariableSetsApi.md#delete_on_background_response_descriptor_variables_library_variable_set_library_variable_set_resource) | **DELETE** /api/libraryvariablesets/{id} | Delete a LibraryVariableSetResource by ID
[**delete_on_background_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces**](LibraryVariableSetsApi.md#delete_on_background_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces) | **DELETE** /api/{baseSpaceId}/libraryvariablesets/{id} | Delete a LibraryVariableSetResource by ID
[**index_response_descriptor_variables_library_variable_set_library_variable_set_resource**](LibraryVariableSetsApi.md#index_response_descriptor_variables_library_variable_set_library_variable_set_resource) | **GET** /api/libraryvariablesets | Get a list of LibraryVariableSetResources
[**index_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces**](LibraryVariableSetsApi.md#index_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces) | **GET** /api/{baseSpaceId}/libraryvariablesets | Get a list of LibraryVariableSetResources
[**list_all_response_descriptor_variables_library_variable_set_library_variable_set_resource**](LibraryVariableSetsApi.md#list_all_response_descriptor_variables_library_variable_set_library_variable_set_resource) | **GET** /api/libraryvariablesets/all | Get a list of LibraryVariableSetResources
[**list_all_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces**](LibraryVariableSetsApi.md#list_all_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces) | **GET** /api/{baseSpaceId}/libraryvariablesets/all | Get a list of LibraryVariableSetResources
[**load_response_descriptor_variables_library_variable_set_library_variable_set_resource**](LibraryVariableSetsApi.md#load_response_descriptor_variables_library_variable_set_library_variable_set_resource) | **GET** /api/libraryvariablesets/{id} | Get a LibraryVariableSetResource by ID
[**load_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces**](LibraryVariableSetsApi.md#load_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces) | **GET** /api/{baseSpaceId}/libraryvariablesets/{id} | Get a LibraryVariableSetResource by ID
[**modify_response_descriptor_variables_library_variable_set_library_variable_set_resource**](LibraryVariableSetsApi.md#modify_response_descriptor_variables_library_variable_set_library_variable_set_resource) | **PUT** /api/libraryvariablesets/{id} | Modify a LibraryVariableSetResource by ID
[**modify_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces**](LibraryVariableSetsApi.md#modify_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces) | **PUT** /api/{baseSpaceId}/libraryvariablesets/{id} | Modify a LibraryVariableSetResource by ID


# **create_response_descriptor_variables_library_variable_set_library_variable_set_resource**
> LibraryVariableSetResource create_response_descriptor_variables_library_variable_set_library_variable_set_resource(library_variable_set_resource=library_variable_set_resource)

Create a LibraryVariableSetResource

Creates a new library variable set.

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
api_instance = octopus_deploy_swagger_client.LibraryVariableSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
library_variable_set_resource = octopus_deploy_swagger_client.LibraryVariableSetResource() # LibraryVariableSetResource | The LibraryVariableSetResource resource to create (optional)

try:
    # Create a LibraryVariableSetResource
    api_response = api_instance.create_response_descriptor_variables_library_variable_set_library_variable_set_resource(library_variable_set_resource=library_variable_set_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryVariableSetsApi->create_response_descriptor_variables_library_variable_set_library_variable_set_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_variable_set_resource** | [**LibraryVariableSetResource**](LibraryVariableSetResource.md)| The LibraryVariableSetResource resource to create | [optional] 

### Return type

[**LibraryVariableSetResource**](LibraryVariableSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces**
> LibraryVariableSetResource create_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces(base_space_id, library_variable_set_resource=library_variable_set_resource)

Create a LibraryVariableSetResource

Creates a new library variable set.

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
api_instance = octopus_deploy_swagger_client.LibraryVariableSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
library_variable_set_resource = octopus_deploy_swagger_client.LibraryVariableSetResource() # LibraryVariableSetResource | The LibraryVariableSetResource resource to create (optional)

try:
    # Create a LibraryVariableSetResource
    api_response = api_instance.create_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces(base_space_id, library_variable_set_resource=library_variable_set_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryVariableSetsApi->create_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **library_variable_set_resource** | [**LibraryVariableSetResource**](LibraryVariableSetResource.md)| The LibraryVariableSetResource resource to create | [optional] 

### Return type

[**LibraryVariableSetResource**](LibraryVariableSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_library_variable_set_usage_list_action**
> LibraryVariableSetUsageResource custom_action_response_descriptor_octopus_server_web_api_actions_library_variable_set_usage_list_action(id)



Lists projects and deployments which are using an library variable set.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.LibraryVariableSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_library_variable_set_usage_list_action(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryVariableSetsApi->custom_action_response_descriptor_octopus_server_web_api_actions_library_variable_set_usage_list_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**LibraryVariableSetUsageResource**](LibraryVariableSetUsageResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_library_variable_set_usage_list_action_spaces**
> LibraryVariableSetUsageResource custom_action_response_descriptor_octopus_server_web_api_actions_library_variable_set_usage_list_action_spaces(base_space_id, id)



Lists projects and deployments which are using an library variable set.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.LibraryVariableSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_library_variable_set_usage_list_action_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryVariableSetsApi->custom_action_response_descriptor_octopus_server_web_api_actions_library_variable_set_usage_list_action_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

[**LibraryVariableSetUsageResource**](LibraryVariableSetUsageResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_variables_library_variable_set_library_variable_set_resource**
> TaskResource delete_on_background_response_descriptor_variables_library_variable_set_library_variable_set_resource(id)

Delete a LibraryVariableSetResource by ID

Deletes an existing library variable set.

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
api_instance = octopus_deploy_swagger_client.LibraryVariableSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the LibraryVariableSetResource to delete

try:
    # Delete a LibraryVariableSetResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_variables_library_variable_set_library_variable_set_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryVariableSetsApi->delete_on_background_response_descriptor_variables_library_variable_set_library_variable_set_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the LibraryVariableSetResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces**
> TaskResource delete_on_background_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces(base_space_id, id)

Delete a LibraryVariableSetResource by ID

Deletes an existing library variable set.

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
api_instance = octopus_deploy_swagger_client.LibraryVariableSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the LibraryVariableSetResource to delete

try:
    # Delete a LibraryVariableSetResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryVariableSetsApi->delete_on_background_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the LibraryVariableSetResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_variables_library_variable_set_library_variable_set_resource**
> ResourceCollectionLibraryVariableSetResource index_response_descriptor_variables_library_variable_set_library_variable_set_resource(skip=skip, take=take)

Get a list of LibraryVariableSetResources

Lists all of the library variable sets in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.

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
api_instance = octopus_deploy_swagger_client.LibraryVariableSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of LibraryVariableSetResources
    api_response = api_instance.index_response_descriptor_variables_library_variable_set_library_variable_set_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryVariableSetsApi->index_response_descriptor_variables_library_variable_set_library_variable_set_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionLibraryVariableSetResource**](ResourceCollectionLibraryVariableSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces**
> ResourceCollectionLibraryVariableSetResource index_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces(base_space_id, skip=skip, take=take)

Get a list of LibraryVariableSetResources

Lists all of the library variable sets in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.

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
api_instance = octopus_deploy_swagger_client.LibraryVariableSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of LibraryVariableSetResources
    api_response = api_instance.index_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces(base_space_id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryVariableSetsApi->index_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionLibraryVariableSetResource**](ResourceCollectionLibraryVariableSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_variables_library_variable_set_library_variable_set_resource**
> list[LibraryVariableSetResource] list_all_response_descriptor_variables_library_variable_set_library_variable_set_resource()

Get a list of LibraryVariableSetResources

Lists all the library variable sets in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.

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
api_instance = octopus_deploy_swagger_client.LibraryVariableSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    # Get a list of LibraryVariableSetResources
    api_response = api_instance.list_all_response_descriptor_variables_library_variable_set_library_variable_set_resource()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryVariableSetsApi->list_all_response_descriptor_variables_library_variable_set_library_variable_set_resource: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LibraryVariableSetResource]**](LibraryVariableSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces**
> list[LibraryVariableSetResource] list_all_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces(base_space_id)

Get a list of LibraryVariableSetResources

Lists all the library variable sets in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.

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
api_instance = octopus_deploy_swagger_client.LibraryVariableSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    # Get a list of LibraryVariableSetResources
    api_response = api_instance.list_all_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryVariableSetsApi->list_all_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**list[LibraryVariableSetResource]**](LibraryVariableSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_variables_library_variable_set_library_variable_set_resource**
> LibraryVariableSetResource load_response_descriptor_variables_library_variable_set_library_variable_set_resource(id)

Get a LibraryVariableSetResource by ID

Gets a single library variable set by ID

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
api_instance = octopus_deploy_swagger_client.LibraryVariableSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the LibraryVariableSetResource to load

try:
    # Get a LibraryVariableSetResource by ID
    api_response = api_instance.load_response_descriptor_variables_library_variable_set_library_variable_set_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryVariableSetsApi->load_response_descriptor_variables_library_variable_set_library_variable_set_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the LibraryVariableSetResource to load | 

### Return type

[**LibraryVariableSetResource**](LibraryVariableSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces**
> LibraryVariableSetResource load_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces(base_space_id, id)

Get a LibraryVariableSetResource by ID

Gets a single library variable set by ID

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
api_instance = octopus_deploy_swagger_client.LibraryVariableSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the LibraryVariableSetResource to load

try:
    # Get a LibraryVariableSetResource by ID
    api_response = api_instance.load_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryVariableSetsApi->load_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the LibraryVariableSetResource to load | 

### Return type

[**LibraryVariableSetResource**](LibraryVariableSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_variables_library_variable_set_library_variable_set_resource**
> LibraryVariableSetResource modify_response_descriptor_variables_library_variable_set_library_variable_set_resource(id, library_variable_set_resource=library_variable_set_resource)

Modify a LibraryVariableSetResource by ID

Modifies an existing library variable set.

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
api_instance = octopus_deploy_swagger_client.LibraryVariableSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the LibraryVariableSetResource to modify
library_variable_set_resource = octopus_deploy_swagger_client.LibraryVariableSetResource() # LibraryVariableSetResource | The LibraryVariableSetResource resource to create (optional)

try:
    # Modify a LibraryVariableSetResource by ID
    api_response = api_instance.modify_response_descriptor_variables_library_variable_set_library_variable_set_resource(id, library_variable_set_resource=library_variable_set_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryVariableSetsApi->modify_response_descriptor_variables_library_variable_set_library_variable_set_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the LibraryVariableSetResource to modify | 
 **library_variable_set_resource** | [**LibraryVariableSetResource**](LibraryVariableSetResource.md)| The LibraryVariableSetResource resource to create | [optional] 

### Return type

[**LibraryVariableSetResource**](LibraryVariableSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces**
> LibraryVariableSetResource modify_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces(base_space_id, id, library_variable_set_resource=library_variable_set_resource)

Modify a LibraryVariableSetResource by ID

Modifies an existing library variable set.

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
api_instance = octopus_deploy_swagger_client.LibraryVariableSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the LibraryVariableSetResource to modify
library_variable_set_resource = octopus_deploy_swagger_client.LibraryVariableSetResource() # LibraryVariableSetResource | The LibraryVariableSetResource resource to create (optional)

try:
    # Modify a LibraryVariableSetResource by ID
    api_response = api_instance.modify_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces(base_space_id, id, library_variable_set_resource=library_variable_set_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryVariableSetsApi->modify_response_descriptor_variables_library_variable_set_library_variable_set_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the LibraryVariableSetResource to modify | 
 **library_variable_set_resource** | [**LibraryVariableSetResource**](LibraryVariableSetResource.md)| The LibraryVariableSetResource resource to create | [optional] 

### Return type

[**LibraryVariableSetResource**](LibraryVariableSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

