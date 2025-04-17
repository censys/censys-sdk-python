# Ipmi


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `capabilities`                                                         | [Optional[models.IpmiCapabilities]](../models/ipmicapabilities.md)     | :heavy_minus_sign:                                                     | N/A                                                                    |
| `command_payload`                                                      | [Optional[models.IpmiCommandPayload]](../models/ipmicommandpayload.md) | :heavy_minus_sign:                                                     | N/A                                                                    |
| `raw`                                                                  | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | The raw data returned by the server                                    |
| `rmcp_header`                                                          | [Optional[models.IpmiRMCPHeader]](../models/ipmirmcpheader.md)         | :heavy_minus_sign:                                                     | N/A                                                                    |
| `session_header`                                                       | [Optional[models.IpmiSessionHeader]](../models/ipmisessionheader.md)   | :heavy_minus_sign:                                                     | N/A                                                                    |