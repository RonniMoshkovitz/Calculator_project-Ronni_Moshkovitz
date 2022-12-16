from MathematicsOperations import *
from OperationCheck import *

"""
Module to preform the mathematical operations supported by the calculator.
It matches the operator to its function, checks that it can be preformed, and preforms it if possible.
"""

# dictionary of all the calculation functions and the check function, for each operator
OPERATORS_FUNCS = {"+": (add, check_binary),
                   "-": (sub, check_binary),
                   "*": (mult, check_binary),
                   "/": (div, check_div_modulo),
                   "^": (power, check_power),
                   "%": (modulo, check_div_modulo),
                   "$": (maximum, check_binary),
                   "&": (minimum, check_binary),
                   "@": (avg, check_binary),
                   "~": (neg, check_unary),
                   "!": (factorial, check_factorial),
                   "#": (sum_digits, check_unary)
                   }


def preform_operation(operator: str, index: int, *operands: float or str) -> float:
    """
    The function gets an operator and its matching operands, and preforms it.
    :param operator: Operator.
    :param index: Index of the operator in the equation.
    :param operands: Matching operands.
    :return: The operation calculation result.
    """
    check_operation(OPERATORS_FUNCS[operator][1], operator, index, *operands)

    # if too many recursions or overflow, the result is so high that the calculation is too much.
    # in this case, the result is inf (infinity)
    try:
        return OPERATORS_FUNCS[operator][0](*operands)
    except (RecursionError, OverflowError):
        return float("inf")
