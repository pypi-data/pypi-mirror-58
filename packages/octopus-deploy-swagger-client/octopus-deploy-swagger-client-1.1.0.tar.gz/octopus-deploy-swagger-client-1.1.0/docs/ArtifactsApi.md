# octopus_deploy_swagger_client.ArtifactsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_response_descriptor_server_tasks_artifact_artifact_resource**](ArtifactsApi.md#create_response_descriptor_server_tasks_artifact_artifact_resource) | **POST** /api/artifacts | Create a ArtifactResource
[**create_response_descriptor_server_tasks_artifact_artifact_resource_spaces**](ArtifactsApi.md#create_response_descriptor_server_tasks_artifact_artifact_resource_spaces) | **POST** /api/{baseSpaceId}/artifacts | Create a ArtifactResource
[**custom_query_response_descriptor_octopus_server_web_api_actions_list_artifacts_responder**](ArtifactsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_list_artifacts_responder) | **GET** /api/artifacts | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_list_artifacts_responder_spaces**](ArtifactsApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_list_artifacts_responder_spaces) | **GET** /api/{baseSpaceId}/artifacts | 
[**delete_on_background_response_descriptor_server_tasks_artifact_artifact_resource**](ArtifactsApi.md#delete_on_background_response_descriptor_server_tasks_artifact_artifact_resource) | **DELETE** /api/artifacts/{id} | Delete a ArtifactResource by ID
[**delete_on_background_response_descriptor_server_tasks_artifact_artifact_resource_spaces**](ArtifactsApi.md#delete_on_background_response_descriptor_server_tasks_artifact_artifact_resource_spaces) | **DELETE** /api/{baseSpaceId}/artifacts/{id} | Delete a ArtifactResource by ID
[**file_response_descriptor_octopus_server_web_api_actions_artifact_content_action**](ArtifactsApi.md#file_response_descriptor_octopus_server_web_api_actions_artifact_content_action) | **GET** /api/artifacts/{id}/content | 
[**file_response_descriptor_octopus_server_web_api_actions_artifact_content_action_0**](ArtifactsApi.md#file_response_descriptor_octopus_server_web_api_actions_artifact_content_action_0) | **PUT** /api/artifacts/{id}/content | 
[**file_response_descriptor_octopus_server_web_api_actions_artifact_content_action_spaces**](ArtifactsApi.md#file_response_descriptor_octopus_server_web_api_actions_artifact_content_action_spaces) | **GET** /api/{baseSpaceId}/artifacts/{id}/content | 
[**file_response_descriptor_octopus_server_web_api_actions_artifact_content_action_spaces_0**](ArtifactsApi.md#file_response_descriptor_octopus_server_web_api_actions_artifact_content_action_spaces_0) | **PUT** /api/{baseSpaceId}/artifacts/{id}/content | 
[**load_response_descriptor_server_tasks_artifact_artifact_resource**](ArtifactsApi.md#load_response_descriptor_server_tasks_artifact_artifact_resource) | **GET** /api/artifacts/{id} | Get a ArtifactResource by ID
[**load_response_descriptor_server_tasks_artifact_artifact_resource_spaces**](ArtifactsApi.md#load_response_descriptor_server_tasks_artifact_artifact_resource_spaces) | **GET** /api/{baseSpaceId}/artifacts/{id} | Get a ArtifactResource by ID
[**modify_response_descriptor_server_tasks_artifact_artifact_resource**](ArtifactsApi.md#modify_response_descriptor_server_tasks_artifact_artifact_resource) | **PUT** /api/artifacts/{id} | Modify a ArtifactResource by ID
[**modify_response_descriptor_server_tasks_artifact_artifact_resource_spaces**](ArtifactsApi.md#modify_response_descriptor_server_tasks_artifact_artifact_resource_spaces) | **PUT** /api/{baseSpaceId}/artifacts/{id} | Modify a ArtifactResource by ID


# **create_response_descriptor_server_tasks_artifact_artifact_resource**
> ArtifactResource create_response_descriptor_server_tasks_artifact_artifact_resource(artifact_resource=artifact_resource)

Create a ArtifactResource

Creates a new artifact.

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
api_instance = octopus_deploy_swagger_client.ArtifactsApi(octopus_deploy_swagger_client.ApiClient(configuration))
artifact_resource = octopus_deploy_swagger_client.ArtifactResource() # ArtifactResource | The ArtifactResource resource to create (optional)

try:
    # Create a ArtifactResource
    api_response = api_instance.create_response_descriptor_server_tasks_artifact_artifact_resource(artifact_resource=artifact_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->create_response_descriptor_server_tasks_artifact_artifact_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_resource** | [**ArtifactResource**](ArtifactResource.md)| The ArtifactResource resource to create | [optional] 

### Return type

[**ArtifactResource**](ArtifactResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response_descriptor_server_tasks_artifact_artifact_resource_spaces**
> ArtifactResource create_response_descriptor_server_tasks_artifact_artifact_resource_spaces(base_space_id, artifact_resource=artifact_resource)

Create a ArtifactResource

Creates a new artifact.

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
api_instance = octopus_deploy_swagger_client.ArtifactsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
artifact_resource = octopus_deploy_swagger_client.ArtifactResource() # ArtifactResource | The ArtifactResource resource to create (optional)

try:
    # Create a ArtifactResource
    api_response = api_instance.create_response_descriptor_server_tasks_artifact_artifact_resource_spaces(base_space_id, artifact_resource=artifact_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->create_response_descriptor_server_tasks_artifact_artifact_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **artifact_resource** | [**ArtifactResource**](ArtifactResource.md)| The ArtifactResource resource to create | [optional] 

### Return type

[**ArtifactResource**](ArtifactResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_list_artifacts_responder**
> ResourceCollectionArtifactResource custom_query_response_descriptor_octopus_server_web_api_actions_list_artifacts_responder()



Lists all of the artifacts in the supplied Octopus Deploy Space, from all releases. The results will be sorted by date from most recently to least recently created.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ArtifactsApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_list_artifacts_responder()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->custom_query_response_descriptor_octopus_server_web_api_actions_list_artifacts_responder: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceCollectionArtifactResource**](ResourceCollectionArtifactResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_list_artifacts_responder_spaces**
> ResourceCollectionArtifactResource custom_query_response_descriptor_octopus_server_web_api_actions_list_artifacts_responder_spaces(base_space_id)



Lists all of the artifacts in the supplied Octopus Deploy Space, from all releases. The results will be sorted by date from most recently to least recently created.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ArtifactsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_list_artifacts_responder_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->custom_query_response_descriptor_octopus_server_web_api_actions_list_artifacts_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**ResourceCollectionArtifactResource**](ResourceCollectionArtifactResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_server_tasks_artifact_artifact_resource**
> TaskResource delete_on_background_response_descriptor_server_tasks_artifact_artifact_resource(id)

Delete a ArtifactResource by ID

Deletes an existing artifact.

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
api_instance = octopus_deploy_swagger_client.ArtifactsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ArtifactResource to delete

try:
    # Delete a ArtifactResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_server_tasks_artifact_artifact_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->delete_on_background_response_descriptor_server_tasks_artifact_artifact_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ArtifactResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_server_tasks_artifact_artifact_resource_spaces**
> TaskResource delete_on_background_response_descriptor_server_tasks_artifact_artifact_resource_spaces(base_space_id, id)

Delete a ArtifactResource by ID

Deletes an existing artifact.

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
api_instance = octopus_deploy_swagger_client.ArtifactsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ArtifactResource to delete

try:
    # Delete a ArtifactResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_server_tasks_artifact_artifact_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->delete_on_background_response_descriptor_server_tasks_artifact_artifact_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ArtifactResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_response_descriptor_octopus_server_web_api_actions_artifact_content_action**
> file file_response_descriptor_octopus_server_web_api_actions_artifact_content_action(id)



Gets the content associated with an artifact.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ArtifactsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the artifact

try:
    api_response = api_instance.file_response_descriptor_octopus_server_web_api_actions_artifact_content_action(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->file_response_descriptor_octopus_server_web_api_actions_artifact_content_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the artifact | 

### Return type

[**file**](file.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_response_descriptor_octopus_server_web_api_actions_artifact_content_action_0**
> file file_response_descriptor_octopus_server_web_api_actions_artifact_content_action_0(id)



Sets the content associated with an artifact.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ArtifactsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the artifact

try:
    api_response = api_instance.file_response_descriptor_octopus_server_web_api_actions_artifact_content_action_0(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->file_response_descriptor_octopus_server_web_api_actions_artifact_content_action_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the artifact | 

### Return type

[**file**](file.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_response_descriptor_octopus_server_web_api_actions_artifact_content_action_spaces**
> file file_response_descriptor_octopus_server_web_api_actions_artifact_content_action_spaces(base_space_id, id)



Gets the content associated with an artifact.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ArtifactsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the artifact

try:
    api_response = api_instance.file_response_descriptor_octopus_server_web_api_actions_artifact_content_action_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->file_response_descriptor_octopus_server_web_api_actions_artifact_content_action_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the artifact | 

### Return type

[**file**](file.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_response_descriptor_octopus_server_web_api_actions_artifact_content_action_spaces_0**
> file file_response_descriptor_octopus_server_web_api_actions_artifact_content_action_spaces_0(base_space_id, id)



Sets the content associated with an artifact.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ArtifactsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the artifact

try:
    api_response = api_instance.file_response_descriptor_octopus_server_web_api_actions_artifact_content_action_spaces_0(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->file_response_descriptor_octopus_server_web_api_actions_artifact_content_action_spaces_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the artifact | 

### Return type

[**file**](file.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_server_tasks_artifact_artifact_resource**
> ArtifactResource load_response_descriptor_server_tasks_artifact_artifact_resource(id)

Get a ArtifactResource by ID

Gets a single artifact by ID.

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
api_instance = octopus_deploy_swagger_client.ArtifactsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ArtifactResource to load

try:
    # Get a ArtifactResource by ID
    api_response = api_instance.load_response_descriptor_server_tasks_artifact_artifact_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->load_response_descriptor_server_tasks_artifact_artifact_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ArtifactResource to load | 

### Return type

[**ArtifactResource**](ArtifactResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_server_tasks_artifact_artifact_resource_spaces**
> ArtifactResource load_response_descriptor_server_tasks_artifact_artifact_resource_spaces(base_space_id, id)

Get a ArtifactResource by ID

Gets a single artifact by ID.

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
api_instance = octopus_deploy_swagger_client.ArtifactsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ArtifactResource to load

try:
    # Get a ArtifactResource by ID
    api_response = api_instance.load_response_descriptor_server_tasks_artifact_artifact_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->load_response_descriptor_server_tasks_artifact_artifact_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ArtifactResource to load | 

### Return type

[**ArtifactResource**](ArtifactResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_server_tasks_artifact_artifact_resource**
> ArtifactResource modify_response_descriptor_server_tasks_artifact_artifact_resource(id, artifact_resource=artifact_resource)

Modify a ArtifactResource by ID

Modifies an existing artifact.

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
api_instance = octopus_deploy_swagger_client.ArtifactsApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the ArtifactResource to modify
artifact_resource = octopus_deploy_swagger_client.ArtifactResource() # ArtifactResource | The ArtifactResource resource to create (optional)

try:
    # Modify a ArtifactResource by ID
    api_response = api_instance.modify_response_descriptor_server_tasks_artifact_artifact_resource(id, artifact_resource=artifact_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->modify_response_descriptor_server_tasks_artifact_artifact_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ArtifactResource to modify | 
 **artifact_resource** | [**ArtifactResource**](ArtifactResource.md)| The ArtifactResource resource to create | [optional] 

### Return type

[**ArtifactResource**](ArtifactResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_server_tasks_artifact_artifact_resource_spaces**
> ArtifactResource modify_response_descriptor_server_tasks_artifact_artifact_resource_spaces(base_space_id, id, artifact_resource=artifact_resource)

Modify a ArtifactResource by ID

Modifies an existing artifact.

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
api_instance = octopus_deploy_swagger_client.ArtifactsApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the ArtifactResource to modify
artifact_resource = octopus_deploy_swagger_client.ArtifactResource() # ArtifactResource | The ArtifactResource resource to create (optional)

try:
    # Modify a ArtifactResource by ID
    api_response = api_instance.modify_response_descriptor_server_tasks_artifact_artifact_resource_spaces(base_space_id, id, artifact_resource=artifact_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->modify_response_descriptor_server_tasks_artifact_artifact_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the ArtifactResource to modify | 
 **artifact_resource** | [**ArtifactResource**](ArtifactResource.md)| The ArtifactResource resource to create | [optional] 

### Return type

[**ArtifactResource**](ArtifactResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

