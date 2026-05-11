# TagAssignmentsList


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `assignments`                                                                       | List[[models.TagAssignment](../models/tagassignment.md)]                            | :heavy_check_mark:                                                                  | The list of tag assignments.                                                        |
| `next_page_token`                                                                   | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Token to retrieve the next page of results. Omitted when there are no more results. |
| `total_size`                                                                        | *int*                                                                               | :heavy_check_mark:                                                                  | Total number of assignments matching the filters.                                   |