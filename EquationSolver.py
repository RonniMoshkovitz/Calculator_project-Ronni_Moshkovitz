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
    :return: a tuple of the equation, and the result
    (if the equation was invalid, the result is an informative message of the cos)"""
    # parsing the equation string may raise a syntax error
    try:
        # crates a reader to read the equation
        equation_reader = EquationReader(convert_to_list(equation_str))
        # converts to string of the vars, separated by spaces to differ the indexes of the equation vars
        equation_str = " ".join(map(str, equation_reader.get_equation()))
        # reads the equation (solves it)
        equation_reader.read_equation()
    except SyntaxError as syntax:
        return equation_str, syntax.__str__()
    except ArithmeticError as math:
        return equation_str, math.__str__()

    return equation_str, equation_reader.get_equation()[0]
