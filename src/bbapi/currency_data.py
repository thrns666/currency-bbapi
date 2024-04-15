import aiohttp


async def get_currency():
    # BelaBank api url here
    url = ''

    with aiohttp.ClientSession() as session:
        response = await session.get(url=url)

    return response
