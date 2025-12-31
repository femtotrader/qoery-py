# PoolsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Pool]**](Pool.md) |  | [optional] 
**credits_used** | **int** | Number of credits consumed by this request | [optional] 

## Example

```python
from qoery.models.pools_response import PoolsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PoolsResponse from a JSON string
pools_response_instance = PoolsResponse.from_json(json)
# print the JSON string representation of the object
print(PoolsResponse.to_json())

# convert the object into a dict
pools_response_dict = pools_response_instance.to_dict()
# create an instance of PoolsResponse from a dict
pools_response_from_dict = PoolsResponse.from_dict(pools_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


