from src.tokenize import tokenize


def resolve_groups(equation):

    """
    :param equation:
    :return:
    """

    ADDITION = "+"
    SUBSTRACTION = "-"
    MULTIPLICATION = "*"
    DIVISION = "/"

    o_equation = equation
    tokens = tokenize(equation)
    accum_tokens = tokens

    for operator in list([MULTIPLICATION, DIVISION, ADDITION, SUBSTRACTION]):

        total_tokens = len(accum_tokens)
        result = 0
        left_tokens = []
        right_tokens = []

        try:
            cursor = tokens.index(operator)

            left_cursor = cursor-1
            right_cursor = cursor + 1

            left_operand = float(accum_tokens[left_cursor])
            right_operand = float(accum_tokens[right_cursor])

            if operator == MULTIPLICATION:
                result = left_operand * right_operand

            if operator == DIVISION:
                result = left_operand / right_operand

            if operator == ADDITION:
                result = left_operand + right_operand

            if operator == SUBSTRACTION:
                result = left_operand - right_operand

            if left_cursor > 0:
                left_tokens = accum_tokens[0:left_cursor]

            if total_tokens >= right_cursor:
                right_tokens = accum_tokens[(right_cursor + 1):]

            accum_tokens = left_tokens + [str(result)] + right_tokens
            # print("left tokens", left_tokens)
            # print("right tokens", right_tokens)
            # print("accum tokens", accum_tokens)

            o_equation = ""

            for i, l in enumerate(accum_tokens):
                o_equation += l

            if len(accum_tokens) > 1:
                resolve_groups(o_equation)

        except:
            pass

    return float(o_equation)


if __name__ == "__main__":
    pass

__author__ = "jaziel lopez github.com/jazlopez"
__version__  = "1.0.0"
