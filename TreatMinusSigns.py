import EquationReader as EquationReader
from configuration import *

"""
Module that treats the extra minus signs in the equation. It's main function 
(edit_minuses_in_equation) gets an EquationReader object and edits its minuses according to the 2nd approach.
"""

# minus signs can only come after an operators that are preformed on operands on their right (or nothing before)
# creates a list of all possible operators before minus signs
POSSIBLE_VARS_BEFORE = [operator for operator, (_, op_type) in OPERATORS_PRIORITY_AND_TYPES.items()
                        if operator != MINUS_SIGN and op_type == "BINARY" or op_type == "UNARY_L"]

# dictionary to match the amount of minuses to the replacement operator or operand sign (1 for odd, 0 for even)
SIGN_COUNT_DICT = {1: ("-", -1), 0: ("+", 1)}


def insert_sign(equation: list[str or float], index: int, count: int) -> int:
    """
    The function attaches the sign to the operand in the given index (according to the amount of minuses found before).
    :param equation: the equation that is edited
    :param index: the operand's index
    :param count: amount of minuses found
    :return: the amount of minuses removed from the equation
    """
    equation[index] *= SIGN_COUNT_DICT[count % 2][1]
    return count


def insert_operator(equation: list[str or float], index: int, count: int) -> int:
    """
    The function inserts the right operator in the given index (according to the amount of minuses found).
    :param equation: the equation that is edited
    :param index: the index to insert the operator
    :param count: amount of minuses found
    :return: the amount of operators removed from the equation
    """
    equation.insert(index, SIGN_COUNT_DICT[count % 2][0])
    return count - 1


# dictionary for the kinds of conversions (according to 2nd approach)
# True for operand sign conversion, False for operator conversion
CONVERSION = {True: insert_sign, False: insert_operator}


def is_sign_addition(equation: list[str or float], index: int) -> bool:
    """
    This function checks if the conversion is for operand sign.
    :param equation: the equation that is edited
    :param index: index of the variable before the first minus in the minus sequence
    :return: True if the conversion is to operand sign, False otherwise (for operator conversion)
    """
    return index == -1 or equation[index] in POSSIBLE_VARS_BEFORE


def is_minus_to_edit(var: float or str, right: float or str or None) -> bool:
    """
    This function checks if the given viable is a minus that needs to be edited.
    :param var: the equation var
    :param right: the var to the right of the equation var
    :return: True if is a minus that needs to be edited, False otherwise
    """
    return var is MINUS_SIGN and type(right) is float


def edit_minuses_in_equation(eq_reader: EquationReader):
    """
    This function edits the minus signs in the equation reader's equation according to the 2nd approach.
    :param eq_reader: equation reader to remove extra minuses from its equation
    """
    equation = eq_reader.get_equation()
    i = len(equation) - 1
    while i > -1:
        count = 0

        # Checks if every "-" in the equation is a minus sign
        while is_minus_to_edit(equation[i], eq_reader.get_right(i)) and i > -1:
            # removes and counts minus signs
            equation.pop(i)
            count += 1
            i -= 1
        # treats the minus signs if were found
        if count:
            to_insert = i + 1
            # dose the conversion
            count = CONVERSION[is_sign_addition(equation, i)](equation, to_insert, count)
            eq_reader.update_vars_in_index(to_insert, to_insert + count)
        i -= 1
