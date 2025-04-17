# EventStatusChange


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `event_time`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `new_status`                                                         | [models.NewStatus](../models/newstatus.md)                           | :heavy_check_mark:                                                   | N/A                                                                  |
| `old_status`                                                         | [Optional[models.OldStatus]](../models/oldstatus.md)                 | :heavy_minus_sign:                                                   | N/A                                                                  |
| `reason`                                                             | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |