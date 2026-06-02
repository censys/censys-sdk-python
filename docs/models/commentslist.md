# CommentsList


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `comments`                                                                          | List[[models.Comment](../models/comment.md)]                                        | :heavy_check_mark:                                                                  | The list of comments.                                                               |
| `next_page_token`                                                                   | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Token to retrieve the next page of results. Omitted when there are no more results. |
| `total_size`                                                                        | *int*                                                                               | :heavy_check_mark:                                                                  | Total number of comments matching the filters.                                      |