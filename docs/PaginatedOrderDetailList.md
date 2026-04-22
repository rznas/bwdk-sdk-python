# PaginatedOrderDetailList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[OrderDetail]**](OrderDetail.md) |  | 

## Example

```python
from bwdk_sdk.models.paginated_order_detail_list import PaginatedOrderDetailList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedOrderDetailList from a JSON string
paginated_order_detail_list_instance = PaginatedOrderDetailList.from_json(json)
# print the JSON string representation of the object
print(PaginatedOrderDetailList.to_json())

# convert the object into a dict
paginated_order_detail_list_dict = paginated_order_detail_list_instance.to_dict()
# create an instance of PaginatedOrderDetailList from a dict
paginated_order_detail_list_from_dict = PaginatedOrderDetailList.from_dict(paginated_order_detail_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


