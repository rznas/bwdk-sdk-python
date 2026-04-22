# OrderItemCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | نام کامل محصول شامل تمام مشخصات | 
**primary_amount** | **int** | قیمت اولیه برای هر واحد بدون تخفیف (به تومان) | [optional] 
**amount** | **int** | قیمت نهایی برای تمام واحدها بعد از تخفیف (به تومان) | [optional] 
**count** | **int** | تعداد واحدهای این کالا در سفارش | 
**discount_amount** | **int** | مبلغ کل تخفیف برای این کالا (به تومان) | [optional] 
**tax_amount** | **int** | مبلغ کل مالیات برای این کالا (به تومان) | [optional] 
**image_link** | **str** | آدرس تصویر محصول | [optional] 
**options** | [**List[Option]**](Option.md) |  | 
**preparation_time** | **int** | Preparation time for the item (in days) | [optional] [default to 2]
**weight** | **float** | Weight of the item (in grams) | [optional] 

## Example

```python
from bwdk_sdk.models.order_item_create import OrderItemCreate

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItemCreate from a JSON string
order_item_create_instance = OrderItemCreate.from_json(json)
# print the JSON string representation of the object
print(OrderItemCreate.to_json())

# convert the object into a dict
order_item_create_dict = order_item_create_instance.to_dict()
# create an instance of OrderItemCreate from a dict
order_item_create_from_dict = OrderItemCreate.from_dict(order_item_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


