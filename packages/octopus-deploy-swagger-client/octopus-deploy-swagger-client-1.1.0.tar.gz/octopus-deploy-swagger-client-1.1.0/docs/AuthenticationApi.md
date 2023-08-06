# octopus_deploy_swagger_client.AuthenticationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_action_response_descriptor_octopus_server_web_api_actions_authentication_authentication_responder**](AuthenticationApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_authentication_authentication_responder) | **GET** /api/authentication | 
[**custom_action_response_descriptor_octopus_server_web_api_actions_authentication_login_initiated_responder**](AuthenticationApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_authentication_login_initiated_responder) | **POST** /api/authentication/checklogininitiated | 


# **custom_action_response_descriptor_octopus_server_web_api_actions_authentication_authentication_responder**
> AuthenticationResource custom_action_response_descriptor_octopus_server_web_api_actions_authentication_authentication_responder()



Provides the details of the enabled authentication providers.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.AuthenticationApi()

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_authentication_authentication_responder()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->custom_action_response_descriptor_octopus_server_web_api_actions_authentication_authentication_responder: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthenticationResource**](AuthenticationResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_action_response_descriptor_octopus_server_web_api_actions_authentication_login_initiated_responder**
> LoginInitiatedResource custom_action_response_descriptor_octopus_server_web_api_actions_authentication_login_initiated_responder()



Given a url query string, determines whether an external server (.e.g Okta) has initiated login and if so the provider's name  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.AuthenticationApi()

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_authentication_login_initiated_responder()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->custom_action_response_descriptor_octopus_server_web_api_actions_authentication_login_initiated_responder: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LoginInitiatedResource**](LoginInitiatedResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

