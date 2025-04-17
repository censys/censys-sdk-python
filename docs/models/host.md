# Host


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `autonomous_system`                                  | [Optional[models.Routing]](../models/routing.md)     | :heavy_minus_sign:                                   | N/A                                                  |
| `dns`                                                | [Optional[models.HostDNS]](../models/hostdns.md)     | :heavy_minus_sign:                                   | N/A                                                  |
| `hardware`                                           | [Optional[models.Attribute]](../models/attribute.md) | :heavy_minus_sign:                                   | N/A                                                  |
| `ip`                                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | N/A                                                  |
| `labels`                                             | List[[models.Label](../models/label.md)]             | :heavy_minus_sign:                                   | N/A                                                  |
| `location`                                           | [Optional[models.Location]](../models/location.md)   | :heavy_minus_sign:                                   | N/A                                                  |
| `operating_system`                                   | [Optional[models.Attribute]](../models/attribute.md) | :heavy_minus_sign:                                   | N/A                                                  |
| `service_count`                                      | *Optional[int]*                                      | :heavy_minus_sign:                                   | N/A                                                  |
| `services`                                           | List[[models.Service](../models/service.md)]         | :heavy_minus_sign:                                   | N/A                                                  |
| `whois`                                              | [Optional[models.Whois]](../models/whois.md)         | :heavy_minus_sign:                                   | N/A                                                  |