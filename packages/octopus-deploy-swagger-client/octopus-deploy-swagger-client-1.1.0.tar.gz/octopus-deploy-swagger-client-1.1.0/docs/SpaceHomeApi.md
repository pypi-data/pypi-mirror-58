# octopus_deploy_swagger_client.SpaceHomeApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_action_response_descriptor_octopus_server_web_api_actions_space_home_responder**](SpaceHomeApi.md#custom_action_response_descriptor_octopus_server_web_api_actions_space_home_responder) | **GET** /api/(?&lt;spaceId&gt;Spaces-\d+) | 


# **custom_action_response_descriptor_octopus_server_web_api_actions_space_home_responder**
> SpaceRootResource custom_action_response_descriptor_octopus_server_web_api_actions_space_home_responder(space_id)



Returns a document describing the specified Space and links to other parts of the API that apply to the Space.  NOTE: This definition is not complete. We will be adding more detail in future releases of Octopus.

### Example
```python
from __future__ import print_function
import time
import octopus_deploy_swagger_client
from octopus_deploy_swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = octopus_deploy_swagger_client.SpaceHomeApi()
space_id = 'space_id_example' # str | ID of the space

try:
    api_response = api_instance.custom_action_response_descriptor_octopus_server_web_api_actions_space_home_responder(space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceHomeApi->custom_action_response_descriptor_octopus_server_web_api_actions_space_home_responder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| ID of the space | 

### Return type

[**SpaceRootResource**](SpaceRootResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

