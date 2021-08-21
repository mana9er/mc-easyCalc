from generated_parser import Lark_StandAlone, Transformer

class Calculator(Transformer):

    def get_first(self, x):
        return x[0]

    add1 = get_first
    mul1 = get_first
    pow1 = get_first
    unary2 = get_first

    def add2(self, x):
        if x[1] == '+':
            return x[0] + x[2]
        else:
            return x[0] - x[2]

    def mul2(self, x):
        if x[1] == '*':
            return x[0] * x[2]
        elif x[1] == '/':
            return x[0] / x[2]
        else:
            return x[0] % x[2]

    def pow2(self, x):
        return x[0] ** x[1]

    def unary1(self, x):
        if x[0] == '-':
            return -x[1]
        else:
            return x[1]

    def primary1(self, x):
        return x[0]

    def primary2(self, x):
        try:
            return int(x[0])
        except:
            return float(x[0])

    def primary3(self, x):
        return 0
