"""
Module for all the Exception that can be raised by the calculator program.
"""


# already exists, but I wanted to keep my format throw the entire Error messages.
class DivisionOperandError(ZeroDivisionError):
    """
    Exception for invalid division operand.
    """
    def __init__(self, index: int):
        """
        Init function to init the exception.
        :param index: the index of where the exception occurred in the equation list
        """
        ArithmeticError.__init__(self, f"Invalid division operand, Can't divide by zero, in index {index}")


class FactorialOperandError(ArithmeticError):
    """
    Exception for invalid factorial operand.
    """
    def __init__(self, index: int):
        """
        Init function to init the exception.
        :param index: the index of where the exception occurred in the equation list
        """
        ArithmeticError.__init__(self, f"Invalid factorial operand, "
                                       f"factorial works on natural numbers only, in index {index}")


class PowerOperandsError(ArithmeticError):
    """
    Exception for invalid division operand.
    """
    def __init__(self, index: int):
        """
        Init function to init the exception.
        :param index: the index of where the exception occurred in the equation list
        """
        ArithmeticError.__init__(self, f"Invalid power operands, negative number by the power of a fracture results in"
                                       f"a complex number, this calculator doesn't support complex numbers, "
                                       f"in index {index}")


class MissingOperatorError(SyntaxError):
    """
    Exception for missing operand.
    """
    def __init__(self, index: int):
        """
        Init function to init the exception.
        :param index: the index of where the exception occurred in the equation list
        """
        SyntaxError.__init__(self, f"Missing operator, in index {index}")


class MissingOperandError(SyntaxError):
    """
    Exception for missing operator.
    """
    def __init__(self, index: int, symbol: str):
        """
        Init function to init the exception.
        :param index: the index of where the exception occurred in the equation list
        :param symbol: the operator that is missing the operand
        """
        SyntaxError.__init__(self, f"Missing operand for {symbol}, in index {index}")


class EmptyEquationError(SyntaxError):
    """
    Exception Empty or white space only equation.
    """
    def __init__(self):
        """
        Init function to init the exception.
        """
        SyntaxError.__init__(self, "Invalid equation, empty equation was entered")


class UnsupportedSymbolError(SyntaxError):
    """
    Exception for unsupported symbol (found in the equation).
    """
    def __init__(self, index: int, symbol: str):
        """
        Init function to init the exception.
        :param index: the index of where the exception occurred in the equation string
        :param symbol: the unsupported symbol that caused the exception.
        """
        SyntaxError.__init__(self, f"Unsupported symbol {symbol}, in index {index}")


class InvalidDotError(SyntaxError):
    """
    Exception for invalid dot.
    """
    def __init__(self, index: int):
        """
        Init function to init the exception.
        :param index: the index of where the exception occurred in the equation sting
        """
        SyntaxError.__init__(self, f"Invalid dot, dots cant be next to one another or without a digit behind"
                                   f", in index {index}")


class MissingBracketError(SyntaxError):
    """
    Exception for missing bracket.
    """
    def __init__(self):
        """
        Init function to init the exception.
        """
        SyntaxError.__init__(self, "Invalid brackets, missing matching bracket")
