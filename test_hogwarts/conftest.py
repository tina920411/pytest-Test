# -*- coding: utf-8 -*-
# -------------------------------
# @Time: 20-12-16  下午3:34
# @Author: tina
# @File: conftest.py
# -------------------------------

import pytest
from Function_code.Calculator import Calculator



@pytest.fixture(scope="module")
def myfixture():
    print()
    print("×××××××××开始计算×××××××××")
    calc = Calculator()

    print("===============我的第一个myfixture============")
    yield calc
    print("×××××××××计算结束×××××××××")
    print()
