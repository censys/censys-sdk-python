# TLSChain


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `fingerprint_sha256`                                                         | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | SHA 256 fingerprint of the certificate in the certificate chain.             |
| `issuer_dn`                                                                  | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Distinguished name of the entity that has signed and issued the certificate. |
| `subject_dn`                                                                 | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Distinguished name of the entity that the certificate belongs to.            |