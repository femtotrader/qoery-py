# UsageResponseCreditsMonth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used** | **int** | Credits used in the current billing period | [optional] 
**limit** | **int** | Credit limit per month | [optional] 
**remaining** | **int** | Credits remaining in the current billing period | [optional] 
**reset_at** | **datetime** | ISO 8601 timestamp | [optional] 
**billing_period_start** | **datetime** | ISO 8601 timestamp | [optional] 

## Example

```python
from qoery.models.usage_response_credits_month import UsageResponseCreditsMonth

# TODO update the JSON string below
json = "{}"
# create an instance of UsageResponseCreditsMonth from a JSON string
usage_response_credits_month_instance = UsageResponseCreditsMonth.from_json(json)
# print the JSON string representation of the object
print(UsageResponseCreditsMonth.to_json())

# convert the object into a dict
usage_response_credits_month_dict = usage_response_credits_month_instance.to_dict()
# create an instance of UsageResponseCreditsMonth from a dict
usage_response_credits_month_from_dict = UsageResponseCreditsMonth.from_dict(usage_response_credits_month_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


