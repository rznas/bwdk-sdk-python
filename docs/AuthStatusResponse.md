# AuthStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_authenticated** | **bool** | Authentication status | 

## Example

```python
from bwdk_sdk.models.auth_status_response import AuthStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthStatusResponse from a JSON string
auth_status_response_instance = AuthStatusResponse.from_json(json)
# print the JSON string representation of the object
print(AuthStatusResponse.to_json())

# convert the object into a dict
auth_status_response_dict = auth_status_response_instance.to_dict()
# create an instance of AuthStatusResponse from a dict
auth_status_response_from_dict = AuthStatusResponse.from_dict(auth_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


