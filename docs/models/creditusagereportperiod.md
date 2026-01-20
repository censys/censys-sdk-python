# CreditUsageReportPeriod


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `credits_added`                                                      | *int*                                                                | :heavy_check_mark:                                                   | The total amount of credits added during the report period.          |
| `credits_consumed`                                                   | *int*                                                                | :heavy_check_mark:                                                   | The total amount of credits consumed during the report period.       |
| `credits_expired`                                                    | *int*                                                                | :heavy_check_mark:                                                   | The total amount of credits expired during the report period.        |
| `end_date`                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | The end date of the window for this report period.                   |
| `start_date`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | The start date of the window for this report period.                 |
| `transaction_count`                                                  | *int*                                                                | :heavy_check_mark:                                                   | The total number of transactions during the report period.           |