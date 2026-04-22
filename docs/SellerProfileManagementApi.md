# bwdk_sdk.SellerProfileManagementApi

All URIs are relative to *https://bwdk-backend.digify.shop*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merchant_api_v1_auth_status_retrieve**](SellerProfileManagementApi.md#merchant_api_v1_auth_status_retrieve) | **GET** /merchant/api/v1/auth/status/ | وضعیت لاگین بودن


# **merchant_api_v1_auth_status_retrieve**
> AuthStatusResponse merchant_api_v1_auth_status_retrieve()

وضعیت لاگین بودن

<div dir="rtl" style="text-align: right;">

بررسی وضعیت احراز هویت فروشنده

## توضیحات

این endpoint برای بررسی اعتبار **API_KEY** فروشنده استفاده می‌شود. اگر کلید معتبر باشد، پاسخ `is_authenticated: true` برمی‌گردد. از این endpoint برای تأیید صحت کلید API قبل از شروع عملیات استفاده کنید.

نیاز به **API_KEY** فروشنده دارد (فقط Header لازم است، بدنه درخواست ندارد).

</div>


### Example

* Api Key Authentication (MerchantAPIKeyAuth):

```python
import bwdk_sdk
from bwdk_sdk.models.auth_status_response import AuthStatusResponse
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
    api_instance = bwdk_sdk.SellerProfileManagementApi(api_client)

    try:
        # وضعیت لاگین بودن
        api_response = api_instance.merchant_api_v1_auth_status_retrieve()
        print("The response of SellerProfileManagementApi->merchant_api_v1_auth_status_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SellerProfileManagementApi->merchant_api_v1_auth_status_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthStatusResponse**](AuthStatusResponse.md)

### Authorization

[MerchantAPIKeyAuth](../README.md#MerchantAPIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

