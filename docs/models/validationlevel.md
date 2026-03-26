# ValidationLevel

The extent to which the certificate's issuer validated the identity of the entity requesting the certificate. Options include Domain validated (DV), Organization Validated (OV), or Extended Validation (EV).

## Example Usage

```python
from censys_platform.models import ValidationLevel

value = ValidationLevel.UNKNOWN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `UNKNOWN` |           |
| `DV`      | dv        |
| `OV`      | ov        |
| `EV`      | ev        |