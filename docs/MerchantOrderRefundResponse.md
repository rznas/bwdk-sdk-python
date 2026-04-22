# MerchantOrderRefundResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**order_uuid** | **UUID** |  | 
**status** | [**OrderStatusEnum**](OrderStatusEnum.md) |  | 
**status_display** | **str** |  | 
**refund_reason** | **str** |  | 

## Example

```python
from bwdk_sdk.models.merchant_order_refund_response import MerchantOrderRefundResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantOrderRefundResponse from a JSON string
merchant_order_refund_response_instance = MerchantOrderRefundResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantOrderRefundResponse.to_json())

# convert the object into a dict
merchant_order_refund_response_dict = merchant_order_refund_response_instance.to_dict()
# create an instance of MerchantOrderRefundResponse from a dict
merchant_order_refund_response_from_dict = MerchantOrderRefundResponse.from_dict(merchant_order_refund_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


