# RCode

A enumerated field indicating the result of the request. The most common values are defined in RFC 1035.


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `UNKNOWN`         |                   |
| `SUCCESS`         | success           |
| `FORMAT_ERROR`    | format_error      |
| `SERVER_FAILURE`  | server_failure    |
| `NAME_ERROR`      | name_error        |
| `NOT_IMPLEMENTED` | not_implemented   |
| `REFUSED`         | refused           |
| `YX_DOMAIN`       | yx_domain         |
| `YX_RRSET`        | yx_rrset          |
| `NX_RRSET`        | nx_rrset          |
| `NOT_AUTH`        | not_auth          |
| `NOT_ZONE`        | not_zone          |
| `BAD_SIG`         | bad_sig           |
| `BAD_KEY`         | bad_key           |
| `BAD_TIME`        | bad_time          |
| `BAD_MODE`        | bad_mode          |
| `BAD_NAME`        | bad_name          |
| `BAD_ALG`         | bad_alg           |
| `BAD_TRUNC`       | bad_trunc         |
| `BAD_COOKIE`      | bad_cookie        |