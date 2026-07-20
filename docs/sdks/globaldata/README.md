# GlobalData

## Overview

Endpoints related to the Global Data product

### Available Operations

* [get_certificates](#get_certificates) - Retrieve multiple certificates
* [get_certificates_raw](#get_certificates_raw) - Retrieve multiple certificates in PEM format
* [get_certificate](#get_certificate) - Get a certificate
* [get_certificate_raw](#get_certificate_raw) - Get a certificate in PEM format
* [get_host_enrichment](#get_host_enrichment) - Get host enrichment
* [get_hosts](#get_hosts) - Retrieve multiple hosts
* [get_host](#get_host) - Get a host
* [list_services_on_host](#list_services_on_host) - Get service history for a host
* [get_host_timeline](#get_host_timeline) - Get host event history
* [get_web_properties](#get_web_properties) - Retrieve multiple web properties
* [get_web_property](#get_web_property) - Get a web property
* [list_dns_ip_resolution_bounds](#list_dns_ip_resolution_bounds) - Get DNS names that resolved to an IP (aggregated bounds)
* [list_dns_ip_resolution_ranges](#list_dns_ip_resolution_ranges) - Get DNS names that resolved to an IP (ranges)
* [list_dns_name_resolution_bounds](#list_dns_name_resolution_bounds) - Get DNS resolution records for a name (aggregated bounds)
* [list_dns_name_resolution_ranges](#list_dns_name_resolution_ranges) - Get DNS resolution records for a name (ranges)
* [create_tracked_scan](#create_tracked_scan) - Live Rescan: Initiate a new rescan
* [get_tracked_scan](#get_tracked_scan) - Get scan status
* [aggregate](#aggregate) - Aggregate results for a search query
* [convert_legacy_search_queries](#convert_legacy_search_queries) - Convert Legacy Search queries to Platform queries
* [search](#search) - Run a search query

## get_certificates

Retrieve information about multiple certificates. You can retrieve up to 1,000 certificates per call. A certificate ID is its SHA-256 fingerprint in the Censys dataset.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-asset-certificate-list-post" method="post" path="/v3/global/asset/certificate" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_certificates(asset_certificate_list_input_body={
        "certificate_ids": [
            "3daf2843a77b6f4e6af43cd9b6f6746053b8c928e056e8a724808db8905a94cf",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `asset_certificate_list_input_body`                                                                                                                                                                                                                                                                                         | [models.AssetCertificateListInputBody](../../models/assetcertificatelistinputbody.md)                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                                                                         |
| `organization_id`                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | The ID of a Censys organization to associate the request with. If omitted, the request will be processed using the authenticated user's free wallet where applicable. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                         |

### Response

**[models.V3GlobaldataAssetCertificateListPostResponse](../../models/v3globaldataassetcertificatelistpostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_certificates_raw

Retrieve the raw PEM-encoded format for multiple certificates. You can retrieve up to 1,000 certificates per call. A certificate ID is its SHA-256 fingerprint in the Censys dataset.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-asset-certificate-list-raw-post" method="post" path="/v3/global/asset/certificate/raw" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_certificates_raw(asset_certificate_list_input_body={
        "certificate_ids": [
            "3daf2843a77b6f4e6af43cd9b6f6746053b8c928e056e8a724808db8905a94cf",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `asset_certificate_list_input_body`                                                                                                                                                                                                                                                                                         | [models.AssetCertificateListInputBody](../../models/assetcertificatelistinputbody.md)                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                                                                         |
| `organization_id`                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | The ID of a Censys organization to associate the request with. If omitted, the request will be processed using the authenticated user's free wallet where applicable. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                         |

### Response

**[models.V3GlobaldataAssetCertificateListRawPostResponse](../../models/v3globaldataassetcertificatelistrawpostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

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

| Parameter                                                                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                 | Example                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `certificate_id`                                                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                                                                          | The SHA-256 certificate fingerprint.                                                                                                                                                                                                                                                                                        | 3daf2843a77b6f4e6af43cd9b6f6746053b8c928e056e8a724808db8905a94cf                                                                                                                                                                                                                                                            |
| `organization_id`                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | The ID of a Censys organization to associate the request with. If omitted, the request will be processed using the authenticated user's free wallet where applicable. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |                                                                                                                                                                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                             |

### Response

**[models.V3GlobaldataAssetCertificateResponse](../../models/v3globaldataassetcertificateresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_certificate_raw

Retrieve the raw PEM-encoded format of a certificate. A certificate ID is its SHA-256 fingerprint in the Censys dataset.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-asset-certificate-raw" method="get" path="/v3/global/asset/certificate/{certificate_id}/raw" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_certificate_raw(certificate_id="3daf2843a77b6f4e6af43cd9b6f6746053b8c928e056e8a724808db8905a94cf")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                 | Example                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `certificate_id`                                                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                                                                          | The SHA-256 certificate fingerprint.                                                                                                                                                                                                                                                                                        | 3daf2843a77b6f4e6af43cd9b6f6746053b8c928e056e8a724808db8905a94cf                                                                                                                                                                                                                                                            |
| `organization_id`                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | The ID of a Censys organization to associate the request with. If omitted, the request will be processed using the authenticated user's free wallet where applicable. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |                                                                                                                                                                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                             |

### Response

**[models.V3GlobaldataAssetCertificateRawResponse](../../models/v3globaldataassetcertificaterawresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_host_enrichment

Retrieve enrichment data for a single host. This endpoint is optimized for high-volume SOC enrichment use cases.<br><br>This endpoint does not consume standard Censys credits. Core organizations may perform up to 20,000 enrichment calls per day. Core + Unlimited Enrichment organizations may perform an unlimited amount of enrichment calls per day.<br><br>[Learn more about the enrichment API here](https://docs.censys.com/docs/host-enrichment).

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-asset-host-enrichment" method="get" path="/v3/global/asset/enrichment/host/{host_ip}" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_host_enrichment(host_ip="8.8.8.8")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          | Example                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `host_ip`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The IP address of a host.                                                                                                                                                                                            | 8.8.8.8                                                                                                                                                                                                              |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |                                                                                                                                                                                                                      |

### Response

**[models.V3GlobaldataAssetHostEnrichmentResponse](../../models/v3globaldataassethostenrichmentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404, 409, 429    | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_hosts

Retrieve information about multiple hosts. You can retrieve up to 100 hosts per call. A host ID is its IP address.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-asset-host-list-post" method="post" path="/v3/global/asset/host" -->
```python
from censys_platform import SDK
from censys_platform.utils import parse_datetime


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_hosts(asset_host_list_input_body={
        "at_time": parse_datetime("2025-01-01T00:00:00Z"),
        "host_ids": [
            "8.8.8.8",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `asset_host_list_input_body`                                                                                                                                                                                                                                                                                                | [models.AssetHostListInputBody](../../models/assethostlistinputbody.md)                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                                                                         |
| `organization_id`                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | The ID of a Censys organization to associate the request with. If omitted, the request will be processed using the authenticated user's free wallet where applicable. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                         |

### Response

**[models.V3GlobaldataAssetHostListPostResponse](../../models/v3globaldataassethostlistpostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

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

| Parameter                                                                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                 | Example                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `host_id`                                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                                                                          | The IP address of a host.                                                                                                                                                                                                                                                                                                   | 8.8.8.8                                                                                                                                                                                                                                                                                                                     |
| `organization_id`                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | The ID of a Censys organization to associate the request with. If omitted, the request will be processed using the authenticated user's free wallet where applicable. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |                                                                                                                                                                                                                                                                                                                             |
| `at_time`                                                                                                                                                                                                                                                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | RFC3339 Timestamp to view a host at a specific point in time. Must be a valid RFC3339 string. Ensure that you suffix the date with T00:00:00Z or a specific time.                                                                                                                                                           | 2025-01-01T00:00:00Z                                                                                                                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                             |

### Response

**[models.V3GlobaldataAssetHostResponse](../../models/v3globaldataassethostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_services_on_host

Retrieve historical service observations for a host. This endpoint returns time ranges during which services were detected on the host.<br><br>You can define a specific time frame of interest. If you do not specify a time frame, this endpoint will search the historical dataset that is available to your account.<br><br>You can filter by port number, protocol, and transport protocol.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-service-on-host" method="get" path="/v3/global/asset/host/{host_id}/observations/services" -->
```python
import censys_platform
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.list_services_on_host(request={
        "start_time": "2024-01-01T00:00:00Z",
        "end_time": "2024-01-31T23:59:59Z",
        "page_size": 50,
        "port": 443,
        "protocol": "HTTP",
        "transport_protocol": censys_platform.QueryParamTransportProtocol.TCP,
        "host_id": "8.8.8.8",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.V3GlobaldataServiceOnHostRequest](../../models/v3globaldataserviceonhostrequest.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.V3GlobaldataServiceOnHostResponse](../../models/v3globaldataserviceonhostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404, 409         | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_host_timeline

Retrieve event history for a host. A host ID is its IP address.<br><br>Note that when a service protocol changes after a new scan (for example, from `UNKNOWN` to `NETBIOS`), this information will be reflected in the `scan` object.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-asset-host-timeline" method="get" path="/v3/global/asset/host/{host_id}/timeline" -->
```python
from censys_platform import SDK
from censys_platform.utils import parse_datetime


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_host_timeline(host_id="8.8.8.8", start_time=parse_datetime("2025-01-02T00:00:00Z"), end_time=parse_datetime("2025-01-01T00:00:00Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                   | Example                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `host_id`                                                                                                                                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                            | The IP address of a host.                                                                                                                                                                                                                                                                                                                                                     | 8.8.8.8                                                                                                                                                                                                                                                                                                                                                                       |
| `start_time`                                                                                                                                                                                                                                                                                                                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                            | Start time of the host timeline. Equivalent to the To field in the event history UI. This must be the timestamp closest to the current time. For example, if you want events from January 1, 2025 to the start of January 2, 2025, input the January 2 timestamp here. Must be a valid RFC3339 string. Ensure that you suffix the date with T00:00:00Z or a specific time.    | 2025-01-02T00:00:00Z                                                                                                                                                                                                                                                                                                                                                          |
| `end_time`                                                                                                                                                                                                                                                                                                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                            | End time of the host timeline. Equivalent to the From field in the event history UI. This must be the timestamp furthest from the current time. For example, if you want events from January 1, 2025 to the start of January 2, 2025, input the January 1 timestamp here. Must be a valid RFC3339 string. Ensure that you suffix the date with T00:00:00Z or a specific time. | 2025-01-01T00:00:00Z                                                                                                                                                                                                                                                                                                                                                          |
| `organization_id`                                                                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                            | The ID of a Censys organization to associate the request with. If omitted, the request will be processed using the authenticated user's free wallet where applicable. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information.                                                   |                                                                                                                                                                                                                                                                                                                                                                               |
| `retries`                                                                                                                                                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                               |

### Response

**[models.V3GlobaldataAssetHostTimelineResponse](../../models/v3globaldataassethosttimelineresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_web_properties

Retrieve information about multiple web properties. You can retrieve up to 100 web properties per call. Web properties are identified using a combination of a hostname and port joined with a colon, such as `platform.censys.io:80`.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-asset-webproperty-list-post" method="post" path="/v3/global/asset/webproperty" -->
```python
from censys_platform import SDK
from censys_platform.utils import parse_datetime


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.get_web_properties(asset_webproperty_list_input_body={
        "at_time": parse_datetime("2025-01-01T00:00:00Z"),
        "webproperty_ids": [
            "platform.censys.io:80",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `asset_webproperty_list_input_body`                                                                                                                                                                                                                                                                                         | [models.AssetWebpropertyListInputBody](../../models/assetwebpropertylistinputbody.md)                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                                                                         |
| `organization_id`                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | The ID of a Censys organization to associate the request with. If omitted, the request will be processed using the authenticated user's free wallet where applicable. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                         |

### Response

**[models.V3GlobaldataAssetWebpropertyListPostResponse](../../models/v3globaldataassetwebpropertylistpostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

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

| Parameter                                                                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                 | Example                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `webproperty_id`                                                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                                                                          | A web property identifier.                                                                                                                                                                                                                                                                                                  | platform.censys.io:80                                                                                                                                                                                                                                                                                                       |
| `organization_id`                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | The ID of a Censys organization to associate the request with. If omitted, the request will be processed using the authenticated user's free wallet where applicable. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |                                                                                                                                                                                                                                                                                                                             |
| `at_time`                                                                                                                                                                                                                                                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | RFC3339 Timestamp to view a webproperty at a specific point in time. Must be a valid RFC3339 string. Ensure that you suffix the date with T00:00:00Z or a specific time                                                                                                                                                     | 2025-01-01T00:00:00Z                                                                                                                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                             |

### Response

**[models.V3GlobaldataAssetWebpropertyResponse](../../models/v3globaldataassetwebpropertyresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404, 422         | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_dns_ip_resolution_bounds

Retrieve the domain names that resolved to an IP during a time frame. You can narrow results with `record_types` (A or AAAA).<br><br>Results are aggregated per domain name and multiple distinct ranges for a name will be grouped into one row of results. For example, if `censys.com` resolved to `1.1.1.1` from January 1 to January 7 during two different ranges of January 1 to January 3 and January 5 to January 7, and you targeted January 1 through January 7 with your API call, then this endpoint will group those ranges into one entry for `censys.com` in the response.<br><br>To retrieve domain names for an IP with each record broken down by time range, use the [ranges endpoint](https://docs.censys.com/reference/v3-globaldata-dns-ip-resolution-ranges)<br><br>This endpoint is only available to organizations on the Censys Search and Censys Core plans.<br><br>[Learn more about Censys Active DNS](https://docs.censys.com/docs/platform-active-dns).

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-dns-ip-resolution-bound" method="get" path="/v3/global/dns/resolutions/ip/{ip}/bounds" -->
```python
import censys_platform
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.list_dns_ip_resolution_bounds(request={
        "start_time": "2024-01-01T00:00:00Z",
        "end_time": "2024-01-31T23:59:59Z",
        "page_size": 50,
        "record_types": [
            censys_platform.RecordTypes.A,
        ],
        "ip": "8.8.8.8",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                 | [models.V3GlobaldataDNSIPResolutionBoundRequest](../../models/v3globaldatadnsipresolutionboundrequest.md) | :heavy_check_mark:                                                                                        | The request object to use for the request.                                                                |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.V3GlobaldataDNSIPResolutionBoundResponse](../../models/v3globaldatadnsipresolutionboundresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404, 409         | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_dns_ip_resolution_ranges

Retrieve the domain names that resolved to an IP during a time frame. You can narrow results with `record_types` (A or AAAA).<br><br>Record results are broken down based on time range. For example, if `censys.com` resolved to `1.1.1.1` from January 1 to January 7 during two different ranges of January 1 to January 3 and January 5 to January 7, and you targeted January 1 through January 7 with your API call, then this endpoint will return one row for each of those distinct ranges.<br><br>To retrieve domain names for an IP with each result aggregated by name, use the [bounds endpoint endpoint](https://docs.censys.com/reference/v3-globaldata-dns-ip-resolution-bound).<br><br>This endpoint is only available to organizations on the Censys Search and Censys Core plans.<br><br>[Learn more about Censys Active DNS](https://docs.censys.com/docs/platform-active-dns).

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-dns-ip-resolution-ranges" method="get" path="/v3/global/dns/resolutions/ip/{ip}/ranges" -->
```python
import censys_platform
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.list_dns_ip_resolution_ranges(request={
        "start_time": "2024-01-01T00:00:00Z",
        "end_time": "2024-01-31T23:59:59Z",
        "page_size": 50,
        "record_types": [
            censys_platform.QueryParamRecordTypes.A,
        ],
        "domain": "platform.censys.io",
        "ip": "8.8.8.8",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                   | [models.V3GlobaldataDNSIPResolutionRangesRequest](../../models/v3globaldatadnsipresolutionrangesrequest.md) | :heavy_check_mark:                                                                                          | The request object to use for the request.                                                                  |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.V3GlobaldataDNSIPResolutionRangesResponse](../../models/v3globaldatadnsipresolutionrangesresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404, 409         | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_dns_name_resolution_bounds

Retrieve the DNS resolution records for a name. This endpoint returns observed A, AAAA, MX, NS, SOA, and TXT records for the name you provide. You can filter by one or more record types using record_types.<br><br>Results are aggregated per record distinct ranges for a record will be grouped into one row of results. For example, if `censys.com` resolved to `1.1.1.1` from January 1 to January 7 during two different ranges of January 1 to January 3 and January 5 to January 7, and you targeted January 1 through January 7 with your API call, then this endpoint will group those ranges into one entry for the `1.1.1.1` A record in the response.<br><br>To retrieve records for a name with each record broken down by time range, use the [ranges endpoint](https://docs.censys.com/reference/v3-globaldata-dns-name-resolution-ranges).<br><br>This endpoint is only available to organizations on the Censys Search and Censys Core plans.<br><br>[Learn more about Censys Active DNS](https://docs.censys.com/docs/platform-active-dns).

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-dns-name-resolution-bound" method="get" path="/v3/global/dns/resolutions/{name}/bounds" -->
```python
import censys_platform
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.list_dns_name_resolution_bounds(request={
        "start_time": "2024-01-01T00:00:00Z",
        "end_time": "2024-01-31T23:59:59Z",
        "page_size": 50,
        "record_types": [
            censys_platform.V3GlobaldataDNSNameResolutionBoundQueryParamRecordTypes.MX,
        ],
        "name": "platform.censys.io",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                     | [models.V3GlobaldataDNSNameResolutionBoundRequest](../../models/v3globaldatadnsnameresolutionboundrequest.md) | :heavy_check_mark:                                                                                            | The request object to use for the request.                                                                    |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.V3GlobaldataDNSNameResolutionBoundResponse](../../models/v3globaldatadnsnameresolutionboundresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404, 409         | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_dns_name_resolution_ranges

Retrieve the records that resolved for a name during a time frame. This endpoint returns observed A, AAAA, MX, NS, SOA, and TXT records for the name you provide. You can filter by one or more record types using `record_types`.<br><br>Record results are broken down based on time range. For example, if `censys.com` resolved to `1.1.1.1` from January 1 to January 7 during two different ranges of January 1 to January 3 and January 5 to January 7, and you targeted January 1 through January 7 with your API call, then this endpoint will return one row for each of those distinct ranges for the `1.1.1.1` A record.<br><br>To retrieve records for a name with each result aggregated per record, use the [bounds endpoint endpoint](https://docs.censys.com/reference/v3-globaldata-dns-name-resolution-bound).<br><br>This endpoint is only available to organizations on the Censys Search and Censys Core plans.<br><br>[Learn more about Censys Active DNS](https://docs.censys.com/docs/platform-active-dns).

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-dns-name-resolution-ranges" method="get" path="/v3/global/dns/resolutions/{name}/ranges" -->
```python
import censys_platform
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.list_dns_name_resolution_ranges(request={
        "start_time": "2024-01-01T00:00:00Z",
        "end_time": "2024-01-31T23:59:59Z",
        "page_size": 50,
        "record_types": [
            censys_platform.V3GlobaldataDNSNameResolutionRangesQueryParamRecordTypes.MX,
        ],
        "name": "platform.censys.io",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                       | [models.V3GlobaldataDNSNameResolutionRangesRequest](../../models/v3globaldatadnsnameresolutionrangesrequest.md) | :heavy_check_mark:                                                                                              | The request object to use for the request.                                                                      |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.V3GlobaldataDNSNameResolutionRangesResponse](../../models/v3globaldatadnsnameresolutionrangesresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404, 409         | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_tracked_scan

Initiate a rescan for a known host service at a specific IP and port (`ip:port`) or hostname and port (`hostname:port`). This is equivalent to the [Live Rescan](https://docs.censys.com/docs/platform-live-rescan#/) feature available in the UI, but you can also target web properties in addition to hosts.<br><br>The scan may take several minutes to complete. The response will contain a scan ID that you can use to [monitor the scan's status](https://docs.censys.com/reference/v3-globaldata-scans-get#/). After the scan completes, perform a lookup on the target asset to retrieve detailed scan information.<br><br>This endpoint is available to all Enterprise customers. It costs 10 credits to execute.

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

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scans_rescan_input_body`                                                                                                                                                                                            | [models.ScansRescanInputBody](../../models/scansrescaninputbody.md)                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                  |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3GlobaldataScansRescanResponse](../../models/v3globaldatascansrescanresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_tracked_scan

Retrieve the current status of a scan by its ID. This endpoint works for both [Live Discovery scans](https://docs.censys.com/reference/v3-threathunting-scans-discovery#/) and [Live Rescans](https://docs.censys.com/reference/v3-globaldata-scans-rescan#/).<br><br>If the scan was successful, perform a lookup on the target asset to retrieve detailed scan information.<br><br>This endpoint is available to all Enterprise customers. This endpoint does not cost any credits to execute.

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

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scan_id`                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The unique identifier of the tracked scan                                                                                                                                                                            |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3GlobaldataScansGetResponse](../../models/v3globaldatascansgetresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

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

| Parameter                                                                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `search_aggregate_input_body`                                                                                                                                                                                                                                                                                               | [models.SearchAggregateInputBody](../../models/searchaggregateinputbody.md)                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                                                                         |
| `organization_id`                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | The ID of a Censys organization to associate the request with. If omitted, the request will be processed using the authenticated user's free wallet where applicable. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                         |

### Response

**[models.V3GlobaldataSearchAggregateResponse](../../models/v3globaldatasearchaggregateresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## convert_legacy_search_queries

Convert Censys Search Language queries used in Legacy Search into Censys Query Language (CenQL) queries for use in the Platform.<br><br>Reference the [documentation on CenQL](https://docs.censys.com/docs/censys-query-language) for more information about query syntax.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-globaldata-search-convert" method="post" path="/v3/global/search/convert" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.convert_legacy_search_queries(search_convert_query_input_body={
        "queries": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `search_convert_query_input_body`                                                                                                                                                                                    | [models.SearchConvertQueryInputBody](../../models/searchconvertqueryinputbody.md)                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                  |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3GlobaldataSearchConvertResponse](../../models/v3globaldatasearchconvertresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403                   | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## search

Run a search query across Censys data. Reference the [documentation on Censys Query Language](https://docs.censys.com/docs/censys-query-language#/) for information about query syntax. Host services that match your search criteria will be returned in a `matched_services` object.

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

| Parameter                                                                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `search_query_input_body`                                                                                                                                                                                                                                                                                                   | [models.SearchQueryInputBody](../../models/searchqueryinputbody.md)                                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                                                                         |
| `organization_id`                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | The ID of a Censys organization to associate the request with. If omitted, the request will be processed using the authenticated user's free wallet where applicable. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                         |

### Response

**[models.V3GlobaldataSearchQueryResponse](../../models/v3globaldatasearchqueryresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |