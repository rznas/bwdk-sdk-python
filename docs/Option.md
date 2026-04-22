# Option


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | [**TypeNameEnum**](TypeNameEnum.md) | نوع ویژگی محصول: رنگ، سایز، گارانتی، وزن یا سایر  * &#x60;color&#x60; - رنگ * &#x60;size&#x60; - اندازه * &#x60;warranty&#x60; - گارانتی * &#x60;weight&#x60; - وزن * &#x60;other&#x60; - سایر | 
**name** | **str** | نام ویژگی (مثلاً &#39;قرمز&#39; برای رنگ قرمز، &#39;XL&#39; برای سایز) | 
**value** | **str** | مقدار ویژگی (مثلاً &#39;#FF0000&#39; برای کد رنگ یا مقدار دیگر) | 
**is_color** | **bool** | اگر نوع ویژگی رنگ است درست است، وگرنه غلط | [optional] [default to False]

## Example

```python
from bwdk_sdk.models.option import Option

# TODO update the JSON string below
json = "{}"
# create an instance of Option from a JSON string
option_instance = Option.from_json(json)
# print the JSON string representation of the object
print(Option.to_json())

# convert the object into a dict
option_dict = option_instance.to_dict()
# create an instance of Option from a dict
option_from_dict = Option.from_dict(option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


