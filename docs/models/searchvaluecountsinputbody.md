# SearchValueCountsInputBody


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `and_count_conditions`                                     | List[[models.CountCondition](../models/countcondition.md)] | :heavy_check_mark:                                         | Groups of field-value pairs to count matches for.          |
| `query`                                                    | *Optional[str]*                                            | :heavy_minus_sign:                                         | CenQL query string to filter documents                     |