# ReviveShipment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preparation_time** | **int** | The preparation time for the order in days. | [optional] 

## Example

```python
from bwdk_sdk.models.revive_shipment import ReviveShipment

# TODO update the JSON string below
json = "{}"
# create an instance of ReviveShipment from a JSON string
revive_shipment_instance = ReviveShipment.from_json(json)
# print the JSON string representation of the object
print(ReviveShipment.to_json())

# convert the object into a dict
revive_shipment_dict = revive_shipment_instance.to_dict()
# create an instance of ReviveShipment from a dict
revive_shipment_from_dict = ReviveShipment.from_dict(revive_shipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


