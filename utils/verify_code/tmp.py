import requests
from PIL import Image
# import ddddocr
import time


# # 获取GIF的各帧
# def getJpg(img):
#     im = Image.open(img)
#     imgs = []
#     try:
#         while True:
#             current = im.tell()
#             img = im.convert('RGB')
#
#             # 可以将各个帧图片保存出来观察一下
#             # img_path = 'pics/' + str(current) + '.jpg'
#             # img.save(img_path)
#
#             # 将获取的图片放到列表里面，给后面合成图片用
#             imgs.append(img)
#             im.seek(current + 1)
#     except:
#         pass
#     return imgs
#
#
# # 多张图片合成一张
# def conflate(img_paths):
#     cage = []  # 笼子，把图片放进来合并，如果有两张就合并，一笼不容二虎
#     num = 0
#     for img in img_paths:
#         num += 1
#         cage.append(img)
#         if len(cage) == 2:
#             merge = Image.blend(cage[0], cage[1], 0.5)  # 合并两张图片，透明度0.5
#             cage = [merge]  # 合并完,重置笼子
#     # 把合成完的图片保存出来，只是为了看看结果，后续直接用merge识别就行了
#     merge.save("cage/intact.jpg")
#     return merge
#
#
# # 识别验证码
# def ivd(img):
#     ocr = ddddocr.DdddOcr()
#     res = ocr.classification(img)
#     return res


def get_gif():
    cookies = {
        '__jsluid_s': 'fcd88146d90dfce997e59a7ebfc679cd',
    }

    headers = {
        'Accept': 'image/avif,image/web,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'http://weather.sz.gov.cn/',
        'sec-ch-ua': 'Chromium;v=118, Google',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'Sec-Fetch-Dest': 'image',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
        # 'Cookie': '__jsluid_s=fcd88146d90dfce997e59a7ebfc679cd',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }

    # response = requests.get('http://Chrome;v=118, Not=A?Brand;v=99', cookies=cookies, headers=headers)

    params = {
        'source': 'pc',
        'gdbsuser': '14f0edb9c3674f8b897a66c5b71be25d',
        'r': int(time.time() * 1000),
    }
    response = requests.get(
        'https://weather.121.com.cn/szqx/api/twt/kfr/gryy/code.do',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    print(response.status_code)
    return response.content


if __name__ == '__main__':
    content = get_gif()
    with open("1.gif","wb") as f:
        f.write(content)
    # imgs = getJpg("1.gif")
    # merge = conflate(imgs)
    # res = ivd(merge)
    # print(res)
