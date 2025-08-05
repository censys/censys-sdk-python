# GlobalData
(*global_data*)

## Overview

Endpoints related to the Global Data product

### Available Operations

* [get_certificates](#get_certificates) - Get multiple certificates
* [get_certificate](#get_certificate) - Get a certificate
* [get_hosts](#get_hosts) - Get multiple hosts
* [get_host](#get_host) - Get a host
* [get_host_timeline](#get_host_timeline) - Get host event history
* [get_web_properties](#get_web_properties) - Get multiple web properties
* [get_web_property](#get_web_property) - Get a web property
* [create_tracked_scan](#create_tracked_scan) - Create a tracked rescan
* [get_tracked_scan](#get_tracked_scan) - Get tracked scan details
* [aggregate](#aggregate) - Aggregate results for a search query
* [search](#search) - Run a search query
* [get_tracked_scan_threat_hunting](#get_tracked_scan_threat_hunting) - Get tracked scan details

## get_certificates

Retrieve information about multiple certificates. A certificate ID is its SHA-256 fingerprint in the Censys dataset.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-asset-certificate-list" method="get" path="/v3/global/asset/certificate" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_certificates(certificate_ids=[
        "3daf2843a77b6f4e6af43cd9b6f6746053b8c928e056e8a724808db8905a94cf",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        | Example                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `certificate_ids`                                                                                                                                                                                  | List[*str*]                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                 | A list of SHA-256 certificate fingerprints.                                                                                                                                                        | [<br/>"3daf2843a77b6f4e6af43cd9b6f6746053b8c928e056e8a724808db8905a94cf"<br/>]                                                                                                                     |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |                                                                                                                                                                                                    |

### Response

**[models.V3GlobaldataAssetCertificateListResponse](../../models/v3globaldataassetcertificatelistresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

## get_certificate

Retrieve information about a single certificate. A certificate ID is its SHA-256 fingerprint in the Censys dataset.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-asset-certificate" method="get" path="/v3/global/asset/certificate/{certificate_id}" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_certificate(certificate_id="3daf2843a77b6f4e6af43cd9b6f6746053b8c928e056e8a724808db8905a94cf")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        | Example                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `certificate_id`                                                                                                                                                                                   | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | The SHA-256 certificate fingerprint.                                                                                                                                                               | 3daf2843a77b6f4e6af43cd9b6f6746053b8c928e056e8a724808db8905a94cf                                                                                                                                   |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |                                                                                                                                                                                                    |

### Response

**[models.V3GlobaldataAssetCertificateResponse](../../models/v3globaldataassetcertificateresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

## get_hosts

Retrieve information about multiple hosts. A host ID is its IP address.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-asset-host-list" method="get" path="/v3/global/asset/host" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_hosts(host_ids=[
        "8.8.8.8",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        | Example                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `host_ids`                                                                                                                                                                                         | List[*str*]                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                 | A list of host IP addresses.                                                                                                                                                                       | [<br/>"8.8.8.8"<br/>]                                                                                                                                                                              |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |                                                                                                                                                                                                    |

### Response

**[models.V3GlobaldataAssetHostListResponse](../../models/v3globaldataassethostlistresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

## get_host

Retrieve information about a single host. A host ID is its IP address.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-asset-host" method="get" path="/v3/global/asset/host/{host_id}" -->
```python
from censys_platform import SDK
from censys_platform.utils import parse_datetime


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_host(host_id="8.8.8.8", at_time=parse_datetime("2025-01-01T00:00:00Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        | Example                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `host_id`                                                                                                                                                                                          | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | The IP address of a host.                                                                                                                                                                          | 8.8.8.8                                                                                                                                                                                            |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |                                                                                                                                                                                                    |
| `at_time`                                                                                                                                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                 | RFC3339 Timestamp to view a host at a specific point in time. Must be a valid RFC3339 string. Ensure that you suffix the date with T00:00:00Z or a specific time.                                  | 2025-01-01T00:00:00Z                                                                                                                                                                               |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |                                                                                                                                                                                                    |

### Response

**[models.V3GlobaldataAssetHostResponse](../../models/v3globaldataassethostresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

## get_host_timeline

Retrieve event history for a host. A host ID is its IP address.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-asset-host-timeline" method="get" path="/v3/global/asset/host/{host_id}/timeline" -->
```python
from censys_platform import SDK
from censys_platform.utils import parse_datetime


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_host_timeline(host_id="8.8.8.8", start_time=parse_datetime("2025-01-01T00:00:00Z"), end_time=parse_datetime("2025-01-02T00:00:00Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        | Example                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `host_id`                                                                                                                                                                                          | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | The IP address of a host.                                                                                                                                                                          | 8.8.8.8                                                                                                                                                                                            |
| `start_time`                                                                                                                                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                 | Start time of the host timeline. Must be a valid RFC3339 string. Ensure that you suffix the date with T00:00:00Z or a specific time.                                                               | 2025-01-01T00:00:00Z                                                                                                                                                                               |
| `end_time`                                                                                                                                                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                 | End time of the host timeline. Must be a valid RFC3339 string. Ensure that you suffix the date with T00:00:00Z or a specific time.                                                                 | 2025-01-02T00:00:00Z                                                                                                                                                                               |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |                                                                                                                                                                                                    |

### Response

**[models.V3GlobaldataAssetHostTimelineResponse](../../models/v3globaldataassethosttimelineresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

## get_web_properties

Retrieve information about multiple web properties. Web properties are identified using a combination of a hostname and port joined with a colon, such as `platform.censys.io:80`.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-asset-webproperty-list" method="get" path="/v3/global/asset/webproperty" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_web_properties(webproperty_ids=[
        "platform.censys.io:80",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        | Example                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `webproperty_ids`                                                                                                                                                                                  | List[*str*]                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                 | A list of web property identifiers.                                                                                                                                                                | [<br/>"platform.censys.io:80"<br/>]                                                                                                                                                                |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |                                                                                                                                                                                                    |

### Response

**[models.V3GlobaldataAssetWebpropertyListResponse](../../models/v3globaldataassetwebpropertylistresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

## get_web_property

Retrieve information about a single web property. Web properties are identified using a combination of a hostname and port joined with a colon, such as `platform.censys.io:80`.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-asset-webproperty" method="get" path="/v3/global/asset/webproperty/{webproperty_id}" -->
```python
from censys_platform import SDK
from censys_platform.utils import parse_datetime


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_web_property(webproperty_id="platform.censys.io:80", at_time=parse_datetime("2025-01-01T00:00:00Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        | Example                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `webproperty_id`                                                                                                                                                                                   | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | A web property identifier.                                                                                                                                                                         | platform.censys.io:80                                                                                                                                                                              |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |                                                                                                                                                                                                    |
| `at_time`                                                                                                                                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                 | RFC3339 Timestamp to view a webproperty at a specific point in time. Must be a valid RFC3339 string. Ensure that you suffix the date with T00:00:00Z or a specific time                            | 2025-01-01T00:00:00Z                                                                                                                                                                               |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |                                                                                                                                                                                                    |

### Response

**[models.V3GlobaldataAssetWebpropertyResponse](../../models/v3globaldataassetwebpropertyresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

## create_tracked_scan

Create a new tracked rescan for a known service or web property. Rescans are used to update information for previously discovered targets. The scan will be queued. The response will contain a scan ID that you can use with the [get tracked scan details endpoint](https://docs.censys.com/reference/v3-globaldata-scans-get#/) to monitor its status and results.<br><br>This endpoint is available to all Enterprise customers.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-scans-rescan" method="post" path="/v3/global/scans/rescan" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.create_tracked_scan(scans_rescan_input_body={
        "target": {
            "web_origin": {
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
| `scans_rescan_input_body`                                                                                                                                                                          | [models.ScansRescanInputBody](../../models/scansrescaninputbody.md)                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                 | N/A                                                                                                                                                                                                |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

### Response

**[models.V3GlobaldataScansRescanResponse](../../models/v3globaldatascansrescanresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

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

    res = sdk.global_data.get_tracked_scan(scan_id="5f39588f-d4c5-48e5-8894-0bb5918c28fa")

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

## aggregate

Aggregate results for a Platform search query. This functionality is equivalent to the [Report Builder](https://docs.censys.com/docs/platform-report-builder#/) in the Platform web UI.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-search-aggregate" method="post" path="/v3/global/search/aggregate" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.aggregate(search_aggregate_input_body={
        "field": "host.services.port",
        "number_of_buckets": 100,
        "query": "host.services.protocol=SSH",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `search_aggregate_input_body`                                                                                                                                                                      | [models.SearchAggregateInputBody](../../models/searchaggregateinputbody.md)                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                 | N/A                                                                                                                                                                                                |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

### Response

**[models.V3GlobaldataSearchAggregateResponse](../../models/v3globaldatasearchaggregateresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

## search

Run a search query across Censys data. Reference the [documentation on Censys Query Language](https://docs.censys.com/docs/censys-query-language#/) for information about query syntax.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-search-query" method="post" path="/v3/global/search/query" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.search(search_query_input_body={
        "fields": [
            "host.ip",
        ],
        "page_size": 1,
        "query": "host.services: (protocol=SSH and not port: 22)",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `search_query_input_body`                                                                                                                                                                          | [models.SearchQueryInputBody](../../models/searchqueryinputbody.md)                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                 | N/A                                                                                                                                                                                                |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

### Response

**[models.V3GlobaldataSearchQueryResponse](../../models/v3globaldatasearchqueryresponse.md)**

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

    res = sdk.global_data.get_tracked_scan_threat_hunting(scan_id="cd62e794-9f12-4c2f-b5b3-153853aaf8d9")

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