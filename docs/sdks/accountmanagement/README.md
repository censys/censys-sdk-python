# AccountManagement

## Overview

Endpoints related to the Account Management product

### Available Operations

* [get_organization_details](#get_organization_details) - Get organization details
* [get_organization_credits](#get_organization_credits) - Get organization credit balance
* [get_organization_credit_usage](#get_organization_credit_usage) - Get organization credit usage
* [invite_user_to_organization](#invite_user_to_organization) - Invite user to organization
* [list_organization_members](#list_organization_members) - List organization members
* [remove_organization_member](#remove_organization_member) - Remove member from organization
* [update_organization_member](#update_organization_member) - Update a member's roles in an organization
* [get_member_credit_usage](#get_member_credit_usage) - Get organization member credit usage
* [get_user_credits](#get_user_credits) - Get Free user credit balance
* [get_user_credits_usage](#get_user_credits_usage) - Get Free user credit usage

## get_organization_details

Retrieve an organization's details, including the count of organization members broken down by role and organization settings such as AI training and MFA requirements.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-accountmanagement-org-details" method="get" path="/v3/accounts/organizations/{organization_id}" -->
```python
from censys_platform import SDK


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.account_management.get_organization_details(organization_id="11111111-2222-3333-4444-555555555555", include_member_counts=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                              | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            | Example                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                                      | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | The ID of a Censys organization. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. | 11111111-2222-3333-4444-555555555555                                                                                                                                                   |
| `include_member_counts`                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                     | Whether to include how many members are in this organization, split by role.                                                                                                           |                                                                                                                                                                                        |
| `retries`                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                    |                                                                                                                                                                                        |

### Response

**[models.V3AccountmanagementOrgDetailsResponse](../../models/v3accountmanagementorgdetailsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_organization_credits

Retrieve credit balance and expiration information for an organization. <br><br>Credits expire 12 months after they are acquired.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-accountmanagement-org-credits" method="get" path="/v3/accounts/organizations/{organization_id}/credits" -->
```python
from censys_platform import SDK


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.account_management.get_organization_credits(organization_id="11111111-2222-3333-4444-555555555555")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                              | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            | Example                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                                      | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | The ID of a Censys organization. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. | 11111111-2222-3333-4444-555555555555                                                                                                                                                   |
| `retries`                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                    |                                                                                                                                                                                        |

### Response

**[models.V3AccountmanagementOrgCreditsResponse](../../models/v3accountmanagementorgcreditsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_organization_credit_usage

Retrieve credit information for an organization over a specific date range. You must include a start date in your request.<br><br>Admins can obtain credit usage information for all users in their organization. Members may only retrieve usage information for their own account.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-accountmanagement-org-credits-usage" method="get" path="/v3/accounts/organizations/{organization_id}/credits/usage" -->
```python
from censys_platform import SDK
from datetime import date


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.account_management.get_organization_credit_usage(request={
        "organization_id": "11111111-2222-3333-4444-555555555555",
        "date_": "2025-11-01",
        "start_date": date.fromisoformat("2025-11-01"),
        "end_date": date.fromisoformat("2025-12-01"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                     | [models.V3AccountmanagementOrgCreditsUsageRequest](../../models/v3accountmanagementorgcreditsusagerequest.md) | :heavy_check_mark:                                                                                            | The request object to use for the request.                                                                    |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.V3AccountmanagementOrgCreditsUsageResponse](../../models/v3accountmanagementorgcreditsusageresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404, 422         | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## invite_user_to_organization

Invite a user to an organization. The user will receive an email to join the organization. This is equivalent to [adding a new member via the UI](https://docs.censys.com/docs/platform-org-management#invite-members).<br><br>Only users with the Admin role in the provided organization can perform this operation.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-accountmanagement-invite-user-to-org" method="post" path="/v3/accounts/organizations/{organization_id}/invitations" -->
```python
from censys_platform import SDK


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.account_management.invite_user_to_organization(organization_id="11111111-2222-3333-4444-555555555555", invite_member_input_body={
        "email": "user@example.com",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                              | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            | Example                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                                      | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | The ID of a Censys organization. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. | 11111111-2222-3333-4444-555555555555                                                                                                                                                   |
| `invite_member_input_body`                                                                                                                                                             | [models.InviteMemberInputBody](../../models/invitememberinputbody.md)                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | N/A                                                                                                                                                                                    |                                                                                                                                                                                        |
| `retries`                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                    |                                                                                                                                                                                        |

### Response

**[models.V3AccountmanagementInviteUserToOrgResponse](../../models/v3accountmanagementinviteusertoorgresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 409, 422         | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_organization_members

Retrieve a paginated list of an organization's members and their user details, including their user ID, email, name, creation time, and roles.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-accountmanagement-list-org-members" method="get" path="/v3/accounts/organizations/{organization_id}/members" -->
```python
from censys_platform import SDK


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.account_management.list_organization_members(organization_id="11111111-2222-3333-4444-555555555555", page_size=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                              | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            | Example                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                                      | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | The ID of a Censys organization. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. | 11111111-2222-3333-4444-555555555555                                                                                                                                                   |
| `page_size`                                                                                                                                                                            | *Optional[int]*                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                     | Number of members to return per page                                                                                                                                                   |                                                                                                                                                                                        |
| `page_token`                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                     | Pagination token for retrieving the next page of results                                                                                                                               |                                                                                                                                                                                        |
| `retries`                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                    |                                                                                                                                                                                        |

### Response

**[models.V3AccountmanagementListOrgMembersResponse](../../models/v3accountmanagementlistorgmembersresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## remove_organization_member

Remove a user from an organization. This is equivalent to [removing a member via the UI](https://docs.censys.com/docs/platform-org-management#remove-members).<br><br>Only users with the Admin role in the provided organization can perform this operation.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-accountmanagement-remove-org-member" method="delete" path="/v3/accounts/organizations/{organization_id}/members/{user_id}" -->
```python
from censys_platform import SDK


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.account_management.remove_organization_member(organization_id="11111111-2222-3333-4444-555555555555", user_id="11111111-2222-3333-4444-555555555555")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                              | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            | Example                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                                      | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | The ID of a Censys organization. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. | 11111111-2222-3333-4444-555555555555                                                                                                                                                   |
| `user_id`                                                                                                                                                                              | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | The ID of a Censys user. You can obtain a user's ID by listing members of an organization.                                                                                             | 11111111-2222-3333-4444-555555555555                                                                                                                                                   |
| `retries`                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                    |                                                                                                                                                                                        |

### Response

**[models.V3AccountmanagementRemoveOrgMemberResponse](../../models/v3accountmanagementremoveorgmemberresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 409, 422         | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update_organization_member

Update the roles assigned to an organization member. This operation replaces a member's roles with the list provided in the request body. To remove all roles from a member, provide an empty list. To completely remove a member from an organization, use the [remove member endpoint](https://docs.censys.com/reference/v3-accountmanagement-remove-org-member).<br><br>Only users with the Admin role in the provided organization can perform this operation.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-accountmanagement-update-org-member" method="patch" path="/v3/accounts/organizations/{organization_id}/members/{user_id}" -->
```python
from censys_platform import SDK


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.account_management.update_organization_member(organization_id="11111111-2222-3333-4444-555555555555", user_id="11111111-2222-3333-4444-555555555555", update_member_role_input_body={
        "roles": None,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                              | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            | Example                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                                      | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | The ID of a Censys organization. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. | 11111111-2222-3333-4444-555555555555                                                                                                                                                   |
| `user_id`                                                                                                                                                                              | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | The ID of a Censys user. You can obtain a user's ID by listing members of an organization.                                                                                             | 11111111-2222-3333-4444-555555555555                                                                                                                                                   |
| `update_member_role_input_body`                                                                                                                                                        | [models.UpdateMemberRoleInputBody](../../models/updatememberroleinputbody.md)                                                                                                          | :heavy_check_mark:                                                                                                                                                                     | N/A                                                                                                                                                                                    |                                                                                                                                                                                        |
| `retries`                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                    |                                                                                                                                                                                        |

### Response

**[models.V3AccountmanagementUpdateOrgMemberResponse](../../models/v3accountmanagementupdateorgmemberresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404, 409, 422    | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_member_credit_usage

Retrieve credit consumption information for an organization member over a specific date range. You must include a start date in your request.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-accountmanagement-member-credits-usage" method="get" path="/v3/accounts/organizations/{organization_id}/members/{user_id}/credits/usage" -->
```python
from censys_platform import SDK
from datetime import date


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.account_management.get_member_credit_usage(request={
        "organization_id": "11111111-2222-3333-4444-555555555555",
        "user_id": "11111111-2222-3333-4444-555555555555",
        "date_": "2025-11-01",
        "start_date": date.fromisoformat("2025-11-01"),
        "end_date": date.fromisoformat("2025-12-01"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                           | [models.V3AccountmanagementMemberCreditsUsageRequest](../../models/v3accountmanagementmembercreditsusagerequest.md) | :heavy_check_mark:                                                                                                  | The request object to use for the request.                                                                          |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.V3AccountmanagementMemberCreditsUsageResponse](../../models/v3accountmanagementmembercreditsusageresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404, 422         | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_user_credits

Retrieve your Free user account credit balance and refresh information. To retrieve the credit balance for a Starter or Enterprise account, use the [get organization credit balance endpoint](https://docs.censys.com/reference/v3-accountmanagement-org-credits).<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-accountmanagement-user-credits" method="get" path="/v3/accounts/users/credits" -->
```python
from censys_platform import SDK


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.account_management.get_user_credits()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.V3AccountmanagementUserCreditsResponse](../../models/v3accountmanagementusercreditsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 404                        | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_user_credits_usage

Retrieve your Free user account credit consumption information over a specific date range. You must include a start date in your request.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-accountmanagement-user-credits-usage" method="get" path="/v3/accounts/users/credits/usage" -->
```python
import censys_platform
from censys_platform import SDK
from datetime import date


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.account_management.get_user_credits_usage(granularity=censys_platform.V3AccountmanagementUserCreditsUsageQueryParamGranularity.DAILY, date_="2025-11-01", start_date=date.fromisoformat("2025-11-01"), end_date=date.fromisoformat("2025-12-01"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `granularity`                                                                                                                                                                                                                                                                        | [models.V3AccountmanagementUserCreditsUsageQueryParamGranularity](../../models/v3accountmanagementusercreditsusagequeryparamgranularity.md)                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                   | Whether to break down credit usage on a daily or monthly basis.                                                                                                                                                                                                                      | daily                                                                                                                                                                                                                                                                                |
| `date_`                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                   | The date for the credit usage report in YYYY-MM-DD format (e.g., 2025-11-06). This field is deprecated and will be removed in a future version. Use start_date and end_date instead. The date must be on or after 2025-01-01 (the earliest date available for credit usage reports). | 2025-11-01                                                                                                                                                                                                                                                                           |
| `start_date`                                                                                                                                                                                                                                                                         | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                   | The start date for the credit usage report in YYYY-MM-DD format (e.g., 2025-11-01). Must be on or after 2025-01-01 (the earliest date available for credit usage reports).                                                                                                           | 2025-11-01                                                                                                                                                                                                                                                                           |
| `end_date`                                                                                                                                                                                                                                                                           | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                   | The end date for the credit usage report in YYYY-MM-DD format (e.g., 2025-12-01). If omitted, will default to today's date. The date range (end_date - start_date) cannot exceed 365 days (1 year).                                                                                  | 2025-12-01                                                                                                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                      |

### Response

**[models.V3AccountmanagementUserCreditsUsageResponse](../../models/v3accountmanagementusercreditsusageresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 404                   | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |