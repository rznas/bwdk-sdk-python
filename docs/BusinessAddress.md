# BusinessAddress

Serializer for BusinessAddress model. Used for merchant and shipping addresses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**address** | **str** |  | 
**postal_code** | **str** |  | [optional] 
**city_name** | **str** |  | 
**state_name** | **str** |  | 
**district_id** | **int** |  | [optional] 
**district_name** | **str** |  | [optional] 
**longitude** | **decimal.Decimal** |  | [optional] 
**latitude** | **decimal.Decimal** |  | [optional] 
**building_number** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**receiver_name** | **str** |  | [optional] 
**receiver_phone** | **str** |  | [optional] 
**is_accurate** | **bool** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**modified_at** | **datetime** |  | [readonly] 

## Example

```python
from bwdk_sdk.models.business_address import BusinessAddress

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessAddress from a JSON string
business_address_instance = BusinessAddress.from_json(json)
# print the JSON string representation of the object
print(BusinessAddress.to_json())

# convert the object into a dict
business_address_dict = business_address_instance.to_dict()
# create an instance of BusinessAddress from a dict
business_address_from_dict = BusinessAddress.from_dict(business_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


