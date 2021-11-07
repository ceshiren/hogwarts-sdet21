"""
__author__ = 'hogwarts_xixi'
"""
from decimal import Decimal, ROUND_HALF_UP

import pytest

from pythoncode.calculator import Calculator


class TestCalculator:
    def setup_class(self):
        self.calc = Calculator()

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    def teardown_class(self):
        print("结束测试")

    def test_case1_add(self):
        assert 2 == self.calc.add(1, 1)

    def test_case2_add(self):
        assert 0.01 == self.calc.add(-0.01, 0.02)

    def test_case3_add(self):
        assert 10.02 == self.calc.add(10, 0.02)

    def change_to_decimal(self, num):
        # 四舍五入的运算模式
        return Decimal(f"{num}").quantize(Decimal('0.0000'), rounding=ROUND_HALF_UP)

    # 浮点数计算 Decimal 类型
    def test_case4_float1(self):
        result = self.calc.add(Decimal("0.1"), Decimal("0.2"))
        r = self.change_to_decimal(result)
        assert r == self.change_to_decimal(0.3)

    def test_case5_float(self):
        result = self.calc.add(0.1, 0.2)
        assert 0.3 == round(result, 4)

    @pytest.mark.parametrize('a,b,errortype', [
        ("*&", 0.2, "TypeError"), ("*&", 0.2, "ZeroDivisionError")])
    def test_case6_specl(self, a, b, errortype):
        # try:
        #     # assert result_expect == self.calc.add(a, b)
        #     1/0
        # except (TypeError,ZeroDivisionError):
        #     print("类型错误")
        with pytest.raises(eval(errortype)) as e:
            self.calc.add(a, b)
