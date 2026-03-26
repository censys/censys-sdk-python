# State

Current state of the job.

## Example Usage

```python
from censys_platform.models import State

value = State.STARTED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `STARTED`   | started     |
| `COMPLETED` | completed   |
| `FAILED`    | failed      |
| `UNKNOWN`   | unknown     |