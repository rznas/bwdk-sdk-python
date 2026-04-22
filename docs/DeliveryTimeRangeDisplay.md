# DeliveryTimeRangeDisplay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_date** | **str** |  | 
**max_date** | **str** |  | 

## Example

```python
from bwdk_sdk.models.delivery_time_range_display import DeliveryTimeRangeDisplay

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryTimeRangeDisplay from a JSON string
delivery_time_range_display_instance = DeliveryTimeRangeDisplay.from_json(json)
# print the JSON string representation of the object
print(DeliveryTimeRangeDisplay.to_json())

# convert the object into a dict
delivery_time_range_display_dict = delivery_time_range_display_instance.to_dict()
# create an instance of DeliveryTimeRangeDisplay from a dict
delivery_time_range_display_from_dict = DeliveryTimeRangeDisplay.from_dict(delivery_time_range_display_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


