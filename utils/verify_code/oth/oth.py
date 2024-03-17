# encoding=utf8
# 识别验证码-GIF

from PIL import Image
import ddddocr
from io import BytesIO
import time


# 获取GIF的各帧
def getJpg(img):
    im = Image.open(img)
    imgs = []
    try:
        while True:
            current = im.tell()
            img = im.convert('RGB')

            # 可以将各个帧图片保存出来观察一下
            # img_path = 'pics/' + str(current) + '.jpg'
            # img.save(img_path)

            # 将获取的图片放到列表里面，给后面合成图片用
            imgs.append(img)
            im.seek(current + 1)
    except:
        pass
    return imgs


# 多张图片合成一张
def conflate(img_paths):
    cage = []  # 笼子，把图片放进来合并，如果有两张就合并，一笼不容二虎
    num = 0
    for img in img_paths:
        num += 1
        cage.append(img)
        if len(cage) == 2:
            merge = Image.blend(cage[0], cage[1], 0.5)  # 合并两张图片，透明度0.5
            cage = [merge]  # 合并完,重置笼子
    # 把合成完的图片保存出来，只是为了看看结果，后续直接用merge识别就行了
    # merge.save("cage/intact.jpg")
    return merge


# 识别验证码x
def ivd(img):
    ocr = ddddocr.DdddOcr(
        # import_onnx_path=r'crnn\gdzw2\gdzw2_1.0_499_3000_2023-11-27-20-56-54.onnx',
        import_onnx_path=r'crnn\gdzw2\gdzw3_0.8888888888888888_15873_107000_2023-11-30-00-31-21.onnx',
        charsets_path=r'crnn\gdzw2\charsets.json',
        show_ad=False,
    )
    res = ocr.classification(img)
    # raise Exception(res)
    return res


def go(content):
    img = BytesIO(content)
    im = Image.open(img)
    # print(imgs)
    # merge = conflate(imgs)
    # # 获取黑色图像的每个像素点
    # pix = merge.load()
    # # 将黑色像素点变成白色像素点
    # for i in range(merge.size[0]):
    #     for j in range(merge.size[1]):
    #         if pix[i, j] == (0, 0, 0): pix[i, j] = (255, 255, 255)
    res = ivd(im)
    now = int(time.time() * 1000)
    im.save(f"cagg/{res}_{now}.jpg")
    return res


def go2(content, idx):
    imgs = getJpg(BytesIO(content))
    merge = conflate(imgs)
    res = ivd(merge)
    merge.save(f"cage_black/{idx}_{res}.jpg")
    # 获取黑色图像的每个像素点
    pix = merge.load()
    # 将黑色像素点变成白色像素点
    for i in range(merge.size[0]):
        for j in range(merge.size[1]):
            if pix[i, j] == (0, 0, 0): pix[i, j] = (255, 255, 255)
    # 保存处理后的白色图像
    merge.save(f"cage_white/{idx}_{res}.jpg")
    return res

# if __name__ == '__main__':
#     from xxx import aaa
#     from io import BytesIO
#     imgs = getJpg(BytesIO(aaa()))
#     merge = conflate(imgs)
#     res = ivd(merge)
#     print(res)
