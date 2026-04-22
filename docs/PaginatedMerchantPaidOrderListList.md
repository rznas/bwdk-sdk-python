# PaginatedMerchantPaidOrderListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[MerchantPaidOrderList]**](MerchantPaidOrderList.md) |  | 

## Example

```python
from bwdk_sdk.models.paginated_merchant_paid_order_list_list import PaginatedMerchantPaidOrderListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMerchantPaidOrderListList from a JSON string
paginated_merchant_paid_order_list_list_instance = PaginatedMerchantPaidOrderListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedMerchantPaidOrderListList.to_json())

# convert the object into a dict
paginated_merchant_paid_order_list_list_dict = paginated_merchant_paid_order_list_list_instance.to_dict()
# create an instance of PaginatedMerchantPaidOrderListList from a dict
paginated_merchant_paid_order_list_list_from_dict = PaginatedMerchantPaidOrderListList.from_dict(paginated_merchant_paid_order_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


