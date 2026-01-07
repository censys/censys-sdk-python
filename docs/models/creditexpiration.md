# CreditExpiration


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `balance`                                                                   | *int*                                                                       | :heavy_check_mark:                                                          | The current balance of the credit expiration.                               |
| `created_at`                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects)        | :heavy_minus_sign:                                                          | The date and time the credit expiration was created.                        |
| `expires_at`                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects)        | :heavy_minus_sign:                                                          | The date and time the credit expiration will expire.                        |
| `initial_balance`                                                           | *int*                                                                       | :heavy_check_mark:                                                          | The initial balance of the credit expiration (i.e. how much was purchased). |