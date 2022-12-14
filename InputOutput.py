"""
Module to communicate with the user. It displays information, and gets user input.
This module supports communication with the user throw the terminal (ordinary input output)
"""

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
    :param msg: message to show the user
    :return: the user's input
    """
    try:
        user_input = input(msg)
    except (EOFError, KeyboardInterrupt) as e:
        display_info(f"{e} ---> exiting program...")
        exit(1)

    return user_input


def get_equation() -> str:
    """
    This function asks the user to enter an equation, and returns the users equation input.
    :return: the users equation string input
    """
    return get_input("\nPlease enter your equation: ")


def display_welcome_msg():
    """
    This function shows the user the calculator's UI menu
    """
    print(WELLCOME_MSG)


def display_info(info: str):
    """
    This function shows the user the given info
    :param info: information to show the client
    """
    print(info)


def display_solution(equation: str, solution: float):
    """
    This function shows the user the equation with its solution in an equation format.
    :param equation: the read equation
    :param solution: the equation's solution
    """
    display_info(f"{equation} = {solution}")


def display_exception(equation: str, exception: str):
    """
    This function shows the user the equation with the exception message for why it failed to execute.
    :param equation: the read equation
    :param exception: exception message
    """
    display_info(f"{equation} ---> {exception}")
    get_input("\npress ENTER to continue...\n")


# dictionary to match result type with the matching presentation format
# (exception to exception display, and solution to solution display)
DISPLAY = {float: display_solution, str: display_exception}


def display_result(equation: str, result: float or str):
    """
    This function gets the equation and the calculation result. It presents it to the client accordingly.
    If failed to execute -> exception display. If managed to solve -> solution display.
    :param equation: the read equation
    :param result: equation's solution or exception message
    """
    DISPLAY[type(result)](equation, result)
