# qoery.MarketDataApi

All URIs are relative to *https://api.qoery.com/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**candles_get**](MarketDataApi.md#candles_get) | **GET** /candles | Get OHLCV Candles
[**ticks_get**](MarketDataApi.md#ticks_get) | **GET** /ticks | Get Raw Tick Data


# **candles_get**
> CandlesResponse candles_get(interval, symbol=symbol, pool=pool, var_from=var_from, to=to, networks=networks, limit=limit)

Get OHLCV Candles

Fetch OHLCV candles for a given symbol pair OR specific pool.

**Required:** Provide either `symbol` OR `pool` parameter (mutually exclusive).

**Optimization:** Use `pool` address for faster response (1 subgraph request vs 2).

**Time Range Defaults:**
- If `from` is omitted: calculated based on `interval` and `limit` to fetch only the requested number of candles (e.g., with `limit=5` and `interval=15m`, defaults to 75 minutes ago)
- If `to` is omitted: defaults to current time (live data)

**Credits:** Each GraphQL query costs 1 credit. Total credits depend on data fetched (swaps, time range, pagination). Using `pool` skips discovery and is more efficient.

### Example

* Api Key Authentication (ApiKeyAuthQuery):
* Api Key Authentication (ApiKeyAuthHeader):

```python
import qoery
from qoery.models.candles_response import CandlesResponse
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
    api_instance = qoery.MarketDataApi(api_client)
    interval = '15m' # str | Candle time interval. Fully flexible. Format: `[number][unit]` where unit is: - `s` = seconds (e.g., \"30s\", \"45s\") - `m` = minutes (e.g., \"1m\", \"5m\", \"15m\") - `h` = hours (e.g., \"1h\", \"4h\", \"12h\") - `d` = days (e.g., \"1d\")  Maximum: 1d 
    symbol = 'ETH-USDC' # str | Trading pair symbol (e.g., \"ETH-USDC\"). Case-insensitive. **Note:** Provide either `symbol` OR `pool`, not both.  (optional)
    pool = '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640' # str | Pool contract address. Use this instead of symbol for faster responses, and less credits used. **Note:** Provide either `symbol` OR `pool`, not both.  (optional)
    var_from = '2023-11-29T12:00:00Z' # datetime | Start timestamp (ISO 8601 format). **Default:** Calculated based on `interval` and `limit` to fetch only the requested number of candles (e.g., with `limit=5` and `interval=15m`, defaults to 75 minutes ago).  (optional)
    to = '2023-11-30T12:00:00Z' # datetime | End timestamp (ISO 8601 format). **Default:** Current time (live data).  (optional)
    networks = 'ethereum,arbitrum' # str | Comma-separated list of networks to query. **Supported networks:** ethereum, arbitrum, polygon, base, optimism **Default:** If not specified, queries `ethereum` first (fastest), then expands to `ethereum,arbitrum,polygon` if no results found.  (optional)
    limit = 5 # int | Maximum number of candles to return. Defaults to 5. Maximum is 100. (optional) (default to 5)

    try:
        # Get OHLCV Candles
        api_response = api_instance.candles_get(interval, symbol=symbol, pool=pool, var_from=var_from, to=to, networks=networks, limit=limit)
        print("The response of MarketDataApi->candles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->candles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interval** | **str**| Candle time interval. Fully flexible. Format: &#x60;[number][unit]&#x60; where unit is: - &#x60;s&#x60; &#x3D; seconds (e.g., \&quot;30s\&quot;, \&quot;45s\&quot;) - &#x60;m&#x60; &#x3D; minutes (e.g., \&quot;1m\&quot;, \&quot;5m\&quot;, \&quot;15m\&quot;) - &#x60;h&#x60; &#x3D; hours (e.g., \&quot;1h\&quot;, \&quot;4h\&quot;, \&quot;12h\&quot;) - &#x60;d&#x60; &#x3D; days (e.g., \&quot;1d\&quot;)  Maximum: 1d  | 
 **symbol** | **str**| Trading pair symbol (e.g., \&quot;ETH-USDC\&quot;). Case-insensitive. **Note:** Provide either &#x60;symbol&#x60; OR &#x60;pool&#x60;, not both.  | [optional] 
 **pool** | **str**| Pool contract address. Use this instead of symbol for faster responses, and less credits used. **Note:** Provide either &#x60;symbol&#x60; OR &#x60;pool&#x60;, not both.  | [optional] 
 **var_from** | **datetime**| Start timestamp (ISO 8601 format). **Default:** Calculated based on &#x60;interval&#x60; and &#x60;limit&#x60; to fetch only the requested number of candles (e.g., with &#x60;limit&#x3D;5&#x60; and &#x60;interval&#x3D;15m&#x60;, defaults to 75 minutes ago).  | [optional] 
 **to** | **datetime**| End timestamp (ISO 8601 format). **Default:** Current time (live data).  | [optional] 
 **networks** | **str**| Comma-separated list of networks to query. **Supported networks:** ethereum, arbitrum, polygon, base, optimism **Default:** If not specified, queries &#x60;ethereum&#x60; first (fastest), then expands to &#x60;ethereum,arbitrum,polygon&#x60; if no results found.  | [optional] 
 **limit** | **int**| Maximum number of candles to return. Defaults to 5. Maximum is 100. | [optional] [default to 5]

### Return type

[**CandlesResponse**](CandlesResponse.md)

### Authorization

[ApiKeyAuthQuery](../README.md#ApiKeyAuthQuery), [ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticks_get**
> TicksResponse ticks_get(symbol=symbol, pool=pool, var_from=var_from, to=to, limit=limit, networks=networks)

Get Raw Tick Data

Fetch raw tick-level swap data for a pool (no OHLCV aggregation).

**Required:** Provide either `symbol` OR `pool` parameter (mutually exclusive).

**Use case:** Real-time trade monitoring, custom aggregation, order flow analysis.

### Example

* Api Key Authentication (ApiKeyAuthQuery):
* Api Key Authentication (ApiKeyAuthHeader):

```python
import qoery
from qoery.models.ticks_response import TicksResponse
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
    api_instance = qoery.MarketDataApi(api_client)
    symbol = 'ETH-USDC' # str | Trading pair symbol (e.g., \"ETH-USDC\"). Case-insensitive. **Note:** Provide either `symbol` OR `pool`, not both.  (optional)
    pool = '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640' # str | Pool contract address. Use this instead of symbol for faster responses, and less credits used. **Note:** Provide either `symbol` OR `pool`, not both.  (optional)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Start timestamp (ISO 8601). Default is 1 hour ago. (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | End timestamp (ISO 8601). Default is now. (optional)
    limit = 100 # int | Maximum number of ticks to return (1-1000, default 100). (optional) (default to 100)
    networks = 'ethereum,arbitrum' # str | Comma-separated list of networks to query. (optional)

    try:
        # Get Raw Tick Data
        api_response = api_instance.ticks_get(symbol=symbol, pool=pool, var_from=var_from, to=to, limit=limit, networks=networks)
        print("The response of MarketDataApi->ticks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketDataApi->ticks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading pair symbol (e.g., \&quot;ETH-USDC\&quot;). Case-insensitive. **Note:** Provide either &#x60;symbol&#x60; OR &#x60;pool&#x60;, not both.  | [optional] 
 **pool** | **str**| Pool contract address. Use this instead of symbol for faster responses, and less credits used. **Note:** Provide either &#x60;symbol&#x60; OR &#x60;pool&#x60;, not both.  | [optional] 
 **var_from** | **datetime**| Start timestamp (ISO 8601). Default is 1 hour ago. | [optional] 
 **to** | **datetime**| End timestamp (ISO 8601). Default is now. | [optional] 
 **limit** | **int**| Maximum number of ticks to return (1-1000, default 100). | [optional] [default to 100]
 **networks** | **str**| Comma-separated list of networks to query. | [optional] 

### Return type

[**TicksResponse**](TicksResponse.md)

### Authorization

[ApiKeyAuthQuery](../README.md#ApiKeyAuthQuery), [ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

