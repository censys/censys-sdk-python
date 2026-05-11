# TagPrivacy

Tag visibility and management settings. `private` tags are only visible to and editable by organization admins. `shared` tags are visible to and editable by all organization members.

## Example Usage

```python
from censys_platform.models import TagPrivacy

value = TagPrivacy.PRIVATE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `PRIVATE` | private   |
| `SHARED`  | shared    |