# TrackedScanTaskStatus

## Example Usage

```python
from censys_platform.models import TrackedScanTaskStatus

value = TrackedScanTaskStatus.UNKNOWN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `UNKNOWN`   |             |
| `SCANNING`  | scanning    |
| `SCANNED`   | scanned     |
| `REJECTED`  | rejected    |
| `TIMED_OUT` | timed_out   |
| `COMPLETED` | completed   |
| `IGNORED`   | ignored     |