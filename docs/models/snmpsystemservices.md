# SnmpSystemServices


## Fields

| Field                              | Type                               | Required                           | Description                        |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `layer_1`                          | *Optional[bool]*                   | :heavy_minus_sign:                 | Physical (e.g. repeaters)          |
| `layer_2`                          | *Optional[bool]*                   | :heavy_minus_sign:                 | Datalink/subnetwork (e.g. bridges) |
| `layer_3`                          | *Optional[bool]*                   | :heavy_minus_sign:                 | Internet (e.g. IP gateways)        |
| `layer_4`                          | *Optional[bool]*                   | :heavy_minus_sign:                 | End-to-end (e.g. IP hosts)         |
| `layer_5`                          | *Optional[bool]*                   | :heavy_minus_sign:                 | OSI layer 5                        |
| `layer_6`                          | *Optional[bool]*                   | :heavy_minus_sign:                 | OSI layer 6                        |
| `layer_7`                          | *Optional[bool]*                   | :heavy_minus_sign:                 | Applications (e.g. mail relays)    |