# pip3 install opencv-contrib-python==4.5.1.48
# https://cloud.tencent.com/developer/article/1577435
# https://github.com/tesseract-ocr/tesseract
# http://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-4.00.00dev.exe
# https://blog.51cto.com/u_15784290/5660498
# SET TESSDATA_PREFIX=D:\Program Files (x86)\Tesseract-OCR\tessdata
import cv2 as cv
import pytesseract
from PIL import Image
from lxml import html
import numpy as np

etree = html.etree

# pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


# 使用opencv进行图像识别来识别 数字+字母验证码，从而实现登陆
def recognize_text(content):
    # image = cv.imread(r'./a.png')
    image = cv.imdecode(np.fromstring(content, np.uint8), 1)
    # 边缘保留滤波  去噪
    blur = cv.pyrMeanShiftFiltering(image, sp=8, sr=60)
    # cv.imshow('dst', blur)
    # 灰度图像
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    # 二值化
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    # print(f'二值化自适应阈值：{ret}')
    # cv.imshow('binary', binary)
    # 形态学操作  获取结构元素  开操作
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 2))
    bin1 = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    # cv.imshow('bin1', bin1)
    kernel = cv.getStructuringElement(cv.MORPH_OPEN, (2, 3))
    bin2 = cv.morphologyEx(bin1, cv.MORPH_OPEN, kernel)
    # cv.imshow('bin2', bin2)
    # 逻辑运算  让背景为白色  字体为黑  便于识别
    cv.bitwise_not(bin2, bin2)
    # cv.imshow('binary-image', bin2)
    # 识别
    test_message = Image.fromarray(bin2)
    text = pytesseract.image_to_string(test_message)
    # cv.destroyAllWindows()
    # print(f'识别结果：{text}')
    # print(text.strip())  # 使用strip()函数去掉末尾残留的奇怪字符
    return text


# print(recognize_text())
# cv.destroyAllWindows()
