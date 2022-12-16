"""
Module to communicate with the user. It displays information, and gets user input.
This module supports communication with the user throw the terminal (ordinary input output)
"""

__all__ = ["get_equation", "display_welcome_msg", "display_info", "display_result"]

WELLCOME_MSG = """
Wellcome to the ADVANCED OMEGA CALCULATOR!\n
This calculator supports the following operations:\n
\t +: addition, in form of <operand>+<operand>\n
\t -: submission, in form of <operand>-<operand>\n
\t *: multiplication, in form of <operand>*<operand>\n
\t /: division, in form of <operand>/<operand>\n
\t ^: power, in form of <operand>^<operand>\n
\t $: maximum, in form of <operand>$<operand>\n
\t &: minimum, in form of <operand>&<operand>\n
\t @: average, in form of <operand>@<operand>\n
\t %: module, in form of <operand>%<operand>\n
\t ~: negative, in form of ~<operand>\n
\t !: factorial, in form of <operand>!\n
\t #: sum digits, in form of <operand>#\n
\n
To display the menu again, please enter: Menu\n
To exit, please enter: EXIT\n
"""


def get_input(msg: str) -> str:
    """
    The function shows the given message to the user, and gets his response input.
    :param msg: Message to show the user.
    :return: The user's input.
    """
    try:
        return input(msg)
    except (EOFError, KeyboardInterrupt) as e:
        display_info(f"{e} ---> exiting program...")
        exit(0)


def get_equation() -> str:
    """
    This function asks the user to enter an equation, and returns the users equation input.
    :return: The users equation string input.
    """
    return get_input("\nPlease enter your equation: ")


def display_welcome_msg():
    """
    This function shows the user the calculator's UI menu.
    :return: None.
    """
    print(WELLCOME_MSG)


def display_info(info: str):
    """
    This function shows the user the given info
    :param info: Information to show the user.
    :return: None.
    """
    print(info)


def display_solution(equation: str, solution: float):
    """
    This function shows the user the equation with its solution in an equation format.
    :param equation: The read equation.
    :param solution: The equation's solution.
    :return: None.
    """
    display_info(f"{equation} = {solution}")


def display_exception(equation: str, exception: str):
    """
    This function shows the user the equation with the exception message for why it failed to execute.
    :param equation: The read equation.
    :param exception: Exception message.
    :return: None.
    """
    display_info(f"{equation} ---> {exception}")
    get_input("\npress ENTER to continue...\n")


# dictionary to match result type with the matching presentation format
# (exception to exception display, and solution to solution display)
DISPLAY = {float: display_solution, str: display_exception}


def display_result(equation: str, result: float or str):
    """
    This function gets the equation and the calculation result. It presents it to the user accordingly.
    If failed to execute -> exception display. If managed to solve -> solution display.
    :param equation: The equation (the list equation as string of equation variables separated by spaces).
    :param result: Equation's solution or exception message.
    :return: None.
    """
    DISPLAY[type(result)](equation, result)
