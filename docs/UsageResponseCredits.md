# UsageResponseCredits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minute** | [**UsageResponseCreditsMinute**](UsageResponseCreditsMinute.md) |  | [optional] 
**month** | [**UsageResponseCreditsMonth**](UsageResponseCreditsMonth.md) |  | [optional] 

## Example

```python
from qoery.models.usage_response_credits import UsageResponseCredits

# TODO update the JSON string below
json = "{}"
# create an instance of UsageResponseCredits from a JSON string
usage_response_credits_instance = UsageResponseCredits.from_json(json)
# print the JSON string representation of the object
print(UsageResponseCredits.to_json())

# convert the object into a dict
usage_response_credits_dict = usage_response_credits_instance.to_dict()
# create an instance of UsageResponseCredits from a dict
usage_response_credits_from_dict = UsageResponseCredits.from_dict(usage_response_credits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


