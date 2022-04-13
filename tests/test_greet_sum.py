"""
Author: your name
Date: 2022-04-13 21:27:41
LastEditTime: 2022-04-13 21:27:43
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /test_pytest/tests/test_greet_sum.py
"""
from lib.greet import print_num


def test_print():
    n = print_num(5)
    assert n == 5


def test_sum():
    n = print_num(6)
    assert n + 1 == 7
