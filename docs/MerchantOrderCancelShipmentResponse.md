# MerchantOrderCancelShipmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | پیام موفق‌‌ | 
**order_uuid** | **UUID** | شناسه منحصر به فرد سفارش | 
**status** | [**OrderStatusEnum**](OrderStatusEnum.md) | وضعیت فعلی سفارش  * &#x60;1&#x60; - اولیه * &#x60;2&#x60; - شروع در * &#x60;3&#x60; - در انتظار * &#x60;4&#x60; - در انتظار درگاه * &#x60;5&#x60; - منقضی شده * &#x60;6&#x60; - لغو شده * &#x60;7&#x60; - ممنوع شده توسط ما * &#x60;8&#x60; - ناموفق در پرداخت * &#x60;9&#x60; - تأیید شده توسط فروشنده * &#x60;10&#x60; - ناموفق در تأیید توسط فروشنده * &#x60;11&#x60; - فروشگاه * &#x60;12&#x60; - لغو شده توسط فروشنده * &#x60;13&#x60; - درخواست بازگرداندن وجه به مشتری به دلیل درخواست مشتری * &#x60;14&#x60; - درخواست بازگرداندن وجه به فروشنده پس از ناموفقی در تأیید توسط فروشنده * &#x60;15&#x60; - درخواست بازگرداندن وجه به مشتری پس از ناموفقی توسط فروشنده * &#x60;16&#x60; - بازگردانده شده به فروشنده پس از لغو توسط فروشنده * &#x60;17&#x60; - بازگرداندن وجه تکمیل شد * &#x60;18&#x60; - زمان مجاز برای منقضی کردن گذشته است * &#x60;19&#x60; - تحویل نشده * &#x60;20&#x60; - مرسوله | 
**status_display** | **str** | وضعیت قابل‌خواندن | 

## Example

```python
from bwdk_sdk.models.merchant_order_cancel_shipment_response import MerchantOrderCancelShipmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantOrderCancelShipmentResponse from a JSON string
merchant_order_cancel_shipment_response_instance = MerchantOrderCancelShipmentResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantOrderCancelShipmentResponse.to_json())

# convert the object into a dict
merchant_order_cancel_shipment_response_dict = merchant_order_cancel_shipment_response_instance.to_dict()
# create an instance of MerchantOrderCancelShipmentResponse from a dict
merchant_order_cancel_shipment_response_from_dict = MerchantOrderCancelShipmentResponse.from_dict(merchant_order_cancel_shipment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


