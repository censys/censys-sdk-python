# HostAssetWithMatchedServices


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `extensions`                                               | Dict[str, *Any*]                                           | :heavy_check_mark:                                         | N/A                                                        |
| `matched_services`                                         | List[[models.MatchedService](../models/matchedservice.md)] | :heavy_minus_sign:                                         | The host services that match the query.                    |
| `resource`                                                 | [models.Host](../models/host.md)                           | :heavy_check_mark:                                         | N/A                                                        |