# bwdk_sdk.MerchantWalletApi

All URIs are relative to *https://bwdk-backend.digify.shop*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wallets_api_v1_wallet_balance_retrieve**](MerchantWalletApi.md#wallets_api_v1_wallet_balance_retrieve) | **GET** /wallets/api/v1/wallet-balance/ | Get Wallet Balance


# **wallets_api_v1_wallet_balance_retrieve**
> WalletBalance wallets_api_v1_wallet_balance_retrieve()

Get Wallet Balance

<div dir="rtl" style="text-align: right;">

موجودی کیف پول فروشنده

## توضیحات

این endpoint موجودی کیف پول فروشنده را برمی‌گرداند. کیف پول برای پرداخت هزینه ارسال دیجی‌اکسپرس استفاده می‌شود. هنگام ثبت مرسوله دیجی‌اکسپرس، هزینه ارسال به‌صورت خودکار از کیف پول کسر می‌شود.

نیاز به **API_KEY** فروشنده دارد.

</div>


### Example

* Api Key Authentication (MerchantAPIKeyAuth):

```python
import bwdk_sdk
from bwdk_sdk.models.wallet_balance import WalletBalance
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
    api_instance = bwdk_sdk.MerchantWalletApi(api_client)

    try:
        # Get Wallet Balance
        api_response = api_instance.wallets_api_v1_wallet_balance_retrieve()
        print("The response of MerchantWalletApi->wallets_api_v1_wallet_balance_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantWalletApi->wallets_api_v1_wallet_balance_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WalletBalance**](WalletBalance.md)

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

