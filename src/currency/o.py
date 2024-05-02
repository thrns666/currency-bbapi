import asyncio
import aiohttp


async def get_currency() -> list:
    url = 'https://belarusbank.by/api/kursExchange'

    print('0.py')

    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as resp:
            return await resp.json()

bb_api = asyncio.run(get_currency())
print(bb_api)
