# SearchQueryInputBody


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `fields`                                                | List[*str*]                                             | :heavy_minus_sign:                                      | Specify fields to return in response and ignore others. |
| `page_size`                                             | *OptionalNullable[int]*                                 | :heavy_minus_sign:                                      | Amount of results to return per page.                   |
| `page_token`                                            | *Optional[str]*                                         | :heavy_minus_sign:                                      | Page token for the requested page of search results.    |
| `query`                                                 | *str*                                                   | :heavy_check_mark:                                      | CenQL query string to search upon.                      |