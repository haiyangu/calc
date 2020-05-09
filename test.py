import pytest


class Calc:

    def add(self, a: int, b: int):
        return a + b

    def div(self, a, b):
        return a / b


class TestCalcAdd:
    calc = Calc()

    def test_add_1(self):
        result = self.calc.add(10, 20)
        assert 30 == result


class TestCalcDiv:
    calc = Calc()

    def test_div_1(self):
        result = self.calc.div(20, 10)
        assert 2 == result


if __name__ == '__main__':
    pytest.main()
