# octopus_deploy_swagger_client.UserRolesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_response_descriptor_users_user_role_user_role_resource**](UserRolesApi.md#create_response_descriptor_users_user_role_user_role_resource) | **POST** /api/userroles | Create a UserRoleResource
[**delete_on_background_response_descriptor_users_user_role_user_role_resource**](UserRolesApi.md#delete_on_background_response_descriptor_users_user_role_user_role_resource) | **DELETE** /api/userroles/{id} | Delete a UserRoleResource by ID
[**index_response_descriptor_users_user_role_user_role_resource**](UserRolesApi.md#index_response_descriptor_users_user_role_user_role_resource) | **GET** /api/userroles | Get a list of UserRoleResources
[**list_all_response_descriptor_users_user_role_user_role_resource**](UserRolesApi.md#list_all_response_descriptor_users_user_role_user_role_resource) | **GET** /api/userroles/all | Get a list of UserRoleResources
[**load_response_descriptor_users_user_role_user_role_resource**](UserRolesApi.md#load_response_descriptor_users_user_role_user_role_resource) | **GET** /api/userroles/{id} | Get a UserRoleResource by ID
[**modify_response_descriptor_users_user_role_user_role_resource**](UserRolesApi.md#modify_response_descriptor_users_user_role_user_role_resource) | **PUT** /api/userroles/{id} | Modify a UserRoleResource by ID


# **create_response_descriptor_users_user_role_user_role_resource**
> UserRoleResource create_response_descriptor_users_user_role_user_role_resource(user_role_resource=user_role_resource)

Create a UserRoleResource

Creates a custom user role definition.

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
api_instance = octopus_deploy_swagger_client.UserRolesApi(octopus_deploy_swagger_client.ApiClient(configuration))
user_role_resource = octopus_deploy_swagger_client.UserRoleResource() # UserRoleResource | The UserRoleResource resource to create (optional)

try:
    # Create a UserRoleResource
    api_response = api_instance.create_response_descriptor_users_user_role_user_role_resource(user_role_resource=user_role_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserRolesApi->create_response_descriptor_users_user_role_user_role_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_role_resource** | [**UserRoleResource**](UserRoleResource.md)| The UserRoleResource resource to create | [optional] 

### Return type

[**UserRoleResource**](UserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_users_user_role_user_role_resource**
> TaskResource delete_on_background_response_descriptor_users_user_role_user_role_resource(id)

Delete a UserRoleResource by ID

Deletes an existing user role.

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
api_instance = octopus_deploy_swagger_client.UserRolesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the UserRoleResource to delete

try:
    # Delete a UserRoleResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_users_user_role_user_role_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserRolesApi->delete_on_background_response_descriptor_users_user_role_user_role_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the UserRoleResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_users_user_role_user_role_resource**
> ResourceCollectionUserRoleResource index_response_descriptor_users_user_role_user_role_resource(skip=skip, take=take)

Get a list of UserRoleResources

Lists all of the user roles in the current Octopus Deploy instance. The results will be sorted alphabetically by name.

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
api_instance = octopus_deploy_swagger_client.UserRolesApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of UserRoleResources
    api_response = api_instance.index_response_descriptor_users_user_role_user_role_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserRolesApi->index_response_descriptor_users_user_role_user_role_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionUserRoleResource**](ResourceCollectionUserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_users_user_role_user_role_resource**
> list[UserRoleResource] list_all_response_descriptor_users_user_role_user_role_resource()

Get a list of UserRoleResources

Lists all of the user roles in the current Octopus Deploy instance. The results will be sorted alphabetically by name.

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
api_instance = octopus_deploy_swagger_client.UserRolesApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    # Get a list of UserRoleResources
    api_response = api_instance.list_all_response_descriptor_users_user_role_user_role_resource()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserRolesApi->list_all_response_descriptor_users_user_role_user_role_resource: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserRoleResource]**](UserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_users_user_role_user_role_resource**
> UserRoleResource load_response_descriptor_users_user_role_user_role_resource(id)

Get a UserRoleResource by ID

Gets a single user role by ID.

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
api_instance = octopus_deploy_swagger_client.UserRolesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the UserRoleResource to load

try:
    # Get a UserRoleResource by ID
    api_response = api_instance.load_response_descriptor_users_user_role_user_role_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserRolesApi->load_response_descriptor_users_user_role_user_role_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the UserRoleResource to load | 

### Return type

[**UserRoleResource**](UserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_users_user_role_user_role_resource**
> UserRoleResource modify_response_descriptor_users_user_role_user_role_resource(id, user_role_resource=user_role_resource)

Modify a UserRoleResource by ID

Modifies an existing user role definition.

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
api_instance = octopus_deploy_swagger_client.UserRolesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the UserRoleResource to modify
user_role_resource = octopus_deploy_swagger_client.UserRoleResource() # UserRoleResource | The UserRoleResource resource to create (optional)

try:
    # Modify a UserRoleResource by ID
    api_response = api_instance.modify_response_descriptor_users_user_role_user_role_resource(id, user_role_resource=user_role_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserRolesApi->modify_response_descriptor_users_user_role_user_role_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the UserRoleResource to modify | 
 **user_role_resource** | [**UserRoleResource**](UserRoleResource.md)| The UserRoleResource resource to create | [optional] 

### Return type

[**UserRoleResource**](UserRoleResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

