# octopus_deploy_swagger_client.EventsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_query_response_descriptor_octopus_server_web_api_actions_list_event_agents_responder**](EventsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_list_event_agents_responder) | **GET** /api/events/agents | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_list_event_agents_responder_spaces**](EventsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_list_event_agents_responder_spaces) | **GET** /api/{baseSpaceId}/events/agents | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_list_event_categories_responder**](EventsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_list_event_categories_responder) | **GET** /api/events/categories | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_list_event_categories_responder_spaces**](EventsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_list_event_categories_responder_spaces) | **GET** /api/{baseSpaceId}/events/categories | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_list_event_document_types_responder**](EventsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_list_event_document_types_responder) | **GET** /api/events/documenttypes | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_list_event_document_types_responder_spaces**](EventsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_list_event_document_types_responder_spaces) | **GET** /api/{baseSpaceId}/events/documenttypes | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_list_event_groups_responder**](EventsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_list_event_groups_responder) | **GET** /api/events/groups | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_list_event_groups_responder_spaces**](EventsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_list_event_groups_responder_spaces) | **GET** /api/{baseSpaceId}/events/groups | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_list_events_responder**](EventsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_list_events_responder) | **GET** /api/events | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_list_events_responder_spaces**](EventsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_list_events_responder_spaces) | **GET** /api/{baseSpaceId}/events | 
[**load_response_descriptor_events_event_event_resource**](EventsApi.md#load_response_descriptor_events_event_event_resource) | **GET** /api/events/{id} | Get a EventResource by ID
[**load_response_descriptor_events_event_event_resource_spaces**](EventsApi.md#load_response_descriptor_events_event_event_resource_spaces) | **GET** /api/{baseSpaceId}/events/{id} | Get a EventResource by ID


# **custom_query_response_descriptor_octopus_server_web_api_actions_list_event_agents_responder**
> list[EventAgentResource] custom_query_response_descriptor_octopus_server_web_api_actions_list_event_agents_responder()



Lists event agents.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.EventsApi()

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_list_event_agents_responder()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->custom_query_response_descriptor_octopus_server_web_api_actions_list_event_agents_responder: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EventAgentResource]**](EventAgentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_list_event_agents_responder_spaces**
> list[EventAgentResource] custom_query_response_descriptor_octopus_server_web_api_actions_list_event_agents_responder_spaces(base_space_id)



Lists event agents.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.EventsApi()
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_list_event_agents_responder_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->custom_query_response_descriptor_octopus_server_web_api_actions_list_event_agents_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**list[EventAgentResource]**](EventAgentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_list_event_categories_responder**
> list[EventCategoryResource] custom_query_response_descriptor_octopus_server_web_api_actions_list_event_categories_responder()



Lists event categories.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.EventsApi()

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_list_event_categories_responder()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->custom_query_response_descriptor_octopus_server_web_api_actions_list_event_categories_responder: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EventCategoryResource]**](EventCategoryResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_list_event_categories_responder_spaces**
> list[EventCategoryResource] custom_query_response_descriptor_octopus_server_web_api_actions_list_event_categories_responder_spaces(base_space_id)



Lists event categories.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.EventsApi()
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_list_event_categories_responder_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->custom_query_response_descriptor_octopus_server_web_api_actions_list_event_categories_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**list[EventCategoryResource]**](EventCategoryResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_list_event_document_types_responder**
> list[DocumentTypeDocument] custom_query_response_descriptor_octopus_server_web_api_actions_list_event_document_types_responder()



Lists subscription event document types.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.EventsApi()

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_list_event_document_types_responder()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->custom_query_response_descriptor_octopus_server_web_api_actions_list_event_document_types_responder: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DocumentTypeDocument]**](DocumentTypeDocument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_list_event_document_types_responder_spaces**
> list[DocumentTypeDocument] custom_query_response_descriptor_octopus_server_web_api_actions_list_event_document_types_responder_spaces(base_space_id)



Lists subscription event document types.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.EventsApi()
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_list_event_document_types_responder_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->custom_query_response_descriptor_octopus_server_web_api_actions_list_event_document_types_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**list[DocumentTypeDocument]**](DocumentTypeDocument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_list_event_groups_responder**
> list[EventGroupResource] custom_query_response_descriptor_octopus_server_web_api_actions_list_event_groups_responder()



Lists subscription event groups.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.EventsApi()

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_list_event_groups_responder()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->custom_query_response_descriptor_octopus_server_web_api_actions_list_event_groups_responder: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EventGroupResource]**](EventGroupResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_list_event_groups_responder_spaces**
> list[EventGroupResource] custom_query_response_descriptor_octopus_server_web_api_actions_list_event_groups_responder_spaces(base_space_id)



Lists subscription event groups.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.EventsApi()
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_list_event_groups_responder_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->custom_query_response_descriptor_octopus_server_web_api_actions_list_event_groups_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**list[EventGroupResource]**](EventGroupResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_list_events_responder**
> custom_query_response_descriptor_octopus_server_web_api_actions_list_events_responder()



List all of the the audit events collected to date. Events can be filtered by various criteria. Events will be ordered by the date of the event, descending.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.EventsApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_list_events_responder()
except ApiException as e:
    print("Exception when calling EventsApi->custom_query_response_descriptor_octopus_server_web_api_actions_list_events_responder: %s\n" % e)
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

# **custom_query_response_descriptor_octopus_server_web_api_actions_list_events_responder_spaces**
> custom_query_response_descriptor_octopus_server_web_api_actions_list_events_responder_spaces(base_space_id)



List all of the the audit events collected to date. Events can be filtered by various criteria. Events will be ordered by the date of the event, descending.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.EventsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_list_events_responder_spaces(base_space_id)
except ApiException as e:
    print("Exception when calling EventsApi->custom_query_response_descriptor_octopus_server_web_api_actions_list_events_responder_spaces: %s\n" % e)
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

# **load_response_descriptor_events_event_event_resource**
> EventResource load_response_descriptor_events_event_event_resource(id)

Get a EventResource by ID

Gets a single event by ID.

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
api_instance = octopus_deploy_swagger_client.EventsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the EventResource to load

try:
    # Get a EventResource by ID
    api_response = api_instance.load_response_descriptor_events_event_event_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->load_response_descriptor_events_event_event_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the EventResource to load | 

### Return type

[**EventResource**](EventResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_events_event_event_resource_spaces**
> EventResource load_response_descriptor_events_event_event_resource_spaces(base_space_id, id)

Get a EventResource by ID

Gets a single event by ID.

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
api_instance = octopus_deploy_swagger_client.EventsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the EventResource to load

try:
    # Get a EventResource by ID
    api_response = api_instance.load_response_descriptor_events_event_event_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->load_response_descriptor_events_event_event_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the EventResource to load | 

### Return type

[**EventResource**](EventResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

