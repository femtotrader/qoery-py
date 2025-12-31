# UsageResponseApiCalls


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minute** | [**UsageResponseApiCallsMinute**](UsageResponseApiCallsMinute.md) |  | [optional] 
**month** | [**UsageResponseApiCallsMonth**](UsageResponseApiCallsMonth.md) |  | [optional] 

## Example

```python
from qoery.models.usage_response_api_calls import UsageResponseApiCalls

# TODO update the JSON string below
json = "{}"
# create an instance of UsageResponseApiCalls from a JSON string
usage_response_api_calls_instance = UsageResponseApiCalls.from_json(json)
# print the JSON string representation of the object
print(UsageResponseApiCalls.to_json())

# convert the object into a dict
usage_response_api_calls_dict = usage_response_api_calls_instance.to_dict()
# create an instance of UsageResponseApiCalls from a dict
usage_response_api_calls_from_dict = UsageResponseApiCalls.from_dict(usage_response_api_calls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


