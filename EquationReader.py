from OperationPreformer import preform_operation
from TreatMinusSigns import edit_minuses_in_equation
from CalculatorExceptions import MissingOperatorError, UnsupportedValueError
from configuration import *

"""
Reads equation list, and tries to solve it. Raises exceptions if misplaced operand or operator
"""


def generate_priority_lists() -> dict[int: list[str]]:
    """
    The function generates a dictionary of priority levels to lists of operands in this level, sorted from high to low.
    :return: The generated dictionary.
    """
    priority_dict = dict()

    for operator, (priority, _) in OPERATORS_PRIORITY_AND_TYPES.items():

        if priority in list(priority_dict.keys()):
            # adds to the list with this priority level (key)
            priority_dict[priority].append(operator)
        else:
            # first operator found from this priority level (key)
            # creates new key (priority level) with list value (the operators) and inserts the operator into it
            priority_dict[priority] = [operator]

    # sorts the dictionary by key value from high to low
    priority_dict = dict(reversed(sorted(priority_dict.items())))
    return priority_dict


# generates the dictionary from priority to list of operands
PRIORITY_LISTS = generate_priority_lists()


class EquationReader:
    """
    Class for Equation Reader. This reader reads the equation by the execution order and solves it accordingly.
    """
    def __init__(self, equation: list[str or float], index_to_brackets: int = -1):
        """
        Init function to create an EquationReader object.
        :param equation: The equation list (operands and operators).
        :param index_to_brackets: Only for brackets equation to follow the total index
        (the index of the opening bracket).
        """
        self.__equation = equation
        # list of variables in the current location (for index followup)
        self.__vars_in_index = [1] * len(equation)
        self.__index_to_brackets = index_to_brackets

    # getters
    def get_equation(self) -> list[str or float]:
        """
        Get function. This function returns the equation.
        :return: The equation.
        """
        return self.__equation

    def __get_right(self, index: int) -> str or float or None:
        """
        Get function. This function returns the variable on the right to the variable in the given index.
        :param index: The current index.
        :return: The value of the variable on the right, or None if there is no variable on the right.
        """
        if index < len(self.__equation) - 1:
            return self.__equation[index + 1]

    def __get_left(self, index: int) -> str or float or None:
        """
        Get function. This function returns the variable on the left to the variable in the given index.
        :param index: The current index.
        :return: The value of the variable on the left, or None if there is no variable on the left.
        """
        if index > 0:
            return self.__equation[index - 1]

    def __get_overall_index(self, list_index: int) -> int:
        """
        Get function. This function returns the overall index of the variable in the current index
        (the list modifies throw the solving process, and so does the indexes of the variables).
        The overall index is the index of the variables in the equation before starting to solve, it stays the same.
        :param list_index: The current index.
        :return: The index of the variable in the equation without starting to solve.
        """
        # starting index count from the equation start
        index = self.__index_to_brackets if self.__index_to_brackets != -1 else 0

        index += sum(self.__vars_in_index[:list_index])
        return index

    # static var to match operator type with operands index (relevant to the index)
    __OPERATOR_TYPES_VARS = {"BINARY": ((__get_left, __get_right), -1),
                             "UNARY_L": ((__get_right,), 0),
                             "UNARY_R": ((__get_left,), -1)}

    # solving
    def read_equation(self):
        """
        This function reads the equation according to the solving order and solves the equation step by step.
        :return: Equation result after reading and solving it.
        """
        self.__treat_brackets()

        # preforms the operations within the equation
        self.__solve_by_order()

        # the solution is the only equation variable left in the equation list after reading it.
        return self.__equation[0]

    def __check_equation_solution(self):
        """
        This function checks to see that the equation result is valid ( if there is more than one
        variable in the equation after finishing reading the equation, there is a missing operator).
        :return: None.
        """
        if len(self.__equation) > 1:
            raise MissingOperatorError(self.__get_overall_index(1))
        if not (-INF < self.__equation[0] < INF):
            raise UnsupportedValueError()

    def __solve_by_order(self):
        """
        This function replaces the operations with their solutions,
        one by one according to their priority order (high to low).
        :return: None.
        """
        # runs from the highest priority operators to lowest
        for operators in PRIORITY_LISTS.values():
            self.__minus_update()

            next_operator = self.__find_next(operators)
            # while there is a next operator to preform in this priority level
            while next_operator != -1:
                self.__insert_operation_solution(next_operator)
                next_operator = self.__find_next(operators, next_operator)
        # check the result
        self.__check_equation_solution()

    def __minus_update(self):
        """
        This function edits the minus signs in the equation, and updates the index followup.
        :return: None.
        """
        minus_updates = edit_minuses_in_equation(self.__equation)
        for update in minus_updates:
            self.__update_vars_in_index(*update)

    def __insert_operation_solution(self, operator_index: int):
        """
        The function replaces the operator and operands from the equation with their solution.
        :param operator_index: The operator's index.
        :return: None.
        """
        result, start_index, end_index = self.__get_operation_replacement_info(operator_index)

        # replaces the operator and operands with their result
        self.__equation[start_index: end_index + 1] = [result]
        self.__update_vars_in_index(start_index, end_index)

    def __update_vars_in_index(self, start: int, end: int):
        """
        This function updated the index's list (contains the amount of variables that were replaced from
        the original equation by their solutions in each current equation variable).
        :param start: The index of the first operation variable.
        :param end: The index of the last operation variable.
        """
        self.__vars_in_index[start: end + 1] = [sum(self.__vars_in_index[start: end + 1])]

    def __get_operation_replacement_info(self, index: int) -> tuple[float, int, int]:
        """
        This function gets the information required to replace the operation variables
        with their result (including the operation's solution).
        :param index: The operator's index.
        :return: The operation's result, it's starting index, it's ending index.
        """
        operator = self.__equation[index]
        operator_type = OPERATORS_PRIORITY_AND_TYPES[operator][1]
        # gets the get functions for the operation's operands
        # and the distance between the operation's start and the operators index
        operands_getters, start = self.__OPERATOR_TYPES_VARS[operator_type]
        start += index

        # creates a list of the operation's operands
        operation_operands = [get_var.__get__(self, type(self))(index) for get_var in operands_getters]

        result = preform_operation(operator, self.__get_overall_index(index), *operation_operands)
        return result, start, start + len(operation_operands)

    def __find_next(self, next_operators: list[str], from_index: int = 0) -> int:
        """
        The function gets an equation and a list of all the next possible operators to execute.
        It returns the index of the next operator to execute. if not found, returns -1.
        :param next_operators: List of the operators in the current priority (next operators to preform).
        :param from_index: The index of the last operator in this priority level that was executed
        (0 if none were executed yet).
        :return: The index of the next operator to execute, or -1 if not found.
        """
        # compares each equation var to the operators in current priority
        # if an operation from this priority level was already executed, no need to check all the vars before it again
        for i, var in enumerate(self.__equation[from_index:]):
            if var in next_operators:
                # returns index of the next operator to be operated
                return i + from_index
        # returns -1 if no next operator was found
        return -1

    # brackets handling
    def __find_brackets(self) -> tuple[int, int]:
        """
        This function finds the location of the inner brackets and returns their
        location (index of opening bracket and index of closing bracket)
        :return: Tuple of index of opening bracket and index of closing bracket.
        """
        for i, var in enumerate(self.__equation):
            if var == BRACKETS[0]:
                start = i
            elif var == BRACKETS[1]:
                return start, i

    def __treat_brackets(self):
        """
        This function replaces all the brackets sub equations in
        the equation with their result (solves the brackets first).
        :return: None.
        """
        while BRACKETS[0] in self.__equation:
            start, end = self.__find_brackets()
            self.__insert_brackets_equation(start, end)

    def __insert_brackets_equation(self, start: int, end: int):
        """
        This function solves the brackets equation located in between
        the given indexes, and replaces it with its result.
        :param start: Index of the opening bracket.
        :param end: Index of the closing bracket.
        :return: None.
        """
        brackets_equation = EquationReader(self.__equation[start + 1: end], self.__get_overall_index(start) + 1)
        # reads and solves the brackets equation
        brackets_equation.read_equation()

        self.__equation[start: end + 1] = brackets_equation.get_equation()
        self.__update_vars_in_index(start, end)
