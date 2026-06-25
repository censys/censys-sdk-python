# TagOperationType

Whether the operation creates or deletes tag assignments.

## Example Usage

```python
from censys_platform.models import TagOperationType

value = TagOperationType.BULK_CREATE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `BULK_CREATE` | bulk_create   |
| `BULK_DELETE` | bulk_delete   |