# octopus_deploy_swagger_client.WorkerPoolsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_response_descriptor_worker_pools_worker_pool_worker_pool_resource**](WorkerPoolsApi.md#create_response_descriptor_worker_pools_worker_pool_worker_pool_resource) | **POST** /api/workerpools | Create a WorkerPoolResource
[**create_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces**](WorkerPoolsApi.md#create_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces) | **POST** /api/{baseSpaceId}/workerpools | Create a WorkerPoolResource
[**custom_action_response_descriptor_octopus_server_web_api_actions_sort_worker_pools_responder**](WorkerPoolsApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_sort_worker_pools_responder) | **PUT** /api/workerpools/sortorder | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_sort_worker_pools_responder_spaces**](WorkerPoolsApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_sort_worker_pools_responder_spaces) | **PUT** /api/{baseSpaceId}/workerpools/sortorder | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_worker_pools_summary_responder**](WorkerPoolsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_worker_pools_summary_responder) | **GET** /api/workerpools/summary | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_worker_pools_summary_responder_spaces**](WorkerPoolsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_worker_pools_summary_responder_spaces) | **GET** /api/{baseSpaceId}/workerpools/summary | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_worker_pools_workers_responder**](WorkerPoolsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_worker_pools_workers_responder) | **GET** /api/workerpools/{id}/workers | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_worker_pools_workers_responder_spaces**](WorkerPoolsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_worker_pools_workers_responder_spaces) | **GET** /api/{baseSpaceId}/workerpools/{id}/workers | 
[**delete_on_background_response_descriptor_worker_pools_worker_pool_worker_pool_resource**](WorkerPoolsApi.md#delete_on_background_response_descriptor_worker_pools_worker_pool_worker_pool_resource) | **DELETE** /api/workerpools/{id} | Delete a WorkerPoolResource by ID
[**delete_on_background_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces**](WorkerPoolsApi.md#delete_on_background_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces) | **DELETE** /api/{baseSpaceId}/workerpools/{id} | Delete a WorkerPoolResource by ID
[**index_response_descriptor_worker_pools_worker_pool_worker_pool_resource**](WorkerPoolsApi.md#index_response_descriptor_worker_pools_worker_pool_worker_pool_resource) | **GET** /api/workerpools | Get a list of WorkerPoolResources
[**index_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces**](WorkerPoolsApi.md#index_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces) | **GET** /api/{baseSpaceId}/workerpools | Get a list of WorkerPoolResources
[**list_all_response_descriptor_worker_pools_worker_pool_worker_pool_resource**](WorkerPoolsApi.md#list_all_response_descriptor_worker_pools_worker_pool_worker_pool_resource) | **GET** /api/workerpools/all | Get a list of WorkerPoolResources
[**list_all_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces**](WorkerPoolsApi.md#list_all_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces) | **GET** /api/{baseSpaceId}/workerpools/all | Get a list of WorkerPoolResources
[**load_response_descriptor_worker_pools_worker_pool_worker_pool_resource**](WorkerPoolsApi.md#load_response_descriptor_worker_pools_worker_pool_worker_pool_resource) | **GET** /api/workerpools/{id} | Get a WorkerPoolResource by ID
[**load_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces**](WorkerPoolsApi.md#load_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces) | **GET** /api/{baseSpaceId}/workerpools/{id} | Get a WorkerPoolResource by ID
[**modify_response_descriptor_worker_pools_worker_pool_worker_pool_resource**](WorkerPoolsApi.md#modify_response_descriptor_worker_pools_worker_pool_worker_pool_resource) | **PUT** /api/workerpools/{id} | Modify a WorkerPoolResource by ID
[**modify_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces**](WorkerPoolsApi.md#modify_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces) | **PUT** /api/{baseSpaceId}/workerpools/{id} | Modify a WorkerPoolResource by ID


# **create_response_descriptor_worker_pools_worker_pool_worker_pool_resource**
> WorkerPoolResource create_response_descriptor_worker_pools_worker_pool_worker_pool_resource(worker_pool_resource=worker_pool_resource)

Create a WorkerPoolResource

Creates a new worker pool.

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
api_instance = octopus_deploy_swagger_client.WorkerPoolsApi(octopus_deploy_swagger_client.ApiClient(configuration))
worker_pool_resource = octopus_deploy_swagger_client.WorkerPoolResource() # WorkerPoolResource | The WorkerPoolResource resource to create (optional)

try:
    # Create a WorkerPoolResource
    api_response = api_instance.create_response_descriptor_worker_pools_worker_pool_worker_pool_resource(worker_pool_resource=worker_pool_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkerPoolsApi->create_response_descriptor_worker_pools_worker_pool_worker_pool_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **worker_pool_resource** | [**WorkerPoolResource**](WorkerPoolResource.md)| The WorkerPoolResource resource to create | [optional] 

### Return type

[**WorkerPoolResource**](WorkerPoolResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces**
> WorkerPoolResource create_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces(base_space_id, worker_pool_resource=worker_pool_resource)

Create a WorkerPoolResource

Creates a new worker pool.

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
api_instance = octopus_deploy_swagger_client.WorkerPoolsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
worker_pool_resource = octopus_deploy_swagger_client.WorkerPoolResource() # WorkerPoolResource | The WorkerPoolResource resource to create (optional)

try:
    # Create a WorkerPoolResource
    api_response = api_instance.create_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces(base_space_id, worker_pool_resource=worker_pool_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkerPoolsApi->create_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **worker_pool_resource** | [**WorkerPoolResource**](WorkerPoolResource.md)| The WorkerPoolResource resource to create | [optional] 

### Return type

[**WorkerPoolResource**](WorkerPoolResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_sort_worker_pools_responder**
> custom_action_response_descriptor_octopus_server_web_api_actions_sort_worker_pools_responder()



Takes an array of work pool IDs as the request body, uses the order of items in the array to sort the worker pools on the server. The ID of every worker pool must be specified.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.WorkerPoolsApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_sort_worker_pools_responder()
except ApiException as e:
    print("Exception when calling WorkerPoolsApi->custom_action_response_descriptor_octopus_server_web_api_actions_sort_worker_pools_responder: %s\n" % e)
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

# **custom_action_response_descriptor_octopus_server_web_api_actions_sort_worker_pools_responder_spaces**
> custom_action_response_descriptor_octopus_server_web_api_actions_sort_worker_pools_responder_spaces(base_space_id)



Takes an array of work pool IDs as the request body, uses the order of items in the array to sort the worker pools on the server. The ID of every worker pool must be specified.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.WorkerPoolsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_sort_worker_pools_responder_spaces(base_space_id)
except ApiException as e:
    print("Exception when calling WorkerPoolsApi->custom_action_response_descriptor_octopus_server_web_api_actions_sort_worker_pools_responder_spaces: %s\n" % e)
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

# **custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_worker_pools_summary_responder**
> custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_worker_pools_summary_responder()



Lists all worker pools, including a summary of machine information  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.WorkerPoolsApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_worker_pools_summary_responder()
except ApiException as e:
    print("Exception when calling WorkerPoolsApi->custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_worker_pools_summary_responder: %s\n" % e)
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

# **custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_worker_pools_summary_responder_spaces**
> custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_worker_pools_summary_responder_spaces(base_space_id)



Lists all worker pools, including a summary of machine information  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.WorkerPoolsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_worker_pools_summary_responder_spaces(base_space_id)
except ApiException as e:
    print("Exception when calling WorkerPoolsApi->custom_query_response_descriptor_octopus_server_web_api_actions_infrastructure_summary_worker_pools_summary_responder_spaces: %s\n" % e)
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

# **custom_query_response_descriptor_octopus_server_web_api_actions_worker_pools_workers_responder**
> custom_query_response_descriptor_octopus_server_web_api_actions_worker_pools_workers_responder(id)



Lists all of the machines that belong to the given worker pool.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.WorkerPoolsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the worker pool

try:
    api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_worker_pools_workers_responder(id)
except ApiException as e:
    print("Exception when calling WorkerPoolsApi->custom_query_response_descriptor_octopus_server_web_api_actions_worker_pools_workers_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the worker pool | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_worker_pools_workers_responder_spaces**
> custom_query_response_descriptor_octopus_server_web_api_actions_worker_pools_workers_responder_spaces(base_space_id, id)



Lists all of the machines that belong to the given worker pool.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.WorkerPoolsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the worker pool

try:
    api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_worker_pools_workers_responder_spaces(base_space_id, id)
except ApiException as e:
    print("Exception when calling WorkerPoolsApi->custom_query_response_descriptor_octopus_server_web_api_actions_worker_pools_workers_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the worker pool | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_worker_pools_worker_pool_worker_pool_resource**
> TaskResource delete_on_background_response_descriptor_worker_pools_worker_pool_worker_pool_resource(id)

Delete a WorkerPoolResource by ID

Deletes an existing pool.

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
api_instance = octopus_deploy_swagger_client.WorkerPoolsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the WorkerPoolResource to delete

try:
    # Delete a WorkerPoolResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_worker_pools_worker_pool_worker_pool_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkerPoolsApi->delete_on_background_response_descriptor_worker_pools_worker_pool_worker_pool_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the WorkerPoolResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces**
> TaskResource delete_on_background_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces(base_space_id, id)

Delete a WorkerPoolResource by ID

Deletes an existing pool.

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
api_instance = octopus_deploy_swagger_client.WorkerPoolsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the WorkerPoolResource to delete

try:
    # Delete a WorkerPoolResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkerPoolsApi->delete_on_background_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the WorkerPoolResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_worker_pools_worker_pool_worker_pool_resource**
> ResourceCollectionWorkerPoolResource index_response_descriptor_worker_pools_worker_pool_worker_pool_resource(skip=skip, take=take)

Get a list of WorkerPoolResources

Lists all of the worker pools in the supplied Octopus Deploy Space. The results will be sorted by the `SortOrder` field on each environment.

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
api_instance = octopus_deploy_swagger_client.WorkerPoolsApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of WorkerPoolResources
    api_response = api_instance.index_response_descriptor_worker_pools_worker_pool_worker_pool_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkerPoolsApi->index_response_descriptor_worker_pools_worker_pool_worker_pool_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionWorkerPoolResource**](ResourceCollectionWorkerPoolResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces**
> ResourceCollectionWorkerPoolResource index_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces(base_space_id, skip=skip, take=take)

Get a list of WorkerPoolResources

Lists all of the worker pools in the supplied Octopus Deploy Space. The results will be sorted by the `SortOrder` field on each environment.

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
api_instance = octopus_deploy_swagger_client.WorkerPoolsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of WorkerPoolResources
    api_response = api_instance.index_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces(base_space_id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkerPoolsApi->index_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionWorkerPoolResource**](ResourceCollectionWorkerPoolResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_worker_pools_worker_pool_worker_pool_resource**
> list[WorkerPoolResource] list_all_response_descriptor_worker_pools_worker_pool_worker_pool_resource()

Get a list of WorkerPoolResources

Lists the name and ID of all of the worker pools in the supplied Octopus Deploy Space. The results will be sorted by the `SortOrder` field on each pool.

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
api_instance = octopus_deploy_swagger_client.WorkerPoolsApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    # Get a list of WorkerPoolResources
    api_response = api_instance.list_all_response_descriptor_worker_pools_worker_pool_worker_pool_resource()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkerPoolsApi->list_all_response_descriptor_worker_pools_worker_pool_worker_pool_resource: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[WorkerPoolResource]**](WorkerPoolResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces**
> list[WorkerPoolResource] list_all_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces(base_space_id)

Get a list of WorkerPoolResources

Lists the name and ID of all of the worker pools in the supplied Octopus Deploy Space. The results will be sorted by the `SortOrder` field on each pool.

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
api_instance = octopus_deploy_swagger_client.WorkerPoolsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    # Get a list of WorkerPoolResources
    api_response = api_instance.list_all_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkerPoolsApi->list_all_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**list[WorkerPoolResource]**](WorkerPoolResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_worker_pools_worker_pool_worker_pool_resource**
> WorkerPoolResource load_response_descriptor_worker_pools_worker_pool_worker_pool_resource(id)

Get a WorkerPoolResource by ID

Gets a single worker pool by ID.

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
api_instance = octopus_deploy_swagger_client.WorkerPoolsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the WorkerPoolResource to load

try:
    # Get a WorkerPoolResource by ID
    api_response = api_instance.load_response_descriptor_worker_pools_worker_pool_worker_pool_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkerPoolsApi->load_response_descriptor_worker_pools_worker_pool_worker_pool_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the WorkerPoolResource to load | 

### Return type

[**WorkerPoolResource**](WorkerPoolResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces**
> WorkerPoolResource load_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces(base_space_id, id)

Get a WorkerPoolResource by ID

Gets a single worker pool by ID.

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
api_instance = octopus_deploy_swagger_client.WorkerPoolsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the WorkerPoolResource to load

try:
    # Get a WorkerPoolResource by ID
    api_response = api_instance.load_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkerPoolsApi->load_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the WorkerPoolResource to load | 

### Return type

[**WorkerPoolResource**](WorkerPoolResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_worker_pools_worker_pool_worker_pool_resource**
> WorkerPoolResource modify_response_descriptor_worker_pools_worker_pool_worker_pool_resource(id, worker_pool_resource=worker_pool_resource)

Modify a WorkerPoolResource by ID

Modifies an existing worker pool.

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
api_instance = octopus_deploy_swagger_client.WorkerPoolsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the WorkerPoolResource to modify
worker_pool_resource = octopus_deploy_swagger_client.WorkerPoolResource() # WorkerPoolResource | The WorkerPoolResource resource to create (optional)

try:
    # Modify a WorkerPoolResource by ID
    api_response = api_instance.modify_response_descriptor_worker_pools_worker_pool_worker_pool_resource(id, worker_pool_resource=worker_pool_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkerPoolsApi->modify_response_descriptor_worker_pools_worker_pool_worker_pool_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the WorkerPoolResource to modify | 
 **worker_pool_resource** | [**WorkerPoolResource**](WorkerPoolResource.md)| The WorkerPoolResource resource to create | [optional] 

### Return type

[**WorkerPoolResource**](WorkerPoolResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces**
> WorkerPoolResource modify_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces(base_space_id, id, worker_pool_resource=worker_pool_resource)

Modify a WorkerPoolResource by ID

Modifies an existing worker pool.

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
api_instance = octopus_deploy_swagger_client.WorkerPoolsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the WorkerPoolResource to modify
worker_pool_resource = octopus_deploy_swagger_client.WorkerPoolResource() # WorkerPoolResource | The WorkerPoolResource resource to create (optional)

try:
    # Modify a WorkerPoolResource by ID
    api_response = api_instance.modify_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces(base_space_id, id, worker_pool_resource=worker_pool_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkerPoolsApi->modify_response_descriptor_worker_pools_worker_pool_worker_pool_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the WorkerPoolResource to modify | 
 **worker_pool_resource** | [**WorkerPoolResource**](WorkerPoolResource.md)| The WorkerPoolResource resource to create | [optional] 

### Return type

[**WorkerPoolResource**](WorkerPoolResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

