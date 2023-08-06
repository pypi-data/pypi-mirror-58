# octopus_deploy_swagger_client.UserTeamsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_action_response_descriptor_octopus_server_web_api_actions_users_user_get_teams_action**](UserTeamsApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_users_user_get_teams_action) | **GET** /api/users/{id}/teams | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_users_user_get_teams_action_spaces**](UserTeamsApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_users_user_get_teams_action_spaces) | **GET** /api/{baseSpaceId}/users/{id}/teams | 


# **custom_action_response_descriptor_octopus_server_web_api_actions_users_user_get_teams_action**
> list[TeamNameResource] custom_action_response_descriptor_octopus_server_web_api_actions_users_user_get_teams_action(id)



Gets a list of teams (id and name only) for the specified user, including any from external auth-provider security groups.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.UserTeamsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_users_user_get_teams_action(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTeamsApi->custom_action_response_descriptor_octopus_server_web_api_actions_users_user_get_teams_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**list[TeamNameResource]**](TeamNameResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_users_user_get_teams_action_spaces**
> list[TeamNameResource] custom_action_response_descriptor_octopus_server_web_api_actions_users_user_get_teams_action_spaces(base_space_id, id)



Gets a list of teams (id and name only) for the specified user, including any from external auth-provider security groups.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.UserTeamsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_users_user_get_teams_action_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTeamsApi->custom_action_response_descriptor_octopus_server_web_api_actions_users_user_get_teams_action_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

[**list[TeamNameResource]**](TeamNameResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

