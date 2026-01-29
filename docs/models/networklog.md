# NetworkLog


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `har_handle`                                                               | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Storage handle for the full HAR network log.                               |
| `resources`                                                                | List[[models.NetworkLogResourceInfo](../models/networklogresourceinfo.md)] | :heavy_minus_sign:                                                         | Resources fetched during page load.                                        |