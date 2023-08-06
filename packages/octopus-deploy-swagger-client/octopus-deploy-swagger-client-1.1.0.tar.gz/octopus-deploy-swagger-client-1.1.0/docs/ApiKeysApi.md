# octopus_deploy_swagger_client.ApiKeysApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_action_response_descriptor_octopus_server_web_api_actions_create_api_key_action**](ApiKeysApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_create_api_key_action) | **POST** /api/users/{userId}/apikeys | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_index_api_keys_responder**](ApiKeysApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_index_api_keys_responder) | **GET** /api/users/{userId}/apikeys | 
[**delete_on_background_response_descriptor_users_api_key_api_key_resource**](ApiKeysApi.md#delete_on_background_response_descriptor_users_api_key_api_key_resource) | **DELETE** /api/users/{userId}/apikeys/{id} | Delete a ApiKeyResource by ID
[**load_response_descriptor_users_api_key_api_key_resource**](ApiKeysApi.md#load_response_descriptor_users_api_key_api_key_resource) | **GET** /api/users/{userId}/apikeys/{id} | Get a ApiKeyResource by ID


# **custom_action_response_descriptor_octopus_server_web_api_actions_create_api_key_action**
> ApiKeyResource custom_action_response_descriptor_octopus_server_web_api_actions_create_api_key_action(user_id)



Generates a new API key for the specified user. The API key returned in the result must be saved by the caller, as it cannot be retrieved subsequently from the Octopus server.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ApiKeysApi(octopus_deploy_swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | ID of the user

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_create_api_key_action(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->custom_action_response_descriptor_octopus_server_web_api_actions_create_api_key_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user | 

### Return type

[**ApiKeyResource**](ApiKeyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_index_api_keys_responder**
> ResourceCollectionApiKeyResource custom_query_response_descriptor_octopus_server_web_api_actions_index_api_keys_responder(user_id)



Lists all API keys for a user, returning the most recent results first.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ApiKeysApi(octopus_deploy_swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | ID of the user

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_index_api_keys_responder(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->custom_query_response_descriptor_octopus_server_web_api_actions_index_api_keys_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user | 

### Return type

[**ResourceCollectionApiKeyResource**](ResourceCollectionApiKeyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_users_api_key_api_key_resource**
> TaskResource delete_on_background_response_descriptor_users_api_key_api_key_resource(id)

Delete a ApiKeyResource by ID

Revokes an existing API key.

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
api_instance = octopus_deploy_swagger_client.ApiKeysApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ApiKeyResource to delete

try:
    # Delete a ApiKeyResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_users_api_key_api_key_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->delete_on_background_response_descriptor_users_api_key_api_key_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ApiKeyResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_users_api_key_api_key_resource**
> ApiKeyResource load_response_descriptor_users_api_key_api_key_resource(id)

Get a ApiKeyResource by ID

Gets a API key by ID.

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
api_instance = octopus_deploy_swagger_client.ApiKeysApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ApiKeyResource to load

try:
    # Get a ApiKeyResource by ID
    api_response = api_instance.load_response_descriptor_users_api_key_api_key_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->load_response_descriptor_users_api_key_api_key_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ApiKeyResource to load | 

### Return type

[**ApiKeyResource**](ApiKeyResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

