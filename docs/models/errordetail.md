# ErrorDetail


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `location`                                                             | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Where the error occurred, e.g. 'body.items[3].tags' or 'path.thing-id' |
| `message`                                                              | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Error message text                                                     |
| `value`                                                                | *Optional[Any]*                                                        | :heavy_minus_sign:                                                     | The value at the given location                                        |