# UsageResponseCreditsMinute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used** | **int** | Credits used in the current minute | [optional] 
**limit** | **int** | Credit limit per minute | [optional] 
**remaining** | **int** | Credits remaining in the current minute | [optional] 
**reset_at** | **datetime** | ISO 8601 timestamp | [optional] 

## Example

```python
from qoery.models.usage_response_credits_minute import UsageResponseCreditsMinute

# TODO update the JSON string below
json = "{}"
# create an instance of UsageResponseCreditsMinute from a JSON string
usage_response_credits_minute_instance = UsageResponseCreditsMinute.from_json(json)
# print the JSON string representation of the object
print(UsageResponseCreditsMinute.to_json())

# convert the object into a dict
usage_response_credits_minute_dict = usage_response_credits_minute_instance.to_dict()
# create an instance of UsageResponseCreditsMinute from a dict
usage_response_credits_minute_from_dict = UsageResponseCreditsMinute.from_dict(usage_response_credits_minute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


