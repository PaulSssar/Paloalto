import asyncio
import base64

import aiohttp


async def base64_encode(decoded_data):
    encoded_data = base64.standard_b64encode(decoded_data.encode())
    if encoded_data:
        encoded_data = encoded_data.decode('utf-8')
        return {'Authorization': 'Basic ' + encoded_data}
    return False

# async def get_token():
#     async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
#         async with session.post(url + '?type=keygen', data=data) as response:
#             token = await parse_xml(await response.text())
#             data_url = url + '?type=log&log-type=data&query='
#             xpankey = await base64_encode(f'{data["user"]}:{data["password"]}')
#             print(xpankey, token)
#         async with session.get(data_url, headers={
#             'Authorization': 'Basic' + xpankey,
#             'X-PAN-KEY': token
#         }
#                                ) as resp:
#             print(await resp.text())
#             return token
