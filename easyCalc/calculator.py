import math
from .generated_parser import Lark_StandAlone, Transformer


POW_LIMIT = 1e8
RET_LIMIT = 1e200


def _check(x):
    if abs(x) > RET_LIMIT:
        raise OverflowError()
    return x


class Calculator(Transformer):

    last_ans = 0

    def get_first(self, x):
        return x[0]


    add1 = get_first
    mul1 = get_first
    pow1 = get_first
    unary2 = get_first

    def add2(self, x):
        if x[1] == '+':
            return _check(x[0] + x[2])
        else:
            return _check(x[0] - x[2])

    def mul2(self, x):
        if x[1] == '*':
            return _check(x[0] * x[2])
        elif x[1] == '/':
            return _check(x[0] / x[2])
        else:
            return _check(x[0] % x[2])

    def pow2(self, x):
        if x[0] != 0 and x[1] != 0:
            logx0 = math.log(abs(x[0]))
            if x[1] * x[1] * logx0 * logx0 * math.log(abs(x[1])) > POW_LIMIT:
                raise OverflowError()
        return _check(x[0] ** x[1])

    def unary1(self, x):
        if x[0] == '-':
            return _check(-x[1])
        else:
            return _check(x[1])

    def primary1(self, x):
        return x[0]

    def primary2(self, x):
        try:
            return _check(int(x[0]))
        except:
            return _check(float(x[0]))

    def primary3(self, x):
        return Calculator.last_ans


def get_parser():
    parser = Lark_StandAlone(transformer=Calculator())
    return parser
