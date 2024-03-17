import aiohttp
import re


async def getOutterIP():
    ip = ''
    try:

        async with aiohttp.ClientSession() as session:
            async with session.get(url='https://myip.ipip.net', timeout=5) as resp:
                data = await resp.text()
                print(data)
                ip = re.findall(r'(\d+\.\d+\.\d+\.\d+)', data)
                ip = ip[0] if ip else ''
    except:
        pass
    return ip


if __name__ == '__main__':
    import asyncio

    print(asyncio.get_event_loop().run_until_complete(getOutterIP()))
