# Pool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Pool contract address | [optional] 
**network** | **str** |  | [optional] 
**protocol_version** | **str** | DEX protocol identifier (e.g., \&quot;uniswap-v3\&quot;, \&quot;uniswap-v4\&quot;) | [optional] 
**fee_tier** | **str** | Fee tier for the pool | [optional] 
**liquidity** | **str** | Current liquidity in the pool | [optional] 
**sqrt_price** | **str** | Square root price (X96 format) | [optional] 
**volume_usd** | **str** | Trading volume in USD | [optional] 
**tx_count** | **str** | Number of transactions | [optional] 
**total_value_locked_usd** | **str** | Total value locked in USD | [optional] 
**token0** | [**Token**](Token.md) |  | [optional] 
**token1** | [**Token**](Token.md) |  | [optional] 

## Example

```python
from qoery.models.pool import Pool

# TODO update the JSON string below
json = "{}"
# create an instance of Pool from a JSON string
pool_instance = Pool.from_json(json)
# print the JSON string representation of the object
print(Pool.to_json())

# convert the object into a dict
pool_dict = pool_instance.to_dict()
# create an instance of Pool from a dict
pool_from_dict = Pool.from_dict(pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


