import datetime
import json
import asyncio

import os

os.environ['NO_PROXY'] = 'inline.app'
import aiohttp

import time

import httpx
import gzip

# url = "http://127.0.0.1/inlineapp/api/orderadd"
#
# form_data = {
#     "header": 'aa',
# }
# response = requests.post(url, data=form_data)
# print(response.text)
import requests

import time
import datetime
import tkinter as tk

zm = ['2024-03-09', '2024-03-10', '2024-03-16', '2024-03-17', '2024-03-23', '2024-03-24', '2024-03-30', '2024-03-31',
      '2024-04-06']
gzr = ['2024-03-08', '2024-03-11', '2024-03-12', '2024-03-13', '2024-03-14', '2024-03-15', '2024-03-18', '2024-03-19',
       '2024-03-20', '2024-03-21', '2024-03-22', '2024-03-25', '2024-03-26', '2024-03-27', '2024-03-28', '2024-03-29',
       '2024-04-01', '2024-04-02', '2024-04-03', '2024-04-04', '2024-04-05']


# 创建一个新的 Tk 对象，它是一个代表了窗口的对象
# root.withdraw()
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


def xxx(text):
    #
    # # 使用 messagebox.showinfo 创建一个信息弹窗
    # messagebox.showinfo("标题", "这是一个弹窗")
    # print("a")
    # # 运行主循环。这会阻塞，直到用户关闭窗口
    # # root.destroy()  # Close the root window and exit the mainloop
    # # root.mainloop()
    # # print("b")
    # # root.quit()  # 关闭消息框后退出mainloop
    # # # 创建按钮
    # # button = tk.Button(window, text="点击我弹出弹窗", command=show_popup)
    # # button.pack()
    # # # 进入主循环
    # # window.mainloop()

    root = tk.Tk()
    root.title("Window Title")

    # Set the window to stay on top
    root.attributes('-topmost', True)

    center_window(root)
    # Rest of your GUI code

    label = tk.Label(root, text=text, fg="red", justify="center")
    label.pack()
    root.mainloop()

order_list = [

    # {
    #     "name": "李昶諺",
    #     "phone": "+886968902286",
    #     "email": "1228597880@qq.com",
    #     "rule": "110010000",
    # },
    {
        "name": "王詠鈞",
        "phone": "+886968550815",
        "email": "",
        "rule": "0100010010000",
    },
    {
        "name": "黃雨歆",
        "phone": "+886900204256",
        "email": "hyx20070912@gmail.com",
        "rule": "1100011000100",
    },
    # {
    #     "xy": "别发中通",
    #     "name": "林禹彤",
    #     "phone": "+886953878677",
    #     "email": "e9090702@gmail.com",
    #     "rule": "0100001010100",
    # },
    {
        "xy": "别发中通",
        "name": "鍾瑞展",
        "phone": "+886986862729",
        "email": "1228597880@qq.com",
        "rule": "0100111010100",
    },
    {
        "name": "黃薏璇",
        "phone": "+886986633185",
        "email": "",
        "rule": "1100010000100",
    },
    {
        "name": "顏思嫻",
        "phone": "+886916932737",
        "email": "",
        "rule": "1100000000100",
    },
    # {
    #     "name": "任馨怡",
    #     "phone": "+886918007409",
    #     "email": "",
    #     "rule": "1000000000100",
    # },
    # {
    #     "name": "康珮妮",
    #     "phone": "+886916932737",
    #     "email": "",
    #     "rule": "1001011100100",
    # },
    # {
    #     "name": "何妤涵",
    #     "phone": "+886988322140",
    #     "email": "",
    #     "rule": "100000000",
    # },
    {
        "name": "李雨欣",
        "phone": "+886937673012",
        "email": "",
        "rule": "1100000000100",
    },
    {
        "name": "彭婉蓉",
        "phone": "+886909222917",
        "email": "s013765@yahoo.com.tw",
        "rule": "1100000000100",
    },
    {
        "name": "范雅淳",
        "phone": "+886965723224",
        "email": "",
        "rule": "1100000000100",
    },
    {
        "name": "张小姐",
        "phone": "+886976121610",
        "email": "",
        "rule": "1110010000100",
    },
    # {
    #     "name": "鄭宇軒",
    #     "phone": "+886958308680",
    #     "email": "",
    #     "rule": "1000000000100",
    # },
    # {
    #     "name": "張靜雯",
    #     "phone": "+886958114044",
    #     "email": "",
    #     "rule": "010000001",
    # },
    # {
    #     "name": "潘佳琪",
    #     "phone": "+886981366882",
    #     "email": "",
    #     "rule": "000000000000",
    # },
    {
        "xy": "帅哥帅哥",
        "name": "黃珮瑤",
        "phone": "+886900675279",
        "email": "peiyao530@gmail.com",
        "rule": "1000000000000",
    },
    # {
    #     "xy": "Fellows",
    #     "name": "黃薏璇",
    #     "phone": "+886953857989",
    #     "email": "",
    #     "rule": "010000001010",
    # },
    {
        "name": "董成庭",
        "phone": "+8617719903602",
        "email": "",
        "rule": "0110010000100",
    },
    # B
    {
        "xy": "不吃香芋派",
        "name": "龍芊",
        "phone": "+8615515072231",
        "email": "",
        "rule": "0000000001010",
    },
    {
        "xy": "我一张卡也不会再买",
        "name": "陳麗銀",
        "phone": "+886971880985",
        "email": "",
        "rule": "0000000000000",
    },
    {
        "xy": "一口西瓜",
        "name": "歐陽萱",
        "phone": "+886976246740",
        "email": "",
        "rule": "0000000001000",
    },
    {
        "xy": "橙子焦糖",
        "name": "袁亮天",
        "phone": "+8613203616383",
        "email": "",
        "rule": "1110000001000",
    },
    {
        "xy": "Ambition",
        "name": "陳泓瑄",
        "phone": "+886954016316",
        "email": "",
        "rule": "1000000001000",
    },
    {
        "xy": "薄荷糖管家peps",
        "name": "湯蘊庭",
        "phone": "+886988895143",
        "email": "",
        "rule": "0110010000000",
    },
    {
        "xy": "Zxyw",
        "name": "袁亮天",
        "phone": "+886902203521",
        "email": "",
        "rule": "1110010000100",
    },
    {
        "xy": "人傻钱多的笨蛋小米粥",
        "name": "熊妮",
        "phone": "+886966902167",
        "email": "",
        "rule": "1100010001001",
    },
    {
        "xy": "一逸逸逸",
        "name": "陳宗霆",
        "phone": "+886988239915",
        "email": "",
        "rule": "1100000001000",
    },
    {
        "xy": "南瓜玉米",
        "name": "鄭宇軒",
        "phone": "+886958308680",
        "email": "",
        "rule": "1000000001000",
    },
    {
        "xy": "小泉桃子",
        "name": "李雨欣",
        "phone": "+886937673012",
        "email": "",
        "rule": "1000000000000",
    },
    {
        "xy": "努力的小天才",
        "name": "徐子雁",
        "phone": "+886960587629",
        "email": "",
        "rule": "1110000001000",
    },
    {
        "xy": "圆佑百货店喜欢您来",
        "name": "王瑞蔻",
        "phone": "+886937087462",
        "email": "",
        "rule": "0100000001000",
    },
    {
        "xy": "事妈白菜精远离我",
        "name": "張靜雯",
        "phone": "+886958114044",
        "email": "",
        "rule": "1100000000000",
    },
    {
        "xy": "不吃了我真不吃了",
        "name": "余念恩",
        "phone": "+886935960504",
        "email": "",
        "rule": "1000000001000",
    },
    {
        "xy": "希尔星蹦极田螺",
        "name": "江東",
        "phone": "+886917261046",
        "email": "",
        "rule": "1110110101000",
    },
]

rule_idx = {'2024-03-14_11:00': [], '2024-03-14_13:00': [], '2024-03-14_15:00': [], '2024-03-14_17:00': [0, 10, 15], '2024-03-14_19:00': [0, 2, 10, 15], '2024-03-15_11:00': [4, 5, 6, 7, 9, 20, 23], '2024-03-15_13:00': [4, 5, 6, 7, 9, 20, 23], '2024-03-15_15:00': [9, 20], '2024-03-15_17:00': [0, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 20, 23], '2024-03-15_19:00': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 20, 23], '2024-03-16_11:00': [0, 1, 3, 4, 5, 6, 7, 9, 20, 23], '2024-03-16_13:00': [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 20, 23], '2024-03-16_15:00': [9, 20], '2024-03-16_17:00': [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 20, 23], '2024-03-16_19:00': [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 20, 23], '2024-03-17_11:00': [0, 1, 3, 4, 5, 6, 7, 9, 20, 23], '2024-03-17_13:00': [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 20, 23], '2024-03-17_15:00': [9, 20], '2024-03-17_17:00': [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 20, 23], '2024-03-17_19:00': [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 20, 23], '2024-03-18_11:00': [4, 5, 6, 7, 9, 20, 23], '2024-03-18_13:00': [4, 5, 6, 7, 9, 20, 23], '2024-03-18_15:00': [9, 20], '2024-03-18_17:00': [0, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 20, 23], '2024-03-18_19:00': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 20, 23], '2024-03-19_11:00': [9, 12, 14, 18, 19, 20, 22, 23, 24], '2024-03-19_13:00': [9, 12, 13, 14, 18, 19, 20, 21, 22, 23, 24], '2024-03-19_15:00': [9, 12, 14, 19, 20, 24], '2024-03-19_17:00': [0, 9, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25], '2024-03-19_19:00': [0, 9, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24], '2024-03-20_11:00': [9, 11, 12, 14, 18, 19, 20, 22, 23, 24], '2024-03-20_13:00': [9, 11, 12, 13, 14, 18, 19, 20, 21, 22, 23, 24], '2024-03-20_15:00': [9, 11, 12, 14, 19, 20, 24], '2024-03-20_17:00': [0, 9, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25], '2024-03-20_19:00': [0, 9, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24], '2024-03-21_11:00': [9, 12, 14, 18, 19, 20, 22, 23, 24], '2024-03-21_13:00': [9, 12, 13, 14, 18, 19, 20, 21, 22, 23, 24], '2024-03-21_15:00': [9, 12, 14, 19, 20, 24], '2024-03-21_17:00': [0, 9, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25], '2024-03-21_19:00': [0, 9, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24]}

async def check():
    local_url = "http://127.0.0.1/inlineapp/api/orders/test"
    while True:
        print("check -header")
        try:
            response = requests.get(local_url)
            break
        except:
            print("retry")
            time.sleep(0.1)

    xx = response.json()
    for row in xx["data"]["data"]:
        print(row["req_b"])
        print(row["req_h"])
        # 获取余票
    headers = row["req_h"]

    if 'content-length' in headers:
        del headers['content-length']

    while True:
        await asyncio.sleep(0.01)
        try:
            url = f'https://inline.app/api/booking-capacitiesV3?companyId=-MeNcbDasiIykiow2Hfb%3Ainline-live-2&branchId=-N3JQxh1vIZe9tECk0Pg'
            response = httpx.get(url, headers=headers)
            # print(response.text)
            datas = response.json()

            print("ok")
            return True
        except:
            print("not ok")
            return False


async def monitor(userinfo_dict, error_count):
    local_url = "http://127.0.0.1/inlineapp/api/orders/test"
    start_time = datetime.datetime.now().strftime("%H:%M:%S")
    while True:
        if 1 in error_count:
            del error_count[1]
        while True:
            print("get -header")
            try:
                response = requests.get(local_url)
                break
            except:
                print("retry")
                time.sleep(0.1)
        print(response.text)
        xx = response.json()
        for row in xx["data"]["data"]:
            print(row["req_b"])
            print(row["req_h"])
            # 获取余票
        headers = row["req_h"]
        # json_data = row["req_b"]
        # params = {
        #     'companyId': '-MeNcbDasiIykiow2Hfb:inline-live-2',
        #     'branchId': '-N3JQxh1vIZe9tECk0Pg',
        # }
        if 'content-length' in headers:
            del headers['content-length']
        aa = 0
        if 1 in error_count:
            del error_count[1]
        while True:
            aa += 1
            if not aa % 100: print(aa)
            await asyncio.sleep(0.01)


            # print(f"-- {ss} -- {ee}")
            try:
                url = f'https://inline.app/api/booking-capacitiesV3?_t=1008611&companyId=-MeNcbDasiIykiow2Hfb%3Ainline-live-2&branchId=-N3JQxh1vIZe9tECk0Pg'
                response = httpx.get(url, headers=headers)
                datas = response.json()
                # print(datas)
            except:
                print(aa)
                print(response.text)
                end_time = datetime.datetime.now().strftime("%H:%M:%S")

                print(f"2Error {start_time} -- {end_time}")

                error_count.update({1: 1})
                await asyncio.sleep(5)
                break
                # xxx(f"Error {start_time} -- {end_time}")
                # raise Exception(f"Error {start_time} -- {end_time}")

            stop = False
            for k, v in datas['default'].items():
                for kk, vv in v.get("times", {}).items():
                    # if vv: print(f"{k}-{kk}-{vv}")
                    if vv and vv[-1] > 1:
                        order_list = rule_idx.get(f"{k}_{kk}", [])
                        if not order_list: continue
                        with open(r'D:\tmp\k_kk', 'w') as f:
                            f.write(f"{k}_{kk}_{order_list[0]}")
                        userinfo_dict.update({1: f"{k}_{kk}_{order_list[0]}"})
                        await asyncio.sleep(0.1)
                        print(f"{k}-{kk}-{vv}")
                        stop = True
                        break
                if stop:
                    break
            else:
                userinfo_dict.update({1: ""})
