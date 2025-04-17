# ValidityPeriod


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `length_seconds`                                                                | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | The duration of the certificate's validity period, in seconds.                  |
| `not_after`                                                                     | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | An RFC-3339-formatted timestamp after which the certificate is no longer valid. |
| `not_before`                                                                    | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | An RFC-3339-formatted timestamp before which the certificate is not valid.      |