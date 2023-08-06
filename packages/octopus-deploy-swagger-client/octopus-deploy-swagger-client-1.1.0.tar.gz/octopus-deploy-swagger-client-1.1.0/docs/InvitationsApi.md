# octopus_deploy_swagger_client.InvitationsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_response_descriptor_users_invitation_invitation_resource**](InvitationsApi.md#create_response_descriptor_users_invitation_invitation_resource) | **POST** /api/users/invitations | Create a InvitationResource
[**create_response_descriptor_users_invitation_invitation_resource_spaces**](InvitationsApi.md#create_response_descriptor_users_invitation_invitation_resource_spaces) | **POST** /api/{baseSpaceId}/users/invitations | Create a InvitationResource
[**load_response_descriptor_users_invitation_invitation_resource**](InvitationsApi.md#load_response_descriptor_users_invitation_invitation_resource) | **GET** /api/users/invitations/{id} | Get a InvitationResource by ID
[**load_response_descriptor_users_invitation_invitation_resource_spaces**](InvitationsApi.md#load_response_descriptor_users_invitation_invitation_resource_spaces) | **GET** /api/{baseSpaceId}/users/invitations/{id} | Get a InvitationResource by ID


# **create_response_descriptor_users_invitation_invitation_resource**
> InvitationResource create_response_descriptor_users_invitation_invitation_resource(invitation_resource=invitation_resource)

Create a InvitationResource

Invite a user to register.

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
api_instance = octopus_deploy_swagger_client.InvitationsApi(octopus_deploy_swagger_client.ApiClient(configuration))
invitation_resource = octopus_deploy_swagger_client.InvitationResource() # InvitationResource | The InvitationResource resource to create (optional)

try:
    # Create a InvitationResource
    api_response = api_instance.create_response_descriptor_users_invitation_invitation_resource(invitation_resource=invitation_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->create_response_descriptor_users_invitation_invitation_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_resource** | [**InvitationResource**](InvitationResource.md)| The InvitationResource resource to create | [optional] 

### Return type

[**InvitationResource**](InvitationResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response_descriptor_users_invitation_invitation_resource_spaces**
> InvitationResource create_response_descriptor_users_invitation_invitation_resource_spaces(base_space_id, invitation_resource=invitation_resource)

Create a InvitationResource

Invite a user to register.

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
api_instance = octopus_deploy_swagger_client.InvitationsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
invitation_resource = octopus_deploy_swagger_client.InvitationResource() # InvitationResource | The InvitationResource resource to create (optional)

try:
    # Create a InvitationResource
    api_response = api_instance.create_response_descriptor_users_invitation_invitation_resource_spaces(base_space_id, invitation_resource=invitation_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->create_response_descriptor_users_invitation_invitation_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **invitation_resource** | [**InvitationResource**](InvitationResource.md)| The InvitationResource resource to create | [optional] 

### Return type

[**InvitationResource**](InvitationResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_users_invitation_invitation_resource**
> InvitationResource load_response_descriptor_users_invitation_invitation_resource(id)

Get a InvitationResource by ID

Gets an existing invitation by ID.

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
api_instance = octopus_deploy_swagger_client.InvitationsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the InvitationResource to load

try:
    # Get a InvitationResource by ID
    api_response = api_instance.load_response_descriptor_users_invitation_invitation_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->load_response_descriptor_users_invitation_invitation_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the InvitationResource to load | 

### Return type

[**InvitationResource**](InvitationResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_users_invitation_invitation_resource_spaces**
> InvitationResource load_response_descriptor_users_invitation_invitation_resource_spaces(base_space_id, id)

Get a InvitationResource by ID

Gets an existing invitation by ID.

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
api_instance = octopus_deploy_swagger_client.InvitationsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the InvitationResource to load

try:
    # Get a InvitationResource by ID
    api_response = api_instance.load_response_descriptor_users_invitation_invitation_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->load_response_descriptor_users_invitation_invitation_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the InvitationResource to load | 

### Return type

[**InvitationResource**](InvitationResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

