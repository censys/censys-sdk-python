# Ldap


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `allows_anonymous_bind`                                              | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Ability to connect with anonymous bind (empty username and password) |
| `attributes`                                                         | List[[models.LdapAttribute](../models/ldapattribute.md)]             | :heavy_minus_sign:                                                   | All root DN attributes available via anonymous bind                  |
| `result_code`                                                        | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Result or error code returned by LDAP instance upon bind             |