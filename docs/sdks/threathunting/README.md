# ThreatHunting
(*threat_hunting*)

## Overview

Endpoints related to the Threat Hunting product

### Available Operations

* [value_counts](#value_counts) - Value Counts

## value_counts

Get counts for specific field-value combinations for threat hunting analysis (requires api-censeye feature flag)

### Example Usage

```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.threat_hunting.value_counts(search_value_counts_input_body={
        "and_count_conditions": [
            [
                {
                    "field": "<value>",
                    "value": "<value>",
                },
            ],
            [],
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