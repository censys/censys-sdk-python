# KubernetesVersionInfo


## Fields

| Field                                | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `build_date`                         | *Optional[str]*                      | :heavy_minus_sign:                   | Date version was built.              |
| `compiler`                           | *Optional[str]*                      | :heavy_minus_sign:                   | Go Compiler used                     |
| `git_commit`                         | *Optional[str]*                      | :heavy_minus_sign:                   | Git commit version built from.       |
| `git_tree_state`                     | *Optional[str]*                      | :heavy_minus_sign:                   | State of the tree when built.        |
| `git_version`                        | *Optional[str]*                      | :heavy_minus_sign:                   | N/A                                  |
| `go_version`                         | *Optional[str]*                      | :heavy_minus_sign:                   | Version of GO used to build version. |
| `major`                              | *Optional[str]*                      | :heavy_minus_sign:                   | Kubernetes major version             |
| `minor`                              | *Optional[str]*                      | :heavy_minus_sign:                   | Kubernetes minor version             |
| `platform`                           | *Optional[str]*                      | :heavy_minus_sign:                   | Platform compiled for                |