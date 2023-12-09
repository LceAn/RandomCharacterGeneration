# -*-  coding : utf-8 -*-
# @Time : 2023/2/15 18:30
# @Autor : LceAn
# @File : PassRandom.py
# @Software : PyCharm
import random
import string
import time


# 定义一个颜色打印函数
def color_print(msg, color):
    print(f"\033[{color}m{msg}\033[0m")


# 输出彩色字符图案
color_print(r"""
 ____               ____                 _                 
|  _ \ __ _ ___ ___|  _ \ __ _ _ __   __| | ___  _ __ ___  
| |_) / _` / __/ __| |_) / _` | '_ \ / _` |/ _ \| '_ ` _ \ 
|  __/ (_| \__ \__ \  _ < (_| | | | | (_| | (_) | | | | | |
|_|   \__,_|___/___/_| \_\__,_|_| |_|\__,_|\___/|_| |_| |_|
                                   Random String Generator by LceAn
""", "1;36")


def generate_random_string(length=12, include_uppercase=True, include_special_chars=True, include_digits=True):
    letters = string.ascii_lowercase
    if include_uppercase:
        letters += string.ascii_uppercase
    if include_special_chars:
        letters += string.punctuation
    if include_digits:
        letters += string.digits

    return ''.join(random.choices(letters, k=length))


length = input("请输入随机字符串长度（默认为12）：")
length = int(length) if length else 12

include_uppercase = input("是否包含大小写字母？（默认为Y，输入N不包含）").lower() != "n"
include_special_chars = input("是否包含特殊字符？（默认为Y，输入N不包含）").lower() != "n"
include_digits = input("是否包含数字？（默认为Y，输入N不包含）").lower() != "n"

random_string = generate_random_string(length, include_uppercase, include_special_chars, include_digits)

print("随机字符串为：", random_string)
