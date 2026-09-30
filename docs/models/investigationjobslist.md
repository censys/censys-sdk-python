# InvestigationJobsList


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `jobs`                                                                                     | List[[models.InvestigationJob](../models/investigationjob.md)]                             | :heavy_check_mark:                                                                         | The caller's investigations in this organization, newest first.                            |
| `next_page_token`                                                                          | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Token to retrieve the next page of investigations. Omitted when there are no more results. |