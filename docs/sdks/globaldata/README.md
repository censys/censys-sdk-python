# GlobalData
(*global_data*)

## Overview

Endpoints related to the Global Data product

### Available Operations

* [get_certificates](#get_certificates) - Asset / Certificate Bulk
* [get_certificate](#get_certificate) - Asset / Certificate
* [get_hosts](#get_hosts) - Asset / Host Bulk
* [get_host](#get_host) - Asset / Host
* [get_host_timeline](#get_host_timeline) - Asset / Host Timeline
* [get_web_properties](#get_web_properties) - Asset / WebProperty Bulk
* [get_web_property](#get_web_property) - Asset / WebProperty
* [aggregate](#aggregate) - Search / Aggregate
* [search](#search) - Search / Query

## get_certificates

Get multiple Certificates

### Example Usage

```python
from censys_platform import SDK


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_certificates(certificate_ids=[
        "<value>",
    ], organization_id="<id>")

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

Get a Certificate

### Example Usage

```python
from censys_platform import SDK


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_certificate(certificate_id="<id>", organization_id="<id>")

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

Get multiple Hosts

### Example Usage

```python
from censys_platform import SDK


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_hosts(host_ids=[], organization_id="<id>")

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

Get a Host

### Example Usage

```python
from censys_platform import SDK


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_host(host_id="<id>", organization_id="<id>")

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

Get the timeline of events for a Host

### Example Usage

```python
from censys_platform import SDK
import dateutil.parser


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_host_timeline(host_id="<id>", start_time=dateutil.parser.isoparse("2024-04-27T09:30:08.024Z"), end_time=dateutil.parser.isoparse("2023-04-13T10:41:42.221Z"), organization_id="<id>")

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

Get multiple WebProperties

### Example Usage

```python
from censys_platform import SDK


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_web_properties(webproperty_ids=[
        "<value>",
    ], organization_id="<id>")

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

Get a WebProperty

### Example Usage

```python
from censys_platform import SDK


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_web_property(webproperty_id="<id>", organization_id="<id>")

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

Run an aggregation via the Global data set

### Example Usage

```python
from censys_platform import SDK


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.aggregate(search_aggregate_input_body={
        "field": "<value>",
        "number_of_buckets": 590414,
        "query": "<value>",
    }, organization_id="<id>")

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

Search the Global data set

### Example Usage

```python
from censys_platform import SDK


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.search(search_query_input_body={
        "query": "<value>",
    }, organization_id="<id>")

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