# SmbSmbCapabilities


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `smb_dfs_support`                             | *Optional[bool]*                              | :heavy_minus_sign:                            | Server supports Distributed File System       |
| `smb_directory_leasing_support`               | *Optional[bool]*                              | :heavy_minus_sign:                            | Server supports directory leasing             |
| `smb_encryption_support`                      | *Optional[bool]*                              | :heavy_minus_sign:                            | Server supports encryption                    |
| `smb_leasing_support`                         | *Optional[bool]*                              | :heavy_minus_sign:                            | Server supports Leasing                       |
| `smb_multichan_support`                       | *Optional[bool]*                              | :heavy_minus_sign:                            | Server supports multiple channels per session |
| `smb_multicredit_support`                     | *Optional[bool]*                              | :heavy_minus_sign:                            | Server supports multi-credit operations       |
| `smb_persistent_handle_support`               | *Optional[bool]*                              | :heavy_minus_sign:                            | Server supports persistent handles            |