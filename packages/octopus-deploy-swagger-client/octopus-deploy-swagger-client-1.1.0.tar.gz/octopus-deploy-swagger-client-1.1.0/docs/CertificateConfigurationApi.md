# octopus_deploy_swagger_client.CertificateConfigurationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_action_response_descriptor_octopus_server_web_api_actions_certificate_public_cer_download_action**](CertificateConfigurationApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_certificate_public_cer_download_action) | **GET** /api/configuration/certificates/{id}/public-cer | 
[**index_response_descriptor_configuration_certificate_configuration_certificate_configuration_resource**](CertificateConfigurationApi.md#index_response_descriptor_configuration_certificate_configuration_certificate_configuration_resource) | **GET** /api/configuration/certificates | Get a list of CertificateConfigurationResources
[**load_response_descriptor_configuration_certificate_configuration_certificate_configuration_resource**](CertificateConfigurationApi.md#load_response_descriptor_configuration_certificate_configuration_certificate_configuration_resource) | **GET** /api/certificates/(?&lt;id&gt;(?i)^(certificate-global)) | Get a CertificateConfigurationResource by ID
[**load_response_descriptor_configuration_certificate_configuration_certificate_configuration_resource_0**](CertificateConfigurationApi.md#load_response_descriptor_configuration_certificate_configuration_certificate_configuration_resource_0) | **GET** /api/configuration/certificates/{id} | Get a CertificateConfigurationResource by ID


# **custom_action_response_descriptor_octopus_server_web_api_actions_certificate_public_cer_download_action**
> file custom_action_response_descriptor_octopus_server_web_api_actions_certificate_public_cer_download_action(id)



Downloads the public portion of the certificate in .cer format  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.CertificateConfigurationApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_certificate_public_cer_download_action(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateConfigurationApi->custom_action_response_descriptor_octopus_server_web_api_actions_certificate_public_cer_download_action: %s\n" % e)
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
 - **Accept**: application/x-x509-ca-cert

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_response_descriptor_configuration_certificate_configuration_certificate_configuration_resource**
> ResourceCollectionCertificateConfigurationResource index_response_descriptor_configuration_certificate_configuration_certificate_configuration_resource(skip=skip, take=take)

Get a list of CertificateConfigurationResources

Lists all of the X509 certificates in the current Octopus Deploy installation.

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
api_instance = octopus_deploy_swagger_client.CertificateConfigurationApi(octopus_deploy_swagger_client.ApiClient(configuration))
skip = 56 # int | Number of items to skip (optional)
take = 56 # int | Number of items to take (optional)

try:
    # Get a list of CertificateConfigurationResources
    api_response = api_instance.index_response_descriptor_configuration_certificate_configuration_certificate_configuration_resource(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateConfigurationApi->index_response_descriptor_configuration_certificate_configuration_certificate_configuration_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of items to skip | [optional] 
 **take** | **int**| Number of items to take | [optional] 

### Return type

[**ResourceCollectionCertificateConfigurationResource**](ResourceCollectionCertificateConfigurationResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_configuration_certificate_configuration_certificate_configuration_resource**
> CertificateConfigurationResource load_response_descriptor_configuration_certificate_configuration_certificate_configuration_resource(id)

Get a CertificateConfigurationResource by ID

Gets a certificate by ID.

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
api_instance = octopus_deploy_swagger_client.CertificateConfigurationApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the CertificateConfigurationResource to load

try:
    # Get a CertificateConfigurationResource by ID
    api_response = api_instance.load_response_descriptor_configuration_certificate_configuration_certificate_configuration_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateConfigurationApi->load_response_descriptor_configuration_certificate_configuration_certificate_configuration_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the CertificateConfigurationResource to load | 

### Return type

[**CertificateConfigurationResource**](CertificateConfigurationResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_response_descriptor_configuration_certificate_configuration_certificate_configuration_resource_0**
> CertificateConfigurationResource load_response_descriptor_configuration_certificate_configuration_certificate_configuration_resource_0(id)

Get a CertificateConfigurationResource by ID

Gets a certificate by ID.

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
api_instance = octopus_deploy_swagger_client.CertificateConfigurationApi(octopus_deploy_swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the CertificateConfigurationResource to load

try:
    # Get a CertificateConfigurationResource by ID
    api_response = api_instance.load_response_descriptor_configuration_certificate_configuration_certificate_configuration_resource_0(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateConfigurationApi->load_response_descriptor_configuration_certificate_configuration_certificate_configuration_resource_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the CertificateConfigurationResource to load | 

### Return type

[**CertificateConfigurationResource**](CertificateConfigurationResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

