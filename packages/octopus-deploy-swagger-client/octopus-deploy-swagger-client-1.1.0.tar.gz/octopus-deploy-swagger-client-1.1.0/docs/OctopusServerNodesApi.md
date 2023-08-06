# octopus_deploy_swagger_client.OctopusServerNodesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_action_response_descriptor_octopus_server_web_api_actions_load_balancer_ping_responder**](OctopusServerNodesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_load_balancer_ping_responder) | **GET** /api/octopusservernodes/ping | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_octopus_server_cluster_summary_responder**](OctopusServerNodesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_octopus_server_cluster_summary_responder) | **GET** /api/octopusservernodes/summary | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_octopus_server_node_details_responder**](OctopusServerNodesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_octopus_server_node_details_responder) | **GET** /api/octopusservernodes/{id}/details | 
[**delete_on_background_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource**](OctopusServerNodesApi.md#delete_on_background_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource) | **DELETE** /api/octopusservernodes/{id} | Delete a OctopusServerNodeResource by ID
[**index_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource**](OctopusServerNodesApi.md#index_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource) | **GET** /api/octopusservernodes | Get a list of OctopusServerNodeResources
[**list_all_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource**](OctopusServerNodesApi.md#list_all_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource) | **GET** /api/octopusservernodes/all | Get a list of OctopusServerNodeResources
[**load_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource**](OctopusServerNodesApi.md#load_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource) | **GET** /api/octopusservernodes/{id} | Get a OctopusServerNodeResource by ID
[**modify_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource**](OctopusServerNodesApi.md#modify_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource) | **PUT** /api/octopusservernodes/{id} | Modify a OctopusServerNodeResource by ID


# **custom_action_response_descriptor_octopus_server_web_api_actions_load_balancer_ping_responder**
> custom_action_response_descriptor_octopus_server_web_api_actions_load_balancer_ping_responder()



Returns HTTP ImATeapot (418) when the Octopus Server node is draining or offline, otherwise HTTP OK (200). Always returns the node information in the body.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.OctopusServerNodesApi()

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_load_balancer_ping_responder()
except ApiException as e:
    print("Exception when calling OctopusServerNodesApi->custom_action_response_descriptor_octopus_server_web_api_actions_load_balancer_ping_responder: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_octopus_server_cluster_summary_responder**
> custom_action_response_descriptor_octopus_server_web_api_actions_octopus_server_cluster_summary_responder()



Returns all nodes, with status information  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.OctopusServerNodesApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_octopus_server_cluster_summary_responder()
except ApiException as e:
    print("Exception when calling OctopusServerNodesApi->custom_action_response_descriptor_octopus_server_web_api_actions_octopus_server_cluster_summary_responder: %s\n" % e)
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

# **custom_action_response_descriptor_octopus_server_web_api_actions_octopus_server_node_details_responder**
> OctopusServerNodeDetailsResource custom_action_response_descriptor_octopus_server_web_api_actions_octopus_server_node_details_responder(id)



A count of the running tasks per node.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.OctopusServerNodesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_octopus_server_node_details_responder(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OctopusServerNodesApi->custom_action_response_descriptor_octopus_server_web_api_actions_octopus_server_node_details_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**OctopusServerNodeDetailsResource**](OctopusServerNodeDetailsResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource**
> TaskResource delete_on_background_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource(id)

Delete a OctopusServerNodeResource by ID

Deletes an Octopus Server node.

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
api_instance = octopus_deploy_swagger_client.OctopusServerNodesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the OctopusServerNodeResource to delete

try:
    # Delete a OctopusServerNodeResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OctopusServerNodesApi->delete_on_background_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the OctopusServerNodeResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource**
> ResourceCollectionOctopusServerNodeResource index_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource(skip=skip, take=take)

Get a list of OctopusServerNodeResources

List all of the Octopus Server nodes participating in the current Octopus Server cluster.

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
api_instance = octopus_deploy_swagger_client.OctopusServerNodesApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of OctopusServerNodeResources
    api_response = api_instance.index_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OctopusServerNodesApi->index_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionOctopusServerNodeResource**](ResourceCollectionOctopusServerNodeResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource**
> list[OctopusServerNodeResource] list_all_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource()

Get a list of OctopusServerNodeResources

Lists the name and ID of all Octopus Server nodes.

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
api_instance = octopus_deploy_swagger_client.OctopusServerNodesApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    # Get a list of OctopusServerNodeResources
    api_response = api_instance.list_all_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OctopusServerNodesApi->list_all_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OctopusServerNodeResource]**](OctopusServerNodeResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource**
> OctopusServerNodeResource load_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource(id)

Get a OctopusServerNodeResource by ID

Gets an Octopus Server node by ID.

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
api_instance = octopus_deploy_swagger_client.OctopusServerNodesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the OctopusServerNodeResource to load

try:
    # Get a OctopusServerNodeResource by ID
    api_response = api_instance.load_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OctopusServerNodesApi->load_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the OctopusServerNodeResource to load | 

### Return type

[**OctopusServerNodeResource**](OctopusServerNodeResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource**
> OctopusServerNodeResource modify_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource(id, octopus_server_node_resource=octopus_server_node_resource)

Modify a OctopusServerNodeResource by ID

Modifies an Octopus Server node.

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
api_instance = octopus_deploy_swagger_client.OctopusServerNodesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the OctopusServerNodeResource to modify
octopus_server_node_resource = octopus_deploy_swagger_client.OctopusServerNodeResource() # OctopusServerNodeResource | The OctopusServerNodeResource resource to create (optional)

try:
    # Modify a OctopusServerNodeResource by ID
    api_response = api_instance.modify_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource(id, octopus_server_node_resource=octopus_server_node_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OctopusServerNodesApi->modify_response_descriptor_clustering_octopus_server_node_octopus_server_node_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the OctopusServerNodeResource to modify | 
 **octopus_server_node_resource** | [**OctopusServerNodeResource**](OctopusServerNodeResource.md)| The OctopusServerNodeResource resource to create | [optional] 

### Return type

[**OctopusServerNodeResource**](OctopusServerNodeResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

