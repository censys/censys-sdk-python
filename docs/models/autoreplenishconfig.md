# AutoReplenishConfig


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `amount`                                                                           | *Optional[int]*                                                                    | :heavy_minus_sign:                                                                 | The amount of credits to replenish when auto-replenish is triggered.               |
| `enabled`                                                                          | *bool*                                                                             | :heavy_check_mark:                                                                 | Whether the organization has auto-replenish enabled.                               |
| `threshold`                                                                        | *Optional[int]*                                                                    | :heavy_minus_sign:                                                                 | The threshold at which the organization's credit balance will be auto-replenished. |