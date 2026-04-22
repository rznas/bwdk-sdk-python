# WalletBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Current wallet balance in Tomans | [optional] 
**negative_settlement_deadline** | **str** | Deadline for settling negative balance | [readonly] 

## Example

```python
from bwdk_sdk.models.wallet_balance import WalletBalance

# TODO update the JSON string below
json = "{}"
# create an instance of WalletBalance from a JSON string
wallet_balance_instance = WalletBalance.from_json(json)
# print the JSON string representation of the object
print(WalletBalance.to_json())

# convert the object into a dict
wallet_balance_dict = wallet_balance_instance.to_dict()
# create an instance of WalletBalance from a dict
wallet_balance_from_dict = WalletBalance.from_dict(wallet_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


