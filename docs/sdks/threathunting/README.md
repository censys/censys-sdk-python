# ThreatHunting
(*threat_hunting*)

## Overview

Endpoints related to the Threat Hunting product

### Available Operations

* [value_counts](#value_counts) - CensEye: Retrieve value counts to discover pivots

## value_counts

Get counts of web assets for specific field-value pairs and combinations of field-value pairs. This is similar to the [CensEye functionality](https://docs.censys.com/docs/platform-threat-hunting-use-censeye-to-build-detections#/) available in the Platform web UI, but it allows you to define specific fields of interest rather than the [default fields](https://docs.censys.com/docs/platform-threat-hunting-use-censeye-to-build-detections#default-pivot-fields) leveraged by the tool in the UI.<br><br>Each array can only target fields within the same nested object. For example, you can combine `host.services.port=80` and `host.services.protocol=SSH` in the same array, but you cannot combine `host.services.port=80` and `host.location.country=”United States”` in the same array. You can input multiple arrays of objects in each API call.<br><br>To use this endpoint, your organization must have access to the Threat Hunting Module. This endpoint costs 1 credit per count condition (array of objects) included in the API call.

### Example Usage

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