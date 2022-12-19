from configuration import INF
from CalculatorExceptions import MissingOperandError, DivisionOperandError, FactorialOperandError, \
                                 PowerOperandsError, UnsupportedValueError


"""
Module containing all the operation validations for the supported operations on the calculator.
The main function (check_operations preforms the validation according to the given parameters,
and raises exceptions if needed.
"""

__all__ = ["check_binary", "check_unary", "check_div_modulo", "check_power", "check_factorial", "check_operation"]


def check_binary(operand_a: float or str, operand_b: float or str) -> str or None:
    """
    The function checks if the operands given are operands.
    :param operand_a: First operand.
    :param operand_b: Second operand.
    :return: None if the operands are valid, otherwise the exception code of missing operand.
    """
    if not (is_operand(operand_a) and is_operand(operand_b)):
        return "MO"


def check_unary(operand: float or str) -> str or None:
    """
    The function checks if the operand given is an operands.
    :param operand: Operand.
    :return: None if the operands are valid, otherwise the exception code of missing operand.
    """
    if not is_operand(operand):
        return "MO"


def check_div_modulo(operand_a: float or str, operand_b: float or str) -> str or None:
    """
    The function checks if the operands are valid for division.
    :param operand_a: First operand.
    :param operand_b: Second operand.
    :return: None if the operands are valid, otherwise the exception code of the invalidity.
    """
    # checks if the operands are operands
    failed = check_binary(operand_a, operand_b)

    if not failed and operand_b == 0:
        return "ZD"
    return failed


def check_power(operand_a: float or str, operand_b: float or str) -> str or None:
    """
    The function checks if the operands are valid for power.
    :param operand_a: First operand.
    :param operand_b: Second operand.
    :return: None if the operands are valid, otherwise the exception code of the invalidity.
    """
    # checks if the operands are operands
    failed = check_binary(operand_a, operand_b)

    if not failed and (operand_a <= 0 and (0 < operand_b < 1 or -1 < operand_b < 0)):
        return "PE"
    return failed


def check_factorial(operand: float or str) -> str or None:
    """
    The function checks if the operands are valid for factorial.
    :param operand: Operand.
    :return: None if the operands are valid, otherwise the exception code of the invalidity.
    """
    # checks if the operands are operands
    failed = check_unary(operand)

    if not failed and (operand < 0 or not operand.is_integer()):
        return "FE"
    return failed


def check_operation(check_func, operator: str, index: int, *operands: float or str):
    """
    The function checks the validity of the operands according to the check function.
    If invalid, raises exception accordingly.
    :param check_func: Check function to activate.
    :param operator: The operator.
    :param index: Index of the operation in the equation (for the informative exception).
    :param operands: Operands to validate.
    :return: None.
    """
    # checks if invalid
    exception_code = check_func(*operands)
    if exception_code:
        raise_exception(exception_code, (index, operator))


def is_operand(operand: float or str) -> bool:
    """
    The function checks if the given operand is a supported number (valid operand).
    :param operand: Operand.
    :return: True if valid, False otherwise.
    """
    is_supported_value_operand(operand)
    return type(operand) is float


def is_supported_value_operand(operand: float or str):
    """
    This function checks if the value of the operand is an unsupported value (infinite). It raises an error accordingly.
    :param operand: Operand.
    :return: None
    """
    # if operand is too high or low, raise ValueError exception
    if operand == INF or operand == -INF:
        raise UnsupportedValueError()


# dictionary to match exception codes with their matching exception (the exception and the amount of vars for init)
ERROR_CODES = {"MO": (MissingOperandError, 2),
               "ZD": (DivisionOperandError, 1),
               "FE": (FactorialOperandError, 1),
               "PE": (PowerOperandsError, 1)}


def raise_exception(exception_code: str, exception_info: tuple[int, str]):
    """
    This function raises an exception according to the given exception code.
    :param exception_code: The exception code.
    :param exception_info: The index and symbol where the exception occurred.
    :return: None.
    """
    exception, var_count = ERROR_CODES[exception_code]
    raise exception(*exception_info[:var_count])
