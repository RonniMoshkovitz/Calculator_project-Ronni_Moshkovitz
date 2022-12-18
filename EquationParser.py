from ValidateInput import validate_input
from configuration import *

"""
Module to parse string equation (input), to a list equation containing operands, operators and brackets.
if conversion is impossible, raises an exception.
"""


def parse_equation(equation_str: str) -> list[int or float]:
    """
    The function converts the input string equation into a calculable list format, containing operators and operands.
    :param equation_str: Input equation.
    :return: List equation (list of operators and operands).
    """
    equation_list = []

    # removes extra spaces and tabs. Might raise exceptions if invalid symbols are found.
    equation_str = validate_input(equation_str)

    index = 0
    while index < len(equation_str):
        index += convert_to_list_var(equation_str[index:], equation_list)

    return equation_list


def convert_to_list_var(equation_str: str, equation_list: list[str or float]) -> int:
    """
    The function gets part of the equation string (the first unconverted symbol to the end of the string), and converts
    the first part of the string to the matching list variable (operand as float, or operator as str).
    It then adds the converted part to the list.
    :param equation_str: Part of the input equation string (from the first unconverted symbol to the end of the string).
    :param equation_list: The list that represents the equation (in the equation format).
    :return: The amount of symbols that were converted and added to the equation list.
    """
    symbol = equation_str[0]
    # converts into operand
    if symbol.isdigit() or symbol == DOT:
        converted, operand = convert_to_operand(equation_str)
        equation_list.append(operand)
        return converted
    # converts into operator or bracket
    if symbol in OPERATORS + BRACKETS:
        equation_list.append(symbol)
        return 1


def convert_to_operand(operand_str: str) -> tuple[int, float]:
    """
    The function gets part of the equation string that starts with an operand. It then converts part of it
    (until it's the end of the operand) into an operand (float variable).
    :param operand_str: Part of the input equation string (from the start of an operand to the end of the string).
    :return: The converted operand and the index of the next variable in the equation (index in the operand string).
    """
    index = 0
    operand = operand_str[index]
    # runs on the operand string and checks where the operand ends (can no longer be converted into an operand)
    while index < len(operand_str):
        try:
            operand = float(operand_str[:index + 1])
        except ValueError:
            if not operand == DOT:
                break
        index += 1

    # accurate up to 10 digits apter the dot
    return index, round(operand, 10)
