# CandlesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Candle]**](Candle.md) |  | [optional] 
**credits_used** | **int** | Number of credits consumed by this request | [optional] 

## Example

```python
from qoery.models.candles_response import CandlesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CandlesResponse from a JSON string
candles_response_instance = CandlesResponse.from_json(json)
# print the JSON string representation of the object
print(CandlesResponse.to_json())

# convert the object into a dict
candles_response_dict = candles_response_instance.to_dict()
# create an instance of CandlesResponse from a dict
candles_response_from_dict = CandlesResponse.from_dict(candles_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


