# Collections
(*collections*)

## Overview

Endpoints related to the Collections product

### Available Operations

* [list](#list) - List collections
* [create](#create) - Create a collection
* [delete](#delete) - Delete a collection
* [get](#get) - Get a collection
* [update](#update) - Update a collection
* [list_events](#list_events) - Get a collection's events
* [aggregate](#aggregate) - Aggregate results for a search query within a collection
* [search](#search) - Run a search query within a collection

## list

List all collections for an organization. Retrieved information includes collection ID, name, query, description, status, and asset count.

### Example Usage

```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.collections.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `page_token`                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | page token for the requested page of collection results                                                                                                                                            |
| `page_size`                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | amount of results to return per page                                                                                                                                                               |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

### Response

**[models.V3CollectionsCrudListResponse](../../models/v3collectionscrudlistresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

## create

Create a new collection.

### Example Usage

```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.collections.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `crud_create_input_body`                                                                                                                                                                           | [Optional[models.CrudCreateInputBody]](../../models/crudcreateinputbody.md)                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                 | N/A                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

### Response

**[models.V3CollectionsCrudCreateResponse](../../models/v3collectionscrudcreateresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

## delete

Delete a collection.

### Example Usage

```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.collections.delete(collection_uid="d9ed2825-23bc-46db-bc4b-b4ac6c48f664")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_uid`                                                                                                                                                                                   | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | The UID for the collection                                                                                                                                                                         |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

### Response

**[models.V3CollectionsCrudDeleteResponse](../../models/v3collectionscruddeleteresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

## get

Retrieve information about a collection. Obtain the collection ID using the [list collections endpoint](https://docs.censys.com/reference/v3-collections-crud-list#/) or via the collection URL when using the web console. Retrieved information includes its name, query, description, status, and asset count.

### Example Usage

```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.collections.get(collection_uid="4d6d3f55-e4ae-405b-8d0f-4207b74028ab")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_uid`                                                                                                                                                                                   | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | The UID for the collection                                                                                                                                                                         |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

### Response

**[models.V3CollectionsCrudGetResponse](../../models/v3collectionscrudgetresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

## update

Update a collection's name, description, and/or query.

### Example Usage

```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.collections.update(collection_uid="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_uid`                                                                                                                                                                                   | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | The UID for the collection                                                                                                                                                                         |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `crud_update_input_body`                                                                                                                                                                           | [Optional[models.CrudUpdateInputBody]](../../models/crudupdateinputbody.md)                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                 | N/A                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

### Response

**[models.V3CollectionsCrudUpdateResponse](../../models/v3collectionscrudupdateresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

## list_events

Retrieve the event history for a collection. This includes the addition or removal of assets as well as collection status changes.

### Example Usage

```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.collections.list_events(request={
        "collection_uid": "ddc110c4-03da-472a-98af-be013b92eff5",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.V3CollectionsListEventsRequest](../../models/v3collectionslisteventsrequest.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.V3CollectionsListEventsResponse](../../models/v3collectionslisteventsresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

## aggregate

Aggregate results for a Platform search query that targets a collection's assets. This functionality is equivalent to the [Report Builder](https://docs.censys.com/docs/platform-report-builder#/) in the Platform web UI.

### Example Usage

```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.collections.aggregate(collection_uid="ee98f78d-a47d-44fb-89f4-0626ceaf34d7", search_aggregate_input_body={
        "field": "<value>",
        "number_of_buckets": 829469,
        "query": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_uid`                                                                                                                                                                                   | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | The UID for the collection                                                                                                                                                                         |
| `search_aggregate_input_body`                                                                                                                                                                      | [models.SearchAggregateInputBody](../../models/searchaggregateinputbody.md)                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                 | N/A                                                                                                                                                                                                |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

### Response

**[models.V3CollectionsSearchAggregateResponse](../../models/v3collectionssearchaggregateresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |

## search

Run a search query across a collection's assets. Reference the [documentation on Censys Query Language](https://docs.censys.com/docs/censys-query-language#/) for information about query syntax.

### Example Usage

```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.collections.search(collection_uid="<id>", search_query_input_body={
        "query": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_uid`                                                                                                                                                                                   | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | The UID for the collection                                                                                                                                                                         |
| `search_query_input_body`                                                                                                                                                                          | [models.SearchQueryInputBody](../../models/searchqueryinputbody.md)                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                 | N/A                                                                                                                                                                                                |
| `organization_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information. |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

### Response

**[models.V3CollectionsSearchQueryResponse](../../models/v3collectionssearchqueryresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.ErrorModel        | 401, 403                 | application/problem+json |
| models.SDKError          | 4XX, 5XX                 | \*/\*                    |