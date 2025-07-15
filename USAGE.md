<!-- Start SDK Example Usage [usage] -->
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
        "page_token": "<next_page_token>",
        "query": "host.services: (protocol=SSH and not port: 22)",
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
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
            "page_token": "<next_page_token>",
            "query": "host.services: (protocol=SSH and not port: 22)",
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->