# TagOperationStatus

The current status of the operation.

## Example Usage

```python
from censys_platform.models import TagOperationStatus

value = TagOperationStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `PENDING`       | pending         |
| `RUNNING`       | running         |
| `SUCCEEDED`     | succeeded       |
| `LIMIT_REACHED` | limit_reached   |
| `FAILED`        | failed          |
| `CANCELLED`     | cancelled       |