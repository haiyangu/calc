import pytest

from calc import Calc

class TestCalcAddFunc():
    """
    A class used to test add function in class Calc.
    """

    calc = Calc()

    # 有效测试用例1
    # 相加的两个数都是整数
    test_data_for_add_validcase_1 = [(1, 2, 3), (-1, -2, -3), (1, -2, -1), (-1, 2, 1),
                                      (1, 0, 1), (0, 2, 2), (0, -2, -2), (-1, 0, -1), (0, 0, 0)]

    @pytest.mark.parametrize("x, y, expect", test_data_for_add_validcase_1)
    def test_add_validcase_1(self, x, y, expect):
        result = self.calc.add(x, y)
        assert expect == result

    # 有效测试用例2
    # 相加的两个数中有浮点数
    test_data_for_add_validcase_2 = [(1.1, 2.2, 3.3), (-1.1, -2.2, -3.3), (1.1, -2.2, -1.1), (-1.1, 2.2, 1.1),
                                      (1.1, 0, 1.1), (0, 2.2, 2.2), (0, -2.2, -2.2), (-1.1, 0, -1.1)]

    @pytest.mark.parametrize("x, y, expect", test_data_for_add_validcase_2)
    def test_add_validcase_2(self, x, y, expect):
        result = self.calc.add(x, y)
        assert expect == round(result, 1)

    # 无效测试用例1
    # 给定的参数中有非数字
    test_data_for_add_invalidcase_1 = [('a', 'b'), ('a', 2), (1, 'b')]

    @pytest.mark.parametrize("x, y", test_data_for_add_invalidcase_1)
    def test_add_invalidcase_1(self, x, y):
        with pytest.raises(ValueError) as ErrInfo:
            self.calc.add(x, y)
            print(ErrInfo.type)
        assert ErrInfo.type == ValueError

    # 无效测试用例2
    # 给定的参数个数大于两个
    def test_add_invalidcase_2(self):
        with pytest.raises(TypeError) as ErrInfo:
            self.calc.add(1, 2, 3)
            print(ErrInfo.type)
        assert ErrInfo.type == TypeError

    # 无效测试用例3
    # 给定的参数个数少于两个
    def test_add_invalidcase_3(self):
        with pytest.raises(TypeError) as ErrInfo:
            self.calc.add(1)
            print(ErrInfo.type)
        assert ErrInfo.type == TypeError

class TestCalcDivFunc():
    """
    A class used to test div function in class Calc.
    """
    calc = Calc()

    # 有效测试用例1
    # 两个参数都是非零整数且分母不为零
    test_data_for_div_validcase_1 = [(1, 2, 0.5), (-1, -2, 0.5), (1, -2, -0.5), (-2, 1, -2), (0, 2, 0), (0, -2, 0)]

    @pytest.mark.parametrize("x, y, expect", test_data_for_div_validcase_1)
    def test_div_validcase_1(self, x, y, expect):
        result = self.calc.div(x, y)
        assert expect == result

    # 有效测试用例2
    # 两个参数中有浮点数且分母不为零
    test_data_for_div_validcase_2 = [(1.4, 2, 0.7), (-1.5, -1.5, 1), (3, -1.5, -2), (-10, 3, -3.3)]

    @pytest.mark.parametrize("x, y, expect", test_data_for_div_validcase_2)
    def test_div_validcase_2(self, x, y, expect):
        result = self.calc.div(x, y)
        assert expect == round(result, 1)

    # 无效测试用例1
    # 分母为零
    test_data_for_div_invalidcase_1 = [(1, 0), (1.1, 0), (-1, 0), (-1.1, 0), (0, 0)]

    @pytest.mark.parametrize("x, y", test_data_for_div_invalidcase_1)
    def test_div_validcase_2(self, x, y):
        with pytest.raises(ZeroDivisionError) as ErrInfo:
            self.calc.div(x, y)
            print(ErrInfo.type)
        assert ErrInfo.type == ZeroDivisionError

    # 无效测试用例2
    # 给定的参数中有非数字
    test_data_for_div_invalidcase_2 = [('a', 'b'), ('a', 2), (1, 'b')]

    @pytest.mark.parametrize("x, y", test_data_for_div_invalidcase_2)
    def test_div_validcase_2(self, x, y):
        with pytest.raises(ValueError) as ErrInfo:
            self.calc.div(x, y)
            print(ErrInfo.type)
        assert ErrInfo.type == ValueError

    # 无效测试用例3
    # 给定的参数个数大于两个
    def test_div_invalidcase_3(self):
        with pytest.raises(TypeError) as ErrInfo:
            self.calc.div(1, 2, 3)
            print(ErrInfo.type)
        assert ErrInfo.type == TypeError

    # 无效测试用例4
    # 给定的参数个数少于两个
    def test_add_invalidcase_4(self):
        with pytest.raises(TypeError) as ErrInfo:
            self.calc.div(1)
            print(ErrInfo.type)
        assert ErrInfo.type == TypeError

if __name__ == '__main__':
    pytest.main()
