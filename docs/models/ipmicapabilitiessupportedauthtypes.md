# IpmiCapabilitiesSupportedAuthTypes


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `extended`                                        | *Optional[bool]*                                  | :heavy_minus_sign:                                | If true, the extended capabilities are present.   |
| `md2`                                             | *Optional[bool]*                                  | :heavy_minus_sign:                                | True if the MD2 AuthType is supported.            |
| `md5`                                             | *Optional[bool]*                                  | :heavy_minus_sign:                                | True if the MD5 AuthType is supported.            |
| `none`                                            | *Optional[bool]*                                  | :heavy_minus_sign:                                | True if the None AuthType is supported.           |
| `oem_proprietary`                                 | *Optional[bool]*                                  | :heavy_minus_sign:                                | True if the OEM Proprietary AuthType is supported |
| `password`                                        | *Optional[bool]*                                  | :heavy_minus_sign:                                | True if the Password AuthType is supported.       |
| `raw`                                             | *Optional[int]*                                   | :heavy_minus_sign:                                | The raw byte, with the bit mask etc               |