# Greynoise


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `actor`                                                | *Optional[str]*                                        | :heavy_minus_sign:                                     | The actor that was observed.                           |
| `classification`                                       | *Optional[str]*                                        | :heavy_minus_sign:                                     | The classification of the IP address.                  |
| `last_observed_time`                                   | *Optional[str]*                                        | :heavy_minus_sign:                                     | The last time the IP address was observed.             |
| `tags`                                                 | List[[models.GreynoiseTag](../models/greynoisetag.md)] | :heavy_minus_sign:                                     | The tags associated with the IP address.               |