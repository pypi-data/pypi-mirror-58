# octopus_deploy_swagger_client.CommunityActionTemplatesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_action_response_descriptor_octopus_server_web_api_actions_action_template_based_on_community_action_template_responder**](CommunityActionTemplatesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_action_template_based_on_community_action_template_responder) | **GET** /api/communityactiontemplates/{id}/actiontemplate/{spaceId?} | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_community_action_template_installation_post_action_responder**](CommunityActionTemplatesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_community_action_template_installation_post_action_responder) | **POST** /api/communityactiontemplates/{id}/installation/{spaceId?} | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_community_action_template_installation_put_action_responder**](CommunityActionTemplatesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_community_action_template_installation_put_action_responder) | **PUT** /api/communityactiontemplates/{id}/installation/{spaceId?} | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_community_action_template_logo_get_responder**](CommunityActionTemplatesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_community_action_template_logo_get_responder) | **GET** /api/communityactiontemplates/{id}/logo | 
[**index_response_descriptor_projects_community_action_template_community_action_template_resource**](CommunityActionTemplatesApi.md#index_response_descriptor_projects_community_action_template_community_action_template_resource) | **GET** /api/communityactiontemplates | Get a list of CommunityActionTemplateResources
[**load_response_descriptor_projects_community_action_template_community_action_template_resource**](CommunityActionTemplatesApi.md#load_response_descriptor_projects_community_action_template_community_action_template_resource) | **GET** /api/communityactiontemplates/{id} | Get a CommunityActionTemplateResource by ID


# **custom_action_response_descriptor_octopus_server_web_api_actions_action_template_based_on_community_action_template_responder**
> ActionTemplateResource custom_action_response_descriptor_octopus_server_web_api_actions_action_template_based_on_community_action_template_responder(space_id, id)



Gets installed version of the template.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.CommunityActionTemplatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
space_id = 'space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_action_template_based_on_community_action_template_responder(space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunityActionTemplatesApi->custom_action_response_descriptor_octopus_server_web_api_actions_action_template_based_on_community_action_template_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

[**ActionTemplateResource**](ActionTemplateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_community_action_template_installation_post_action_responder**
> ActionTemplateResource custom_action_response_descriptor_octopus_server_web_api_actions_community_action_template_installation_post_action_responder(space_id, id)



Installs community step template.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.CommunityActionTemplatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
space_id = 'space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_community_action_template_installation_post_action_responder(space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunityActionTemplatesApi->custom_action_response_descriptor_octopus_server_web_api_actions_community_action_template_installation_post_action_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

[**ActionTemplateResource**](ActionTemplateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_community_action_template_installation_put_action_responder**
> ActionTemplateResource custom_action_response_descriptor_octopus_server_web_api_actions_community_action_template_installation_put_action_responder(space_id, id)



Updates installed community step template to the latest version.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.CommunityActionTemplatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
space_id = 'space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_community_action_template_installation_put_action_responder(space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunityActionTemplatesApi->custom_action_response_descriptor_octopus_server_web_api_actions_community_action_template_installation_put_action_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

[**ActionTemplateResource**](ActionTemplateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_community_action_template_logo_get_responder**
> file custom_action_response_descriptor_octopus_server_web_api_actions_community_action_template_logo_get_responder(id)



Gets the logo associated with the community step template.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.CommunityActionTemplatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_community_action_template_logo_get_responder(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunityActionTemplatesApi->custom_action_response_descriptor_octopus_server_web_api_actions_community_action_template_logo_get_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**file**](file.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_projects_community_action_template_community_action_template_resource**
> ResourceCollectionCommunityActionTemplateResource index_response_descriptor_projects_community_action_template_community_action_template_resource(skip=skip, take=take)

Get a list of CommunityActionTemplateResources



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
api_instance = octopus_deploy_swagger_client.CommunityActionTemplatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of CommunityActionTemplateResources
    api_response = api_instance.index_response_descriptor_projects_community_action_template_community_action_template_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunityActionTemplatesApi->index_response_descriptor_projects_community_action_template_community_action_template_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionCommunityActionTemplateResource**](ResourceCollectionCommunityActionTemplateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_projects_community_action_template_community_action_template_resource**
> CommunityActionTemplateResource load_response_descriptor_projects_community_action_template_community_action_template_resource(id)

Get a CommunityActionTemplateResource by ID

Gets a single community step template.

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
api_instance = octopus_deploy_swagger_client.CommunityActionTemplatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the CommunityActionTemplateResource to load

try:
    # Get a CommunityActionTemplateResource by ID
    api_response = api_instance.load_response_descriptor_projects_community_action_template_community_action_template_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunityActionTemplatesApi->load_response_descriptor_projects_community_action_template_community_action_template_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the CommunityActionTemplateResource to load | 

### Return type

[**CommunityActionTemplateResource**](CommunityActionTemplateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

