# KEVSource

The source checked to determine whether the CVE is in the KEV catalog.

## Example Usage

```python
from censys_platform.models import KEVSource

value = KEVSource.UNKNOWN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `UNKNOWN`     |               |
| `CISA`        | cisa          |
| `THIRD_PARTY` | third_party   |