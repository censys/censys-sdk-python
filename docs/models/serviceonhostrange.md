# ServiceOnHostRange


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `end_time`                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | When the service was last observed                                   |
| `ip`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | IP address where the service was observed                            |
| `port`                                                               | *str*                                                                | :heavy_check_mark:                                                   | Port number where the service was observed                           |
| `protocol`                                                           | *str*                                                                | :heavy_check_mark:                                                   | Application protocol (e.g., HTTP, HTTPS)                             |
| `start_time`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | When the service was first observed                                  |
| `transport_protocol`                                                 | *str*                                                                | :heavy_check_mark:                                                   | Transport protocol (e.g., TCP, UDP, QUIC)                            |