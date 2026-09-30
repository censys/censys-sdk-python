# ContentType

The media type of the file to upload. Send it bare: a type carrying parameters, such as a charset, is not accepted.

## Example Usage

```python
from censys_platform.models import ContentType

value = ContentType.APPLICATION_PDF
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `APPLICATION_PDF` | application/pdf   |
| `TEXT_HTML`       | text/html         |
| `TEXT_CSV`        | text/csv          |
| `TEXT_PLAIN`      | text/plain        |
| `IMAGE_PNG`       | image/png         |
| `IMAGE_JPEG`      | image/jpeg        |
| `IMAGE_WEBP`      | image/webp        |