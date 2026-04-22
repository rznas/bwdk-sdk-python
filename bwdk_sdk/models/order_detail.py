# coding: utf-8

"""
    BWDK API

    <div dir=\"rtl\" style=\"text-align: right;\">  # مستندات فروشندگان در سرویس خرید با دیجی‌کالا  این پلتفرم برای فروشندگان (مرچنت‌ها) جهت یکپارچه‌سازی خدمات پرداخت و تجارت الکترونیکی با سیستم خرید با دیجی‌کالا. شامل مدیریت سفارشات، ارسال، و احراز هویت فروشندگان است.   <div dir=\"rtl\" style=\"text-align: right;\">  <!-- ## توضیح وضعیت‌های سفارش  ### ۱. INITIAL — ایجاد اولیه سفارش  **معنا:** سفارش توسط بک‌اند مرچنت ساخته شده ولی هنوز هیچ کاربری به آن اختصاص داده نشده است.  **چگونه اتفاق می‌افتد:** مرچنت با ارسال درخواست `POST /api/v1/orders/create` و ارائه اطلاعات کالاها، مبلغ و `callback_url`، یک سفارش جدید ایجاد می‌کند. BWDK یک `order_uuid` منحصربه‌فرد و لینک شروع سفارش (`order_start_url`) برمی‌گرداند.  **وابستگی‌ها:** نیازی به کاربر یا پرداخت ندارد. فقط اطلاعات کالا از سمت مرچنت کافی است.  ---  ### ۲. STARTED — آغاز جریان خرید  **معنا:** مشتری روی لینک شروع سفارش کلیک کرده و وارد محیط BWDK شده است، اما هنوز لاگین نکرده.  **چگونه اتفاق می‌افتد:** وقتی مشتری به `order_start_url` هدایت می‌شود، BWDK وضعیت سفارش را از `INITIAL` به `STARTED` تغییر می‌دهد. در این مرحله فرآیند احراز هویت (SSO) آغاز می‌شود.  **وابستگی‌ها:** مشتری باید به لینک شروع هدایت شده باشد.  ---  ### ۳. PENDING — انتظار برای تکمیل سفارش  **معنا:** مشتری با موفقیت وارد سیستم شده و سفارش به حساب او اختصاص یافته. مشتری در حال انتخاب آدرس، روش ارسال، بسته‌بندی یا تخفیف است.  **چگونه اتفاق می‌افتد:** پس از تکمیل ورود به سیستم (SSO)، BWDK سفارش را به کاربر وصل کرده و وضعیت را به `PENDING` تغییر می‌دهد.  **وابستگی‌ها:** ورود موفق کاربر به سیستم (SSO). در این مرحله مشتری می‌تواند آدرس، شیپینگ، پکینگ و تخفیف را انتخاب کند.  ---  ### ۴. WAITING_FOR_GATEWAY — انتظار برای پرداخت  **معنا:** مشتری اطلاعات سفارش را تأیید کرده و به درگاه پرداخت هدایت شده است.  **چگونه اتفاق می‌افتد:** مشتری دکمه «پرداخت» را می‌زند (`POST /api/v1/orders/submit`)، سیستم یک رکورد پرداخت ایجاد می‌کند و کاربر به درگاه Digipay هدایت می‌شود. وضعیت سفارش به `WAITING_FOR_GATEWAY` تغییر می‌کند.  **وابستگی‌ها:** انتخاب آدرس، روش ارسال و بسته‌بندی الزامی است. پرداخت باید ایجاد شده باشد.  ---  ### ۷. PAID_BY_USER — پرداخت موفق  **معنا:** تراکنش پرداخت با موفقیت انجام شده و وجه از حساب مشتری کسر شده است.  **چگونه اتفاق می‌افتد:** درگاه پرداخت نتیجه موفق را به BWDK اطلاع می‌دهد. سیستم پرداخت را تأیید و وضعیت سفارش را به `PAID_BY_USER` تغییر می‌دهد. در این لحظه مشتری به `callback_url` مرچنت هدایت می‌شود.  **وابستگی‌ها:** تأیید موفق تراکنش از سوی درگاه پرداخت (Digipay).  ---  ### ۹. VERIFIED_BY_MERCHANT — تأیید توسط مرچنت  **معنا:** مرچنت سفارش را بررسی کرده و موجودی کالا و صحت اطلاعات را تأیید نموده است. سفارش آماده ارسال است.  **چگونه اتفاق می‌افتد:** مرچنت با ارسال درخواست `POST /api/v1/orders/manager/{uuid}/verify` سفارش را تأیید می‌کند. این مرحله **اجباری** است و باید پس از پرداخت موفق انجام شود.  **وابستگی‌ها:** سفارش باید در وضعیت `PAID_BY_USER` باشد. مرچنت باید موجودی کالا را بررسی کند.  ---  ### ۲۰. SHIPPED — ارسال شد  **معنا:** سفارش از انبار خارج شده و در حال ارسال به مشتری است.  **چگونه اتفاق می‌افتد:** مرچنت پس از ارسال کالا، وضعیت سفارش را از طریق API به `SHIPPED` تغییر می‌دهد.  **وابستگی‌ها:** سفارش باید در وضعیت `VERIFIED_BY_MERCHANT` باشد.  ---  ### ۱۹. DELIVERED — تحویل داده شد  **معنا:** سفارش به دست مشتری رسیده و فرآیند خرید به پایان رسیده است.  **چگونه اتفاق می‌افتد:** مرچنت پس از تحویل موفق، وضعیت را به `DELIVERED` تغییر می‌دهد.  **وابستگی‌ها:** سفارش باید در وضعیت `SHIPPED` باشد.  ---  ### ۵. EXPIRED — منقضی شد  **معنا:** زمان رزرو سفارش به پایان رسیده و سفارش به صورت خودکار لغو شده است.  **چگونه اتفاق می‌افتد:** یک Task دوره‌ای به طور خودکار سفارش‌هایی که `reservation_expired_at` آن‌ها گذشته را پیدا کرده و وضعیتشان را به `EXPIRED` تغییر می‌دهد. این مکانیزم مانع بلوکه شدن موجودی کالا می‌شود.  **وابستگی‌ها:** سفارش باید در یکی از وضعیت‌های `INITIAL`، `STARTED`، `PENDING` یا `WAITING_FOR_GATEWAY` باشد و زمان رزرو آن گذشته باشد.  ---  ### ۱۸. EXPIRATION_TIME_EXCEEDED — زمان انقضا گذشت  **معنا:** در لحظه ثبت نهایی یا پرداخت، مشخص شد که زمان مجاز سفارش تمام شده است.  **چگونه اتفاق می‌افتد:** هنگام ارسال درخواست پرداخت (`submit_order`)، سیستم بررسی می‌کند که `expiration_time` سفارش هنوز معتبر است یا خیر. در صورت گذشتن زمان، وضعیت به `EXPIRATION_TIME_EXCEEDED` تغییر می‌کند.  **وابستگی‌ها:** سفارش در وضعیت `PENDING` یا `WAITING_FOR_GATEWAY` است و فیلد `expiration_time` سپری شده.  ---  ### ۶. CANCELLED — لغو توسط مشتری  **معنا:** مشتری در حین فرآیند خرید (قبل از پرداخت) سفارش را لغو کرده یا از صفحه خارج شده است.  **چگونه اتفاق می‌افتد:** مشتری در صفحه checkout دکمه «انصراف» را می‌زند یا پرداخت ناموفق بوده و سفارش به حالت لغو درمی‌آید.  **وابستگی‌ها:** سفارش باید در وضعیت `PENDING` یا `WAITING_FOR_GATEWAY` باشد. پرداختی انجام نشده است.  ---  ### ۸. FAILED_TO_PAY — پرداخت ناموفق  **معنا:** تراکنش پرداخت انجام نشد یا با خطا مواجه شد.  **چگونه اتفاق می‌افتد:** درگاه پرداخت نتیجه ناموفق برمی‌گرداند یا فرآیند بازگشت وجه در مرحله پرداخت با شکست مواجه می‌شود.  **وابستگی‌ها:** سفارش باید در وضعیت `WAITING_FOR_GATEWAY` بوده باشد.  ---  ### ۱۰. FAILED_TO_VERIFY_BY_MERCHANT — تأیید ناموفق توسط مرچنت  **معنا:** مرچنت سفارش را رد کرده است؛ معمولاً به دلیل ناموجود بودن کالا یا مغایرت اطلاعات.  **چگونه اتفاق می‌افتد:** مرچنت در پاسخ به درخواست verify، خطا برمی‌گرداند یا API آن وضعیت ناموفق تنظیم می‌کند. پس از این وضعیت، فرآیند استرداد وجه آغاز می‌شود.  **وابستگی‌ها:** سفارش باید در وضعیت `PAID_BY_USER` باشد.  ---  ### ۱۱. FAILED_BY_MERCHANT — خطا از سمت مرچنت  **معنا:** مرچنت پس از تأیید اولیه، اعلام می‌کند که قادر به انجام سفارش نیست (مثلاً به دلیل اتمام موجودی).  **چگونه اتفاق می‌افتد:** مرچنت وضعیت را به `FAILED_BY_MERCHANT` تغییر می‌دهد. وجه پرداختی مشتری مسترد خواهد شد.  **وابستگی‌ها:** سفارش باید در وضعیت `PAID_BY_USER` باشد.  ---  ### ۱۲. CANCELLED_BY_MERCHANT — لغو توسط مرچنت  **معنا:** مرچنت پس از پرداخت، سفارش را به هر دلیلی لغو کرده است.  **چگونه اتفاق می‌افتد:** مرچنت درخواست لغو سفارش را ارسال می‌کند. وجه پرداختی مشتری به او بازگردانده می‌شود.  **وابستگی‌ها:** سفارش باید در وضعیت `PAID_BY_USER` یا `VERIFIED_BY_MERCHANT` باشد.  ---  ### ۱۳. REQUEST_TO_REFUND — درخواست استرداد توسط مشتری  **معنا:** مشتری درخواست بازگشت وجه داده و سیستم در حال پردازش استرداد است.  **چگونه اتفاق می‌افتد:** مرچنت از طریق API درخواست استرداد را ثبت می‌کند (`POST /api/v1/orders/manager/{uuid}/refund`). سفارش وارد صف پردازش استرداد می‌شود.  **وابستگی‌ها:** سفارش باید در وضعیت `PAID_BY_USER` یا `VERIFIED_BY_MERCHANT` باشد.  ---  ### ۱۴، ۱۵، ۱۶. سایر وضعیت‌های درخواست استرداد  این وضعیت‌ها بر اساس دلیل استرداد از هم تفکیک می‌شوند:  - **۱۴ — REQUEST_TO_REFUND_TO_MERCHANT_AFTER_FAILED_TO_VERIFY:** استرداد پس از ناموفق بودن تأیید مرچنت؛ وجه به حساب مرچنت بازمی‌گردد. - **۱۵ — REQUEST_TO_REFUND_TO_CUSTOMER_AFTER_FAILED_BY_MERCHANT:** استرداد پس از خطای مرچنت؛ وجه به مشتری بازمی‌گردد. - **۱۶ — REQUEST_TO_REFUND_TO_MERCHANT_AFTER_CANCELLED_BY_MERCHANT:** استرداد پس از لغو توسط مرچنت؛ وجه به حساب مرچنت برمی‌گردد.  **چگونه اتفاق می‌افتد:** به صورت خودکار پس از رسیدن به وضعیت‌های ناموفق/لغو مربوطه توسط سیستم تنظیم می‌شود.  ---  ### ۱۷. REFUND_COMPLETED — استرداد تکمیل شد  **معنا:** وجه با موفقیت به صاحب آن (مشتری یا مرچنت بسته به نوع استرداد) بازگردانده شده است.  **چگونه اتفاق می‌افتد:** Task پردازش استرداد (`process_order_refund`) پس از تأیید موفق بازگشت وجه از سوی Digipay، وضعیت سفارش را به `REFUND_COMPLETED` تغییر می‌دهد.  **وابستگی‌ها:** یکی از وضعیت‌های درخواست استرداد (۱۳، ۱۴، ۱۵ یا ۱۶) باید فعال باشد و Digipay تراکنش استرداد را تأیید کرده باشد.  --> </div> 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from uuid import UUID
from bwdk_sdk.models.merchant import Merchant
from bwdk_sdk.models.order_item_create import OrderItemCreate
from bwdk_sdk.models.order_status_enum import OrderStatusEnum
from bwdk_sdk.models.order_user import OrderUser
from bwdk_sdk.models.packing import Packing
from bwdk_sdk.models.payment_order import PaymentOrder
from bwdk_sdk.models.shipping_method import ShippingMethod
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class OrderDetail(BaseModel):
    """
    OrderDetail
    """ # noqa: E501
    id: StrictInt
    created_at: datetime
    order_uuid: UUID
    reservation_expired_at: Optional[StrictInt] = Field(description="Unix timestamp تا زمانی که سفارش برای پرداخت رزرو شده است")
    merchant_order_id: StrictStr = Field(description="شناسه منحصر به فرد سفارش در سیستم فروشنده")
    status: OrderStatusEnum
    status_display: StrictStr
    main_amount: StrictInt = Field(description="مجموع قیمت اولیه تمام کالاهای سفارش بدون تخفیف (به تومان)")
    final_amount: StrictInt = Field(description="قیمت نهایی قابل پرداخت توسط مشتری: مبلغ_اصلی - مبلغ_تخفیف + مبلغ_مالیات (به تومان)")
    total_paid_amount: StrictInt = Field(description="مبلغ کل پرداخت شده توسط کاربر: مبلغ_نهایی + هزینه_ارسال (به تومان)")
    discount_amount: StrictInt = Field(description="مبلغ کل تخفیف اعمال شده بر سفارش (به تومان)")
    tax_amount: StrictInt = Field(description="مبلغ کل مالیات برای سفارش (به تومان)")
    shipping_amount: StrictInt = Field(description="هزینه ارسال برای سفارش (به تومان)")
    loyalty_amount: StrictInt = Field(description="مقدار تخفیف از برنامه باشگاه مشتریان/پاداش (به تومان)")
    callback_url: StrictStr = Field(description="آدرسی برای دریافت اطلاع رسانی وضعیت پرداخت پس از تکمیل سفارش")
    merchant: Merchant
    items: List[OrderItemCreate]
    source_address: Optional[Any]
    destination_address: Optional[Any]
    selected_shipping_method: ShippingMethod
    shipping_selected_at: Optional[datetime]
    address_selected_at: Optional[datetime]
    packing_amount: StrictInt = Field(description="هزینه روش بسته‌بندی انتخاب‌شده (به تومان)")
    packing_selected_at: Optional[datetime]
    selected_packing: Packing
    can_select_packing: StrictBool
    can_select_shipping: StrictBool
    can_select_address: StrictBool
    can_proceed_to_payment: StrictBool
    is_paid: StrictBool
    user: OrderUser
    payment: PaymentOrder
    preparation_time: StrictInt = Field(description="Preparation time for the order (in days)")
    weight: Union[StrictFloat, StrictInt] = Field(description="Total weight of the order (in grams)")
    selected_shipping_data: Dict[str, Any]
    reference_code: StrictStr = Field(description="کد مرجع یکتا برای پیگیری سفارش مشتری (قالب: BD-XXXXXXXX)")
    promotion_discount_amount: Union[StrictFloat, StrictInt]
    promotion_data: Dict[str, Any]
    digipay_markup_amount: StrictInt = Field(description="Markup amount for the order (in Tomans)")
    markup_commission_percentage: StrictInt = Field(description="Markup commission percentage for the order (in percent)")
    previous_status: Optional[OrderStatusEnum]
    previous_status_display: StrictStr
    __properties: ClassVar[List[str]] = ["id", "created_at", "order_uuid", "reservation_expired_at", "merchant_order_id", "status", "status_display", "main_amount", "final_amount", "total_paid_amount", "discount_amount", "tax_amount", "shipping_amount", "loyalty_amount", "callback_url", "merchant", "items", "source_address", "destination_address", "selected_shipping_method", "shipping_selected_at", "address_selected_at", "packing_amount", "packing_selected_at", "selected_packing", "can_select_packing", "can_select_shipping", "can_select_address", "can_proceed_to_payment", "is_paid", "user", "payment", "preparation_time", "weight", "selected_shipping_data", "reference_code", "promotion_discount_amount", "promotion_data", "digipay_markup_amount", "markup_commission_percentage", "previous_status", "previous_status_display"]

    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(to_jsonable_python(self.to_dict()))

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OrderDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "created_at",
            "order_uuid",
            "reservation_expired_at",
            "merchant_order_id",
            "status",
            "status_display",
            "main_amount",
            "final_amount",
            "total_paid_amount",
            "discount_amount",
            "tax_amount",
            "shipping_amount",
            "loyalty_amount",
            "callback_url",
            "source_address",
            "destination_address",
            "selected_shipping_method",
            "shipping_selected_at",
            "address_selected_at",
            "packing_amount",
            "packing_selected_at",
            "selected_packing",
            "can_select_packing",
            "can_select_shipping",
            "can_select_address",
            "can_proceed_to_payment",
            "is_paid",
            "user",
            "payment",
            "preparation_time",
            "weight",
            "selected_shipping_data",
            "reference_code",
            "promotion_discount_amount",
            "promotion_data",
            "digipay_markup_amount",
            "markup_commission_percentage",
            "previous_status",
            "previous_status_display",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of merchant
        if self.merchant:
            _dict['merchant'] = self.merchant.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item_items in self.items:
                if _item_items:
                    _items.append(_item_items.to_dict())
            _dict['items'] = _items
        # override the default output from pydantic by calling `to_dict()` of selected_shipping_method
        if self.selected_shipping_method:
            _dict['selected_shipping_method'] = self.selected_shipping_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of selected_packing
        if self.selected_packing:
            _dict['selected_packing'] = self.selected_packing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment
        if self.payment:
            _dict['payment'] = self.payment.to_dict()
        # set to None if reservation_expired_at (nullable) is None
        # and model_fields_set contains the field
        if self.reservation_expired_at is None and "reservation_expired_at" in self.model_fields_set:
            _dict['reservation_expired_at'] = None

        # set to None if source_address (nullable) is None
        # and model_fields_set contains the field
        if self.source_address is None and "source_address" in self.model_fields_set:
            _dict['source_address'] = None

        # set to None if destination_address (nullable) is None
        # and model_fields_set contains the field
        if self.destination_address is None and "destination_address" in self.model_fields_set:
            _dict['destination_address'] = None

        # set to None if shipping_selected_at (nullable) is None
        # and model_fields_set contains the field
        if self.shipping_selected_at is None and "shipping_selected_at" in self.model_fields_set:
            _dict['shipping_selected_at'] = None

        # set to None if address_selected_at (nullable) is None
        # and model_fields_set contains the field
        if self.address_selected_at is None and "address_selected_at" in self.model_fields_set:
            _dict['address_selected_at'] = None

        # set to None if packing_selected_at (nullable) is None
        # and model_fields_set contains the field
        if self.packing_selected_at is None and "packing_selected_at" in self.model_fields_set:
            _dict['packing_selected_at'] = None

        # set to None if previous_status (nullable) is None
        # and model_fields_set contains the field
        if self.previous_status is None and "previous_status" in self.model_fields_set:
            _dict['previous_status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "order_uuid": obj.get("order_uuid"),
            "reservation_expired_at": obj.get("reservation_expired_at"),
            "merchant_order_id": obj.get("merchant_order_id"),
            "status": obj.get("status"),
            "status_display": obj.get("status_display"),
            "main_amount": obj.get("main_amount"),
            "final_amount": obj.get("final_amount"),
            "total_paid_amount": obj.get("total_paid_amount"),
            "discount_amount": obj.get("discount_amount"),
            "tax_amount": obj.get("tax_amount"),
            "shipping_amount": obj.get("shipping_amount"),
            "loyalty_amount": obj.get("loyalty_amount"),
            "callback_url": obj.get("callback_url"),
            "merchant": Merchant.from_dict(obj["merchant"]) if obj.get("merchant") is not None else None,
            "items": [OrderItemCreate.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "source_address": obj.get("source_address"),
            "destination_address": obj.get("destination_address"),
            "selected_shipping_method": ShippingMethod.from_dict(obj["selected_shipping_method"]) if obj.get("selected_shipping_method") is not None else None,
            "shipping_selected_at": obj.get("shipping_selected_at"),
            "address_selected_at": obj.get("address_selected_at"),
            "packing_amount": obj.get("packing_amount"),
            "packing_selected_at": obj.get("packing_selected_at"),
            "selected_packing": Packing.from_dict(obj["selected_packing"]) if obj.get("selected_packing") is not None else None,
            "can_select_packing": obj.get("can_select_packing"),
            "can_select_shipping": obj.get("can_select_shipping"),
            "can_select_address": obj.get("can_select_address"),
            "can_proceed_to_payment": obj.get("can_proceed_to_payment"),
            "is_paid": obj.get("is_paid"),
            "user": OrderUser.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "payment": PaymentOrder.from_dict(obj["payment"]) if obj.get("payment") is not None else None,
            "preparation_time": obj.get("preparation_time"),
            "weight": obj.get("weight"),
            "selected_shipping_data": obj.get("selected_shipping_data"),
            "reference_code": obj.get("reference_code"),
            "promotion_discount_amount": obj.get("promotion_discount_amount"),
            "promotion_data": obj.get("promotion_data"),
            "digipay_markup_amount": obj.get("digipay_markup_amount"),
            "markup_commission_percentage": obj.get("markup_commission_percentage"),
            "previous_status": obj.get("previous_status"),
            "previous_status_display": obj.get("previous_status_display")
        })
        return _obj


