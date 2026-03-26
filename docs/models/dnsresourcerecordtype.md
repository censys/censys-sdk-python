# DNSResourceRecordType

An enumerated field indicating what type of data is in the "services.dns.additionals.response" field. For example, "A" signifies that the value in "services.dns.additionals.response" is an IPv4 address for the FQDN in "services.dns.additionals.name".

## Example Usage

```python
from censys_platform.models import DNSResourceRecordType

value = DNSResourceRecordType.UNKNOWN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `UNKNOWN` |           |
| `A`       | a         |
| `TXT`     | txt       |
| `NS`      | ns        |