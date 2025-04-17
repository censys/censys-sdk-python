# Signature


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `self_signed`                                              | *Optional[bool]*                                           | :heavy_minus_sign:                                         | Whether the certificate was signed by its own key.         |
| `signature_algorithm`                                      | [Optional[models.KeyAlgorithm]](../models/keyalgorithm.md) | :heavy_minus_sign:                                         | N/A                                                        |
| `valid`                                                    | *Optional[bool]*                                           | :heavy_minus_sign:                                         | Whether the signature is valid.                            |
| `value`                                                    | *Optional[str]*                                            | :heavy_minus_sign:                                         | Contents of the signature.                                 |