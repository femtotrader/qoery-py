# UsageResponseApiCallsMinute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used** | **int** | API calls made in the current minute | [optional] 

## Example

```python
from qoery.models.usage_response_api_calls_minute import UsageResponseApiCallsMinute

# TODO update the JSON string below
json = "{}"
# create an instance of UsageResponseApiCallsMinute from a JSON string
usage_response_api_calls_minute_instance = UsageResponseApiCallsMinute.from_json(json)
# print the JSON string representation of the object
print(UsageResponseApiCallsMinute.to_json())

# convert the object into a dict
usage_response_api_calls_minute_dict = usage_response_api_calls_minute_instance.to_dict()
# create an instance of UsageResponseApiCallsMinute from a dict
usage_response_api_calls_minute_from_dict = UsageResponseApiCallsMinute.from_dict(usage_response_api_calls_minute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


