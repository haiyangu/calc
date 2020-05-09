import pytest

from calc import Calc

class TestCalcAddFunc():
    """
    A class used to test add function in class Calc.
    """
    calc = Calc()
    test_data_for_add_validcase_01 = [(1, 2, 3), (-1, -2, -3), (1, -2, -1), (-1, 2, 1),
                                      (1, 0, 1), (0, 2, 2), (0, -2, -2), (-1, 0, -1), (0, 0, 0)]

    @pytest.mark.parametrize("x, y, expect", test_data_for_add_validcase_01)
    def test_add_validcase_01(self, x, y, expect):
        result = self.calc.add(x, y)
        assert expect == result

    test_data_for_add_validcase_02 = [(1.1, 2.2, 3.3), (-1.1, -2.2, -3.3), (1.1, -2.2, -1.1), (-1.1, 2.2, 1.1),
                                      (1.1, 0, 1.1), (0, 2.2, 2.2), (0, -2.2, -2.2), (-1.1, 0, -1.1)]

    @pytest.mark.parametrize("x, y, expect", test_data_for_add_validcase_02)
    def test_add_validcase_02(self, x, y, expect):
        result = self.calc.add(x, y)
        assert expect == round(result, 1)

    test_data_for_add_invalidcase_03 = [('a', 'b'), ('a', 2), (1, 'b')]

    @pytest.mark.parametrize("x, y", test_data_for_add_invalidcase_03)
    def test_add_invalidcase_03(self, x, y):
        with pytest.raises(ValueError) as ErrInfo:
            self.calc.add(x, y)
            print(ErrInfo.type)
        assert ErrInfo.type == ValueError

    def test_add_invalidcase_04(self):
        with pytest.raises(TypeError) as ErrInfo:
            self.calc.add(1, 2, 3)
            print(ErrInfo.type)
        assert ErrInfo.type == TypeError

    def test_add_invalidcase_05(self):
        with pytest.raises(TypeError) as ErrInfo:
            self.calc.add(1)
            print(ErrInfo.type)
        assert ErrInfo.type == TypeError

class TestCalcDivFunc():
    """
    A class used to test div function in class Calc.
    """
    calc = Calc()

    def test_div_validcase_01(self):
        result = self.calc.div(30, 10)
        assert 3 == result


if __name__ == '__main__':
    pytest.main()
