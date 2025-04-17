# Threat


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `actors`                                                     | List[[models.ThreatActor](../models/threatactor.md)]         | :heavy_minus_sign:                                           | N/A                                                          |
| `confidence`                                                 | *Optional[float]*                                            | :heavy_minus_sign:                                           | N/A                                                          |
| `details`                                                    | [Optional[models.ThreatDetails]](../models/threatdetails.md) | :heavy_minus_sign:                                           | N/A                                                          |
| `evidence`                                                   | List[[models.Evidence](../models/evidence.md)]               | :heavy_minus_sign:                                           | N/A                                                          |
| `id`                                                         | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          |
| `malware`                                                    | [Optional[models.ThreatMalware]](../models/threatmalware.md) | :heavy_minus_sign:                                           | N/A                                                          |
| `name`                                                       | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          |
| `source`                                                     | [Optional[models.ThreatSource]](../models/threatsource.md)   | :heavy_minus_sign:                                           | N/A                                                          |
| `tactic`                                                     | List[*str*]                                                  | :heavy_minus_sign:                                           | N/A                                                          |
| `type`                                                       | List[*str*]                                                  | :heavy_minus_sign:                                           | N/A                                                          |