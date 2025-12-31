# UsageResponseApiCallsMonth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used** | **int** | API calls made in the current billing period | [optional] 

## Example

```python
from qoery.models.usage_response_api_calls_month import UsageResponseApiCallsMonth

# TODO update the JSON string below
json = "{}"
# create an instance of UsageResponseApiCallsMonth from a JSON string
usage_response_api_calls_month_instance = UsageResponseApiCallsMonth.from_json(json)
# print the JSON string representation of the object
print(UsageResponseApiCallsMonth.to_json())

# convert the object into a dict
usage_response_api_calls_month_dict = usage_response_api_calls_month_instance.to_dict()
# create an instance of UsageResponseApiCallsMonth from a dict
usage_response_api_calls_month_from_dict = UsageResponseApiCallsMonth.from_dict(usage_response_api_calls_month_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


