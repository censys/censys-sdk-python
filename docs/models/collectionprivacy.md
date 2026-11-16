# CollectionPrivacy

Collection visibility. `private` collections are visible to their creator and organization admins. `shared` collections are also visible to all organization members. Only the creator and organization admins can edit a collection.

## Example Usage

```python
from censys_platform.models import CollectionPrivacy

value = CollectionPrivacy.PRIVATE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `PRIVATE` | private   |
| `SHARED`  | shared    |