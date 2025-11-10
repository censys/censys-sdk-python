# CreditUsageReport


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `end_date`                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | The end date of the window for this report.                          |
| `source_breakdown`                                                   | [models.SourceUsageBreakdown](../models/sourceusagebreakdown.md)     | :heavy_check_mark:                                                   | N/A                                                                  |
| `start_date`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | The start date of the window for this report.                        |
| `total_consumed`                                                     | *int*                                                                | :heavy_check_mark:                                                   | The total amount of credits consumed during the report period.       |