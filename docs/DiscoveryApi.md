# qoery.DiscoveryApi

All URIs are relative to *https://api.qoery.com/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pools_get**](DiscoveryApi.md#pools_get) | **GET** /pools | Find Liquidity Pools


# **pools_get**
> PoolsResponse pools_get(symbol)

Find Liquidity Pools

Find the best liquidity pools for a given symbol pair across all networks.

### Example

* Api Key Authentication (ApiKeyAuthQuery):
* Api Key Authentication (ApiKeyAuthHeader):

```python
import qoery
from qoery.models.pools_response import PoolsResponse
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
    api_instance = qoery.DiscoveryApi(api_client)
    symbol = 'ETH-USDC' # str | Trading pair symbol (e.g., \"ETH-USDC\"). Case-insensitive.

    try:
        # Find Liquidity Pools
        api_response = api_instance.pools_get(symbol)
        print("The response of DiscoveryApi->pools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryApi->pools_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading pair symbol (e.g., \&quot;ETH-USDC\&quot;). Case-insensitive. | 

### Return type

[**PoolsResponse**](PoolsResponse.md)

### Authorization

[ApiKeyAuthQuery](../README.md#ApiKeyAuthQuery), [ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of found pools sorted by liquidity |  -  |
**400** | Invalid parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

