# TagsAndComments

## Overview

Endpoints related to asset tagging and commenting

### Available Operations

* [list_comments](#list_comments) - List comments
* [create_comment](#create_comment) - Create a comment
* [delete_comment](#delete_comment) - Delete a comment
* [update_comment](#update_comment) - Update a comment
* [list_tags](#list_tags) - List tags
* [create_tag](#create_tag) - Create a tag
* [delete_tag](#delete_tag) - Delete a tag
* [get_tag](#get_tag) - Get a tag
* [update_tag](#update_tag) - Update a tag
* [list_tag_assignments](#list_tag_assignments) - List tag assignments
* [create_tag_assignment](#create_tag_assignment) - Create a tag assignment
* [bulk_create_tag_assignments](#bulk_create_tag_assignments) - Bulk create tag assignments
* [bulk_delete_tag_assignments](#bulk_delete_tag_assignments) - Bulk delete tag assignments
* [delete_tag_assignment](#delete_tag_assignment) - Delete a tag assignment
* [list_tag_operations](#list_tag_operations) - List tag operations
* [get_tag_operation](#get_tag_operation) - Get a tag operation
* [cancel_tag_operation](#cancel_tag_operation) - Cancel a tag operation

## list_comments

Retrieve a paginated list of comments in your organization. Use query parameters to filter by asset, creator, or creation time.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-comments-list-comments" method="get" path="/v3/comments" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.tags_and_comments.list_comments(request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.V3CommentsListCommentsRequest](../../models/v3commentslistcommentsrequest.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.V3CommentsListCommentsResponse](../../models/v3commentslistcommentsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 422                   | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_comment

Add a comment on an asset in your organization.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-comments-create-comment" method="post" path="/v3/comments" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.tags_and_comments.create_comment(create_comment_input_body={
        "asset_id": "8.8.8.8",
        "body": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `create_comment_input_body`                                                                                                                                                                                          | [models.CreateCommentInputBody](../../models/createcommentinputbody.md)                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                  |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3CommentsCreateCommentResponse](../../models/v3commentscreatecommentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 422                   | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete_comment

Delete a comment. Only the comment's creator or an organization admin can delete a comment. This action is permanent and cannot be undone.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-comments-delete-comment" method="delete" path="/v3/comments/{comment_id}" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.tags_and_comments.delete_comment(comment_id="e6faeec1-9f2b-49af-a7e6-119b37d54575")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `comment_id`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The ID of the comment to delete.                                                                                                                                                                                     |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3CommentsDeleteCommentResponse](../../models/v3commentsdeletecommentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update_comment

Update the body of an existing comment. Only the comment's creator can update it.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-comments-update-comment" method="put" path="/v3/comments/{comment_id}" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.tags_and_comments.update_comment(comment_id="361c6ff7-2549-4a6d-b212-8ce011a86612", update_comment_input_body={
        "body": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `comment_id`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The ID of the comment to update.                                                                                                                                                                                     |
| `update_comment_input_body`                                                                                                                                                                                          | [models.UpdateCommentInputBody](../../models/updatecommentinputbody.md)                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                  |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3CommentsUpdateCommentResponse](../../models/v3commentsupdatecommentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_tags

Retrieve a paginated list of tags in your organization. Private tags created by other users are not included in the results unless your account is an organization admin.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-tags-list-tags" method="get" path="/v3/tags" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.tags_and_comments.list_tags(request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.V3TagsListTagsRequest](../../models/v3tagslisttagsrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.V3TagsListTagsResponse](../../models/v3tagslisttagsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 422                   | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_tag

Create a new tag in your organization. Tags can be used to label and organize assets.<br><br>Specify a privacy setting to control visibility: `private` tags are only visible to you and organization admins, while `shared` tags are visible and manageable by all organization members.<br><br>Tag names must be unique within your organization.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-tags-create-tag" method="post" path="/v3/tags" -->
```python
import censys_platform
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.tags_and_comments.create_tag(create_tag_input_body={
        "name": "<value>",
        "privacy": censys_platform.CreateTagInputBodyPrivacy.PRIVATE,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `create_tag_input_body`                                                                                                                                                                                              | [models.CreateTagInputBody](../../models/createtaginputbody.md)                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                  |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3TagsCreateTagResponse](../../models/v3tagscreatetagresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 409, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete_tag

Delete a tag and all of its assignments from your organization. This action is permanent and cannot be undone.<br><br>Only the tag's creator or an organization admin can delete a `private` tag. Tags that are `shared` can be deleted by any organization member.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-tags-delete-tag" method="delete" path="/v3/tags/{tag_id}" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.tags_and_comments.delete_tag(tag_id="8e09cd66-475a-4284-88f2-228e9d76dd20")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tag_id`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The ID of the tag to delete.                                                                                                                                                                                         |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3TagsDeleteTagResponse](../../models/v3tagsdeletetagresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_tag

Retrieve a tag by its ID or name. Tag names are unique within an organization and can be used interchangeably with the tag ID in the path parameter.<br><br>Only tags that are visible to the caller are returned: private tags created by other users are not accessible unless your account is an organization admin.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-tags-get-tag" method="get" path="/v3/tags/{tag_id}" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.tags_and_comments.get_tag(tag_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          | Example                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tag_id`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The ID or name of the tag to retrieve.                                                                                                                                                                               | **Example 1:** 123e4567-e89b-12d3-a456-426614174000<br/>**Example 2:** my-tag                                                                                                                                        |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |                                                                                                                                                                                                                      |

### Response

**[models.V3TagsGetTagResponse](../../models/v3tagsgettagresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update_tag

Update an existing tag in your organization. Only the fields provided in the request body will be updated; omitted fields are left unchanged.<br><br>Only the tag's creator or an organization admin can update a `private` tag. Tags with the `shared` setting can be updated by any organization member.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-tags-update-tag" method="put" path="/v3/tags/{tag_id}" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.tags_and_comments.update_tag(tag_id="8367b125-0db2-4688-accc-c2a97a4bdc56", update_tag_input_body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tag_id`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The ID of the tag to update.                                                                                                                                                                                         |
| `update_tag_input_body`                                                                                                                                                                                              | [models.UpdateTagInputBody](../../models/updatetaginputbody.md)                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                  |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3TagsUpdateTagResponse](../../models/v3tagsupdatetagresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 409, 422         | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_tag_assignments

Retrieve a paginated list of assignments for a tag in your organization. Use query parameters to filter results by asset, created_by, or creation time. Only assignments for tags visible to your account are returned.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-tags-list-assignments" method="get" path="/v3/tags/{tag_id}/assignments" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.tags_and_comments.list_tag_assignments(request={
        "tag_id": "8b1458f5-044a-4cc5-a600-d602c09ca004",
        "asset_id": "8.8.8.8",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.V3TagsListAssignmentsRequest](../../models/v3tagslistassignmentsrequest.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.V3TagsListAssignmentsResponse](../../models/v3tagslistassignmentsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_tag_assignment

Assign a tag to an asset. Tag assignments are only visible to members of your organization, depending on the tag's privacy settings. You must have access to the tag to assign it to an asset.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-tags-create-assignment" method="post" path="/v3/tags/{tag_id}/assignments" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.tags_and_comments.create_tag_assignment(tag_id="2063be9e-6fe8-43db-9f99-815ede3d1b5c", create_tag_assignment_input_body={
        "asset_id": "8.8.8.8",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tag_id`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The ID of the tag to assign.                                                                                                                                                                                         |
| `create_tag_assignment_input_body`                                                                                                                                                                                   | [models.CreateTagAssignmentInputBody](../../models/createtagassignmentinputbody.md)                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                  |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3TagsCreateAssignmentResponse](../../models/v3tagscreateassignmentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 409, 422         | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## bulk_create_tag_assignments

Start a long-running operation that assigns a tag to every asset matching a CenQL query. The operation runs asynchronously; use the returned operation to track its progress.<br><br>A tag can hold a limited number of asset assignments, and the limit depends on your plan. If the operation reaches that limit before every matching asset is tagged, it finishes with status `limit_reached`.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-tags-bulk-create-assignments" method="post" path="/v3/tags/{tag_id}/assignments/bulk-create" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.tags_and_comments.bulk_create_tag_assignments(tag_id="1de943e6-02d8-47bb-8655-559621fc968c", bulk_create_tag_assignments_input_body={
        "query": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tag_id`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The ID of the tag to assign.                                                                                                                                                                                         |
| `bulk_create_tag_assignments_input_body`                                                                                                                                                                             | [models.BulkCreateTagAssignmentsInputBody](../../models/bulkcreatetagassignmentsinputbody.md)                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                  |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3TagsBulkCreateAssignmentsResponse](../../models/v3tagsbulkcreateassignmentsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 409, 422         | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## bulk_delete_tag_assignments

Start a long-running operation that removes a tag from its assigned assets, optionally restricted to a creation-time window. The operation runs asynchronously; use the returned operation to track its progress.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-tags-bulk-delete-assignments" method="post" path="/v3/tags/{tag_id}/assignments/bulk-delete" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.tags_and_comments.bulk_delete_tag_assignments(tag_id="4fb0c28f-5f77-4d94-8d15-c0c621009061", bulk_delete_tag_assignments_input_body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tag_id`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The ID of the tag whose assignments to delete.                                                                                                                                                                       |
| `bulk_delete_tag_assignments_input_body`                                                                                                                                                                             | [models.BulkDeleteTagAssignmentsInputBody](../../models/bulkdeletetagassignmentsinputbody.md)                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                  |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3TagsBulkDeleteAssignmentsResponse](../../models/v3tagsbulkdeleteassignmentsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 409, 422         | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete_tag_assignment

Remove a tag assignment from an asset. This action is permanent and cannot be undone. Removing an assignment only detaches the tag from the specified asset; the tag itself is not deleted. Only the tag's creator or an organization admin can delete an assignment for a `private` tag. Assignments for `shared` tags can be deleted by any organization member.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-tags-delete-assignment" method="delete" path="/v3/tags/{tag_id}/assignments/{assignment_id}" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.tags_and_comments.delete_tag_assignment(tag_id="ad98c1dc-289b-4487-b11f-d41cd4391806", assignment_id="35060ce7-9fe8-4c5f-9889-efb0572473c2")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tag_id`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The ID of the tag.                                                                                                                                                                                                   |
| `assignment_id`                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The ID of the assignment to delete.                                                                                                                                                                                  |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3TagsDeleteAssignmentResponse](../../models/v3tagsdeleteassignmentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_tag_operations

Retrieve a paginated list of bulk tag operations. Provide a tag ID in the path to scope the listing to a single tag, or `-` to list operations across all tags in your organization. Use query parameters to filter by type or status.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-tags-list-operations" method="get" path="/v3/tags/{tag_id}/operations" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.tags_and_comments.list_tag_operations(request={
        "tag_id": "123e4567-e89b-12d3-a456-426614174000",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.V3TagsListOperationsRequest](../../models/v3tagslistoperationsrequest.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.V3TagsListOperationsResponse](../../models/v3tagslistoperationsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 409, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_tag_operation

Retrieve a single bulk tag operation by ID, including its current status and progress counts. Use this to poll the status of an operation started by the bulk-create or bulk-delete endpoints.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-tags-get-operation" method="get" path="/v3/tags/{tag_id}/operations/{operation_id}" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.tags_and_comments.get_tag_operation(tag_id="7fd3732a-0f74-46ae-9b99-cf8d471365c7", operation_id="1d645480-2c36-4fbe-b3ee-eabcaa515ece")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tag_id`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The ID of the tag the operation belongs to.                                                                                                                                                                          |
| `operation_id`                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The ID of the operation to retrieve.                                                                                                                                                                                 |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3TagsGetOperationResponse](../../models/v3tagsgetoperationresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 409, 422         | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## cancel_tag_operation

Request cancellation of an in-progress bulk tag operation. Cancellation is cooperative: the operation finishes the page it is currently processing, then stops. Work already committed before cancellation is preserved.<br><br>Cancellation is not a rollback — it stops further work but does not remove assignments the operation already created. To remove assignments, use the bulk-delete endpoint. An operation that has already finished cannot be cancelled.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-tags-cancel-operation" method="post" path="/v3/tags/{tag_id}/operations/{operation_id}/cancel" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.tags_and_comments.cancel_tag_operation(tag_id="59da45bf-13dd-4601-8b86-c3af7e33fd9a", operation_id="174d4e39-b9c5-4b3f-aa69-5937abd03e40")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tag_id`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The ID of the tag the operation belongs to.                                                                                                                                                                          |
| `operation_id`                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The ID of the operation to cancel.                                                                                                                                                                                   |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3TagsCancelOperationResponse](../../models/v3tagscanceloperationresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 409, 422         | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |