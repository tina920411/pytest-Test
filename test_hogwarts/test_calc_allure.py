# -*- coding: utf-8 -*-
#-------------------------------
# @Time: 20-12-16  下午3:42
# @Author: tina
# @File: test_calc_allure.py
#-------------------------------
import pytest
import yaml
from Function_code.Calculator import Calculator


class TestCalc:
    """
    生成加减乘除四种方法，以及他们的setup和tesrdown
    """
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expect",
                             yaml.safe_load(open("./data_add.yaml"))["datas"],
                             ids=yaml.safe_load(open("./data_add.yaml"))["myid"])
    def test_add(self,a,b,expect,myfixture):
        print("正在执行 add 运算：%s + %s = %s" % (a,b,expect))
        assert expect == myfixture.add(a, b)

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a,b,expect",
                             yaml.safe_load(open("./data_sub.yaml"))["datas"],
                             ids=yaml.safe_load(open("./data_sub.yaml"))["myid"])
    def test_sub(self,a,b,expect,myfixture):
        print("正在执行 sub 运算：%s - %s = %s" % (a, b, expect))
        assert expect == myfixture.sub(a, b)

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expect",
                             yaml.safe_load(open("./data_mul.yaml"))["datas"],
                             ids = yaml.safe_load(open("./data_mul.yaml"))["myid"])
    def test_mul(self, a, b, expect, myfixture):
        print("正在执行 mul 运算：%s * %s = %s" % (a, b, expect))
        assert expect == myfixture.mul(a, b)

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expect",
                             yaml.safe_load(open("./data_div.yaml"))["datas"],
                             ids = yaml.safe_load(open("./data_div.yaml"))["myid"])
    def test_div(self, a, b, expect, myfixture):
        print("正在执行 div 运算：%s / %s = %s" % (a, b, expect))
        try:
            assert expect == myfixture.div(a, b)
        except ZeroDivisionError as e:
            print(e)
            print("警告：除数不能为0")

if __name__ == '__main__':
    pytest.main(['test_calc_allure.py', '-sv'])
