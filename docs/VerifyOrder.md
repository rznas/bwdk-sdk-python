# VerifyOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_unique_id** | **str** | شناسه منحصر به فرد ارسال شده هنگام ایجاد سفارش برای تأیید اصالت سفارش | 

## Example

```python
from bwdk_sdk.models.verify_order import VerifyOrder

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyOrder from a JSON string
verify_order_instance = VerifyOrder.from_json(json)
# print the JSON string representation of the object
print(VerifyOrder.to_json())

# convert the object into a dict
verify_order_dict = verify_order_instance.to_dict()
# create an instance of VerifyOrder from a dict
verify_order_from_dict = VerifyOrder.from_dict(verify_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


