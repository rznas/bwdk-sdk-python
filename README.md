# bwdk-sdk
<div dir=\"rtl\" style=\"text-align: right;\">

# مستندات فروشندگان در سرویس خرید با دیجی‌کالا

این پلتفرم برای فروشندگان (مرچنت‌ها) جهت یکپارچه‌سازی خدمات پرداخت و تجارت الکترونیکی با سیستم خرید با دیجی‌کالا.
شامل مدیریت سفارشات، ارسال، و احراز هویت فروشندگان است.


<div dir=\"rtl\" style=\"text-align: right;\">

<!-- ## توضیح وضعیت‌های سفارش

### ۱. INITIAL — ایجاد اولیه سفارش

**معنا:** سفارش توسط بک‌اند مرچنت ساخته شده ولی هنوز هیچ کاربری به آن اختصاص داده نشده است.

**چگونه اتفاق می‌افتد:** مرچنت با ارسال درخواست `POST /api/v1/orders/create` و ارائه اطلاعات کالاها، مبلغ و `callback_url`، یک سفارش جدید ایجاد می‌کند. BWDK یک `order_uuid` منحصربه‌فرد و لینک شروع سفارش (`order_start_url`) برمی‌گرداند.

**وابستگی‌ها:** نیازی به کاربر یا پرداخت ندارد. فقط اطلاعات کالا از سمت مرچنت کافی است.

---

### ۲. STARTED — آغاز جریان خرید

**معنا:** مشتری روی لینک شروع سفارش کلیک کرده و وارد محیط BWDK شده است، اما هنوز لاگین نکرده.

**چگونه اتفاق می‌افتد:** وقتی مشتری به `order_start_url` هدایت می‌شود، BWDK وضعیت سفارش را از `INITIAL` به `STARTED` تغییر می‌دهد. در این مرحله فرآیند احراز هویت (SSO) آغاز می‌شود.

**وابستگی‌ها:** مشتری باید به لینک شروع هدایت شده باشد.

---

### ۳. PENDING — انتظار برای تکمیل سفارش

**معنا:** مشتری با موفقیت وارد سیستم شده و سفارش به حساب او اختصاص یافته. مشتری در حال انتخاب آدرس، روش ارسال، بسته‌بندی یا تخفیف است.

**چگونه اتفاق می‌افتد:** پس از تکمیل ورود به سیستم (SSO)، BWDK سفارش را به کاربر وصل کرده و وضعیت را به `PENDING` تغییر می‌دهد.

**وابستگی‌ها:** ورود موفق کاربر به سیستم (SSO). در این مرحله مشتری می‌تواند آدرس، شیپینگ، پکینگ و تخفیف را انتخاب کند.

---

### ۴. WAITING_FOR_GATEWAY — انتظار برای پرداخت

**معنا:** مشتری اطلاعات سفارش را تأیید کرده و به درگاه پرداخت هدایت شده است.

**چگونه اتفاق می‌افتد:** مشتری دکمه «پرداخت» را می‌زند (`POST /api/v1/orders/submit`)، سیستم یک رکورد پرداخت ایجاد می‌کند و کاربر به درگاه Digipay هدایت می‌شود. وضعیت سفارش به `WAITING_FOR_GATEWAY` تغییر می‌کند.

**وابستگی‌ها:** انتخاب آدرس، روش ارسال و بسته‌بندی الزامی است. پرداخت باید ایجاد شده باشد.

---

### ۷. PAID_BY_USER — پرداخت موفق

**معنا:** تراکنش پرداخت با موفقیت انجام شده و وجه از حساب مشتری کسر شده است.

**چگونه اتفاق می‌افتد:** درگاه پرداخت نتیجه موفق را به BWDK اطلاع می‌دهد. سیستم پرداخت را تأیید و وضعیت سفارش را به `PAID_BY_USER` تغییر می‌دهد. در این لحظه مشتری به `callback_url` مرچنت هدایت می‌شود.

**وابستگی‌ها:** تأیید موفق تراکنش از سوی درگاه پرداخت (Digipay).

---

### ۹. VERIFIED_BY_MERCHANT — تأیید توسط مرچنت

**معنا:** مرچنت سفارش را بررسی کرده و موجودی کالا و صحت اطلاعات را تأیید نموده است. سفارش آماده ارسال است.

**چگونه اتفاق می‌افتد:** مرچنت با ارسال درخواست `POST /api/v1/orders/manager/{uuid}/verify` سفارش را تأیید می‌کند. این مرحله **اجباری** است و باید پس از پرداخت موفق انجام شود.

**وابستگی‌ها:** سفارش باید در وضعیت `PAID_BY_USER` باشد. مرچنت باید موجودی کالا را بررسی کند.

---

### ۲۰. SHIPPED — ارسال شد

**معنا:** سفارش از انبار خارج شده و در حال ارسال به مشتری است.

**چگونه اتفاق می‌افتد:** مرچنت پس از ارسال کالا، وضعیت سفارش را از طریق API به `SHIPPED` تغییر می‌دهد.

**وابستگی‌ها:** سفارش باید در وضعیت `VERIFIED_BY_MERCHANT` باشد.

---

### ۱۹. DELIVERED — تحویل داده شد

**معنا:** سفارش به دست مشتری رسیده و فرآیند خرید به پایان رسیده است.

**چگونه اتفاق می‌افتد:** مرچنت پس از تحویل موفق، وضعیت را به `DELIVERED` تغییر می‌دهد.

**وابستگی‌ها:** سفارش باید در وضعیت `SHIPPED` باشد.

---

### ۵. EXPIRED — منقضی شد

**معنا:** زمان رزرو سفارش به پایان رسیده و سفارش به صورت خودکار لغو شده است.

**چگونه اتفاق می‌افتد:** یک Task دوره‌ای به طور خودکار سفارش‌هایی که `reservation_expired_at` آن‌ها گذشته را پیدا کرده و وضعیتشان را به `EXPIRED` تغییر می‌دهد. این مکانیزم مانع بلوکه شدن موجودی کالا می‌شود.

**وابستگی‌ها:** سفارش باید در یکی از وضعیت‌های `INITIAL`، `STARTED`، `PENDING` یا `WAITING_FOR_GATEWAY` باشد و زمان رزرو آن گذشته باشد.

---

### ۱۸. EXPIRATION_TIME_EXCEEDED — زمان انقضا گذشت

**معنا:** در لحظه ثبت نهایی یا پرداخت، مشخص شد که زمان مجاز سفارش تمام شده است.

**چگونه اتفاق می‌افتد:** هنگام ارسال درخواست پرداخت (`submit_order`)، سیستم بررسی می‌کند که `expiration_time` سفارش هنوز معتبر است یا خیر. در صورت گذشتن زمان، وضعیت به `EXPIRATION_TIME_EXCEEDED` تغییر می‌کند.

**وابستگی‌ها:** سفارش در وضعیت `PENDING` یا `WAITING_FOR_GATEWAY` است و فیلد `expiration_time` سپری شده.

---

### ۶. CANCELLED — لغو توسط مشتری

**معنا:** مشتری در حین فرآیند خرید (قبل از پرداخت) سفارش را لغو کرده یا از صفحه خارج شده است.

**چگونه اتفاق می‌افتد:** مشتری در صفحه checkout دکمه «انصراف» را می‌زند یا پرداخت ناموفق بوده و سفارش به حالت لغو درمی‌آید.

**وابستگی‌ها:** سفارش باید در وضعیت `PENDING` یا `WAITING_FOR_GATEWAY` باشد. پرداختی انجام نشده است.

---

### ۸. FAILED_TO_PAY — پرداخت ناموفق

**معنا:** تراکنش پرداخت انجام نشد یا با خطا مواجه شد.

**چگونه اتفاق می‌افتد:** درگاه پرداخت نتیجه ناموفق برمی‌گرداند یا فرآیند بازگشت وجه در مرحله پرداخت با شکست مواجه می‌شود.

**وابستگی‌ها:** سفارش باید در وضعیت `WAITING_FOR_GATEWAY` بوده باشد.

---

### ۱۰. FAILED_TO_VERIFY_BY_MERCHANT — تأیید ناموفق توسط مرچنت

**معنا:** مرچنت سفارش را رد کرده است؛ معمولاً به دلیل ناموجود بودن کالا یا مغایرت اطلاعات.

**چگونه اتفاق می‌افتد:** مرچنت در پاسخ به درخواست verify، خطا برمی‌گرداند یا API آن وضعیت ناموفق تنظیم می‌کند. پس از این وضعیت، فرآیند استرداد وجه آغاز می‌شود.

**وابستگی‌ها:** سفارش باید در وضعیت `PAID_BY_USER` باشد.

---

### ۱۱. FAILED_BY_MERCHANT — خطا از سمت مرچنت

**معنا:** مرچنت پس از تأیید اولیه، اعلام می‌کند که قادر به انجام سفارش نیست (مثلاً به دلیل اتمام موجودی).

**چگونه اتفاق می‌افتد:** مرچنت وضعیت را به `FAILED_BY_MERCHANT` تغییر می‌دهد. وجه پرداختی مشتری مسترد خواهد شد.

**وابستگی‌ها:** سفارش باید در وضعیت `PAID_BY_USER` باشد.

---

### ۱۲. CANCELLED_BY_MERCHANT — لغو توسط مرچنت

**معنا:** مرچنت پس از پرداخت، سفارش را به هر دلیلی لغو کرده است.

**چگونه اتفاق می‌افتد:** مرچنت درخواست لغو سفارش را ارسال می‌کند. وجه پرداختی مشتری به او بازگردانده می‌شود.

**وابستگی‌ها:** سفارش باید در وضعیت `PAID_BY_USER` یا `VERIFIED_BY_MERCHANT` باشد.

---

### ۱۳. REQUEST_TO_REFUND — درخواست استرداد توسط مشتری

**معنا:** مشتری درخواست بازگشت وجه داده و سیستم در حال پردازش استرداد است.

**چگونه اتفاق می‌افتد:** مرچنت از طریق API درخواست استرداد را ثبت می‌کند (`POST /api/v1/orders/manager/{uuid}/refund`). سفارش وارد صف پردازش استرداد می‌شود.

**وابستگی‌ها:** سفارش باید در وضعیت `PAID_BY_USER` یا `VERIFIED_BY_MERCHANT` باشد.

---

### ۱۴، ۱۵، ۱۶. سایر وضعیت‌های درخواست استرداد

این وضعیت‌ها بر اساس دلیل استرداد از هم تفکیک می‌شوند:

- **۱۴ — REQUEST_TO_REFUND_TO_MERCHANT_AFTER_FAILED_TO_VERIFY:** استرداد پس از ناموفق بودن تأیید مرچنت؛ وجه به حساب مرچنت بازمی‌گردد.
- **۱۵ — REQUEST_TO_REFUND_TO_CUSTOMER_AFTER_FAILED_BY_MERCHANT:** استرداد پس از خطای مرچنت؛ وجه به مشتری بازمی‌گردد.
- **۱۶ — REQUEST_TO_REFUND_TO_MERCHANT_AFTER_CANCELLED_BY_MERCHANT:** استرداد پس از لغو توسط مرچنت؛ وجه به حساب مرچنت برمی‌گردد.

**چگونه اتفاق می‌افتد:** به صورت خودکار پس از رسیدن به وضعیت‌های ناموفق/لغو مربوطه توسط سیستم تنظیم می‌شود.

---

### ۱۷. REFUND_COMPLETED — استرداد تکمیل شد

**معنا:** وجه با موفقیت به صاحب آن (مشتری یا مرچنت بسته به نوع استرداد) بازگردانده شده است.

**چگونه اتفاق می‌افتد:** Task پردازش استرداد (`process_order_refund`) پس از تأیید موفق بازگشت وجه از سوی Digipay، وضعیت سفارش را به `REFUND_COMPLETED` تغییر می‌دهد.

**وابستگی‌ها:** یکی از وضعیت‌های درخواست استرداد (۱۳، ۱۴، ۱۵ یا ۱۶) باید فعال باشد و Digipay تراکنش استرداد را تأیید کرده باشد.
 -->
</div>


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.3
- Generator version: 7.21.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import bwdk_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import bwdk_sdk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import bwdk_sdk
from bwdk_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://bwdk-backend.digify.shop
# See configuration.py for a list of all supported configuration parameters.
configuration = bwdk_sdk.Configuration(
    host = "https://bwdk-backend.digify.shop"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: MerchantAPIKeyAuth
configuration.api_key['MerchantAPIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['MerchantAPIKeyAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with bwdk_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bwdk_sdk.MerchantOrdersApi(api_client)
    order_create = bwdk_sdk.OrderCreate() # OrderCreate | 

    try:
        # ساخت سفارش
        api_response = api_instance.order_api_v1_create_order_create(order_create)
        print("The response of MerchantOrdersApi->order_api_v1_create_order_create:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MerchantOrdersApi->order_api_v1_create_order_create: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://bwdk-backend.digify.shop*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*MerchantOrdersApi* | [**order_api_v1_create_order_create**](docs/MerchantOrdersApi.md#order_api_v1_create_order_create) | **POST** /order/api/v1/create-order/ | ساخت سفارش
*MerchantOrdersApi* | [**order_api_v1_manager_list**](docs/MerchantOrdersApi.md#order_api_v1_manager_list) | **GET** /order/api/v1/manager/ | لیست سفارشات
*MerchantOrdersApi* | [**order_api_v1_manager_paid_list**](docs/MerchantOrdersApi.md#order_api_v1_manager_paid_list) | **GET** /order/api/v1/manager/paid/ | سفارش پرداخت‌شده و تایید‌نشده
*MerchantOrdersApi* | [**order_api_v1_manager_refund_create**](docs/MerchantOrdersApi.md#order_api_v1_manager_refund_create) | **POST** /order/api/v1/manager/{order_uuid}/refund/ | بازگشت سفارش
*MerchantOrdersApi* | [**order_api_v1_manager_retrieve**](docs/MerchantOrdersApi.md#order_api_v1_manager_retrieve) | **GET** /order/api/v1/manager/{order_uuid}/ | دریافت سفارش
*MerchantOrdersApi* | [**order_api_v1_manager_update_status_update**](docs/MerchantOrdersApi.md#order_api_v1_manager_update_status_update) | **PUT** /order/api/v1/manager/{order_uuid}/update-status/ | Update Order Status
*MerchantOrdersApi* | [**order_api_v1_manager_verify_create**](docs/MerchantOrdersApi.md#order_api_v1_manager_verify_create) | **POST** /order/api/v1/manager/{order_uuid}/verify/ | تایید سفارش
*MerchantWalletApi* | [**wallets_api_v1_wallet_balance_retrieve**](docs/MerchantWalletApi.md#wallets_api_v1_wallet_balance_retrieve) | **GET** /wallets/api/v1/wallet-balance/ | Get Wallet Balance
*OrderShippingApi* | [**order_api_v1_manager_cancel_shipment_create**](docs/OrderShippingApi.md#order_api_v1_manager_cancel_shipment_create) | **POST** /order/api/v1/manager/{order_uuid}/cancel-shipment/ | Cancel Shipment
*OrderShippingApi* | [**order_api_v1_manager_change_shipping_method_update**](docs/OrderShippingApi.md#order_api_v1_manager_change_shipping_method_update) | **PUT** /order/api/v1/manager/{order_uuid}/change-shipping-method/ | Change Shipping Method
*OrderShippingApi* | [**order_api_v1_manager_revive_shipment_create**](docs/OrderShippingApi.md#order_api_v1_manager_revive_shipment_create) | **POST** /order/api/v1/manager/{order_uuid}/revive-shipment/ | Revive Shipment
*SellerProfileManagementApi* | [**merchant_api_v1_auth_status_retrieve**](docs/SellerProfileManagementApi.md#merchant_api_v1_auth_status_retrieve) | **GET** /merchant/api/v1/auth/status/ | وضعیت لاگین بودن


## Documentation For Models

 - [AuthStatusResponse](docs/AuthStatusResponse.md)
 - [BusinessAddress](docs/BusinessAddress.md)
 - [DeliveryTimeRangeDisplay](docs/DeliveryTimeRangeDisplay.md)
 - [ErrorEnum](docs/ErrorEnum.md)
 - [GatewayTypeEnum](docs/GatewayTypeEnum.md)
 - [Merchant](docs/Merchant.md)
 - [MerchantOrderCancelShipmentResponse](docs/MerchantOrderCancelShipmentResponse.md)
 - [MerchantOrderRefundResponse](docs/MerchantOrderRefundResponse.md)
 - [MerchantOrderReviveShipmentResponse](docs/MerchantOrderReviveShipmentResponse.md)
 - [MerchantPaidOrderList](docs/MerchantPaidOrderList.md)
 - [NullEnum](docs/NullEnum.md)
 - [Option](docs/Option.md)
 - [OrderCreate](docs/OrderCreate.md)
 - [OrderCreateResponse](docs/OrderCreateResponse.md)
 - [OrderDetail](docs/OrderDetail.md)
 - [OrderError](docs/OrderError.md)
 - [OrderItemCreate](docs/OrderItemCreate.md)
 - [OrderStatusEnum](docs/OrderStatusEnum.md)
 - [OrderUser](docs/OrderUser.md)
 - [Packing](docs/Packing.md)
 - [PaginatedMerchantPaidOrderListList](docs/PaginatedMerchantPaidOrderListList.md)
 - [PaginatedOrderDetailList](docs/PaginatedOrderDetailList.md)
 - [PaymentOrder](docs/PaymentOrder.md)
 - [RefundOrder](docs/RefundOrder.md)
 - [ReviveShipment](docs/ReviveShipment.md)
 - [ShippingMethod](docs/ShippingMethod.md)
 - [ShippingTypeEnum](docs/ShippingTypeEnum.md)
 - [TypeNameEnum](docs/TypeNameEnum.md)
 - [UpdateOrderStatus](docs/UpdateOrderStatus.md)
 - [VerifyOrder](docs/VerifyOrder.md)
 - [WalletBalance](docs/WalletBalance.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="MerchantAPIKeyAuth"></a>
### MerchantAPIKeyAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




