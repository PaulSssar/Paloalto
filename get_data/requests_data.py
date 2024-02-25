import aiohttp


async def request_get(url, headers=None):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url, headers=headers) as response:
            if response is None:
                return False
            data = await response.text()
            return data


async def request_post(url, data, headers):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.post(url, data=data, headers=headers) as response:
            return response
