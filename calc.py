class Calc:

    def add(self, a, b):
        if (isinstance(a, (int, float)) and isinstance(b, (int, float))) is True:
            return a + b
        else:
            raise ValueError("Only int and float are allowed!")

    def div(self, a, b):
        if (isinstance(a, (int, float)) and isinstance(b, (int, float))) is True:
            if ( b == 0):
                raise ZeroDivisionError("Can't divide by 0!")
            else:
                return a / b
        else:
            raise ValueError("Only int and float are allowed!")

