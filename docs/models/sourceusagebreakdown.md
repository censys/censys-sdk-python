# SourceUsageBreakdown


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `api`                                                      | *int*                                                      | :heavy_check_mark:                                         | The amount of credits consumed through the Platform API.   |
| `auto_replenishment`                                       | *Optional[int]*                                            | :heavy_minus_sign:                                         | The amount of credits consumed through auto-replenishment. |
| `other`                                                    | *Optional[int]*                                            | :heavy_minus_sign:                                         | The amount of credits consumed through other operations.   |
| `ui`                                                       | *int*                                                      | :heavy_check_mark:                                         | The amount of credits consumed through the Platform UI.    |