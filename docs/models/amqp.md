# Amqp


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `explicit_tls`                                             | *Optional[bool]*                                           | :heavy_minus_sign:                                         | Connected via a TLS connection after initial handshake     |
| `implicit_tls`                                             | *Optional[bool]*                                           | :heavy_minus_sign:                                         | Connected via a TLS wrapped connection (AMQPS)             |
| `protocol_id`                                              | [Optional[models.AmqpProtocol]](../models/amqpprotocol.md) | :heavy_minus_sign:                                         | N/A                                                        |
| `version`                                                  | [Optional[models.AmqpVersion]](../models/amqpversion.md)   | :heavy_minus_sign:                                         | N/A                                                        |