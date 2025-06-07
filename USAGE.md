<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from censys_platform import SDK


with SDK(
    organization_id="<id>",
    personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.global_data.search(search_query_input_body={
        "query": "<value>",
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
        organization_id="<id>",
        personal_access_token="<YOUR_BEARER_TOKEN_HERE>",
    ) as sdk:

        res = await sdk.global_data.search_async(search_query_input_body={
            "query": "<value>",
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->