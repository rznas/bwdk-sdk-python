# OrderDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**order_uuid** | **UUID** |  | [readonly] 
**reservation_expired_at** | **int** | Unix timestamp تا زمانی که سفارش برای پرداخت رزرو شده است | [readonly] 
**merchant_order_id** | **str** | شناسه منحصر به فرد سفارش در سیستم فروشنده | [readonly] 
**status** | [**OrderStatusEnum**](OrderStatusEnum.md) |  | [readonly] 
**status_display** | **str** |  | [readonly] 
**main_amount** | **int** | مجموع قیمت اولیه تمام کالاهای سفارش بدون تخفیف (به تومان) | [readonly] 
**final_amount** | **int** | قیمت نهایی قابل پرداخت توسط مشتری: مبلغ_اصلی - مبلغ_تخفیف + مبلغ_مالیات (به تومان) | [readonly] 
**total_paid_amount** | **int** | مبلغ کل پرداخت شده توسط کاربر: مبلغ_نهایی + هزینه_ارسال (به تومان) | [readonly] 
**discount_amount** | **int** | مبلغ کل تخفیف اعمال شده بر سفارش (به تومان) | [readonly] 
**tax_amount** | **int** | مبلغ کل مالیات برای سفارش (به تومان) | [readonly] 
**shipping_amount** | **int** | هزینه ارسال برای سفارش (به تومان) | [readonly] 
**loyalty_amount** | **int** | مقدار تخفیف از برنامه باشگاه مشتریان/پاداش (به تومان) | [readonly] 
**callback_url** | **str** | آدرسی برای دریافت اطلاع رسانی وضعیت پرداخت پس از تکمیل سفارش | [readonly] 
**merchant** | [**Merchant**](Merchant.md) |  | 
**items** | [**List[OrderItemCreate]**](OrderItemCreate.md) |  | 
**source_address** | **object** |  | [readonly] 
**destination_address** | **object** |  | [readonly] 
**selected_shipping_method** | [**ShippingMethod**](ShippingMethod.md) |  | [readonly] 
**shipping_selected_at** | **datetime** |  | [readonly] 
**address_selected_at** | **datetime** |  | [readonly] 
**packing_amount** | **int** | هزینه روش بسته‌بندی انتخاب‌شده (به تومان) | [readonly] 
**packing_selected_at** | **datetime** |  | [readonly] 
**selected_packing** | [**Packing**](Packing.md) |  | [readonly] 
**can_select_packing** | **bool** |  | [readonly] 
**can_select_shipping** | **bool** |  | [readonly] 
**can_select_address** | **bool** |  | [readonly] 
**can_proceed_to_payment** | **bool** |  | [readonly] 
**is_paid** | **bool** |  | [readonly] 
**user** | [**OrderUser**](OrderUser.md) |  | [readonly] 
**payment** | [**PaymentOrder**](PaymentOrder.md) |  | [readonly] 
**preparation_time** | **int** | Preparation time for the order (in days) | [readonly] 
**weight** | **float** | Total weight of the order (in grams) | [readonly] 
**selected_shipping_data** | **Dict[str, object]** |  | [readonly] 
**reference_code** | **str** | کد مرجع یکتا برای پیگیری سفارش مشتری (قالب: BD-XXXXXXXX) | [readonly] 
**promotion_discount_amount** | **float** |  | [readonly] 
**promotion_data** | **Dict[str, object]** |  | [readonly] 
**digipay_markup_amount** | **int** | Markup amount for the order (in Tomans) | [readonly] 
**markup_commission_percentage** | **int** | Markup commission percentage for the order (in percent) | [readonly] 
**previous_status** | [**OrderStatusEnum**](OrderStatusEnum.md) |  | [readonly] 
**previous_status_display** | **str** |  | [readonly] 

## Example

```python
from bwdk_sdk.models.order_detail import OrderDetail

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetail from a JSON string
order_detail_instance = OrderDetail.from_json(json)
# print the JSON string representation of the object
print(OrderDetail.to_json())

# convert the object into a dict
order_detail_dict = order_detail_instance.to_dict()
# create an instance of OrderDetail from a dict
order_detail_from_dict = OrderDetail.from_dict(order_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


