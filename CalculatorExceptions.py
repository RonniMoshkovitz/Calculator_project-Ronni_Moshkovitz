"""
Calculator exceptions types.
"""


class EquationSyntaxError(SyntaxError):
    """
    Exception for claculator syntax errors (found in the parsing process)
    """

    __ERROR_MSG = {"NE": "Empty equation was entered",
                   "NS": "Not supported symbol",
                   "DE": "Invalid dot, dots cant be next to one another or without a digit behind",
                   "IB": "Invalid brackets, missing matching bracket"}

    def __init__(self, code: str, index: int = -1):
        """
        Inits the exception.
        :param code: message code
        :param index: exception index in the equation (if not mentioned = -1)
        """
        super().__init__(self.__ERROR_MSG[code] if index == -1 else f"{self.__ERROR_MSG[code]}\n\tin index: {index}")


class EquationMathError(ArithmeticError):
    """
    Exception for claculator mathematical errors (found in the reading process)
    """
    __ERROR_MSG = {"MON": "Missing operand",
                   "MOT": "Missing operator",
                   "ZD": "Can't divide by zero",
                   "FE": "Invalid factorial operand, factorial works on natural numbers only",
                   "PE": "Invalid power operand, negative number by the power of a fracture is a complex number, this calculator doesn't support complex numbers"}

    def __init__(self, code: str, index: int, operator: str = ""):
        """
        Inits the exception.
        :param code: message code
        :param index: exception index in the equation
        :param operator: the operator that raised the exception (if not mentioned -> empty string)
        """
        super().__init__(f"{self.__ERROR_MSG[code]}{operator}\n\tin index: {index}")
