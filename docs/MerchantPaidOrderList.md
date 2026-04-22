# MerchantPaidOrderList

Serializer for manager view listing PAID_BY_USER orders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_uuid** | **UUID** |  | [readonly] 
**merchant_order_id** | **str** | شناسه منحصر به فرد سفارش در سیستم فروشنده | [readonly] 
**merchant_unique_id** | **str** | شناسه منحصر به فرد برای پذیرنده برای تأیید سفارش | [readonly] 
**paid_at** | **datetime** |  | [readonly] 
**refunds_at** | **datetime** |  | [readonly] 

## Example

```python
from bwdk_sdk.models.merchant_paid_order_list import MerchantPaidOrderList

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantPaidOrderList from a JSON string
merchant_paid_order_list_instance = MerchantPaidOrderList.from_json(json)
# print the JSON string representation of the object
print(MerchantPaidOrderList.to_json())

# convert the object into a dict
merchant_paid_order_list_dict = merchant_paid_order_list_instance.to_dict()
# create an instance of MerchantPaidOrderList from a dict
merchant_paid_order_list_from_dict = MerchantPaidOrderList.from_dict(merchant_paid_order_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


