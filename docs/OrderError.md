# OrderError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ErrorEnum**](ErrorEnum.md) |  | 

## Example

```python
from bwdk_sdk.models.order_error import OrderError

# TODO update the JSON string below
json = "{}"
# create an instance of OrderError from a JSON string
order_error_instance = OrderError.from_json(json)
# print the JSON string representation of the object
print(OrderError.to_json())

# convert the object into a dict
order_error_dict = order_error_instance.to_dict()
# create an instance of OrderError from a dict
order_error_from_dict = OrderError.from_dict(order_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


