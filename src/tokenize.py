def tokenize(stmt):
    """

    :param stmt:
    :return:
    """
    i = 0
    operand_value = ""
    operands = []

    while i < len(stmt):
        cursor = stmt[i]

        if cursor.isdigit():
            operand_value += cursor
        else:
            operands.append(operand_value)
            operands.append(cursor)
            operand_value = ""
        i += 1

    if len(operand_value):
        operands.append(operand_value)

    return operands

if __name__ == "__main__":
    pass

__author__ = "jaziel lopez github.com/jazlopez"
__version__  = "1.0.0"

