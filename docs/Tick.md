# Tick


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique swap transaction ID | [optional] 
**timestamp** | **datetime** | ISO 8601 timestamp | [optional] 
**price** | **float** | Execution price (token1 per token0, e.g. USDT per WBTC) | [optional] 
**side** | **str** | Trade direction - \&quot;buy\&quot; means buying token0, \&quot;sell\&quot; means selling token0 | [optional] 
**amount0** | **str** | Amount of token0 traded (negative &#x3D; sold, positive &#x3D; bought) | [optional] 
**amount1** | **str** | Amount of token1 traded (negative &#x3D; sold, positive &#x3D; bought) | [optional] 
**amount_usd** | **float** | USD value of the swap | [optional] 
**sqrt_price_x96** | **str** | Square root price in X96 format (for advanced users) | [optional] 
**token0** | **str** | Token0 symbol | [optional] 
**token1** | **str** | Token1 symbol | [optional] 

## Example

```python
from qoery.models.tick import Tick

# TODO update the JSON string below
json = "{}"
# create an instance of Tick from a JSON string
tick_instance = Tick.from_json(json)
# print the JSON string representation of the object
print(Tick.to_json())

# convert the object into a dict
tick_dict = tick_instance.to_dict()
# create an instance of Tick from a dict
tick_from_dict = Tick.from_dict(tick_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


