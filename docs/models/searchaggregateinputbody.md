# SearchAggregateInputBody


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `field`                                  | *str*                                    | :heavy_check_mark:                       | Specify field to aggregate by.           |
| `number_of_buckets`                      | *int*                                    | :heavy_check_mark:                       | Number of buckets to split results into. |
| `query`                                  | *str*                                    | :heavy_check_mark:                       | CenQL query string to search upon.       |