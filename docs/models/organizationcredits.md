# OrganizationCredits


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `auto_replenish_config`                                        | [models.AutoReplenishConfig](../models/autoreplenishconfig.md) | :heavy_check_mark:                                             | N/A                                                            |
| `balance`                                                      | *int*                                                          | :heavy_check_mark:                                             | The current credit balance for the organization.               |
| `credit_expirations`                                           | List[[models.CreditExpiration](../models/creditexpiration.md)] | :heavy_check_mark:                                             | The credit expirations for the organization.                   |
| `uid`                                                          | *str*                                                          | :heavy_check_mark:                                             | The ID of a Censys organization.                               |