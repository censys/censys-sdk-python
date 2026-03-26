# NetworkClassification


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `hosting`                                                            | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Whether the host belongs to an Internet hosting service provider.    |
| `mobile`                                                             | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Whether the host belongs to a mobile network.                        |
| `mobile_info`                                                        | [Optional[models.NetworkMobileInfo]](../models/networkmobileinfo.md) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `satellite`                                                          | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Whether the host belongs to a statellite network.                    |
| `source`                                                             | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The source of the data.                                              |