# Vnc


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `connection_failed_reason`                                  | *Optional[str]*                                             | :heavy_minus_sign:                                          | If server terminates handshake, the reason offered (if any) |
| `desktop_name`                                              | *Optional[str]*                                             | :heavy_minus_sign:                                          | Desktop name provided by the server, capped at 255 bytes    |
| `pixel_encoding`                                            | [Optional[models.VncKeyValue]](../models/vnckeyvalue.md)    | :heavy_minus_sign:                                          | N/A                                                         |
| `screen_info`                                               | [Optional[models.DesktopInfo]](../models/desktopinfo.md)    | :heavy_minus_sign:                                          | N/A                                                         |
| `security_types`                                            | List[[models.VncKeyValue](../models/vnckeyvalue.md)]        | :heavy_minus_sign:                                          | server-specified security options                           |
| `version`                                                   | *Optional[str]*                                             | :heavy_minus_sign:                                          | N/A                                                         |