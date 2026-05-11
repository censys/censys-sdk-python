# TagsList


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `next_page_token`                                                                   | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Token to retrieve the next page of results. Omitted when there are no more results. |
| `tags`                                                                              | List[[models.Tag](../models/tag.md)]                                                | :heavy_check_mark:                                                                  | The list of tags.                                                                   |
| `total_size`                                                                        | *int*                                                                               | :heavy_check_mark:                                                                  | Total number of tags visible to the caller in this organization.                    |