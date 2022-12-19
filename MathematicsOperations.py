"""
Module containing all the mathematics operations functions supported on this calculator.
"""


def add(operand_a: float, operand_b: float) -> float:
    """
    The function preforms addition of two operands, and returns the result.
    :param operand_a: First operand.
    :param operand_b: Second operand.
    :return: Addition result.
    """
    return operand_a + operand_b


def sub(operand_a: float, operand_b: float) -> float:
    """
    The function preforms subtraction on two operands, and returns the result.
    :param operand_a: First operand.
    :param operand_b: Second operand.
    :return: Subtraction result.
    """
    return operand_a - operand_b


def mult(operand_a: float, operand_b: float) -> float:
    """
    The function preforms multiplication of two operands, and returns the result.
    :param operand_a: First operand.
    :param operand_b: Second operand.
    :return: Multiplication result.
    """
    return operand_a * operand_b


def div(operand_a: float, operand_b: float) -> float:
    """
    The function preforms division on two operands, and returns the result.
    :param operand_a: First operand.
    :param operand_b: Second operand.
    :return: Division result.
    """
    return operand_a / operand_b


def power(operand_a: float, operand_b: float) -> float:
    """
    The function preforms the first operand by the power of the second operand, and returns the result.
    :param operand_a: First operand.
    :param operand_b: Second operand.
    :return: Power result.
    """
    return pow(operand_a, operand_b)


def modulo(operand_a: float, operand_b: float) -> float:
    """
    The function preforms modulo on two operands, and returns the result.
    :param operand_a: First operand.
    :param operand_b: Second operand.
    :return: Modulo result.
    """
    return operand_a % operand_b


def maximum(operand_a: float, operand_b: float) -> float:
    """
    The function returns the operand with the higher value.
    :param operand_a: First operand.
    :param operand_b: Second operand.
    :return: Operand with the higher value.
    """
    return operand_a if operand_a > operand_b else operand_b


def minimum(operand_a: float, operand_b: float) -> float:
    """
    The function returns the operand with the lower value.
    :param operand_a: First operand.
    :param operand_b: Second operand.
    :return: Operand with the lower value.
    """
    return operand_a if operand_a < operand_b else operand_b


def avg(operand_a: float, operand_b: float) -> float:
    """
    The function returns the average of the operands.
    :param operand_a: First operand.
    :param operand_b: Second operand.
    :return: Average of operands.
    """
    return (operand_a + operand_b) / 2


def neg(operand: float) -> float:
    """
    The function returns the negative value to the operand.
    :param operand: Operand.
    :return: Negative value to the operand.
    """
    return -operand


def factorial(operand: float) -> float:
    """
    The function returns the factorial of the operand.
    :param operand: Operand.
    :return: Factorial result.
    """
    if operand == 1 or operand == 0:
        return 1.0
    # runs recursively and multiples by all the natural nums from 1 to the operand
    return factorial(operand - 1) * operand


def sum_digits(operand: float) -> float:
    """
    This function gets returns the sum of all the digits in the operand.
    :param operand: operand.
    :return: Sum of the digits.
    """
    # if operand is long enough to be displayed with an e, the # sums the digits in this number.
    # for example: 1e+306# = 1 + 3 + 0 + 6 = 10
    operand_str = str(operand)
    # runs on all the digits in the operand, and only if it really a digit, it adds it to a list, then it sums this list
    sum_dig = float(sum([float(digit) for digit in operand_str if digit.isdigit()]))
    return sum_dig if operand >= 0 else -sum_dig
