# octopus_deploy_swagger_client.HomeApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_action_response_descriptor_octopus_server_web_api_actions_home_responder**](HomeApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_home_responder) | **GET** /api | 


# **custom_action_response_descriptor_octopus_server_web_api_actions_home_responder**
> RootResource custom_action_response_descriptor_octopus_server_web_api_actions_home_responder()



Returns a document describing the current Octopus Server and links to other parts of the API.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.HomeApi()

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_home_responder()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomeApi->custom_action_response_descriptor_octopus_server_web_api_actions_home_responder: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RootResource**](RootResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

