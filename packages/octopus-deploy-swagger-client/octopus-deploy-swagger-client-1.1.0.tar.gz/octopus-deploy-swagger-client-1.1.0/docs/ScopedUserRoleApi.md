# octopus_deploy_swagger_client.ScopedUserRoleApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_response_descriptor_users_scoped_user_role_scoped_user_role_resource**](ScopedUserRoleApi.md#create_response_descriptor_users_scoped_user_role_scoped_user_role_resource) | **POST** /api/scopeduserroles | Create a ScopedUserRoleResource
[**create_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces**](ScopedUserRoleApi.md#create_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces) | **POST** /api/{baseSpaceId}/scopeduserroles | Create a ScopedUserRoleResource
[**custom_query_response_descriptor_octopus_server_web_api_actions_list_scoped_user_role_responder**](ScopedUserRoleApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_list_scoped_user_role_responder) | **GET** /api/scopeduserroles | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_list_scoped_user_role_responder_spaces**](ScopedUserRoleApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_list_scoped_user_role_responder_spaces) | **GET** /api/{baseSpaceId}/scopeduserroles | 
[**delete_on_background_response_descriptor_users_scoped_user_role_scoped_user_role_resource**](ScopedUserRoleApi.md#delete_on_background_response_descriptor_users_scoped_user_role_scoped_user_role_resource) | **DELETE** /api/scopeduserroles/{id} | Delete a ScopedUserRoleResource by ID
[**delete_on_background_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces**](ScopedUserRoleApi.md#delete_on_background_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces) | **DELETE** /api/{baseSpaceId}/scopeduserroles/{id} | Delete a ScopedUserRoleResource by ID
[**load_response_descriptor_users_scoped_user_role_scoped_user_role_resource**](ScopedUserRoleApi.md#load_response_descriptor_users_scoped_user_role_scoped_user_role_resource) | **GET** /api/scopeduserroles/{id} | Get a ScopedUserRoleResource by ID
[**load_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces**](ScopedUserRoleApi.md#load_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces) | **GET** /api/{baseSpaceId}/scopeduserroles/{id} | Get a ScopedUserRoleResource by ID
[**modify_response_descriptor_users_scoped_user_role_scoped_user_role_resource**](ScopedUserRoleApi.md#modify_response_descriptor_users_scoped_user_role_scoped_user_role_resource) | **PUT** /api/scopeduserroles/{id} | Modify a ScopedUserRoleResource by ID
[**modify_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces**](ScopedUserRoleApi.md#modify_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces) | **PUT** /api/{baseSpaceId}/scopeduserroles/{id} | Modify a ScopedUserRoleResource by ID


# **create_response_descriptor_users_scoped_user_role_scoped_user_role_resource**
> ScopedUserRoleResource create_response_descriptor_users_scoped_user_role_scoped_user_role_resource(scoped_user_role_resource=scoped_user_role_resource)

Create a ScopedUserRoleResource

Creates a scoped user role.

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
api_instance = octopus_deploy_swagger_client.ScopedUserRoleApi(octopus_deploy_swagger_client.ApiClient(configuration))
scoped_user_role_resource = octopus_deploy_swagger_client.ScopedUserRoleResource() # ScopedUserRoleResource | The ScopedUserRoleResource resource to create (optional)

try:
    # Create a ScopedUserRoleResource
    api_response = api_instance.create_response_descriptor_users_scoped_user_role_scoped_user_role_resource(scoped_user_role_resource=scoped_user_role_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->create_response_descriptor_users_scoped_user_role_scoped_user_role_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scoped_user_role_resource** | [**ScopedUserRoleResource**](ScopedUserRoleResource.md)| The ScopedUserRoleResource resource to create | [optional] 

### Return type

[**ScopedUserRoleResource**](ScopedUserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces**
> ScopedUserRoleResource create_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces(base_space_id, scoped_user_role_resource=scoped_user_role_resource)

Create a ScopedUserRoleResource

Creates a scoped user role.

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
api_instance = octopus_deploy_swagger_client.ScopedUserRoleApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
scoped_user_role_resource = octopus_deploy_swagger_client.ScopedUserRoleResource() # ScopedUserRoleResource | The ScopedUserRoleResource resource to create (optional)

try:
    # Create a ScopedUserRoleResource
    api_response = api_instance.create_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces(base_space_id, scoped_user_role_resource=scoped_user_role_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->create_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **scoped_user_role_resource** | [**ScopedUserRoleResource**](ScopedUserRoleResource.md)| The ScopedUserRoleResource resource to create | [optional] 

### Return type

[**ScopedUserRoleResource**](ScopedUserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_list_scoped_user_role_responder**
> ResourceCollectionScopedUserRoleResource custom_query_response_descriptor_octopus_server_web_api_actions_list_scoped_user_role_responder(id)



Lists the name and ID of all of the scoped user roles in the supplied Octopus Deploy Space. The results will be sorted by name.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ScopedUserRoleApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the team

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_list_scoped_user_role_responder(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->custom_query_response_descriptor_octopus_server_web_api_actions_list_scoped_user_role_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the team | 

### Return type

[**ResourceCollectionScopedUserRoleResource**](ResourceCollectionScopedUserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_list_scoped_user_role_responder_spaces**
> ResourceCollectionScopedUserRoleResource custom_query_response_descriptor_octopus_server_web_api_actions_list_scoped_user_role_responder_spaces(base_space_id, id)



Lists the name and ID of all of the scoped user roles in the supplied Octopus Deploy Space. The results will be sorted by name.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ScopedUserRoleApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the team

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_list_scoped_user_role_responder_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->custom_query_response_descriptor_octopus_server_web_api_actions_list_scoped_user_role_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the team | 

### Return type

[**ResourceCollectionScopedUserRoleResource**](ResourceCollectionScopedUserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_users_scoped_user_role_scoped_user_role_resource**
> TaskResource delete_on_background_response_descriptor_users_scoped_user_role_scoped_user_role_resource(id)

Delete a ScopedUserRoleResource by ID

Deletes an existing scoped user role.

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
api_instance = octopus_deploy_swagger_client.ScopedUserRoleApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ScopedUserRoleResource to delete

try:
    # Delete a ScopedUserRoleResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_users_scoped_user_role_scoped_user_role_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->delete_on_background_response_descriptor_users_scoped_user_role_scoped_user_role_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ScopedUserRoleResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces**
> TaskResource delete_on_background_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces(base_space_id, id)

Delete a ScopedUserRoleResource by ID

Deletes an existing scoped user role.

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
api_instance = octopus_deploy_swagger_client.ScopedUserRoleApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ScopedUserRoleResource to delete

try:
    # Delete a ScopedUserRoleResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->delete_on_background_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ScopedUserRoleResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_users_scoped_user_role_scoped_user_role_resource**
> ScopedUserRoleResource load_response_descriptor_users_scoped_user_role_scoped_user_role_resource(id)

Get a ScopedUserRoleResource by ID

Gets a scoped user role by ID.

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
api_instance = octopus_deploy_swagger_client.ScopedUserRoleApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ScopedUserRoleResource to load

try:
    # Get a ScopedUserRoleResource by ID
    api_response = api_instance.load_response_descriptor_users_scoped_user_role_scoped_user_role_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->load_response_descriptor_users_scoped_user_role_scoped_user_role_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ScopedUserRoleResource to load | 

### Return type

[**ScopedUserRoleResource**](ScopedUserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces**
> ScopedUserRoleResource load_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces(base_space_id, id)

Get a ScopedUserRoleResource by ID

Gets a scoped user role by ID.

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
api_instance = octopus_deploy_swagger_client.ScopedUserRoleApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ScopedUserRoleResource to load

try:
    # Get a ScopedUserRoleResource by ID
    api_response = api_instance.load_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->load_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ScopedUserRoleResource to load | 

### Return type

[**ScopedUserRoleResource**](ScopedUserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_users_scoped_user_role_scoped_user_role_resource**
> ScopedUserRoleResource modify_response_descriptor_users_scoped_user_role_scoped_user_role_resource(id, scoped_user_role_resource=scoped_user_role_resource)

Modify a ScopedUserRoleResource by ID

Modifies an existing scoped user role.

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
api_instance = octopus_deploy_swagger_client.ScopedUserRoleApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ScopedUserRoleResource to modify
scoped_user_role_resource = octopus_deploy_swagger_client.ScopedUserRoleResource() # ScopedUserRoleResource | The ScopedUserRoleResource resource to create (optional)

try:
    # Modify a ScopedUserRoleResource by ID
    api_response = api_instance.modify_response_descriptor_users_scoped_user_role_scoped_user_role_resource(id, scoped_user_role_resource=scoped_user_role_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->modify_response_descriptor_users_scoped_user_role_scoped_user_role_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ScopedUserRoleResource to modify | 
 **scoped_user_role_resource** | [**ScopedUserRoleResource**](ScopedUserRoleResource.md)| The ScopedUserRoleResource resource to create | [optional] 

### Return type

[**ScopedUserRoleResource**](ScopedUserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces**
> ScopedUserRoleResource modify_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces(base_space_id, id, scoped_user_role_resource=scoped_user_role_resource)

Modify a ScopedUserRoleResource by ID

Modifies an existing scoped user role.

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
api_instance = octopus_deploy_swagger_client.ScopedUserRoleApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ScopedUserRoleResource to modify
scoped_user_role_resource = octopus_deploy_swagger_client.ScopedUserRoleResource() # ScopedUserRoleResource | The ScopedUserRoleResource resource to create (optional)

try:
    # Modify a ScopedUserRoleResource by ID
    api_response = api_instance.modify_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces(base_space_id, id, scoped_user_role_resource=scoped_user_role_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopedUserRoleApi->modify_response_descriptor_users_scoped_user_role_scoped_user_role_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ScopedUserRoleResource to modify | 
 **scoped_user_role_resource** | [**ScopedUserRoleResource**](ScopedUserRoleResource.md)| The ScopedUserRoleResource resource to create | [optional] 

### Return type

[**ScopedUserRoleResource**](ScopedUserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

