# from tortoise import Tortoise
# from common.settings import TORTOISE_ORM
# from service.gdzw_service import GdzwService
# from api.tj_api import TjApid
from dddd import monitor
from d1 import xxx


async def main():
    # await init_orm()
    userinfo_dict = {1: ""}
    error_count = {}
    tasks = []
    tasks.append(asyncio.create_task(monitor(userinfo_dict, error_count)))
    tasks.append(asyncio.create_task(xxx(userinfo_dict, error_count)))
    # tasks.append(asyncio.create_task(GdzwService.run_ordersa(userinfo_dict)))
    # tasks.append(asyncio.create_task(GdzwService.login_scheduler(userinfo_dict)))
    # await GdzwService.run_orders(userinfo_dict)
    results = await asyncio.gather(*tasks)
    print(results)


if __name__ == '__main__':
    import asyncio

    # asyncio.run(init_orm())
    asyncio.get_event_loop().run_until_complete(main())
