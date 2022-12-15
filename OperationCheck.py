from CalculatorExceptions import *

"""
Module containing all the operation validations (checks) for the supported operations on the calculator.
The main function (check_operations preforms the validation according to the given parameters,
and raises exceptions if needed.
"""


def check_binary(operand_a: float, operand_b: float) -> str or None:
    """
    The function checks if the operands given are operands.
    :param operand_a: first operand
    :param operand_b: second operand
    :return: None if the operands are valid, otherwise the exception code of missing operand.
    """
    if not (is_operand(operand_a) and is_operand(operand_b)):
        return "MON"


def check_unary(operand: float) -> str or None:
    """
    The function checks if the operand given is an operands.
    :param operand: operand
    :return: None if the operands are valid, otherwise the exception code of missing operand.
    """
    if not is_operand(operand):
        return "MON"


def check_div_modulo(operand_a: float, operand_b: float) -> str or None:
    """
    The function checks if the operands are valid for division.
    :param operand_a: first operand
    :param operand_b: second operand
    :return: None if the operands are valid, otherwise the exception code of the invalidity.
    """
    # checks if the operands are operands
    failed = check_binary(operand_a, operand_b)

    if not failed and operand_b == 0:
        return "ZD"
    return failed


def check_power(operand_a: float, operand_b: float) -> str or None:
    """
    The function checks if the operands are valid for power.
    :param operand_a: first operand
    :param operand_b: second operand
    :return: None if the operands are valid, otherwise the exception code of the invalidity.
    """
    # checks if the operands are operands
    failed = check_binary(operand_a, operand_b)

    if not failed and (operand_a <= 0 and 0 < operand_b < 1):
        return "PE"
    return failed


def check_factorial(operand: float) -> str or None:
    """
    The function checks if the operands are valid for factorial.
    :param operand: operand
    :return: None if the operands are valid, otherwise the exception code of the invalidity.
    """
    # checks if the operands are operands
    failed = check_unary(operand)

    if not failed and (operand <= 0 or not operand.is_integer()):
        return "FE"
    return failed


def check_operation(check_func, operator: str, index, *operands: float or str):
    """
    The function checks the validity of the operands according to the check function.
    If invalid, raises exception accordingly.
    :param check_func: check function to activate
    :param operator: the operator
    :param index: index of the operation in the equation (for the informative exception)
    :param operands: operands to validate
    """
    # checks if invalid
    exception_code = check_func(*operands)
    if exception_code:
        raise_exception(exception_code, (index, operator))


def is_operand(operand: float) -> bool:
    """
    The function checks if the given operand is a number (valid operand).
    :param operand: operand
    :return: True if valid, False otherwise
    """
    return type(operand) is float


ERROR_CODES = {"MON": (MissingOperandError, 2),
               "MOT": (MissingOperatorError, 1),
               "ZD": (DivisionOperandError, 1),
               "FE": (FactorialOperandError, 1),
               "PE": (PowerOperandsError, 1)}


def raise_exception(exception_code, exception_info: tuple[int, str]):
    """
    This function raises an exception according to the given exception code.
    :param exception_code: the exception code
    :param exception_info: the index and symbol where the exception occurred
    """
    exception, var_count = ERROR_CODES[exception_code]
    raise exception(*exception_info[:var_count])
