# CreatedInvestigationJobState

The current state of the investigation. Completed means the investigation succeeded, not that its results are still available to download, and unknown means only that this API is older than the state the service reported.

## Example Usage

```python
from censys_platform.models import CreatedInvestigationJobState

value = CreatedInvestigationJobState.STARTED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `STARTED`   | started     |
| `COMPLETED` | completed   |
| `FAILED`    | failed      |
| `UNKNOWN`   | unknown     |