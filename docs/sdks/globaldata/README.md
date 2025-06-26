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
* [aggregate](#aggregate) - Aggregate results for a search query
* [search](#search) - Run a search query

## get_certificates

Retrieve information about multiple certificates. A certificate ID is its SHA-256 fingerprint in the Censys dataset.

### Example Usage

```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_certificates(certificate_ids=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `certificate_ids`                                                                                                                                                                                  | List[*str*]                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                 | A list of SHA-256 certificate fingerprints.                                                                                                                                                        |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

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

```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_certificate(certificate_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `certificate_id`                                                                                                                                                                                   | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | The SHA-256 certificate fingerprint.                                                                                                                                                               |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

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

```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_hosts(host_ids=[
        "<value 1>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `host_ids`                                                                                                                                                                                         | List[*str*]                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                 | A list of host IP addresses.                                                                                                                                                                       |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

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

```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_host(host_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `host_id`                                                                                                                                                                                          | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | The IP address of a host.                                                                                                                                                                          |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `at_time`                                                                                                                                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                 | RFC3339 Timestamp to view a host at a specific point in time. Must be a valid RFC3339 string. Ensure that you suffix the date with T00:00:00Z or a specific time.                                  |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

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

```python
from censys_platform import SDK
from censys_platform.utils import parse_datetime


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_host_timeline(host_id="<id>", start_time=parse_datetime("2024-10-02T01:32:37.490Z"), end_time=parse_datetime("2025-02-08T13:31:28.844Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `host_id`                                                                                                                                                                                          | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | The IP address of a host.                                                                                                                                                                          |
| `start_time`                                                                                                                                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                 | Start time of the host timeline. Must be a valid RFC3339 string. Ensure that you suffix the date with T00:00:00Z or a specific time.                                                               |
| `end_time`                                                                                                                                                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                 | End time of the host timeline. Must be a valid RFC3339 string. Ensure that you suffix the date with T00:00:00Z or a specific time.                                                                 |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

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

```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_web_properties(webproperty_ids=[
        "<value 1>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `webproperty_ids`                                                                                                                                                                                  | List[*str*]                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                 | A web property host identifier, the format is hostname:port.                                                                                                                                       |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

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

```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_web_property(webproperty_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `webproperty_id`                                                                                                                                                                                   | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | A web property host identifier, the format is hostname:port.                                                                                                                                       |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `at_time`                                                                                                                                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                 | RFC3339 Timestamp to view a webproperty at a specific point in time. Must be a valid RFC3339 string. Ensure that you suffix the date with T00:00:00Z or a specific time                            |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

### Response

**[models.V3GlobaldataAssetWebpropertyResponse](../../models/v3globaldataassetwebpropertyresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

## aggregate

Aggregate results for a Platform search query. This functionality is equivalent to the [Report Builder](https://docs.censys.com/docs/platform-report-builder#/) in the Platform web UI.

### Example Usage

```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.aggregate(search_aggregate_input_body={
        "field": "<value>",
        "number_of_buckets": 309828,
        "query": "<value>",
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

```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.search(search_query_input_body={
        "query": "<value>",
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