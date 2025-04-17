# IpmiCapabilitiesAuthStatus


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `anonymous_login_enabled`                    | *Optional[bool]*                             | :heavy_minus_sign:                           | If true, the server allows anonymous login.  |
| `auth_each_message`                          | *Optional[bool]*                             | :heavy_minus_sign:                           | If true, each message must be authenticated. |
| `has_anonymous_users`                        | *Optional[bool]*                             | :heavy_minus_sign:                           | If true, the server has anonymous users.     |
| `has_named_users`                            | *Optional[bool]*                             | :heavy_minus_sign:                           | If true, the server supports named users.    |
| `two_key_login_required`                     | *Optional[bool]*                             | :heavy_minus_sign:                           | The KG field.                                |
| `user_auth_disabled`                         | *Optional[bool]*                             | :heavy_minus_sign:                           | If true, user authentication is disabled.    |