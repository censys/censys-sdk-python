# AdversaryInvestigation

## Overview

Endpoints related to the Adversary Investigation product

### Available Operations

* [create_censeye_job](#create_censeye_job) - CensEye: Create a pivot analysis job
* [get_censeye_job](#get_censeye_job) - CensEye: Get job status
* [get_censeye_job_results](#get_censeye_job_results) - CensEye: Get job results
* [get_host_observations_with_certificate](#get_host_observations_with_certificate) - Get host history for a certificate
* [create_investigation_file_upload](#create_investigation_file_upload) - Investigations: Create file upload
* [list_investigation_jobs](#list_investigation_jobs) - Investigations: List jobs
* [create_investigation_job](#create_investigation_job) - Investigations: Create job
* [get_investigation_job](#get_investigation_job) - Investigations: Get job status
* [get_investigation_job_results](#get_investigation_job_results) - Investigations: Get job results
* [get_investigation_usage](#get_investigation_usage) - Investigations: Get usage
* [create_tracked_scan](#create_tracked_scan) - Live Discovery: Initiate a new scan
* [list_threats](#list_threats) - List active threats
* [value_counts](#value_counts) - CensEye: Retrieve value counts to discover pivots

## create_censeye_job

Create an asynchronous CensEye pivot analysis job for a host, web property, or certificate. The job extracts [default pivot fields](https://docs.censys.com/docs/platform-threat-hunting-use-censeye-to-build-detections#default-pivot-fields) from the target asset and counts matching documents for each field-value pair. Poll the job status endpoint to track progress, then retrieve results when complete.<br><br>To use this endpoint, your organization must have access to the Adversary Investigation module.<br><br>This endpoint costs 44 credits to execute for a host, 28 credits to execute for a web property, and 7 credits to execute for a certificate.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-threathunting-censeye-jobs-create" method="post" path="/v3/threat-hunting/censeye/jobs" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.adversary_investigation.create_censeye_job(create_censeye_job_input_body={
        "target": {
            "certificate_id": "3daf2843a77b6f4e6af43cd9b6f6746053b8c928e056e8a724808db8905a94cf",
            "host_id": "8.8.8.8",
            "webproperty_id": "example.com:443",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `create_censeye_job_input_body`                                                                                                                                                                                      | [models.CreateCenseyeJobInputBody](../../models/createcenseyejobinputbody.md)                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                  |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3ThreathuntingCenseyeJobsCreateResponse](../../models/v3threathuntingcenseyejobscreateresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_censeye_job

Retrieve the current status of a CensEye pivot analysis job. Use this to poll for completion before fetching results.<br><br>To use this endpoint, your organization must have access to the Adversary Investigation module.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-threathunting-censeye-jobs-get" method="get" path="/v3/threat-hunting/censeye/jobs/{job_id}" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.adversary_investigation.get_censeye_job(job_id="3c47b971-5db6-4a9e-8d59-14fc0486172b")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `job_id`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The unique identifier of the CensEye job.                                                                                                                                                                            |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3ThreathuntingCenseyeJobsGetResponse](../../models/v3threathuntingcenseyejobsgetresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_censeye_job_results

Retrieve the results of a completed CensEye pivot analysis job. Each result contains a count and the field-value pairs that were analyzed. Results may be empty if the job is still running.<br><br>Results are paginated. Use the `next_page_token` from the response to fetch subsequent pages.<br><br>To use this endpoint, your organization must have access to the Adversary Investigation module.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-threathunting-censeye-job-results" method="get" path="/v3/threat-hunting/censeye/jobs/{job_id}/results" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.adversary_investigation.get_censeye_job_results(job_id="e58e9a0e-e104-42cf-9d0e-fe88713bc6e3", page_size=100)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `job_id`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The unique identifier of the CensEye job.                                                                                                                                                                            |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `page_size`                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | Number of results per page (max 100)                                                                                                                                                                                 |
| `page_token`                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | Pagination token from previous response                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3ThreathuntingCenseyeJobResultsResponse](../../models/v3threathuntingcenseyejobresultsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_host_observations_with_certificate

Retrieve the historical observations of hosts associated with a certificate. This is useful for threat hunting, detection engineering, and timeline generation. Certificate history is also visible to Adversary Investigation users in the Platform UI on the [certificate timeline](https://docs.censys.com/docs/platform-threat-hunting-use-cert-history-to-build-better-detections#/).<br><br>You can define a specific time frame of interest. If you do not specify a time frame, this endpoint will search the historical dataset that is available to your account.<br><br>For workspaces with a history limit, the API returns observation ranges that overlap the allowed history window. The window starts at 00:00 UTC the allowed number of days ago and ends at the time of the request. Ranges are returned in full, with their original start and end times, even if they extend outside the window.<br><br>You may also filter results by port and transport protocol.<br><br>This endpoint is available to organizations that have access to the Adversary Investigation module. This endpoint costs one credit per page of results.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-threathunting-get-host-observations-with-certificate" method="get" path="/v3/threat-hunting/certificate/{certificate_id}/observations/hosts" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.adversary_investigation.get_host_observations_with_certificate(request={
        "certificate_id": "55af8a301eb51abdaf7c31bec951638fe5a99d5d92117eca2be493026613fa46",
        "start_time": "2023-01-01T00:00:00Z",
        "end_time": "2023-12-31T23:59:59Z",
        "port": 443,
        "protocol": "TCP",
        "page_size": 50,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                   | Type                                                                                                                                        | Required                                                                                                                                    | Description                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                   | [models.V3ThreathuntingGetHostObservationsWithCertificateRequest](../../models/v3threathuntinggethostobservationswithcertificaterequest.md) | :heavy_check_mark:                                                                                                                          | The request object to use for the request.                                                                                                  |
| `retries`                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                            | :heavy_minus_sign:                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                         |

### Response

**[models.V3ThreathuntingGetHostObservationsWithCertificateResponse](../../models/v3threathuntinggethostobservationswithcertificateresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 404              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_investigation_file_upload

Prepare to attach an evidence file to an investigation. This endpoint does not accept the file. It returns a URL to send the file to and an identifier to pass to the [create job endpoint](https://docs.censys.com/reference/v3-threathunting-investigations-jobs-create) afterwards.<br><br>Upload the file with an HTTP PUT to `upload_url` and send `upload_headers` exactly as returned by this endpoint. The URL grants access to that one file and stops working at `expire_time`; a file uploaded before that stays usable afterwards. Prepare one upload per file.<br><br>Start the investigation promptly after uploading. There is a limit on how many uploaded files you may hold without using them and starting an investigation from a file releases its slot. A file that no investigation references is discarded once it passes the service's retention window for unused uploads. A file an investigation does reference is kept with that investigation for as long as the investigation itself.<br><br>To use this endpoint, your organization must have access to the Adversary Investigation module.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-threathunting-investigations-files-create" method="post" path="/v3/threat-hunting/investigations/files" -->
```python
import censys_platform
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.adversary_investigation.create_investigation_file_upload(create_investigation_file_input_body={
        "content_type": censys_platform.ContentType.APPLICATION_PDF,
        "filename": "incident-report.pdf",
        "size_bytes": 1048576,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `create_investigation_file_input_body`                                                                                                                                                                               | [models.CreateInvestigationFileInputBody](../../models/createinvestigationfileinputbody.md)                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                  |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3ThreathuntingInvestigationsFilesCreateResponse](../../models/v3threathuntinginvestigationsfilescreateresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 409, 413, 422, 429    | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_investigation_jobs

List the AI investigations you have started. The most recent investigations are listed first and only investigations that have not passed their retention period are shown. Results are paginated and include investigations started in the Platform UI as well as through the API.<br><br>To use this endpoint, your organization must have access to the Adversary Investigation module.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-threathunting-investigations-jobs-list" method="get" path="/v3/threat-hunting/investigations/jobs" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.adversary_investigation.list_investigation_jobs(page_size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `page_size`                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | Number of investigations to return per page. Zero or omitted returns at most 50; values above 200 are reduced to 200.                                                                                                |
| `page_token`                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | Pagination token from the next_page_token of a previous response. Omit it to start from the first page.                                                                                                              |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3ThreathuntingInvestigationsJobsListResponse](../../models/v3threathuntinginvestigationsjobslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 409, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_investigation_job

Start an [AI investigation](https://docs.censys.com/docs/platform-ai-investigations) from a set of indicators, a set of previously uploaded evidence files, or both. Supply at least one `indicators` or `file_ids`. To use files, upload them first with the [create file upload endpoint](https://docs.censys.com/reference/v3-threathunting-investigations-files-create).<br><br>This endpoint returns a `job_id` that you can poll to retrieve its status and results.<br><br>Provide `start_time` and `end_time` to scope the investigation to a time frame, or `start_time` alone to scope it from that time up to now. Omit both to investigate current data.<br><br>To use this endpoint, your organization must have access to the Adversary Investigation module.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-threathunting-investigations-jobs-create" method="post" path="/v3/threat-hunting/investigations/jobs" -->
```python
from censys_platform import SDK
from censys_platform.utils import parse_datetime


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.adversary_investigation.create_investigation_job(create_investigation_job_input_body={
        "end_time": parse_datetime("2026-08-01T00:00:00Z"),
        "file_ids": [
            "file_550e8400-e29b-41d4-a716-446655440000",
        ],
        "indicators": [
            "1.1.1.1",
            "example.com",
        ],
        "start_time": parse_datetime("2026-06-01T00:00:00Z"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `create_investigation_job_input_body`                                                                                                                                                                                | [models.CreateInvestigationJobInputBody](../../models/createinvestigationjobinputbody.md)                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                  |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3ThreathuntingInvestigationsJobsCreateResponse](../../models/v3threathuntinginvestigationsjobscreateresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 409, 413, 422, 429    | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_investigation_job

Retrieve the status of one AI investigation. Poll this endpoint until the investigation is completed, then download its report and evidence.<br><br>An investigation that does not exist, belongs to another user, or has passed its retention window will return a “not found” response.<br><br>To use this endpoint, your organization must have access to the Adversary Investigation module.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-threathunting-investigations-jobs-get" method="get" path="/v3/threat-hunting/investigations/jobs/{job_id}" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.adversary_investigation.get_investigation_job(job_id="9f1c7f36-34af-416b-82b3-b496756f4d5e")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `job_id`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The unique identifier of the investigation.                                                                                                                                                                          |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3ThreathuntingInvestigationsJobsGetResponse](../../models/v3threathuntinginvestigationsjobsgetresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 409, 422         | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_investigation_job_results

Download the ZIP archive that contains a completed AI investigation's report and evidence. You can only retrieve the job results for an investigation you started. The archive is composed when you request it and is never stored.<br><br>Investigations that did not publish any findings or have passed their retention windows will return a “not found” response.<br><br>If an investigation’s ZIP archive is larger than 20 megabytes, you will receive a “payload too large” response. You can only retrieve the results for investigations that exceed this size limit within the Platform UI.<br><br>To use this endpoint, your organization must have access to the Adversary Investigation module.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-threathunting-investigations-jobs-results" method="get" path="/v3/threat-hunting/investigations/jobs/{job_id}/results" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.adversary_investigation.get_investigation_job_results(job_id="abfb0cd9-3719-491a-be31-8dbbaaff559c")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `job_id`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The unique identifier of the investigation.                                                                                                                                                                          |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3ThreathuntingInvestigationsJobsResultsResponse](../../models/v3threathuntinginvestigationsjobsresultsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 404, 409, 413, 422    | application/problem+json   |
| models.ErrorModel          | 500, 503, 504              | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_investigation_usage

Retrieve your organization's investigation limit, current usage, and the number of remaining investigations.<br><br>To use this endpoint, your organization must have access to the Adversary Investigation module.<br><br>This endpoint does not cost any credits to execute.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-threathunting-investigations-usage-get" method="get" path="/v3/threat-hunting/investigations/usage" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.adversary_investigation.get_investigation_usage()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3ThreathuntingInvestigationsUsageGetResponse](../../models/v3threathuntinginvestigationsusagegetresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 403, 409, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_tracked_scan

Initiate a scan to look for a currently unobserved service at a specific IP and port (`ip:port`) or hostname and port (`hostname:port`). This is equivalent to the [Live Discovery](https://docs.censys.com/docs/platform-threat-hunting-use-live-scan-and-rescan-to-validate-infrastructure#/) feature available in the UI, but you can also target web properties in addition to hosts.<br><br>The scan may take several minutes to complete. The response will contain a scan ID that you can use to [monitor the scan's status](https://docs.censys.com/reference/v3-threathunting-scans-get#/). After the scan completes, perform a lookup on the target asset to retrieve detailed scan information.<br><br>This endpoint is available to organizations that have access to the Adversary Investigation module. It costs 15 credits to execute this endpoint.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-threathunting-scans-discovery" method="post" path="/v3/threat-hunting/scans/discovery" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.adversary_investigation.create_tracked_scan(scans_discovery_input_body={
        "target": {
            "hostname_port": {
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
| `scans_discovery_input_body`                                                                                                                                                                                         | [models.ScansDiscoveryInputBody](../../models/scansdiscoveryinputbody.md)                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                  |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3ThreathuntingScansDiscoveryResponse](../../models/v3threathuntingscansdiscoveryresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_threats

Retrieve a list of active threats observed by Censys by aggregating threat IDs across hosts and web properties. Threats are active if their fingerprint has been identified on hosts or web properties by Censys scans. This information is also available on the [Explore Threats page in the Platform web UI](https://platform.censys.io/threats).<br><br>This endpoint is available to organizations that have access to the Adversary Investigation module.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-threathunting-threats-list" method="get" path="/v3/threat-hunting/threats" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.adversary_investigation.list_threats(query="*")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          | Example                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |                                                                                                                                                                                                                      |
| `query`                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | Optional CenQL filter to constrain threats list                                                                                                                                                                      | *                                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |                                                                                                                                                                                                                      |

### Response

**[models.V3ThreathuntingThreatsListResponse](../../models/v3threathuntingthreatslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## value_counts

Get counts of web assets for specific field-value pairs and combinations of field-value pairs. This is similar to the [CensEye functionality](https://docs.censys.com/docs/platform-threat-hunting-use-censeye-to-build-detections#/) available in the Platform web UI, but it allows you to define specific fields of interest rather than the [default fields](https://docs.censys.com/docs/platform-threat-hunting-use-censeye-to-build-detections#default-pivot-fields) leveraged by the tool in the UI.<br><br>Each array can only target fields within the same nested object and may contain at most 5 field-value pairs. For example, you can combine `host.services.port=80` and `host.services.protocol=SSH` in the same array, but you cannot combine `host.services.port=80` and `host.location.country="United States"` in the same array. You can input multiple arrays of objects in each API call.<br><br>To use this endpoint, your organization must have access to the Adversary Investigation module. This endpoint costs 1 credit per count condition (array of objects) included in the API call.

### Example Usage

<!-- UsageSnippet language="python" operationID="v3-threathunting-value-counts" method="post" path="/v3/threat-hunting/value-counts" -->
```python
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.adversary_investigation.value_counts(search_value_counts_input_body={
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

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `search_value_counts_input_body`                                                                                                                                                                                     | [models.SearchValueCountsInputBody](../../models/searchvaluecountsinputbody.md)                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                  |
| `organization_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                   | The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-find-and-use-your-organization-id-optional) for more information. |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[models.V3ThreathuntingValueCountsResponse](../../models/v3threathuntingvaluecountsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AuthenticationError | 401                        | application/json           |
| models.ErrorModel          | 400, 403, 422              | application/problem+json   |
| models.ErrorModel          | 500                        | application/problem+json   |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |