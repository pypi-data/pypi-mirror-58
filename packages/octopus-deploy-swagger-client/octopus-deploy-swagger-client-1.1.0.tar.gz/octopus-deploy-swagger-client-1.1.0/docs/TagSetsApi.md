# octopus_deploy_swagger_client.TagSetsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_response_descriptor_tag_sets_tag_set_tag_set_resource**](TagSetsApi.md#create_response_descriptor_tag_sets_tag_set_tag_set_resource) | **POST** /api/tagsets | Create a TagSetResource
[**create_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces**](TagSetsApi.md#create_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces) | **POST** /api/{baseSpaceId}/tagsets | Create a TagSetResource
[**custom_action_response_descriptor_octopus_server_web_api_actions_sort_tag_sets_responder**](TagSetsApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_sort_tag_sets_responder) | **PUT** /api/tagsets/sortorder | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_sort_tag_sets_responder_spaces**](TagSetsApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_sort_tag_sets_responder_spaces) | **PUT** /api/{baseSpaceId}/tagsets/sortorder | 
[**delete_on_background_response_descriptor_tag_sets_tag_set_tag_set_resource**](TagSetsApi.md#delete_on_background_response_descriptor_tag_sets_tag_set_tag_set_resource) | **DELETE** /api/tagsets/{id} | Delete a TagSetResource by ID
[**delete_on_background_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces**](TagSetsApi.md#delete_on_background_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces) | **DELETE** /api/{baseSpaceId}/tagsets/{id} | Delete a TagSetResource by ID
[**index_response_descriptor_tag_sets_tag_set_tag_set_resource**](TagSetsApi.md#index_response_descriptor_tag_sets_tag_set_tag_set_resource) | **GET** /api/tagsets | Get a list of TagSetResources
[**index_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces**](TagSetsApi.md#index_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces) | **GET** /api/{baseSpaceId}/tagsets | Get a list of TagSetResources
[**list_all_response_descriptor_tag_sets_tag_set_tag_set_resource**](TagSetsApi.md#list_all_response_descriptor_tag_sets_tag_set_tag_set_resource) | **GET** /api/tagsets/all | Get a list of TagSetResources
[**list_all_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces**](TagSetsApi.md#list_all_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces) | **GET** /api/{baseSpaceId}/tagsets/all | Get a list of TagSetResources
[**load_response_descriptor_tag_sets_tag_set_tag_set_resource**](TagSetsApi.md#load_response_descriptor_tag_sets_tag_set_tag_set_resource) | **GET** /api/tagsets/{id} | Get a TagSetResource by ID
[**load_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces**](TagSetsApi.md#load_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces) | **GET** /api/{baseSpaceId}/tagsets/{id} | Get a TagSetResource by ID
[**modify_response_descriptor_tag_sets_tag_set_tag_set_resource**](TagSetsApi.md#modify_response_descriptor_tag_sets_tag_set_tag_set_resource) | **PUT** /api/tagsets/{id} | Modify a TagSetResource by ID
[**modify_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces**](TagSetsApi.md#modify_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces) | **PUT** /api/{baseSpaceId}/tagsets/{id} | Modify a TagSetResource by ID


# **create_response_descriptor_tag_sets_tag_set_tag_set_resource**
> TagSetResource create_response_descriptor_tag_sets_tag_set_tag_set_resource(tag_set_resource=tag_set_resource)

Create a TagSetResource

Creates a new tag set.

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
api_instance = octopus_deploy_swagger_client.TagSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
tag_set_resource = octopus_deploy_swagger_client.TagSetResource() # TagSetResource | The TagSetResource resource to create (optional)

try:
    # Create a TagSetResource
    api_response = api_instance.create_response_descriptor_tag_sets_tag_set_tag_set_resource(tag_set_resource=tag_set_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagSetsApi->create_response_descriptor_tag_sets_tag_set_tag_set_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_set_resource** | [**TagSetResource**](TagSetResource.md)| The TagSetResource resource to create | [optional] 

### Return type

[**TagSetResource**](TagSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces**
> TagSetResource create_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces(base_space_id, tag_set_resource=tag_set_resource)

Create a TagSetResource

Creates a new tag set.

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
api_instance = octopus_deploy_swagger_client.TagSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
tag_set_resource = octopus_deploy_swagger_client.TagSetResource() # TagSetResource | The TagSetResource resource to create (optional)

try:
    # Create a TagSetResource
    api_response = api_instance.create_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces(base_space_id, tag_set_resource=tag_set_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagSetsApi->create_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **tag_set_resource** | [**TagSetResource**](TagSetResource.md)| The TagSetResource resource to create | [optional] 

### Return type

[**TagSetResource**](TagSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_sort_tag_sets_responder**
> custom_action_response_descriptor_octopus_server_web_api_actions_sort_tag_sets_responder()



Takes an array of tag set IDs as the request body, uses the order of items in the array to sort the tag sets on the server. The ID of every tag set must be specified.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.TagSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_sort_tag_sets_responder()
except ApiException as e:
    print("Exception when calling TagSetsApi->custom_action_response_descriptor_octopus_server_web_api_actions_sort_tag_sets_responder: %s\n" % e)
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

# **custom_action_response_descriptor_octopus_server_web_api_actions_sort_tag_sets_responder_spaces**
> custom_action_response_descriptor_octopus_server_web_api_actions_sort_tag_sets_responder_spaces(base_space_id)



Takes an array of tag set IDs as the request body, uses the order of items in the array to sort the tag sets on the server. The ID of every tag set must be specified.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.TagSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_sort_tag_sets_responder_spaces(base_space_id)
except ApiException as e:
    print("Exception when calling TagSetsApi->custom_action_response_descriptor_octopus_server_web_api_actions_sort_tag_sets_responder_spaces: %s\n" % e)
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

# **delete_on_background_response_descriptor_tag_sets_tag_set_tag_set_resource**
> TaskResource delete_on_background_response_descriptor_tag_sets_tag_set_tag_set_resource(id)

Delete a TagSetResource by ID

Deletes an existing tag set.

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
api_instance = octopus_deploy_swagger_client.TagSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the TagSetResource to delete

try:
    # Delete a TagSetResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_tag_sets_tag_set_tag_set_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagSetsApi->delete_on_background_response_descriptor_tag_sets_tag_set_tag_set_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the TagSetResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces**
> TaskResource delete_on_background_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces(base_space_id, id)

Delete a TagSetResource by ID

Deletes an existing tag set.

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
api_instance = octopus_deploy_swagger_client.TagSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the TagSetResource to delete

try:
    # Delete a TagSetResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagSetsApi->delete_on_background_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the TagSetResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_tag_sets_tag_set_tag_set_resource**
> ResourceCollectionTagSetResource index_response_descriptor_tag_sets_tag_set_tag_set_resource(skip=skip, take=take)

Get a list of TagSetResources

Lists all of the tag sets in the supplied Octopus Deploy Space. The results will be sorted alphabetically by the `SortOrder` field on each tag set.

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
api_instance = octopus_deploy_swagger_client.TagSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of TagSetResources
    api_response = api_instance.index_response_descriptor_tag_sets_tag_set_tag_set_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagSetsApi->index_response_descriptor_tag_sets_tag_set_tag_set_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionTagSetResource**](ResourceCollectionTagSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces**
> ResourceCollectionTagSetResource index_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces(base_space_id, skip=skip, take=take)

Get a list of TagSetResources

Lists all of the tag sets in the supplied Octopus Deploy Space. The results will be sorted alphabetically by the `SortOrder` field on each tag set.

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
api_instance = octopus_deploy_swagger_client.TagSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of TagSetResources
    api_response = api_instance.index_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces(base_space_id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagSetsApi->index_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionTagSetResource**](ResourceCollectionTagSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_tag_sets_tag_set_tag_set_resource**
> list[TagSetResource] list_all_response_descriptor_tag_sets_tag_set_tag_set_resource()

Get a list of TagSetResources

Lists the details of all of the tag sets in the supplied Octopus Deploy Space. The results will be sorted by the `SortOrder` field on each tag set.

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
api_instance = octopus_deploy_swagger_client.TagSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    # Get a list of TagSetResources
    api_response = api_instance.list_all_response_descriptor_tag_sets_tag_set_tag_set_resource()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagSetsApi->list_all_response_descriptor_tag_sets_tag_set_tag_set_resource: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TagSetResource]**](TagSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces**
> list[TagSetResource] list_all_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces(base_space_id)

Get a list of TagSetResources

Lists the details of all of the tag sets in the supplied Octopus Deploy Space. The results will be sorted by the `SortOrder` field on each tag set.

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
api_instance = octopus_deploy_swagger_client.TagSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    # Get a list of TagSetResources
    api_response = api_instance.list_all_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagSetsApi->list_all_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**list[TagSetResource]**](TagSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_tag_sets_tag_set_tag_set_resource**
> TagSetResource load_response_descriptor_tag_sets_tag_set_tag_set_resource(id)

Get a TagSetResource by ID

Gets a tag set by ID.

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
api_instance = octopus_deploy_swagger_client.TagSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the TagSetResource to load

try:
    # Get a TagSetResource by ID
    api_response = api_instance.load_response_descriptor_tag_sets_tag_set_tag_set_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagSetsApi->load_response_descriptor_tag_sets_tag_set_tag_set_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the TagSetResource to load | 

### Return type

[**TagSetResource**](TagSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces**
> TagSetResource load_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces(base_space_id, id)

Get a TagSetResource by ID

Gets a tag set by ID.

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
api_instance = octopus_deploy_swagger_client.TagSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the TagSetResource to load

try:
    # Get a TagSetResource by ID
    api_response = api_instance.load_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagSetsApi->load_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the TagSetResource to load | 

### Return type

[**TagSetResource**](TagSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_tag_sets_tag_set_tag_set_resource**
> TagSetResource modify_response_descriptor_tag_sets_tag_set_tag_set_resource(id, tag_set_resource=tag_set_resource)

Modify a TagSetResource by ID

Modifies an existing tag set.

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
api_instance = octopus_deploy_swagger_client.TagSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the TagSetResource to modify
tag_set_resource = octopus_deploy_swagger_client.TagSetResource() # TagSetResource | The TagSetResource resource to create (optional)

try:
    # Modify a TagSetResource by ID
    api_response = api_instance.modify_response_descriptor_tag_sets_tag_set_tag_set_resource(id, tag_set_resource=tag_set_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagSetsApi->modify_response_descriptor_tag_sets_tag_set_tag_set_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the TagSetResource to modify | 
 **tag_set_resource** | [**TagSetResource**](TagSetResource.md)| The TagSetResource resource to create | [optional] 

### Return type

[**TagSetResource**](TagSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces**
> TagSetResource modify_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces(base_space_id, id, tag_set_resource=tag_set_resource)

Modify a TagSetResource by ID

Modifies an existing tag set.

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
api_instance = octopus_deploy_swagger_client.TagSetsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the TagSetResource to modify
tag_set_resource = octopus_deploy_swagger_client.TagSetResource() # TagSetResource | The TagSetResource resource to create (optional)

try:
    # Modify a TagSetResource by ID
    api_response = api_instance.modify_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces(base_space_id, id, tag_set_resource=tag_set_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagSetsApi->modify_response_descriptor_tag_sets_tag_set_tag_set_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the TagSetResource to modify | 
 **tag_set_resource** | [**TagSetResource**](TagSetResource.md)| The TagSetResource resource to create | [optional] 

### Return type

[**TagSetResource**](TagSetResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

