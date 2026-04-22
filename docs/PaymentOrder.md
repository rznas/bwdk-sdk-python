# PaymentOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**final_amount** | **int** |  | [readonly] 
**gateway_type** | [**GatewayTypeEnum**](GatewayTypeEnum.md) |  | [readonly] 
**gateway_type_display** | **str** |  | [readonly] 
**paid_at** | **str** |  | [readonly] 
**gateway_name** | **str** |  | [readonly] 
**invoice_id** | **str** |  | [readonly] 
**settlement_date** | **str** |  | [readonly] 
**settlement_status** | **int** |  | [readonly] 
**settlement_status_display** | **str** |  | [readonly] 

## Example

```python
from bwdk_sdk.models.payment_order import PaymentOrder

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentOrder from a JSON string
payment_order_instance = PaymentOrder.from_json(json)
# print the JSON string representation of the object
print(PaymentOrder.to_json())

# convert the object into a dict
payment_order_dict = payment_order_instance.to_dict()
# create an instance of PaymentOrder from a dict
payment_order_from_dict = PaymentOrder.from_dict(payment_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


