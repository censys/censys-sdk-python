# ThreatHunting
(*threat_hunting*)

## Overview

Endpoints related to the Threat Hunting product

### Available Operations

* [get_tracked_scan](#get_tracked_scan) - Get tracked scan details
* [create_tracked_scan](#create_tracked_scan) - Create a tracked discovery scan
* [get_tracked_scan_threat_hunting](#get_tracked_scan_threat_hunting) - Get tracked scan details
* [value_counts](#value_counts) - CensEye: Retrieve value counts to discover pivots

## get_tracked_scan

Retrieve the current status and results of a tracked scan by its ID.
        This endpoint works for both discovery scans and rescans.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-scans-get" method="get" path="/v3/global/scans/{scan_id}" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.threat_hunting.get_tracked_scan(scan_id="5f39588f-d4c5-48e5-8894-0bb5918c28fa")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scan_id`                                                                                                                                                                                          | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | The unique identifier of the tracked scan                                                                                                                                                          |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

### Response

**[models.V3GlobaldataScansGetResponse](../../models/v3globaldatascansgetresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

## create_tracked_scan

Create a new tracked discovery scan for a specified target. Discovery scans are used to scan new targets that have not been previously identified. The scan will be queued. The response will contain a scan ID that you can use with the [get tracked scan details endpoint](https://docs.censys.com/reference/v3-globaldata-scans-get#/) to monitor its status and results.<br><br>This endpoint is available to organizations that have access to the Threat Hunting module.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-threathunting-scans-discovery" method="post" path="/v3/threat-hunting/scans/discovery" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.threat_hunting.create_tracked_scan(scans_discovery_input_body={
        "target": {
            "hostname_port": {
                "hostname": "censys.io",
                "port": 443,
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scans_discovery_input_body`                                                                                                                                                                       | [models.ScansDiscoveryInputBody](../../models/scansdiscoveryinputbody.md)                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                 | N/A                                                                                                                                                                                                |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

### Response

**[models.V3ThreathuntingScansDiscoveryResponse](../../models/v3threathuntingscansdiscoveryresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

## get_tracked_scan_threat_hunting

Retrieve the current status and results of a tracked scan by its ID.
        This endpoint works for both discovery scans and rescans.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-threathunting-scans-get" method="get" path="/v3/threat-hunting/scans/{scan_id}" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.threat_hunting.get_tracked_scan_threat_hunting(scan_id="cd62e794-9f12-4c2f-b5b3-153853aaf8d9")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scan_id`                                                                                                                                                                                          | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | The unique identifier of the tracked scan                                                                                                                                                          |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

### Response

**[models.V3ThreathuntingScansGetResponse](../../models/v3threathuntingscansgetresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

## value_counts

Get counts of web assets for specific field-value pairs and combinations of field-value pairs. This is similar to the [CensEye functionality](https://docs.censys.com/docs/platform-threat-hunting-use-censeye-to-build-detections#/) available in the Platform web UI, but it allows you to define specific fields of interest rather than the [default fields](https://docs.censys.com/docs/platform-threat-hunting-use-censeye-to-build-detections#default-pivot-fields) leveraged by the tool in the UI.<br><br>Each array can only target fields within the same nested object. For example, you can combine `host.services.port=80` and `host.services.protocol=SSH` in the same array, but you cannot combine `host.services.port=80` and `host.location.country=”United States”` in the same array. You can input multiple arrays of objects in each API call.<br><br>To use this endpoint, your organization must have access to the Threat Hunting Module. This endpoint costs 1 credit per count condition (array of objects) included in the API call.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-threathunting-value-counts" method="post" path="/v3/threat-hunting/value-counts" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.threat_hunting.value_counts(search_value_counts_input_body={
        "and_count_conditions": [
            {
                "field_value_pairs": [
                    {
                        "field": "host.services.port",
                        "value": "80",
                    },
                ],
            },
            {
                "field_value_pairs": [],
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `search_value_counts_input_body`                                                                                                                                                                   | [models.SearchValueCountsInputBody](../../models/searchvaluecountsinputbody.md)                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                 | N/A                                                                                                                                                                                                |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

### Response

**[models.V3ThreathuntingValueCountsResponse](../../models/v3threathuntingvaluecountsresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |