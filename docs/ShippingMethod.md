# ShippingMethod

Serializer for shipping method details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | نام روش ارسال | 
**description** | **str** | توضیحات روش ارسال و جزئیات تحویل آن | [optional] 
**shipping_type** | [**ShippingTypeEnum**](ShippingTypeEnum.md) | نوع روش ارسال: عادی یا دیجی اکسپرس  * &#x60;1&#x60; - سایر * &#x60;2&#x60; - دیجی اکسپرس | [optional] 
**get_shipping_type_display** | **str** |  | [readonly] 
**shipping_type_display** | **str** |  | [readonly] 
**cost** | **int** | هزینه ارسال برای منطقه اولیه (مثلاً تهران) به تومان | [optional] 
**secondary_cost** | **int** | هزینه ارسال برای مناطق دیگر به تومان | [optional] 
**minimum_time_sending** | **int** | حداقل تعداد روزها از تاریخ سفارش تا تحویل | [optional] 
**maximum_time_sending** | **int** | حداکثر تعداد روزها از تاریخ سفارش تا تحویل | [optional] 
**delivery_time_display** | **str** |  | [readonly] 
**delivery_time_range_display** | [**DeliveryTimeRangeDisplay**](DeliveryTimeRangeDisplay.md) |  | [readonly] 
**inventory_address** | [**BusinessAddress**](BusinessAddress.md) |  | [readonly] 
**is_pay_at_destination** | **bool** | Whether the shipping method is pay at destination | [optional] 

## Example

```python
from bwdk_sdk.models.shipping_method import ShippingMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingMethod from a JSON string
shipping_method_instance = ShippingMethod.from_json(json)
# print the JSON string representation of the object
print(ShippingMethod.to_json())

# convert the object into a dict
shipping_method_dict = shipping_method_instance.to_dict()
# create an instance of ShippingMethod from a dict
shipping_method_from_dict = ShippingMethod.from_dict(shipping_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


