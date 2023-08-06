# octopus_deploy_swagger_client.ServerStatusApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_action_response_descriptor_octopus_server_web_api_actions_status_extension_stats_responder**](ServerStatusApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_status_extension_stats_responder) | **GET** /api/serverstatus/extensions | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_status_recent_logs_responder**](ServerStatusApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_status_recent_logs_responder) | **GET** /api/serverstatus/logs | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_status_server_status_health_responder**](ServerStatusApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_status_server_status_health_responder) | **GET** /api/serverstatus/health | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_status_server_status_responder**](ServerStatusApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_status_server_status_responder) | **GET** /api/serverstatus | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_status_system_garbage_collect_responder**](ServerStatusApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_status_system_garbage_collect_responder) | **POST** /api/serverstatus/gc-collect | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_status_system_info_responder**](ServerStatusApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_status_system_info_responder) | **GET** /api/serverstatus/system-info | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_status_system_report_responder**](ServerStatusApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_status_system_report_responder) | **GET** /api/serverstatus/system-report | 
[**custom_query_response_descriptor_octopus_server_web_api_actions_list_server_timezones_responder**](ServerStatusApi.md#custom_query_response_descriptor_octopus_server_web_api_actions_list_server_timezones_responder) | **GET** /api/serverstatus/timezones | 


# **custom_action_response_descriptor_octopus_server_web_api_actions_status_extension_stats_responder**
> list[ExtensionsInfoResource] custom_action_response_descriptor_octopus_server_web_api_actions_status_extension_stats_responder()



Provides statistics for the loaded server extensions.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ServerStatusApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_status_extension_stats_responder()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerStatusApi->custom_action_response_descriptor_octopus_server_web_api_actions_status_extension_stats_responder: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ExtensionsInfoResource]**](ExtensionsInfoResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_status_recent_logs_responder**
> custom_action_response_descriptor_octopus_server_web_api_actions_status_recent_logs_responder()



Retrieves the most recent high-priority log messages from this execution of the Octopus Server process.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ServerStatusApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_status_recent_logs_responder()
except ApiException as e:
    print("Exception when calling ServerStatusApi->custom_action_response_descriptor_octopus_server_web_api_actions_status_recent_logs_responder: %s\n" % e)
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

# **custom_action_response_descriptor_octopus_server_web_api_actions_status_server_status_health_responder**
> ServerStatusHealthResource custom_action_response_descriptor_octopus_server_web_api_actions_status_server_status_health_responder()



Provides a super simple interface perfect for checking the general health of your entire Octopus Server cluster.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.ServerStatusApi()

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_status_server_status_health_responder()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerStatusApi->custom_action_response_descriptor_octopus_server_web_api_actions_status_server_status_health_responder: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerStatusHealthResource**](ServerStatusHealthResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_status_server_status_responder**
> custom_action_response_descriptor_octopus_server_web_api_actions_status_server_status_responder()



Shows information about the status of the Octopus Server.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ServerStatusApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_status_server_status_responder()
except ApiException as e:
    print("Exception when calling ServerStatusApi->custom_action_response_descriptor_octopus_server_web_api_actions_status_server_status_responder: %s\n" % e)
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

# **custom_action_response_descriptor_octopus_server_web_api_actions_status_system_garbage_collect_responder**
> custom_action_response_descriptor_octopus_server_web_api_actions_status_system_garbage_collect_responder()



Forces a GC collect.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ServerStatusApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_status_system_garbage_collect_responder()
except ApiException as e:
    print("Exception when calling ServerStatusApi->custom_action_response_descriptor_octopus_server_web_api_actions_status_system_garbage_collect_responder: %s\n" % e)
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

# **custom_action_response_descriptor_octopus_server_web_api_actions_status_system_info_responder**
> custom_action_response_descriptor_octopus_server_web_api_actions_status_system_info_responder()



Provides information about the Octopus Server process and the machine on which it is running.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ServerStatusApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_status_system_info_responder()
except ApiException as e:
    print("Exception when calling ServerStatusApi->custom_action_response_descriptor_octopus_server_web_api_actions_status_system_info_responder: %s\n" % e)
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

# **custom_action_response_descriptor_octopus_server_web_api_actions_status_system_report_responder**
> custom_action_response_descriptor_octopus_server_web_api_actions_status_system_report_responder()



Creates a .zip archive containing an aggregate of the other system information APIs.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ServerStatusApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_status_system_report_responder()
except ApiException as e:
    print("Exception when calling ServerStatusApi->custom_action_response_descriptor_octopus_server_web_api_actions_status_system_report_responder: %s\n" % e)
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

# **custom_query_response_descriptor_octopus_server_web_api_actions_list_server_timezones_responder**
> list[ServerTimezoneResource] custom_query_response_descriptor_octopus_server_web_api_actions_list_server_timezones_responder()



Lists timezones supported by the server.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

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
api_instance = octopus_deploy_swagger_client.ServerStatusApi(octopus_deploy_swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.custom_query_response_descriptor_octopus_server_web_api_actions_list_server_timezones_responder()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerStatusApi->custom_query_response_descriptor_octopus_server_web_api_actions_list_server_timezones_responder: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ServerTimezoneResource]**](ServerTimezoneResource.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQuery](../README.md#APIKeyQuery), [NugetApiKeyHeader](../README.md#NugetApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

