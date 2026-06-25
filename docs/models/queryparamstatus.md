# QueryParamStatus

Filter by operation status.

## Example Usage

```python
from censys_platform.models import QueryParamStatus

value = QueryParamStatus.PENDING
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