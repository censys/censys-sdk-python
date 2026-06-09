# DNSNameResolutionBoundResponse


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | The domain name that was queried.                                    |
| `next_page_token`                                                    | *str*                                                                | :heavy_check_mark:                                                   | A token that can be used to retrieve the next page of records.       |
| `records`                                                            | List[[models.DNSResolutionRecord](../models/dnsresolutionrecord.md)] | :heavy_check_mark:                                                   | The list of DNS records.                                             |
| `total_records`                                                      | *int*                                                                | :heavy_check_mark:                                                   | The number of records that exist in total across all pages.          |