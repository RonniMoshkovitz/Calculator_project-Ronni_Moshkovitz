from configuration import *
from CalculatorExceptions import EquationSyntaxError

"""
Module to validates the entered string, to be parsed.
It checks for invalid appearances in the equation and raises exceptions if needed.  
"""


def validate_input(equation_str: str) -> str:
    """
    The function removes extra spaces and tabs and checks for invalid symbols in the equation input string.
    May raise exception if needed (for invalid symbols, spaces, or missing brackets).
    :param equation_str: input equation
    :return: validated string equation (the input equation without extra minus signs, spaces and tabs)
    """
    # Removes extras
    equation_str = remove_extra_spaces(equation_str)

    # Checks for invalid symbols in the equation, may raise an exception accordingly
    check_validity(equation_str)

    return equation_str


def check_validity(equation_str: str):
    """
    Checks for invalid symbols in the equation string. It raises an exception if an invalid symbol is found, an empty
    string was entered, if an invalid dot was detected, or if there are missing brackets.
    :param equation_str: string of the equation
    """
    # Checks for empty equation
    if is_empty(equation_str):
        raise EquationSyntaxError("NE")

    for i, symbol in enumerate(equation_str):
        # Checks for invalid symbols
        if not is_valid_symbol(symbol):
            raise EquationSyntaxError("NS", i)
        # Checks for invalid dots
        if symbol is DOT and not is_valid_dot(equation_str, i):
            raise EquationSyntaxError("DE", i)

    # Checks for misplaced or missing brackets
    if not are_valid_brackets(equation_str):
        raise EquationSyntaxError("IB")


def remove_extra_spaces(equation_str: str) -> str:
    """
    The function removes extra spaces from the input string.
    :param equation_str: input equation string
    :return: the input equation without spaces and tabs
    """
    return "".join(equation_str.split())


def is_empty(equation_str: str) -> bool:
    """
    The function checks if the equation is an empty string.
    :param equation_str: equation string
    :return: True if its empty, False otherwise
    """
    return equation_str == ""


def is_valid_symbol(symbol: str) -> bool:
    """
    The function checks if the current symbol is valid (supported by the calculator)
    :param symbol: symbol in the equation
    :return: True if the symbol is valid, False otherwise
    """
    return symbol.isdigit() or symbol in OPERATORS + BRACKETS + DOT


def is_valid_dot(equation_str: str, index: int) -> bool:
    """
    The function checks if the current symbol is a valid dot.
    :param equation_str: string of the equation
    :param index: index of the dot
    :return: True if the dot is valid, False otherwise
    """
    # 12. is invalid:
    return index < len(equation_str) - 1 and equation_str[index + 1].isdigit()


def are_valid_brackets(equation_str: str, ) -> bool:
    """
    The function checks for missing brackets in the equation.
    :param equation_str: string of the equation
    :return: True if the brackets are valid, False for missing brackets
    """
    bracket_count = 0
    for symbol in equation_str:
        # A closing bracket was placed before an opening one (missing an opening bracket)
        if bracket_count < 0:
            return False
        # Counts opening and closing brackets in the equation ( adds one for opening ones and subs one for opening ones)
        if symbol == BRACKETS[0]:
            bracket_count += 1
        if symbol == BRACKETS[1]:
            bracket_count -= 1
    # Checks for missing bracket (missing closing brackets)
    return bracket_count == 0
