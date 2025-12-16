# censys-sdk-python

Developer-friendly & type-safe Python SDK specifically catered to leverage *openapi* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=openapi&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<!-- Start Summary [summary] -->
## Summary


<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [censys-sdk-python](https://github.com/censys/censys-sdk-python/blob/master/#censys-sdk-python)
  * [SDK Installation](https://github.com/censys/censys-sdk-python/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/censys/censys-sdk-python/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/censys/censys-sdk-python/blob/master/#sdk-example-usage)
  * [Available Resources and Operations](https://github.com/censys/censys-sdk-python/blob/master/#available-resources-and-operations)
  * [Global Parameters](https://github.com/censys/censys-sdk-python/blob/master/#global-parameters)
  * [Retries](https://github.com/censys/censys-sdk-python/blob/master/#retries)
  * [Error Handling](https://github.com/censys/censys-sdk-python/blob/master/#error-handling)
  * [Server Selection](https://github.com/censys/censys-sdk-python/blob/master/#server-selection)
  * [Custom HTTP Client](https://github.com/censys/censys-sdk-python/blob/master/#custom-http-client)
  * [Authentication](https://github.com/censys/censys-sdk-python/blob/master/#authentication)
  * [Resource Management](https://github.com/censys/censys-sdk-python/blob/master/#resource-management)
  * [Debugging](https://github.com/censys/censys-sdk-python/blob/master/#debugging)
* [Development](https://github.com/censys/censys-sdk-python/blob/master/#development)
  * [Maturity](https://github.com/censys/censys-sdk-python/blob/master/#maturity)
  * [Contributions](https://github.com/censys/censys-sdk-python/blob/master/#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add censys-platform
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install censys-platform
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add censys-platform
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from censys-platform python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "censys-platform",
# ]
# ///

from censys_platform import SDK

sdk = SDK(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from censys_platform import SDK

async def main():

    async with SDK(
        organization_id="11111111-2222-3333-4444-555555555555",
        personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
    ) as sdk:

        res = await sdk.global_data.search_async(search_query_input_body={
            "fields": [
                "host.ip",
            ],
            "page_size": 1,
            "query": "host.services: (protocol=SSH and not port: 22)",
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [AccountManagement](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/accountmanagement/README.md)

* [get_organization_details](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/accountmanagement/README.md#get_organization_details) - Get organization details
* [get_organization_credits](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/accountmanagement/README.md#get_organization_credits) - Get organization credit details
* [get_organization_credit_usage](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/accountmanagement/README.md#get_organization_credit_usage) - Get organization credit usage
* [invite_user_to_organization](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/accountmanagement/README.md#invite_user_to_organization) - Invite user to organization
* [list_organization_members](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/accountmanagement/README.md#list_organization_members) - List organization members
* [remove_organization_member](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/accountmanagement/README.md#remove_organization_member) - Remove member from organization
* [update_organization_member](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/accountmanagement/README.md#update_organization_member) - Update a member's roles in an organization
* [get_member_credit_usage](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/accountmanagement/README.md#get_member_credit_usage) - Get member credit usage
* [get_user_credits](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/accountmanagement/README.md#get_user_credits) - Get Free user credit details

### [Collections](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/collections/README.md)

* [list](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/collections/README.md#list) - List collections
* [create](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/collections/README.md#create) - Create a collection
* [delete](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/collections/README.md#delete) - Delete a collection
* [get](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/collections/README.md#get) - Get a collection
* [update](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/collections/README.md#update) - Update a collection
* [list_events](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/collections/README.md#list_events) - Get a collection's events
* [aggregate](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/collections/README.md#aggregate) - Aggregate results for a search query within a collection
* [search](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/collections/README.md#search) - Run a search query within a collection

### [GlobalData](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/globaldata/README.md)

* [get_certificates](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/globaldata/README.md#get_certificates) - Retrieve multiple certificates
* [get_certificates_raw](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/globaldata/README.md#get_certificates_raw) - Retrieve multiple certificates in PEM format
* [get_certificate](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/globaldata/README.md#get_certificate) - Get a certificate
* [get_certificate_raw](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/globaldata/README.md#get_certificate_raw) - Get a certificate in PEM format
* [get_hosts](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/globaldata/README.md#get_hosts) - Retrieve multiple hosts
* [get_host](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/globaldata/README.md#get_host) - Get a host
* [get_host_timeline](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/globaldata/README.md#get_host_timeline) - Get host event history
* [get_web_properties](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/globaldata/README.md#get_web_properties) - Retrieve multiple web properties
* [get_web_property](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/globaldata/README.md#get_web_property) - Get a web property
* [create_tracked_scan](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/globaldata/README.md#create_tracked_scan) - Live Rescan: Initiate a new rescan
* [get_tracked_scan](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/globaldata/README.md#get_tracked_scan) - Get scan status
* [aggregate](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/globaldata/README.md#aggregate) - Aggregate results for a search query
* [convert_legacy_search_queries](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/globaldata/README.md#convert_legacy_search_queries) - Convert Legacy Search queries to Platform queries
* [search](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/globaldata/README.md#search) - Run a search query

### [ThreatHunting](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/threathunting/README.md)

* [get_host_observations_with_certificate](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/threathunting/README.md#get_host_observations_with_certificate) - Get host history for a certificate
* [create_tracked_scan](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/threathunting/README.md#create_tracked_scan) - Live Discovery: Initiate a new scan
* [get_tracked_scan_threat_hunting](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/threathunting/README.md#get_tracked_scan_threat_hunting) - Get scan status
* [list_threats](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/threathunting/README.md#list_threats) - List active threats
* [value_counts](https://github.com/censys/censys-sdk-python/blob/master/docs/sdks/threathunting/README.md#value_counts) - CensEye: Retrieve value counts to discover pivots

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Global Parameters [global-parameters] -->
## Global Parameters

A parameter is configured globally. This parameter may be set on the SDK client instance itself during initialization. When configured as an option during SDK initialization, This global value will be used as the default on the operations that use it. When such operations are called, there is a place in each to override the global value, if needed.

For example, you can set `organization_id` to `` at SDK initialization and then you do not have to pass the same value on calls to operations like `get_organization_details`. But if you want to do so you may, which will locally override the global setting. See the example code below for a demonstration.


### Available Globals

The following global parameter is available.

| Name            | Type | Description                    |
| --------------- | ---- | ------------------------------ |
| organization_id | str  | The organization_id parameter. |

### Example

```python
from censys_platform import SDK


with SDK(
    organization_id="11111111-2222-3333-4444-555555555555",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.account_management.get_organization_details(organization_id="11111111-2222-3333-4444-555555555555", include_member_counts=False)

    # Handle response
    print(res)

```
<!-- End Global Parameters [global-parameters] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from censys_platform import SDK
from censys_platform.utils import BackoffStrategy, RetryConfig


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.account_management.get_organization_details(organization_id="11111111-2222-3333-4444-555555555555", include_member_counts=False,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from censys_platform import SDK
from censys_platform.utils import BackoffStrategy, RetryConfig


with SDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.account_management.get_organization_details(organization_id="11111111-2222-3333-4444-555555555555", include_member_counts=False)

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`SDKBaseError`](https://github.com/censys/censys-sdk-python/blob/master/./src/censys_platform/models/sdkbaseerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](https://github.com/censys/censys-sdk-python/blob/master/#error-classes). |

### Example
```python
import censys_platform
from censys_platform import SDK, models


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:
    res = None
    try:

        res = sdk.account_management.get_organization_details(organization_id="11111111-2222-3333-4444-555555555555", include_member_counts=False)

        # Handle response
        print(res)


    except models.SDKBaseError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, models.AuthenticationError):
            print(e.data.error)  # Optional[censys_platform.AuthenticationErrorDetail]
```

### Error Classes
**Primary errors:**
* [`SDKBaseError`](https://github.com/censys/censys-sdk-python/blob/master/./src/censys_platform/models/sdkbaseerror.py): The base class for HTTP error responses.
  * [`ErrorModel`](https://github.com/censys/censys-sdk-python/blob/master/./src/censys_platform/models/errormodel.py): Generic error.
  * [`AuthenticationError`](https://github.com/censys/censys-sdk-python/blob/master/./src/censys_platform/models/authenticationerror.py): Request does not contain a valid Authorization token. Status code `401`.

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`SDKBaseError`](https://github.com/censys/censys-sdk-python/blob/master/./src/censys_platform/models/sdkbaseerror.py)**:
* [`ResponseValidationError`](https://github.com/censys/censys-sdk-python/blob/master/./src/censys_platform/models/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from censys_platform import SDK


with SDK(
    server_url="https://api.platform.censys.io",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.account_management.get_organization_details(organization_id="11111111-2222-3333-4444-555555555555", include_member_counts=False)

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from censys_platform import SDK
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = SDK(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from censys_platform import SDK
from censys_platform.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = SDK(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                    | Type | Scheme      |
| ----------------------- | ---- | ----------- |
| `personal_access_token` | http | HTTP Bearer |

To authenticate with the API the `personal_access_token` parameter must be set when initializing the SDK client instance. For example:
```python
from censys_platform import SDK


with SDK(
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.account_management.get_organization_details(organization_id="11111111-2222-3333-4444-555555555555", include_member_counts=False)

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `SDK` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from censys_platform import SDK
def main():

    with SDK(
        organization_id="11111111-2222-3333-4444-555555555555",
        personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
    ) as sdk:
        # Rest of application here...


# Or when using async:
async def amain():

    async with SDK(
        organization_id="11111111-2222-3333-4444-555555555555",
        personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
    ) as sdk:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from censys_platform import SDK
import logging

logging.basicConfig(level=logging.DEBUG)
s = SDK(debug_logger=logging.getLogger("censys_platform"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=openapi&utm_campaign=python)
