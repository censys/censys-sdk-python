# Collections

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

List all collections for an organization. Retrieved information includes collection ID, name, query, description, status, and asset count.<br><br>This endpoint does not cost credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-collections-crud-list" method="get" path="/v3/collections" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.collections.list(page_token="<next_page_token>", page_size=1)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          | Example                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |                                                                                                                                                                                                                      |
| `page_token`                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | page token for the requested page of collection results                                                                                                                                                              |                                                                                                                                                                                                                      |
| `page_size`                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | amount of results to return per page                                                                                                                                                                                 | 1                                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |                                                                                                                                                                                                                      |

### Response

**[models.V3CollectionsCrudListResponse](../../models/v3collectionscrudlistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a new collection.<br><br>This endpoint does not cost credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-collections-crud-create" method="post" path="/v3/collections" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.collections.create(crud_create_input_body={
        "description": "Hosts with services with AsyncRAT indicator in cert subject DN",
        "name": "Hosts services with AsyncRAT indicator",
        "query": "host.services.cert.parsed.subject_dn: \"asyncrat\"",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `crud_create_input_body`                                                                                                                                                                                             | [Optional[models.CrudCreateInputBody]](../../models/crudcreateinputbody.md)                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3CollectionsCrudCreateResponse](../../models/v3collectionscrudcreateresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete a collection.<br><br>This endpoint does not cost credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-collections-crud-delete" method="delete" path="/v3/collections/{collection_uid}" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.collections.delete(collection_uid="11111111-2222-3333-4444-555555555555")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          | Example                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_uid`                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The UID for the collection. Obtain the collection ID using the [list collections endpoint](https://docs.censys.com/reference/v3-collections-crud-list#/) or via the collection URL when using the web console.       | 11111111-2222-3333-4444-555555555555                                                                                                                                                                                 |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |                                                                                                                                                                                                                      |

### Response

**[models.V3CollectionsCrudDeleteResponse](../../models/v3collectionscruddeleteresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404                   | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Retrieve information about a collection. Retrieved information includes its name, query, description, status, and asset count.<br><br>This endpoint does not cost credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-collections-crud-get" method="get" path="/v3/collections/{collection_uid}" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.collections.get(collection_uid="11111111-2222-3333-4444-555555555555")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          | Example                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_uid`                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The UID for the collection. Obtain the collection ID using the [list collections endpoint](https://docs.censys.com/reference/v3-collections-crud-list#/) or via the collection URL when using the web console.       | 11111111-2222-3333-4444-555555555555                                                                                                                                                                                 |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |                                                                                                                                                                                                                      |

### Response

**[models.V3CollectionsCrudGetResponse](../../models/v3collectionscrudgetresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404                   | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update

Update a collection's name, description, and/or query.<br><br>This endpoint does not cost credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-collections-crud-update" method="put" path="/v3/collections/{collection_uid}" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.collections.update(collection_uid="11111111-2222-3333-4444-555555555555", crud_update_input_body={
        "description": "Hosts with services with AsyncRAT indicator in cert subject DN",
        "name": "Hosts services with AsyncRAT indicator",
        "query": "host.services.cert.parsed.subject_dn: \"asyncrat\"",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          | Example                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_uid`                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The UID for the collection                                                                                                                                                                                           | 11111111-2222-3333-4444-555555555555                                                                                                                                                                                 |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |                                                                                                                                                                                                                      |
| `crud_update_input_body`                                                                                                                                                                                             | [Optional[models.CrudUpdateInputBody]](../../models/crudupdateinputbody.md)                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                  |                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |                                                                                                                                                                                                                      |

### Response

**[models.V3CollectionsCrudUpdateResponse](../../models/v3collectionscrudupdateresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404                   | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_events

Retrieve the event history for a collection. This includes the addition or removal of assets as well as collection status changes.<br><br>This endpoint does not cost credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-collections-list-events" method="get" path="/v3/collections/{collection_uid}/events" -->
```python
from censys_platform import SDK
from censys_platform.utils import parse_datetime


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.collections.list_events(request={
        "collection_uid": "11111111-2222-3333-4444-555555555555",
        "page_size": 1,
        "page_token": "<next_page_token>",
        "start_time": parse_datetime("2025-01-01T00:00:00Z"),
        "end_time": parse_datetime("2025-01-02T00:00:00Z"),
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

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404                   | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## aggregate

Aggregate results for a Platform search query that targets a collection's assets. This functionality is equivalent to the [Report Builder](https://docs.censys.com/docs/platform-report-builder#/) in the Platform web UI.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-collections-search-aggregate" method="post" path="/v3/collections/{collection_uid}/search/aggregate" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.collections.aggregate(collection_uid="11111111-2222-3333-4444-555555555555", search_aggregate_input_body={
        "field": "host.services.port",
        "number_of_buckets": 100,
        "query": "host.services.protocol=SSH",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          | Example                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_uid`                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The UID for the collection. Obtain the collection ID using the [list collections endpoint](https://docs.censys.com/reference/v3-collections-crud-list#/) or via the collection URL when using the web console.       | 11111111-2222-3333-4444-555555555555                                                                                                                                                                                 |
| `search_aggregate_input_body`                                                                                                                                                                                        | [models.SearchAggregateInputBody](../../models/searchaggregateinputbody.md)                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                  |                                                                                                                                                                                                                      |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |                                                                                                                                                                                                                      |

### Response

**[models.V3CollectionsSearchAggregateResponse](../../models/v3collectionssearchaggregateresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 422              | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## search

Run a search query across a collection's assets. Reference the [documentation on Censys Query Language](https://docs.censys.com/docs/censys-query-language#/) for information about query syntax. Host services that match your search criteria will be returned in a `matched_services` object.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-collections-search-query" method="post" path="/v3/collections/{collection_uid}/search/query" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.collections.search(collection_uid="<id>", search_query_input_body={
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

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_uid`                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The UID for the collection                                                                                                                                                                                           |
| `search_query_input_body`                                                                                                                                                                                            | [models.SearchQueryInputBody](../../models/searchqueryinputbody.md)                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                  |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3CollectionsSearchQueryResponse](../../models/v3collectionssearchqueryresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404                   | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |