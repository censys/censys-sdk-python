# CVSSv4ComponentsAvailability

If an attack renders information unavailable, such as when a system crashes or through a DDoS attack, availability is negatively impacted. Availability has three possible values: None (N) – There is no loss of availability, Low (L) – Availability might be intermittently limited, or performance might be negatively impacted, as a result of a successful attack, High (H) – There is a complete loss of availability of the impacted system or information.

## Example Usage

```python
from censys_platform.models import CVSSv4ComponentsAvailability

value = CVSSv4ComponentsAvailability.UNKNOWN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `UNKNOWN` |           |
| `NONE`    | none      |
| `LOW`     | low       |
| `HIGH`    | high      |