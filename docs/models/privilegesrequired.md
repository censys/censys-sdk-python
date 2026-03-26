# PrivilegesRequired

Describes the level of privileges or access an attacker must have before successful exploitation. There are three possible values: None (N) – There is no privilege or special access required to conduct the attack, Low (L) – The attacker requires basic, “user” level privileges to leverage the exploit, High (H) – Administrative or similar access privileges are required for successful attack.

## Example Usage

```python
from censys_platform.models import PrivilegesRequired

value = PrivilegesRequired.UNKNOWN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `UNKNOWN` |           |
| `NONE`    | none      |
| `LOW`     | low       |
| `HIGH`    | high      |