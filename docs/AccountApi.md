# qoery.AccountApi

All URIs are relative to *https://api.qoery.com/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usage_get**](AccountApi.md#usage_get) | **GET** /usage | Get API Usage Statistics


# **usage_get**
> UsageResponse usage_get()

Get API Usage Statistics

Get detailed usage statistics for your API key, including:
- Credits used (per minute and per month)
- API calls made (per minute and per month)
- Rate limits and remaining quota
- Billing period information

### Example

* Api Key Authentication (ApiKeyAuthQuery):
* Api Key Authentication (ApiKeyAuthHeader):

```python
import qoery
from qoery.models.usage_response import UsageResponse
from qoery.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.qoery.com/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = qoery.Configuration(
    host = "https://api.qoery.com/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuthQuery
configuration.api_key['ApiKeyAuthQuery'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuthQuery'] = 'Bearer'

# Configure API key authorization: ApiKeyAuthHeader
configuration.api_key['ApiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuthHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with qoery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qoery.AccountApi(api_client)

    try:
        # Get API Usage Statistics
        api_response = api_instance.usage_get()
        print("The response of AccountApi->usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->usage_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UsageResponse**](UsageResponse.md)

### Authorization

[ApiKeyAuthQuery](../README.md#ApiKeyAuthQuery), [ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage statistics |  -  |
**401** | Unauthorized - API key required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

