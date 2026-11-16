# CrudCreateInputBodyPrivacy

Collection visibility. `private` collections are visible to their creator and organization admins. `shared` collections are also visible to all organization members. Only the creator and organization admins can edit a collection.

## Example Usage

```python
from censys_platform.models import CrudCreateInputBodyPrivacy

value = CrudCreateInputBodyPrivacy.PRIVATE
```


## Values

| Name      | Value     |
| --------- | --------- |
| `PRIVATE` | private   |
| `SHARED`  | shared    |