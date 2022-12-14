"""
Classes for all the Exceptions that may be raised by the calculator program.
"""


# already exists, but I wanted to customize it.
class DivisionOperandError(ZeroDivisionError):
    """
    Exception class for invalid division operand.
    """
    def __init__(self, index: int):
        """
        Init function to init the exception.
        :param index: The index of where the exception occurred in the equation list.
        """
        ArithmeticError.__init__(self, f"Invalid division operand, Can't divide by zero, "
                                       f"for equation variable in index {index}")


class FactorialOperandError(ArithmeticError):
    """
    Exception class for invalid factorial operand.
    """
    def __init__(self, index: int):
        """
        Init function to init the exception.
        :param index: The index of where the exception occurred in the equation list.
        """
        ArithmeticError.__init__(self, f"Invalid factorial operand, factorial works on natural numbers only, "
                                       f"for equation variable in index {index}")


class PowerOperandsError(ArithmeticError):
    """
    Exception class for invalid power operand.
    """
    def __init__(self, index: int):
        """
        Init function to init the exception.
        :param index: The index of where the exception occurred in the equation list.
        """
        ArithmeticError.__init__(self, f"Invalid power operands, negative number by the power of a fracture "
                                       f"results in a complex number.\nThis calculator doesn't support complex "
                                       f"numbers, for equation variable in index {index}")


class MissingOperatorError(SyntaxError):
    """
    Exception class for missing operand.
    """
    def __init__(self, index: int):
        """
        Init function to init the exception.
        :param index: The index of where the exception occurred in the equation list.
        """
        SyntaxError.__init__(self, f"Missing operator, before equation variable in index {index}")


class MissingOperandError(SyntaxError):
    """
    Exception class for missing operator.
    """
    def __init__(self, index: int, symbol: str):
        """
        Init function to init the exception.
        :param index: The index of where the exception occurred in the equation list.
        :param symbol: The operator that is missing the operand.
        """
        SyntaxError.__init__(self, f"Missing operand, for {symbol} equation variable in index {index}")


class EmptyEquationError(SyntaxError):
    """
    Exception class Empty or white space only equation.
    """
    def __init__(self):
        """
        Init function to init the exception.
        """
        SyntaxError.__init__(self, "Invalid equation, empty equation was entered")


class UnsupportedSymbolError(SyntaxError):
    """
    Exception class for unsupported symbol (found in the equation).
    """
    def __init__(self, index: int, symbol: str):
        """
        Init function to init the exception.
        :param index: The index of where the exception occurred in the equation string.
        :param symbol: The unsupported symbol that caused the exception.
        """
        SyntaxError.__init__(self, f"Unsupported symbol {symbol}, in index {index}")


class InvalidDotError(SyntaxError):
    """
    Exception class for invalid dot.
    """
    def __init__(self, index: int):
        """
        Init function to init the exception.
        :param index: The index of where the exception occurred in the equation sting.
        """
        SyntaxError.__init__(self, f"Invalid dot, dots can only appear as part of an operand, in index {index}")


class MissingBracketError(SyntaxError):
    """
    Exception class for missing bracket.
    """
    def __init__(self):
        """
        Init function to init the exception.
        """
        SyntaxError.__init__(self, "Invalid brackets, missing matching bracket")


class EmptyBracketsError(SyntaxError):
    """
    Exception class for empty brackets error.
    """
    def __init__(self, index: int):
        """
        Init function to init the exception.
        :param index: The index of where the exception occurred in the equation sting.
        """
        SyntaxError.__init__(self, f"Invalid brackets, empty brackets were entered, in index {index}")


class UnsupportedValueError(ValueError):
    """
    Exception class for unsupported operation values (if entered value or calculation result value is infinity or
    minus infinity, the calculator doesn't support it).
    """
    def __init__(self):
        """
        Init function to init the exception.
        """
        ValueError.__init__(self, "Unsupported value (number too high or low) in equation, "
                                  "infinite numbers aren't supported by this calculator")
