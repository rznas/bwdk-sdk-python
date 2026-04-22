# RefundOrder

Serializer for refunding an order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | دلیل اختیاری برای بازگرداندن وجه | [optional] 

## Example

```python
from bwdk_sdk.models.refund_order import RefundOrder

# TODO update the JSON string below
json = "{}"
# create an instance of RefundOrder from a JSON string
refund_order_instance = RefundOrder.from_json(json)
# print the JSON string representation of the object
print(RefundOrder.to_json())

# convert the object into a dict
refund_order_dict = refund_order_instance.to_dict()
# create an instance of RefundOrder from a dict
refund_order_from_dict = RefundOrder.from_dict(refund_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


