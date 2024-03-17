import datetime
import json

import time

import requests
import httpx
import urllib.request
import gzip
import os


# os.environ['NO_PROXY'] = 'inline.app'
async def xx():
    url = "http://127.0.0.1/inlineapp/api/orders/test"
    start_time = datetime.datetime.now().strftime("%H:%M:%S")
    while True:

        response = requests.get(url)
        xx = response.json()
        for row in xx["data"]["data"]:
            print(row["req_b"])
            print(row["req_h"])
            # 获取余票
        headers = row["req_h"]
        json_data = row["req_b"]
        # params = {
        #     'companyId': '-MeNcbDasiIykiow2Hfb:inline-live-2',
        #     'branchId': '-N3JQxh1vIZe9tECk0Pg',
        # }
        if 'content-length' in headers:
            del headers['content-length']
        aa = 0
        while True:
            # time.sleep(2)
            aa += 1
            print(aa)

            start_time = datetime.datetime.now().strftime("%H:%M:%S")
            # req = urllib.request.Request(
            #     'https://inline.app/api/booking-capacitiesV3?&companyId=-MeNcbDasiIykiow2Hfb%3Ainline-live-2&branchId=-N3JQxh1vIZe9tECk0Pg',
            #     headers=headers)
            # f = urllib.request.urlopen(req)
            # # print(urllib.request.urlopen(response).read())
            # encoding = f.info().get('Content-Encoding')
            # if encoding == 'gzip':
            #     content = gzip.decompress(f.read())
            # else:
            #     content = f.read()
            # print(content)
            # datas = json.loads(str(content, 'utf-8'))
            print(headers)
            req = httpx.get(
                'https://inline.app/api/booking-capacitiesV3?companyId=-MeNcbDasiIykiow2Hfb%3Ainline-live-2&branchId=-N3JQxh1vIZe9tECk0Pg',
                headers=headers,
                verify=False,
                proxies="http://localhost:9090"
            )
            print(req.text)
            #
            # # raise Exception(111)
            # # datas = urllib.parse.urlencode(json.dumps(json_data)).encode('utf-8')
            # # req = urllib.request.Request(
            # #     'https://inline.app/api/reservations/booking',
            # #     headers=headers, data=datas)
            # print(datas)


async def main():
    # await init_orm()
    userinfo_dict = {1: ""}
    error_count = {}
    tasks = []
    tasks.append(asyncio.create_task(xx()))
    # tasks.append(asyncio.create_task(xxx(userinfo_dict, error_count)))
    # tasks.append(asyncio.create_task(GdzwService.run_ordersa(userinfo_dict)))
    # tasks.append(asyncio.create_task(GdzwService.login_scheduler(userinfo_dict)))
    # await GdzwService.run_orders(userinfo_dict)
    results = await asyncio.gather(*tasks)
    print(results)


if __name__ == '__main__':
    import asyncio

    # asyncio.run(init_orm())
    asyncio.get_event_loop().run_until_complete(main())
