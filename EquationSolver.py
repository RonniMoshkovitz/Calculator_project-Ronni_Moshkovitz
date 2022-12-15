from EquationParser import *
from EquationReader import *

"""
Module to Solve the equation. from string equation to final results.
Also treats exceptions that might occur during the process.
"""


def solve_equation(equation_str: str) -> tuple[str, str or float]:
    """
    The function gets a string equation, reformats it, and solves it (tries to).
    :param equation_str: the input equation string
    :return: Tuple of the equation, and the result (if the equation is invalid,
    the result is an informative message of the cause)"""

    try:
        # crates a reader to read the equation
        equation_reader = EquationReader(convert_to_list(equation_str))
        # converts to string of the equation variables, separated by spaces
        # to differ the indexes of the equation variables
        equation_str = " ".join(map(str, equation_reader.get_equation()))
        # reads the equation (solves it)
        equation_reader.read_equation()

    except SyntaxError as syntax:
        return equation_str, syntax.__str__()
    except ArithmeticError as math:
        return equation_str, math.__str__()

    # the solution is the only equation variable left in the equation list after reading it.
    return equation_str, equation_reader.get_equation()[0]
