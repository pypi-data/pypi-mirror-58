# octopus_deploy_swagger_client.LifecyclesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_response_descriptor_lifecycles_lifecycle_lifecycle_resource**](LifecyclesApi.md#create_response_descriptor_lifecycles_lifecycle_lifecycle_resource) | **POST** /api/lifecycles | Create a LifecycleResource
[**create_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces**](LifecyclesApi.md#create_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces) | **POST** /api/{baseSpaceId}/lifecycles | Create a LifecycleResource
[**custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_preview_action**](LifecyclesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_preview_action) | **GET** /api/lifecycles/{id}/preview | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_preview_action_spaces**](LifecyclesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_preview_action_spaces) | **GET** /api/{baseSpaceId}/lifecycles/{id}/preview | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_projects_action**](LifecyclesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_projects_action) | **GET** /api/lifecycles/{id}/projects | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_projects_action_spaces**](LifecyclesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_projects_action_spaces) | **GET** /api/{baseSpaceId}/lifecycles/{id}/projects | 
[**delete_on_background_response_descriptor_lifecycles_lifecycle_lifecycle_resource**](LifecyclesApi.md#delete_on_background_response_descriptor_lifecycles_lifecycle_lifecycle_resource) | **DELETE** /api/lifecycles/{id} | Delete a LifecycleResource by ID
[**delete_on_background_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces**](LifecyclesApi.md#delete_on_background_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces) | **DELETE** /api/{baseSpaceId}/lifecycles/{id} | Delete a LifecycleResource by ID
[**index_response_descriptor_lifecycles_lifecycle_lifecycle_resource**](LifecyclesApi.md#index_response_descriptor_lifecycles_lifecycle_lifecycle_resource) | **GET** /api/lifecycles | Get a list of LifecycleResources
[**index_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces**](LifecyclesApi.md#index_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces) | **GET** /api/{baseSpaceId}/lifecycles | Get a list of LifecycleResources
[**list_all_response_descriptor_lifecycles_lifecycle_lifecycle_resource**](LifecyclesApi.md#list_all_response_descriptor_lifecycles_lifecycle_lifecycle_resource) | **GET** /api/lifecycles/all | Get a list of LifecycleResources
[**list_all_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces**](LifecyclesApi.md#list_all_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces) | **GET** /api/{baseSpaceId}/lifecycles/all | Get a list of LifecycleResources
[**load_response_descriptor_lifecycles_lifecycle_lifecycle_resource**](LifecyclesApi.md#load_response_descriptor_lifecycles_lifecycle_lifecycle_resource) | **GET** /api/lifecycles/{id} | Get a LifecycleResource by ID
[**load_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces**](LifecyclesApi.md#load_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces) | **GET** /api/{baseSpaceId}/lifecycles/{id} | Get a LifecycleResource by ID
[**modify_response_descriptor_lifecycles_lifecycle_lifecycle_resource**](LifecyclesApi.md#modify_response_descriptor_lifecycles_lifecycle_lifecycle_resource) | **PUT** /api/lifecycles/{id} | Modify a LifecycleResource by ID
[**modify_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces**](LifecyclesApi.md#modify_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces) | **PUT** /api/{baseSpaceId}/lifecycles/{id} | Modify a LifecycleResource by ID


# **create_response_descriptor_lifecycles_lifecycle_lifecycle_resource**
> LifecycleResource create_response_descriptor_lifecycles_lifecycle_lifecycle_resource(lifecycle_resource=lifecycle_resource)

Create a LifecycleResource

Creates a new lifecycle.

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
api_instance = octopus_deploy_swagger_client.LifecyclesApi(octopus_deploy_swagger_client.ApiClient(configuration))
lifecycle_resource = octopus_deploy_swagger_client.LifecycleResource() # LifecycleResource | The LifecycleResource resource to create (optional)

try:
    # Create a LifecycleResource
    api_response = api_instance.create_response_descriptor_lifecycles_lifecycle_lifecycle_resource(lifecycle_resource=lifecycle_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->create_response_descriptor_lifecycles_lifecycle_lifecycle_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lifecycle_resource** | [**LifecycleResource**](LifecycleResource.md)| The LifecycleResource resource to create | [optional] 

### Return type

[**LifecycleResource**](LifecycleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces**
> LifecycleResource create_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces(base_space_id, lifecycle_resource=lifecycle_resource)

Create a LifecycleResource

Creates a new lifecycle.

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
api_instance = octopus_deploy_swagger_client.LifecyclesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
lifecycle_resource = octopus_deploy_swagger_client.LifecycleResource() # LifecycleResource | The LifecycleResource resource to create (optional)

try:
    # Create a LifecycleResource
    api_response = api_instance.create_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces(base_space_id, lifecycle_resource=lifecycle_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->create_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **lifecycle_resource** | [**LifecycleResource**](LifecycleResource.md)| The LifecycleResource resource to create | [optional] 

### Return type

[**LifecycleResource**](LifecycleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_preview_action**
> LifecycleResource custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_preview_action(id)



Gets a single lifecycle by ID, as a preview.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.LifecyclesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_preview_action(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_preview_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**LifecycleResource**](LifecycleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_preview_action_spaces**
> LifecycleResource custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_preview_action_spaces(base_space_id, id)



Gets a single lifecycle by ID, as a preview.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.LifecyclesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_preview_action_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_preview_action_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

[**LifecycleResource**](LifecycleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_projects_action**
> list[ProjectResource] custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_projects_action(id)



Gets a all projects that use this lifecycle.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.LifecyclesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_projects_action(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_projects_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**list[ProjectResource]**](ProjectResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_projects_action_spaces**
> list[ProjectResource] custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_projects_action_spaces(base_space_id, id)



Gets a all projects that use this lifecycle.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.LifecyclesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_projects_action_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->custom_action_response_descriptor_octopus_server_web_api_actions_lifecycle_projects_action_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

[**list[ProjectResource]**](ProjectResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_lifecycles_lifecycle_lifecycle_resource**
> TaskResource delete_on_background_response_descriptor_lifecycles_lifecycle_lifecycle_resource(id)

Delete a LifecycleResource by ID

Deletes an existing lifecycle.

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
api_instance = octopus_deploy_swagger_client.LifecyclesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the LifecycleResource to delete

try:
    # Delete a LifecycleResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_lifecycles_lifecycle_lifecycle_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->delete_on_background_response_descriptor_lifecycles_lifecycle_lifecycle_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the LifecycleResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces**
> TaskResource delete_on_background_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces(base_space_id, id)

Delete a LifecycleResource by ID

Deletes an existing lifecycle.

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
api_instance = octopus_deploy_swagger_client.LifecyclesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the LifecycleResource to delete

try:
    # Delete a LifecycleResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->delete_on_background_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the LifecycleResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_lifecycles_lifecycle_lifecycle_resource**
> ResourceCollectionLifecycleResource index_response_descriptor_lifecycles_lifecycle_lifecycle_resource(skip=skip, take=take)

Get a list of LifecycleResources

Lists all of the lifecycles in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.

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
api_instance = octopus_deploy_swagger_client.LifecyclesApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of LifecycleResources
    api_response = api_instance.index_response_descriptor_lifecycles_lifecycle_lifecycle_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->index_response_descriptor_lifecycles_lifecycle_lifecycle_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionLifecycleResource**](ResourceCollectionLifecycleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces**
> ResourceCollectionLifecycleResource index_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces(base_space_id, skip=skip, take=take)

Get a list of LifecycleResources

Lists all of the lifecycles in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.

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
api_instance = octopus_deploy_swagger_client.LifecyclesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of LifecycleResources
    api_response = api_instance.index_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces(base_space_id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->index_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionLifecycleResource**](ResourceCollectionLifecycleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_lifecycles_lifecycle_lifecycle_resource**
> list[LifecycleResource] list_all_response_descriptor_lifecycles_lifecycle_lifecycle_resource()

Get a list of LifecycleResources

Lists all the lifecycles in the supplied Octopus Deploy Space.

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
api_instance = octopus_deploy_swagger_client.LifecyclesApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    # Get a list of LifecycleResources
    api_response = api_instance.list_all_response_descriptor_lifecycles_lifecycle_lifecycle_resource()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->list_all_response_descriptor_lifecycles_lifecycle_lifecycle_resource: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LifecycleResource]**](LifecycleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces**
> list[LifecycleResource] list_all_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces(base_space_id)

Get a list of LifecycleResources

Lists all the lifecycles in the supplied Octopus Deploy Space.

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
api_instance = octopus_deploy_swagger_client.LifecyclesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    # Get a list of LifecycleResources
    api_response = api_instance.list_all_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->list_all_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**list[LifecycleResource]**](LifecycleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_lifecycles_lifecycle_lifecycle_resource**
> LifecycleResource load_response_descriptor_lifecycles_lifecycle_lifecycle_resource(id)

Get a LifecycleResource by ID

Gets a single lifecycle by ID.

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
api_instance = octopus_deploy_swagger_client.LifecyclesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the LifecycleResource to load

try:
    # Get a LifecycleResource by ID
    api_response = api_instance.load_response_descriptor_lifecycles_lifecycle_lifecycle_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->load_response_descriptor_lifecycles_lifecycle_lifecycle_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the LifecycleResource to load | 

### Return type

[**LifecycleResource**](LifecycleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces**
> LifecycleResource load_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces(base_space_id, id)

Get a LifecycleResource by ID

Gets a single lifecycle by ID.

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
api_instance = octopus_deploy_swagger_client.LifecyclesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the LifecycleResource to load

try:
    # Get a LifecycleResource by ID
    api_response = api_instance.load_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->load_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the LifecycleResource to load | 

### Return type

[**LifecycleResource**](LifecycleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_lifecycles_lifecycle_lifecycle_resource**
> LifecycleResource modify_response_descriptor_lifecycles_lifecycle_lifecycle_resource(id, lifecycle_resource=lifecycle_resource)

Modify a LifecycleResource by ID

Modifies an existing lifecycle.

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
api_instance = octopus_deploy_swagger_client.LifecyclesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the LifecycleResource to modify
lifecycle_resource = octopus_deploy_swagger_client.LifecycleResource() # LifecycleResource | The LifecycleResource resource to create (optional)

try:
    # Modify a LifecycleResource by ID
    api_response = api_instance.modify_response_descriptor_lifecycles_lifecycle_lifecycle_resource(id, lifecycle_resource=lifecycle_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->modify_response_descriptor_lifecycles_lifecycle_lifecycle_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the LifecycleResource to modify | 
 **lifecycle_resource** | [**LifecycleResource**](LifecycleResource.md)| The LifecycleResource resource to create | [optional] 

### Return type

[**LifecycleResource**](LifecycleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces**
> LifecycleResource modify_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces(base_space_id, id, lifecycle_resource=lifecycle_resource)

Modify a LifecycleResource by ID

Modifies an existing lifecycle.

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
api_instance = octopus_deploy_swagger_client.LifecyclesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the LifecycleResource to modify
lifecycle_resource = octopus_deploy_swagger_client.LifecycleResource() # LifecycleResource | The LifecycleResource resource to create (optional)

try:
    # Modify a LifecycleResource by ID
    api_response = api_instance.modify_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces(base_space_id, id, lifecycle_resource=lifecycle_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->modify_response_descriptor_lifecycles_lifecycle_lifecycle_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the LifecycleResource to modify | 
 **lifecycle_resource** | [**LifecycleResource**](LifecycleResource.md)| The LifecycleResource resource to create | [optional] 

### Return type

[**LifecycleResource**](LifecycleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

