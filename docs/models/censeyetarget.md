# CenseyeTarget


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      | Example                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `certificate_id`                                                 | *Optional[str]*                                                  | :heavy_minus_sign:                                               | SHA-256 fingerprint of the certificate to analyze.               | 3daf2843a77b6f4e6af43cd9b6f6746053b8c928e056e8a724808db8905a94cf |
| `host_id`                                                        | *Optional[str]*                                                  | :heavy_minus_sign:                                               | IP address of the host to analyze.                               | 8.8.8.8                                                          |
| `webproperty_id`                                                 | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Web property identifier (hostname:port) to analyze.              | example.com:443                                                  |