# SearchQueryInputBody


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `fields`                                               | List[*str*]                                            | :heavy_minus_sign:                                     | specify fields to return in response and ignore others | host.ip                                                |
| `page_size`                                            | *OptionalNullable[int]*                                | :heavy_minus_sign:                                     | amount of results to return per page                   | 1                                                      |
| `page_token`                                           | *Optional[str]*                                        | :heavy_minus_sign:                                     | page token for the requested page of search results    | <next_page_token>                                      |
| `query`                                                | *str*                                                  | :heavy_check_mark:                                     | CenQL query string to search upon                      | host.services: (protocol=SSH and not port: 22)         |