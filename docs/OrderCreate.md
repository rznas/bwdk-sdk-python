# OrderCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_order_id** | **str** | شناسه منحصر به فرد این سفارش در سیستم فروشنده | 
**merchant_unique_id** | **str** | شناسه منحصر به فرد برای تأیید اصالت سفارش | 
**main_amount** | **int** | مجموع قیمت‌های اولیه تمام کالاها بدون تخفیف (به تومان) | [optional] 
**final_amount** | **int** | مبلغ نهایی: مبلغ_اصلی - مبلغ_تخفیف + مبلغ_مالیات (به تومان) | [optional] 
**total_paid_amount** | **int** | مبلغ کل پرداخت شده توسط کاربر: مبلغ_نهایی + هزینه_ارسال (به تومان) | [optional] 
**discount_amount** | **int** | مبلغ کل تخفیف برای تمام سفارش (به تومان) | [optional] 
**tax_amount** | **int** | مبلغ کل مالیات برای تمام سفارش (به تومان) | [optional] 
**shipping_amount** | **int** | هزینه ارسال برای سفارش (به تومان) | [optional] 
**loyalty_amount** | **int** | مبلغ تخفیف باشگاه مشتریان/پاداش (به تومان) | [optional] 
**callback_url** | **str** | آدرس وب‌هوک برای دریافت اطلاع رسانی وضعیت پرداخت | 
**destination_address** | **object** |  | [readonly] 
**items** | [**List[OrderItemCreate]**](OrderItemCreate.md) |  | 
**merchant** | **int** | مقدار توسط سیستم جایگذاری می شود | [optional] 
**source_address** | **object** | مقدار توسط سیستم جایگذاری می شود | [optional] 
**user** | **int** |  | [readonly] 
**reservation_expired_at** | **int** | مهلت پرداخت (به عنوان Unix timestamp) قبل از اتمام سفارش | [optional] 
**reference_code** | **str** | کد مرجع منحصر به فرد برای پیگیری سفارش مشتری (فرمت: BD-XXXXXXXX) | [readonly] 
**preparation_time** | **int** | زمان آمادهسازی سفارش (به روز) | [optional] [default to 2]
**weight** | **float** | وزن کل سفارش (بر حسب گرم) | [optional] 

## Example

```python
from bwdk_sdk.models.order_create import OrderCreate

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreate from a JSON string
order_create_instance = OrderCreate.from_json(json)
# print the JSON string representation of the object
print(OrderCreate.to_json())

# convert the object into a dict
order_create_dict = order_create_instance.to_dict()
# create an instance of OrderCreate from a dict
order_create_from_dict = OrderCreate.from_dict(order_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


