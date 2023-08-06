# octopus_deploy_swagger_client.LetsEncryptApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_action_response_descriptor_octopus_server_web_api_actions_lets_encrypt_configuration_get_action**](LetsEncryptApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_lets_encrypt_configuration_get_action) | **GET** api/letsencryptconfiguration | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_lets_encrypt_configuration_update_action**](LetsEncryptApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_lets_encrypt_configuration_update_action) | **PUT** api/letsencryptconfiguration | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_lets_encrypt_http_challenge_responder**](LetsEncryptApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_lets_encrypt_http_challenge_responder) | **GET** /.well-known/acme-challenge//{token} | 


# **custom_action_response_descriptor_octopus_server_web_api_actions_lets_encrypt_configuration_get_action**
> custom_action_response_descriptor_octopus_server_web_api_actions_lets_encrypt_configuration_get_action()



Returns the current Let's Encrypt configuration  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.LetsEncryptApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_lets_encrypt_configuration_get_action()
except ApiException as e:
    print("Exception when calling LetsEncryptApi->custom_action_response_descriptor_octopus_server_web_api_actions_lets_encrypt_configuration_get_action: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_lets_encrypt_configuration_update_action**
> custom_action_response_descriptor_octopus_server_web_api_actions_lets_encrypt_configuration_update_action()



Updates the Let's Encrypt configuration used by the Octopus Server.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.LetsEncryptApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_lets_encrypt_configuration_update_action()
except ApiException as e:
    print("Exception when calling LetsEncryptApi->custom_action_response_descriptor_octopus_server_web_api_actions_lets_encrypt_configuration_update_action: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_lets_encrypt_http_challenge_responder**
> custom_action_response_descriptor_octopus_server_web_api_actions_lets_encrypt_http_challenge_responder(token)



Returns the computed HTTP challenge for a given token  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.LetsEncryptApi()
token = 'token_example' # str | LetsEncrypt response token

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_lets_encrypt_http_challenge_responder(token)
except ApiException as e:
    print("Exception when calling LetsEncryptApi->custom_action_response_descriptor_octopus_server_web_api_actions_lets_encrypt_http_challenge_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| LetsEncrypt response token | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

