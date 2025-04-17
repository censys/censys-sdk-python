# IpmiRMCPHeaderMessageClass


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `class_`                                                        | *Optional[int]*                                                 | :heavy_minus_sign:                                              | Just the class part of the byte (lower 5 bits of raw)           |
| `is_ack`                                                        | *Optional[bool]*                                                | :heavy_minus_sign:                                              | True if the message is an acknowledgment to a previous message. |
| `name`                                                          | *Optional[str]*                                                 | :heavy_minus_sign:                                              | The human-readable name of the message class                    |
| `raw`                                                           | *Optional[int]*                                                 | :heavy_minus_sign:                                              | The raw message class byte.                                     |