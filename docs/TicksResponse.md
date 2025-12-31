# TicksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Tick]**](Tick.md) |  | [optional] 
**credits_used** | **int** | Number of credits consumed by this request | [optional] 

## Example

```python
from qoery.models.ticks_response import TicksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TicksResponse from a JSON string
ticks_response_instance = TicksResponse.from_json(json)
# print the JSON string representation of the object
print(TicksResponse.to_json())

# convert the object into a dict
ticks_response_dict = ticks_response_instance.to_dict()
# create an instance of TicksResponse from a dict
ticks_response_from_dict = TicksResponse.from_dict(ticks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


