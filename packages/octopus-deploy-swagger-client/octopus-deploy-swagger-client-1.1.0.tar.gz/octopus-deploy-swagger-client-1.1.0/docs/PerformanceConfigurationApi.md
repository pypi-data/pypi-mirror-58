# octopus_deploy_swagger_client.PerformanceConfigurationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_action_response_descriptor_octopus_server_web_api_actions_performance_configuration_get_action**](PerformanceConfigurationApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_performance_configuration_get_action) | **GET** /api/performanceconfiguration | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_performance_configuration_update_action**](PerformanceConfigurationApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_performance_configuration_update_action) | **PUT** /api/performanceconfiguration | 


# **custom_action_response_descriptor_octopus_server_web_api_actions_performance_configuration_get_action**
> PerformanceConfigurationResource custom_action_response_descriptor_octopus_server_web_api_actions_performance_configuration_get_action()



Get performance settings for the Octopus Server  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.PerformanceConfigurationApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_performance_configuration_get_action()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceConfigurationApi->custom_action_response_descriptor_octopus_server_web_api_actions_performance_configuration_get_action: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PerformanceConfigurationResource**](PerformanceConfigurationResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_performance_configuration_update_action**
> PerformanceConfigurationResource custom_action_response_descriptor_octopus_server_web_api_actions_performance_configuration_update_action()



Updates the performance settings for the Octopus Server  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.PerformanceConfigurationApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_performance_configuration_update_action()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceConfigurationApi->custom_action_response_descriptor_octopus_server_web_api_actions_performance_configuration_update_action: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PerformanceConfigurationResource**](PerformanceConfigurationResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

