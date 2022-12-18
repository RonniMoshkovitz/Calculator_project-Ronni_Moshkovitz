from EquationParser import parse_equation
from EquationReader import EquationReader

"""
Module to Solve the equation. from string equation to final results.
Also treats exceptions that might occur during the process.
"""


def solve_equation(equation_str: str) -> tuple[str, str or float]:
    """
    The function gets a string equation, parses it (turns it into calculable list of operators and operands),
    and solves it (tries to). It returns the result of the equation (solution or exception message).
    :param equation_str: The input equation string.
    :return: Tuple of the equation, and the result (if the equation is invalid,
    the result is an informative message of the cause).
    """
    try_result = try_to_parse(equation_str)
    # if the input is valid, the try_result contains the parsed equation (list of operators and operands)
    if type(try_result) is list:
        equation_reader = EquationReader(try_result)

        # converts to string of the equation variables, separated by spaces
        # to differ the indexes of the equation variables
        equation_str = " ".join(map(str, try_result))

        try_result = try_to_solve(equation_reader)
    return equation_str, try_result


def try_to_parse(equation_str: str) -> list[float or str] or str:
    """
    This function tries to parse the equation string. if it fails, it returns an informative message of the reason.
    :param equation_str: The equation string.
    :return: The parsed equation (equation_list) if solvable, or the exception message (reason for failure) otherwise.
    """
    try:
        return parse_equation(equation_str)
    except SyntaxError as syntax:
        return f"SyntaxError: {syntax}"


def try_to_solve(reader: EquationReader) -> float or str:
    """
    This function tries to solve the reader's equation. if it fails, it returns an informative message of the reason.
    :param reader: The EquationReader with the equation to solve.
    :return: The equations solution (if solvable), the exception message (reason for failure) otherwise.
    """
    try:
        # try to solve equation
        return reader.read_equation()

    except SyntaxError as syntax:
        return f"SyntaxError: {syntax}"

    except ArithmeticError as arithmetic:
        return f"ArithmeticError: {arithmetic}"
