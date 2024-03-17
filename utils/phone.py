import random


def telphone():
    second = random.choice([3, 4, 5, 7, 8])  # 第二位值，从此列表随机生成

    third = {
        3: random.randint(0, 9),
        4: random.choice([5, 7]),
        5: random.choice([0, 1, 2, 3, 5, 6, 7, 8, 9]),
        7: random.choice([6, 7, 8]),
        8: random.randint(0, 9)
    }[second]  # 根据second的值，来生成第3位的值

    behind = ''  # 定义个空字符串
    for i in range(8):
        behind = behind + str(random.randint(0, 9))  # 8位数字中的每一位从0-9中生成，8次循环后，字符串相加成为8位数
    phone_number = str(1) + str(second) + str(third) + behind  # 四组字符相加，生成手机号
    return phone_number
