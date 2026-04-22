# Packing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | نام روش/گزینه بسته‌بندی | 
**price** | **int** | هزینه بسته بندی به تومان | [optional] 

## Example

```python
from bwdk_sdk.models.packing import Packing

# TODO update the JSON string below
json = "{}"
# create an instance of Packing from a JSON string
packing_instance = Packing.from_json(json)
# print the JSON string representation of the object
print(Packing.to_json())

# convert the object into a dict
packing_dict = packing_instance.to_dict()
# create an instance of Packing from a dict
packing_from_dict = Packing.from_dict(packing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


