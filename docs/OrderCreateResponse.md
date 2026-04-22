# OrderCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_start_url** | **str** |  | 
**order_uuid** | **UUID** |  | 

## Example

```python
from bwdk_sdk.models.order_create_response import OrderCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateResponse from a JSON string
order_create_response_instance = OrderCreateResponse.from_json(json)
# print the JSON string representation of the object
print(OrderCreateResponse.to_json())

# convert the object into a dict
order_create_response_dict = order_create_response_instance.to_dict()
# create an instance of OrderCreateResponse from a dict
order_create_response_from_dict = OrderCreateResponse.from_dict(order_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


