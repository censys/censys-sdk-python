# ServicesOnHostResponse


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `next_page_token`                                                  | *str*                                                              | :heavy_check_mark:                                                 | A token that can be used to retrieve the next page of ranges.      |
| `ranges`                                                           | List[[models.ServiceOnHostRange](../models/serviceonhostrange.md)] | :heavy_check_mark:                                                 | The list of requested services.                                    |