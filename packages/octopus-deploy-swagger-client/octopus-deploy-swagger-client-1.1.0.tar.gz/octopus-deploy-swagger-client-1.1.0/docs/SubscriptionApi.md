# octopus_deploy_swagger_client.SubscriptionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_response_descriptor_subscriptions_subscription_subscription_resource**](SubscriptionApi.md#create_response_descriptor_subscriptions_subscription_subscription_resource) | **POST** /api/subscriptions | Create a SubscriptionResource
[**create_response_descriptor_subscriptions_subscription_subscription_resource_spaces**](SubscriptionApi.md#create_response_descriptor_subscriptions_subscription_subscription_resource_spaces) | **POST** /api/{baseSpaceId}/subscriptions | Create a SubscriptionResource
[**delete_on_background_response_descriptor_subscriptions_subscription_subscription_resource**](SubscriptionApi.md#delete_on_background_response_descriptor_subscriptions_subscription_subscription_resource) | **DELETE** /api/subscriptions/{id} | Delete a SubscriptionResource by ID
[**delete_on_background_response_descriptor_subscriptions_subscription_subscription_resource_spaces**](SubscriptionApi.md#delete_on_background_response_descriptor_subscriptions_subscription_subscription_resource_spaces) | **DELETE** /api/{baseSpaceId}/subscriptions/{id} | Delete a SubscriptionResource by ID
[**index_response_descriptor_subscriptions_subscription_subscription_resource**](SubscriptionApi.md#index_response_descriptor_subscriptions_subscription_subscription_resource) | **GET** /api/subscriptions | Get a list of SubscriptionResources
[**index_response_descriptor_subscriptions_subscription_subscription_resource_spaces**](SubscriptionApi.md#index_response_descriptor_subscriptions_subscription_subscription_resource_spaces) | **GET** /api/{baseSpaceId}/subscriptions | Get a list of SubscriptionResources
[**list_all_response_descriptor_subscriptions_subscription_subscription_resource**](SubscriptionApi.md#list_all_response_descriptor_subscriptions_subscription_subscription_resource) | **GET** /api/subscriptions/all | Get a list of SubscriptionResources
[**list_all_response_descriptor_subscriptions_subscription_subscription_resource_spaces**](SubscriptionApi.md#list_all_response_descriptor_subscriptions_subscription_subscription_resource_spaces) | **GET** /api/{baseSpaceId}/subscriptions/all | Get a list of SubscriptionResources
[**load_response_descriptor_subscriptions_subscription_subscription_resource**](SubscriptionApi.md#load_response_descriptor_subscriptions_subscription_subscription_resource) | **GET** /api/subscriptions/{id} | Get a SubscriptionResource by ID
[**load_response_descriptor_subscriptions_subscription_subscription_resource_spaces**](SubscriptionApi.md#load_response_descriptor_subscriptions_subscription_subscription_resource_spaces) | **GET** /api/{baseSpaceId}/subscriptions/{id} | Get a SubscriptionResource by ID
[**modify_response_descriptor_subscriptions_subscription_subscription_resource**](SubscriptionApi.md#modify_response_descriptor_subscriptions_subscription_subscription_resource) | **PUT** /api/subscriptions/{id} | Modify a SubscriptionResource by ID
[**modify_response_descriptor_subscriptions_subscription_subscription_resource_spaces**](SubscriptionApi.md#modify_response_descriptor_subscriptions_subscription_subscription_resource_spaces) | **PUT** /api/{baseSpaceId}/subscriptions/{id} | Modify a SubscriptionResource by ID


# **create_response_descriptor_subscriptions_subscription_subscription_resource**
> SubscriptionResource create_response_descriptor_subscriptions_subscription_subscription_resource(subscription_resource=subscription_resource)

Create a SubscriptionResource

Creates a new subscription

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
api_instance = octopus_deploy_swagger_client.SubscriptionApi(octopus_deploy_swagger_client.ApiClient(configuration))
subscription_resource = octopus_deploy_swagger_client.SubscriptionResource() # SubscriptionResource | The SubscriptionResource resource to create (optional)

try:
    # Create a SubscriptionResource
    api_response = api_instance.create_response_descriptor_subscriptions_subscription_subscription_resource(subscription_resource=subscription_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->create_response_descriptor_subscriptions_subscription_subscription_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_resource** | [**SubscriptionResource**](SubscriptionResource.md)| The SubscriptionResource resource to create | [optional] 

### Return type

[**SubscriptionResource**](SubscriptionResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response_descriptor_subscriptions_subscription_subscription_resource_spaces**
> SubscriptionResource create_response_descriptor_subscriptions_subscription_subscription_resource_spaces(base_space_id, subscription_resource=subscription_resource)

Create a SubscriptionResource

Creates a new subscription

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
api_instance = octopus_deploy_swagger_client.SubscriptionApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
subscription_resource = octopus_deploy_swagger_client.SubscriptionResource() # SubscriptionResource | The SubscriptionResource resource to create (optional)

try:
    # Create a SubscriptionResource
    api_response = api_instance.create_response_descriptor_subscriptions_subscription_subscription_resource_spaces(base_space_id, subscription_resource=subscription_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->create_response_descriptor_subscriptions_subscription_subscription_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **subscription_resource** | [**SubscriptionResource**](SubscriptionResource.md)| The SubscriptionResource resource to create | [optional] 

### Return type

[**SubscriptionResource**](SubscriptionResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_subscriptions_subscription_subscription_resource**
> TaskResource delete_on_background_response_descriptor_subscriptions_subscription_subscription_resource(id)

Delete a SubscriptionResource by ID

Deletes an existing subscription.

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
api_instance = octopus_deploy_swagger_client.SubscriptionApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the SubscriptionResource to delete

try:
    # Delete a SubscriptionResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_subscriptions_subscription_subscription_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->delete_on_background_response_descriptor_subscriptions_subscription_subscription_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the SubscriptionResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_subscriptions_subscription_subscription_resource_spaces**
> TaskResource delete_on_background_response_descriptor_subscriptions_subscription_subscription_resource_spaces(base_space_id, id)

Delete a SubscriptionResource by ID

Deletes an existing subscription.

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
api_instance = octopus_deploy_swagger_client.SubscriptionApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the SubscriptionResource to delete

try:
    # Delete a SubscriptionResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_subscriptions_subscription_subscription_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->delete_on_background_response_descriptor_subscriptions_subscription_subscription_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the SubscriptionResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_subscriptions_subscription_subscription_resource**
> ResourceCollectionSubscriptionResource index_response_descriptor_subscriptions_subscription_subscription_resource(skip=skip, take=take)

Get a list of SubscriptionResources

Lists all of the subscriptions in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.

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
api_instance = octopus_deploy_swagger_client.SubscriptionApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of SubscriptionResources
    api_response = api_instance.index_response_descriptor_subscriptions_subscription_subscription_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->index_response_descriptor_subscriptions_subscription_subscription_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionSubscriptionResource**](ResourceCollectionSubscriptionResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_subscriptions_subscription_subscription_resource_spaces**
> ResourceCollectionSubscriptionResource index_response_descriptor_subscriptions_subscription_subscription_resource_spaces(base_space_id, skip=skip, take=take)

Get a list of SubscriptionResources

Lists all of the subscriptions in the supplied Octopus Deploy Space. The results will be sorted alphabetically by name.

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
api_instance = octopus_deploy_swagger_client.SubscriptionApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of SubscriptionResources
    api_response = api_instance.index_response_descriptor_subscriptions_subscription_subscription_resource_spaces(base_space_id, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->index_response_descriptor_subscriptions_subscription_subscription_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionSubscriptionResource**](ResourceCollectionSubscriptionResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_subscriptions_subscription_subscription_resource**
> list[SubscriptionResource] list_all_response_descriptor_subscriptions_subscription_subscription_resource()

Get a list of SubscriptionResources

Lists all the subscriptions in the supplied Octopus Deploy Space.

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
api_instance = octopus_deploy_swagger_client.SubscriptionApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    # Get a list of SubscriptionResources
    api_response = api_instance.list_all_response_descriptor_subscriptions_subscription_subscription_resource()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->list_all_response_descriptor_subscriptions_subscription_subscription_resource: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SubscriptionResource]**](SubscriptionResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_subscriptions_subscription_subscription_resource_spaces**
> list[SubscriptionResource] list_all_response_descriptor_subscriptions_subscription_subscription_resource_spaces(base_space_id)

Get a list of SubscriptionResources

Lists all the subscriptions in the supplied Octopus Deploy Space.

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
api_instance = octopus_deploy_swagger_client.SubscriptionApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    # Get a list of SubscriptionResources
    api_response = api_instance.list_all_response_descriptor_subscriptions_subscription_subscription_resource_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->list_all_response_descriptor_subscriptions_subscription_subscription_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**list[SubscriptionResource]**](SubscriptionResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_subscriptions_subscription_subscription_resource**
> SubscriptionResource load_response_descriptor_subscriptions_subscription_subscription_resource(id)

Get a SubscriptionResource by ID

Get a subscription

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
api_instance = octopus_deploy_swagger_client.SubscriptionApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the SubscriptionResource to load

try:
    # Get a SubscriptionResource by ID
    api_response = api_instance.load_response_descriptor_subscriptions_subscription_subscription_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->load_response_descriptor_subscriptions_subscription_subscription_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the SubscriptionResource to load | 

### Return type

[**SubscriptionResource**](SubscriptionResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_subscriptions_subscription_subscription_resource_spaces**
> SubscriptionResource load_response_descriptor_subscriptions_subscription_subscription_resource_spaces(base_space_id, id)

Get a SubscriptionResource by ID

Get a subscription

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
api_instance = octopus_deploy_swagger_client.SubscriptionApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the SubscriptionResource to load

try:
    # Get a SubscriptionResource by ID
    api_response = api_instance.load_response_descriptor_subscriptions_subscription_subscription_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->load_response_descriptor_subscriptions_subscription_subscription_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the SubscriptionResource to load | 

### Return type

[**SubscriptionResource**](SubscriptionResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_subscriptions_subscription_subscription_resource**
> SubscriptionResource modify_response_descriptor_subscriptions_subscription_subscription_resource(id, subscription_resource=subscription_resource)

Modify a SubscriptionResource by ID

Updates an existing subscription

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
api_instance = octopus_deploy_swagger_client.SubscriptionApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the SubscriptionResource to modify
subscription_resource = octopus_deploy_swagger_client.SubscriptionResource() # SubscriptionResource | The SubscriptionResource resource to create (optional)

try:
    # Modify a SubscriptionResource by ID
    api_response = api_instance.modify_response_descriptor_subscriptions_subscription_subscription_resource(id, subscription_resource=subscription_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->modify_response_descriptor_subscriptions_subscription_subscription_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the SubscriptionResource to modify | 
 **subscription_resource** | [**SubscriptionResource**](SubscriptionResource.md)| The SubscriptionResource resource to create | [optional] 

### Return type

[**SubscriptionResource**](SubscriptionResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_subscriptions_subscription_subscription_resource_spaces**
> SubscriptionResource modify_response_descriptor_subscriptions_subscription_subscription_resource_spaces(base_space_id, id, subscription_resource=subscription_resource)

Modify a SubscriptionResource by ID

Updates an existing subscription

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
api_instance = octopus_deploy_swagger_client.SubscriptionApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the SubscriptionResource to modify
subscription_resource = octopus_deploy_swagger_client.SubscriptionResource() # SubscriptionResource | The SubscriptionResource resource to create (optional)

try:
    # Modify a SubscriptionResource by ID
    api_response = api_instance.modify_response_descriptor_subscriptions_subscription_subscription_resource_spaces(base_space_id, id, subscription_resource=subscription_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->modify_response_descriptor_subscriptions_subscription_subscription_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the SubscriptionResource to modify | 
 **subscription_resource** | [**SubscriptionResource**](SubscriptionResource.md)| The SubscriptionResource resource to create | [optional] 

### Return type

[**SubscriptionResource**](SubscriptionResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

