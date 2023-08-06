# octopus_deploy_swagger_client.ProxiesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_response_descriptor_machines_proxy_proxy_resource**](ProxiesApi.md#create_response_descriptor_machines_proxy_proxy_resource) | **POST** /api/proxies | Create a ProxyResource
[**create_response_descriptor_machines_proxy_proxy_resource_spaces**](ProxiesApi.md#create_response_descriptor_machines_proxy_proxy_resource_spaces) | **POST** /api/{baseSpaceId}/proxies | Create a ProxyResource
[**delete_on_background_response_descriptor_machines_proxy_proxy_resource**](ProxiesApi.md#delete_on_background_response_descriptor_machines_proxy_proxy_resource) | **DELETE** /api/proxies/{id} | Delete a ProxyResource by ID
[**delete_on_background_response_descriptor_machines_proxy_proxy_resource_spaces**](ProxiesApi.md#delete_on_background_response_descriptor_machines_proxy_proxy_resource_spaces) | **DELETE** /api/{baseSpaceId}/proxies/{id} | Delete a ProxyResource by ID
[**index_response_descriptor_machines_proxy_proxy_resource**](ProxiesApi.md#index_response_descriptor_machines_proxy_proxy_resource) | **GET** /api/proxies | Get a list of ProxyResources
[**index_response_descriptor_machines_proxy_proxy_resource_spaces**](ProxiesApi.md#index_response_descriptor_machines_proxy_proxy_resource_spaces) | **GET** /api/{baseSpaceId}/proxies | Get a list of ProxyResources
[**list_all_response_descriptor_machines_proxy_proxy_resource**](ProxiesApi.md#list_all_response_descriptor_machines_proxy_proxy_resource) | **GET** /api/proxies/all | Get a list of ProxyResources
[**list_all_response_descriptor_machines_proxy_proxy_resource_spaces**](ProxiesApi.md#list_all_response_descriptor_machines_proxy_proxy_resource_spaces) | **GET** /api/{baseSpaceId}/proxies/all | Get a list of ProxyResources
[**load_response_descriptor_machines_proxy_proxy_resource**](ProxiesApi.md#load_response_descriptor_machines_proxy_proxy_resource) | **GET** /api/proxies/{id} | Get a ProxyResource by ID
[**load_response_descriptor_machines_proxy_proxy_resource_spaces**](ProxiesApi.md#load_response_descriptor_machines_proxy_proxy_resource_spaces) | **GET** /api/{baseSpaceId}/proxies/{id} | Get a ProxyResource by ID
[**modify_response_descriptor_machines_proxy_proxy_resource**](ProxiesApi.md#modify_response_descriptor_machines_proxy_proxy_resource) | **PUT** /api/proxies/{id} | Modify a ProxyResource by ID
[**modify_response_descriptor_machines_proxy_proxy_resource_spaces**](ProxiesApi.md#modify_response_descriptor_machines_proxy_proxy_resource_spaces) | **PUT** /api/{baseSpaceId}/proxies/{id} | Modify a ProxyResource by ID


# **create_response_descriptor_machines_proxy_proxy_resource**
> ProxyResource create_response_descriptor_machines_proxy_proxy_resource(proxy_resource=proxy_resource)

Create a ProxyResource

Creates a proxy.

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
api_instance = octopus_deploy_swagger_client.ProxiesApi(octopus_deploy_swagger_client.ApiClient(configuration))
proxy_resource = octopus_deploy_swagger_client.ProxyResource() # ProxyResource | The ProxyResource resource to create (optional)

try:
    # Create a ProxyResource
    api_response = api_instance.create_response_descriptor_machines_proxy_proxy_resource(proxy_resource=proxy_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProxiesApi->create_response_descriptor_machines_proxy_proxy_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proxy_resource** | [**ProxyResource**](ProxyResource.md)| The ProxyResource resource to create | [optional] 

### Return type

[**ProxyResource**](ProxyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response_descriptor_machines_proxy_proxy_resource_spaces**
> ProxyResource create_response_descriptor_machines_proxy_proxy_resource_spaces(base_space_id, proxy_resource=proxy_resource)

Create a ProxyResource

Creates a proxy.

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
api_instance = octopus_deploy_swagger_client.ProxiesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
proxy_resource = octopus_deploy_swagger_client.ProxyResource() # ProxyResource | The ProxyResource resource to create (optional)

try:
    # Create a ProxyResource
    api_response = api_instance.create_response_descriptor_machines_proxy_proxy_resource_spaces(base_space_id, proxy_resource=proxy_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProxiesApi->create_response_descriptor_machines_proxy_proxy_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **proxy_resource** | [**ProxyResource**](ProxyResource.md)| The ProxyResource resource to create | [optional] 

### Return type

[**ProxyResource**](ProxyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_machines_proxy_proxy_resource**
> TaskResource delete_on_background_response_descriptor_machines_proxy_proxy_resource(id)

Delete a ProxyResource by ID

Deletes an existing proxy.

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
api_instance = octopus_deploy_swagger_client.ProxiesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ProxyResource to delete

try:
    # Delete a ProxyResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_machines_proxy_proxy_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProxiesApi->delete_on_background_response_descriptor_machines_proxy_proxy_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ProxyResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_machines_proxy_proxy_resource_spaces**
> TaskResource delete_on_background_response_descriptor_machines_proxy_proxy_resource_spaces(base_space_id, id)

Delete a ProxyResource by ID

Deletes an existing proxy.

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
api_instance = octopus_deploy_swagger_client.ProxiesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ProxyResource to delete

try:
    # Delete a ProxyResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_machines_proxy_proxy_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProxiesApi->delete_on_background_response_descriptor_machines_proxy_proxy_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ProxyResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_machines_proxy_proxy_resource**
> ResourceCollectionProxyResource index_response_descriptor_machines_proxy_proxy_resource(skip=skip, take=take)

Get a list of ProxyResources

Lists all of the proxies in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.

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
api_instance = octopus_deploy_swagger_client.ProxiesApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of ProxyResources
    api_response = api_instance.index_response_descriptor_machines_proxy_proxy_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProxiesApi->index_response_descriptor_machines_proxy_proxy_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionProxyResource**](ResourceCollectionProxyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_machines_proxy_proxy_resource_spaces**
> ResourceCollectionProxyResource index_response_descriptor_machines_proxy_proxy_resource_spaces(base_space_id, skip=skip, take=take)

Get a list of ProxyResources

Lists all of the proxies in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.

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
api_instance = octopus_deploy_swagger_client.ProxiesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of ProxyResources
    api_response = api_instance.index_response_descriptor_machines_proxy_proxy_resource_spaces(base_space_id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProxiesApi->index_response_descriptor_machines_proxy_proxy_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionProxyResource**](ResourceCollectionProxyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_machines_proxy_proxy_resource**
> list[ProxyResource] list_all_response_descriptor_machines_proxy_proxy_resource()

Get a list of ProxyResources

Lists the name and ID of all of the proxies in the supplied Octopus Deploy Space. The results will be sorted by name.

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
api_instance = octopus_deploy_swagger_client.ProxiesApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    # Get a list of ProxyResources
    api_response = api_instance.list_all_response_descriptor_machines_proxy_proxy_resource()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProxiesApi->list_all_response_descriptor_machines_proxy_proxy_resource: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ProxyResource]**](ProxyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_machines_proxy_proxy_resource_spaces**
> list[ProxyResource] list_all_response_descriptor_machines_proxy_proxy_resource_spaces(base_space_id)

Get a list of ProxyResources

Lists the name and ID of all of the proxies in the supplied Octopus Deploy Space. The results will be sorted by name.

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
api_instance = octopus_deploy_swagger_client.ProxiesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    # Get a list of ProxyResources
    api_response = api_instance.list_all_response_descriptor_machines_proxy_proxy_resource_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProxiesApi->list_all_response_descriptor_machines_proxy_proxy_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**list[ProxyResource]**](ProxyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_machines_proxy_proxy_resource**
> ProxyResource load_response_descriptor_machines_proxy_proxy_resource(id)

Get a ProxyResource by ID

Gets a proxy by ID.

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
api_instance = octopus_deploy_swagger_client.ProxiesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ProxyResource to load

try:
    # Get a ProxyResource by ID
    api_response = api_instance.load_response_descriptor_machines_proxy_proxy_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProxiesApi->load_response_descriptor_machines_proxy_proxy_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ProxyResource to load | 

### Return type

[**ProxyResource**](ProxyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_machines_proxy_proxy_resource_spaces**
> ProxyResource load_response_descriptor_machines_proxy_proxy_resource_spaces(base_space_id, id)

Get a ProxyResource by ID

Gets a proxy by ID.

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
api_instance = octopus_deploy_swagger_client.ProxiesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ProxyResource to load

try:
    # Get a ProxyResource by ID
    api_response = api_instance.load_response_descriptor_machines_proxy_proxy_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProxiesApi->load_response_descriptor_machines_proxy_proxy_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ProxyResource to load | 

### Return type

[**ProxyResource**](ProxyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_machines_proxy_proxy_resource**
> ProxyResource modify_response_descriptor_machines_proxy_proxy_resource(id, proxy_resource=proxy_resource)

Modify a ProxyResource by ID

Modifies an existing proxy.

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
api_instance = octopus_deploy_swagger_client.ProxiesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ProxyResource to modify
proxy_resource = octopus_deploy_swagger_client.ProxyResource() # ProxyResource | The ProxyResource resource to create (optional)

try:
    # Modify a ProxyResource by ID
    api_response = api_instance.modify_response_descriptor_machines_proxy_proxy_resource(id, proxy_resource=proxy_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProxiesApi->modify_response_descriptor_machines_proxy_proxy_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ProxyResource to modify | 
 **proxy_resource** | [**ProxyResource**](ProxyResource.md)| The ProxyResource resource to create | [optional] 

### Return type

[**ProxyResource**](ProxyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_machines_proxy_proxy_resource_spaces**
> ProxyResource modify_response_descriptor_machines_proxy_proxy_resource_spaces(base_space_id, id, proxy_resource=proxy_resource)

Modify a ProxyResource by ID

Modifies an existing proxy.

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
api_instance = octopus_deploy_swagger_client.ProxiesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ProxyResource to modify
proxy_resource = octopus_deploy_swagger_client.ProxyResource() # ProxyResource | The ProxyResource resource to create (optional)

try:
    # Modify a ProxyResource by ID
    api_response = api_instance.modify_response_descriptor_machines_proxy_proxy_resource_spaces(base_space_id, id, proxy_resource=proxy_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProxiesApi->modify_response_descriptor_machines_proxy_proxy_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ProxyResource to modify | 
 **proxy_resource** | [**ProxyResource**](ProxyResource.md)| The ProxyResource resource to create | [optional] 

### Return type

[**ProxyResource**](ProxyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

