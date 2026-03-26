# Type

The certificate's type. Options include root, intermediate, or leaf.

## Example Usage

```python
from censys_platform.models import Type

value = Type.UNKNOWN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `UNKNOWN`      |                |
| `ROOT`         | root           |
| `INTERMEDIATE` | intermediate   |
| `LEAF`         | leaf           |