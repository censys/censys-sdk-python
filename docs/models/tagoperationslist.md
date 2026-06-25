# TagOperationsList


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `next_page_token`                                                                   | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Token to retrieve the next page of results. Omitted when there are no more results. |
| `operations`                                                                        | List[[models.TagOperation](../models/tagoperation.md)]                              | :heavy_check_mark:                                                                  | The list of tag operations.                                                         |
| `total_size`                                                                        | *int*                                                                               | :heavy_check_mark:                                                                  | Total number of operations matching the filters.                                    |