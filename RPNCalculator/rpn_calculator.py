from operator import add, mul, sub, truediv

OPERATORS = {
    "+": add,
    "*": mul,
    "/": truediv,
    "-": sub,
}


class RpnCalculator(object):
    def __init__(self, expression: str):
        self.expression = expression

    @classmethod
    def eval_atomic(cls, operand1, operand2, operator):
        result = OPERATORS[operator](int(operand1), int(operand2))
        return str(result)

    def eval(self, expression: str) -> str:
        elements = expression.split()
        if len(elements) < 3:
            return expression.replace(" ", "\n")

        if len(elements) == 3:
            return self.eval_atomic(*elements)

        for i, element in enumerate(elements):
            if element in OPERATORS:
                result = self.eval_atomic(*elements[i-2:i+1])
                elements = elements[0:i-2] + [result] + elements[i+1:]
                return self.eval(" ".join(elements))
