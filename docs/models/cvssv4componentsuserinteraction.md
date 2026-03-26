# CVSSv4ComponentsUserInteraction

Describes whether a user, other than the attacker, is required to do anything or participate in exploitation of the vulnerability. User interaction has two possible values: None (N) – No user interaction is required, Required (R) – A user must complete some steps for the exploit to succeed. For example, a user might be required to install some software.

## Example Usage

```python
from censys_platform.models import CVSSv4ComponentsUserInteraction

value = CVSSv4ComponentsUserInteraction.UNKNOWN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `UNKNOWN`  |            |
| `NONE`     | none       |
| `REQUIRED` | required   |