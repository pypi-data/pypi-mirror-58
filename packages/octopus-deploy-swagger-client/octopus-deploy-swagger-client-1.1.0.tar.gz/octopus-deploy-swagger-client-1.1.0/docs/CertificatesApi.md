# octopus_deploy_swagger_client.CertificatesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_response_descriptor_certificate_certificate_resource**](CertificatesApi.md#create_response_descriptor_certificate_certificate_resource) | **POST** /api/certificates | Create a CertificateResource
[**create_response_descriptor_certificate_certificate_resource_spaces**](CertificatesApi.md#create_response_descriptor_certificate_certificate_resource_spaces) | **POST** /api/{baseSpaceId}/certificates | Create a CertificateResource
[**custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_archive_action**](CertificatesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_archive_action) | **POST** /api/certificates/{id}/archive | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_archive_action_spaces**](CertificatesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_archive_action_spaces) | **POST** /api/{baseSpaceId}/certificates/{id}/archive | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_export_action**](CertificatesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_export_action) | **GET** /api/certificates/{id}/export | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_export_action_spaces**](CertificatesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_export_action_spaces) | **GET** /api/{baseSpaceId}/certificates/{id}/export | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_replace_action**](CertificatesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_replace_action) | **POST** /api/certificates/{id}/replace | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_replace_action_spaces**](CertificatesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_replace_action_spaces) | **POST** /api/{baseSpaceId}/certificates/{id}/replace | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_un_archive_action**](CertificatesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_un_archive_action) | **POST** /api/certificates/{id}/unarchive | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_un_archive_action_spaces**](CertificatesApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_un_archive_action_spaces) | **POST** /api/{baseSpaceId}/certificates/{id}/unarchive | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_by_id_or_thumbprint_responder**](CertificatesApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_by_id_or_thumbprint_responder) | **GET** /api/certificates/(?&lt;idOrThumbprint&gt;(?i)^(?!(certificate-global)).*) | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_by_id_or_thumbprint_responder_spaces**](CertificatesApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_by_id_or_thumbprint_responder_spaces) | **GET** /api/{baseSpaceId}/certificates/(?&lt;idOrThumbprint&gt;(?i)^(?!(certificate-global)).*) | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_usage_responder**](CertificatesApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_usage_responder) | **GET** /api/certificates/{id}/usages | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_usage_responder_spaces**](CertificatesApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_usage_responder_spaces) | **GET** /api/{baseSpaceId}/certificates/{id}/usages | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificates_list_responder**](CertificatesApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificates_list_responder) | **GET** /api/certificates | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificates_list_responder_spaces**](CertificatesApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificates_list_responder_spaces) | **GET** /api/{baseSpaceId}/certificates | 
[**delete_on_background_response_descriptor_certificate_certificate_resource**](CertificatesApi.md#delete_on_background_response_descriptor_certificate_certificate_resource) | **DELETE** /api/certificates/{id} | Delete a CertificateResource by ID
[**delete_on_background_response_descriptor_certificate_certificate_resource_spaces**](CertificatesApi.md#delete_on_background_response_descriptor_certificate_certificate_resource_spaces) | **DELETE** /api/{baseSpaceId}/certificates/{id} | Delete a CertificateResource by ID
[**list_all_response_descriptor_certificate_certificate_resource**](CertificatesApi.md#list_all_response_descriptor_certificate_certificate_resource) | **GET** /api/certificates/all | Get a list of CertificateResources
[**list_all_response_descriptor_certificate_certificate_resource_spaces**](CertificatesApi.md#list_all_response_descriptor_certificate_certificate_resource_spaces) | **GET** /api/{baseSpaceId}/certificates/all | Get a list of CertificateResources
[**modify_response_descriptor_certificate_certificate_resource**](CertificatesApi.md#modify_response_descriptor_certificate_certificate_resource) | **PUT** /api/certificates/{id} | Modify a CertificateResource by ID
[**modify_response_descriptor_certificate_certificate_resource_spaces**](CertificatesApi.md#modify_response_descriptor_certificate_certificate_resource_spaces) | **PUT** /api/{baseSpaceId}/certificates/{id} | Modify a CertificateResource by ID


# **create_response_descriptor_certificate_certificate_resource**
> CertificateResource create_response_descriptor_certificate_certificate_resource(certificate_resource=certificate_resource)

Create a CertificateResource

Adds a new certificate

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
certificate_resource = octopus_deploy_swagger_client.CertificateResource() # CertificateResource | The CertificateResource resource to create (optional)

try:
    # Create a CertificateResource
    api_response = api_instance.create_response_descriptor_certificate_certificate_resource(certificate_resource=certificate_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->create_response_descriptor_certificate_certificate_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_resource** | [**CertificateResource**](CertificateResource.md)| The CertificateResource resource to create | [optional] 

### Return type

[**CertificateResource**](CertificateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_response_descriptor_certificate_certificate_resource_spaces**
> CertificateResource create_response_descriptor_certificate_certificate_resource_spaces(base_space_id, certificate_resource=certificate_resource)

Create a CertificateResource

Adds a new certificate

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
certificate_resource = octopus_deploy_swagger_client.CertificateResource() # CertificateResource | The CertificateResource resource to create (optional)

try:
    # Create a CertificateResource
    api_response = api_instance.create_response_descriptor_certificate_certificate_resource_spaces(base_space_id, certificate_resource=certificate_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->create_response_descriptor_certificate_certificate_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **certificate_resource** | [**CertificateResource**](CertificateResource.md)| The CertificateResource resource to create | [optional] 

### Return type

[**CertificateResource**](CertificateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_archive_action**
> custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_archive_action(id)



Archives a certificate  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_archive_action(id)
except ApiException as e:
    print("Exception when calling CertificatesApi->custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_archive_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_archive_action_spaces**
> custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_archive_action_spaces(base_space_id, id)



Archives a certificate  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_archive_action_spaces(base_space_id, id)
except ApiException as e:
    print("Exception when calling CertificatesApi->custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_archive_action_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_export_action**
> file custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_export_action(id)



Exports the certificate  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_export_action(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_export_action: %s\n" % e)
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
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_export_action_spaces**
> file custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_export_action_spaces(base_space_id, id)



Exports the certificate  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_export_action_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_export_action_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

[**file**](file.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_replace_action**
> CertificateResource custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_replace_action(id)



Replaces a certificate with another  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_replace_action(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_replace_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**CertificateResource**](CertificateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_replace_action_spaces**
> CertificateResource custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_replace_action_spaces(base_space_id, id)



Replaces a certificate with another  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_replace_action_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_replace_action_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

[**CertificateResource**](CertificateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_un_archive_action**
> custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_un_archive_action(id)



Un-archives a certificate  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_un_archive_action(id)
except ApiException as e:
    print("Exception when calling CertificatesApi->custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_un_archive_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_un_archive_action_spaces**
> custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_un_archive_action_spaces(base_space_id, id)



Un-archives a certificate  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the resource

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_un_archive_action_spaces(base_space_id, id)
except ApiException as e:
    print("Exception when calling CertificatesApi->custom_action_response_descriptor_octopus_server_web_api_actions_certificates_certificate_un_archive_action_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the resource | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_by_id_or_thumbprint_responder**
> CertificateResource custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_by_id_or_thumbprint_responder(id_or_thumbprint)



Get a certificate by ID or thumbprint  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id_or_thumbprint = 'id_or_thumbprint_example' # str | ID or thumbprint of certificate

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_by_id_or_thumbprint_responder(id_or_thumbprint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_by_id_or_thumbprint_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_thumbprint** | **str**| ID or thumbprint of certificate | 

### Return type

[**CertificateResource**](CertificateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_by_id_or_thumbprint_responder_spaces**
> CertificateResource custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_by_id_or_thumbprint_responder_spaces(base_space_id, id_or_thumbprint)



Get a certificate by ID or thumbprint  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id_or_thumbprint = 'id_or_thumbprint_example' # str | ID or thumbprint of certificate

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_by_id_or_thumbprint_responder_spaces(base_space_id, id_or_thumbprint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_by_id_or_thumbprint_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id_or_thumbprint** | **str**| ID or thumbprint of certificate | 

### Return type

[**CertificateResource**](CertificateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_usage_responder**
> CertificateUsageResource custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_usage_responder(id)



Get the usages of a certificate  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the certificate

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_usage_responder(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_usage_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the certificate | 

### Return type

[**CertificateUsageResource**](CertificateUsageResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_usage_responder_spaces**
> CertificateUsageResource custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_usage_responder_spaces(base_space_id, id)



Get the usages of a certificate  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the certificate

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_usage_responder_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificate_usage_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the certificate | 

### Return type

[**CertificateUsageResource**](CertificateUsageResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificates_list_responder**
> ResourceCollectionCertificateResource custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificates_list_responder()



Lists X.509 certificates managed by Octopus  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificates_list_responder()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificates_list_responder: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceCollectionCertificateResource**](ResourceCollectionCertificateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificates_list_responder_spaces**
> ResourceCollectionCertificateResource custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificates_list_responder_spaces(base_space_id)



Lists X.509 certificates managed by Octopus  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificates_list_responder_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->custom_query_response_descriptor_octopus_server_web_api_actions_certificates_certificates_list_responder_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**ResourceCollectionCertificateResource**](ResourceCollectionCertificateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_certificate_certificate_resource**
> TaskResource delete_on_background_response_descriptor_certificate_certificate_resource(id)

Delete a CertificateResource by ID

Permanently deletes a certificate

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the CertificateResource to delete

try:
    # Delete a CertificateResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_certificate_certificate_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->delete_on_background_response_descriptor_certificate_certificate_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the CertificateResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_on_background_response_descriptor_certificate_certificate_resource_spaces**
> TaskResource delete_on_background_response_descriptor_certificate_certificate_resource_spaces(base_space_id, id)

Delete a CertificateResource by ID

Permanently deletes a certificate

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the CertificateResource to delete

try:
    # Delete a CertificateResource by ID
    api_response = api_instance.delete_on_background_response_descriptor_certificate_certificate_resource_spaces(base_space_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->delete_on_background_response_descriptor_certificate_certificate_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the CertificateResource to delete | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_certificate_certificate_resource**
> list[CertificateResource] list_all_response_descriptor_certificate_certificate_resource()

Get a list of CertificateResources

Lists X.509 certificates managed by Octopus

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    # Get a list of CertificateResources
    api_response = api_instance.list_all_response_descriptor_certificate_certificate_resource()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->list_all_response_descriptor_certificate_certificate_resource: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CertificateResource]**](CertificateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_response_descriptor_certificate_certificate_resource_spaces**
> list[CertificateResource] list_all_response_descriptor_certificate_certificate_resource_spaces(base_space_id)

Get a list of CertificateResources

Lists X.509 certificates managed by Octopus

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space

try:
    # Get a list of CertificateResources
    api_response = api_instance.list_all_response_descriptor_certificate_certificate_resource_spaces(base_space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->list_all_response_descriptor_certificate_certificate_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 

### Return type

[**list[CertificateResource]**](CertificateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_certificate_certificate_resource**
> CertificateResource modify_response_descriptor_certificate_certificate_resource(id, certificate_resource=certificate_resource)

Modify a CertificateResource by ID

Modifies an existing certificate

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the CertificateResource to modify
certificate_resource = octopus_deploy_swagger_client.CertificateResource() # CertificateResource | The CertificateResource resource to create (optional)

try:
    # Modify a CertificateResource by ID
    api_response = api_instance.modify_response_descriptor_certificate_certificate_resource(id, certificate_resource=certificate_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->modify_response_descriptor_certificate_certificate_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the CertificateResource to modify | 
 **certificate_resource** | [**CertificateResource**](CertificateResource.md)| The CertificateResource resource to create | [optional] 

### Return type

[**CertificateResource**](CertificateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_response_descriptor_certificate_certificate_resource_spaces**
> CertificateResource modify_response_descriptor_certificate_certificate_resource_spaces(base_space_id, id, certificate_resource=certificate_resource)

Modify a CertificateResource by ID

Modifies an existing certificate

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
api_instance = octopus_deploy_swagger_client.CertificatesApi(octopus_deploy_swagger_client.ApiClient(configuration))
base_space_id = 'base_space_id_example' # str | ID of the space
id = 'id_example' # str | ID of the CertificateResource to modify
certificate_resource = octopus_deploy_swagger_client.CertificateResource() # CertificateResource | The CertificateResource resource to create (optional)

try:
    # Modify a CertificateResource by ID
    api_response = api_instance.modify_response_descriptor_certificate_certificate_resource_spaces(base_space_id, id, certificate_resource=certificate_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->modify_response_descriptor_certificate_certificate_resource_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_space_id** | **str**| ID of the space | 
 **id** | **str**| ID of the CertificateResource to modify | 
 **certificate_resource** | [**CertificateResource**](CertificateResource.md)| The CertificateResource resource to create | [optional] 

### Return type

[**CertificateResource**](CertificateResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

