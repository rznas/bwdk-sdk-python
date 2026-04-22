# MerchantOrderCancelShipmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Success message | 
**order_uuid** | **UUID** | Order unique identifier | 
**status** | [**OrderStatusEnum**](OrderStatusEnum.md) | Current order status  * &#x60;1&#x60; - اولیه * &#x60;2&#x60; - شروع شده * &#x60;3&#x60; - در انتظار * &#x60;4&#x60; - در انتظار درگاه * &#x60;5&#x60; - منقضی شده * &#x60;6&#x60; - لغو شده * &#x60;7&#x60; - پرداخت‌شده توسط کاربر * &#x60;8&#x60; - پرداخت موفیت آمیز نبود * &#x60;9&#x60; - تأیید شده توسط فروشگاه * &#x60;10&#x60; - تأیید توسط فروشگاه ناموفق بود * &#x60;11&#x60; - ناموفق از سوی فروشگاه * &#x60;12&#x60; - لغوشده توسط فروشگاه * &#x60;13&#x60; - درخواست بازگشت وجه به مشتری به دلیل درخواست مشتری * &#x60;14&#x60; - درخواست بازگشت وجه به فروشگاه پس از عدم تأیید توسط فروشگاه * &#x60;15&#x60; - درخواست بازگشت وجه به مشتری پس از ناموفق بودن توسط فروشگاه * &#x60;16&#x60; - بازپرداخت به فروشگاه پس از لغو توسط فروشگاه * &#x60;17&#x60; - بازپرداخت تکمیل شد * &#x60;18&#x60; - زمان انقضا گذشته است * &#x60;19&#x60; - تحویل شده * &#x60;20&#x60; - جمع اوری شده و در حال ارسال | 
**status_display** | **str** | Human-readable status | 

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


