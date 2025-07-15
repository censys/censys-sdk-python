# SearchAggregateInputBody


## Fields

| Field                                   | Type                                    | Required                                | Description                             | Example                                 |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `field`                                 | *str*                                   | :heavy_check_mark:                      | field to aggregate by                   | web.endpoints.http.html_title           |
| `number_of_buckets`                     | *int*                                   | :heavy_check_mark:                      | number of buckets to split results into | 100                                     |
| `query`                                 | *str*                                   | :heavy_check_mark:                      | CenQL query string to search upon       | web: *                                  |