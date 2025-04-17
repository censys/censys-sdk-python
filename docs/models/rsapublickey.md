# RsaPublicKey


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `exponent`                                        | *Optional[int]*                                   | :heavy_minus_sign:                                | The RSA key's public exponent (e).                |
| `length`                                          | *Optional[int]*                                   | :heavy_minus_sign:                                | Bit-length of the RSA modulus.                    |
| `modulus`                                         | *Optional[str]*                                   | :heavy_minus_sign:                                | The RSA key's modulus (n) in big-endian encoding. |