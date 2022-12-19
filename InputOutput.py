"""
Module to communicate with the user. It displays and styles information, and gets user input.
This module supports communication with the user throw the terminal (basic input output).
"""

__all__ = ["get_equation", "display_welcome_msg", "display_info", "display_result"]

# dictionary to define styles to implement in output string
STYLES = {"blue": "\033[94m",
          "cyan": "\033[96m",
          "green": "\033[92m",
          "yellow": "\033[93m",
          "red": "\033[91m",
          "bold": "\033[1m",
          "underline": "\033[4m",
          "end_style": "\033[0m"}

# the welcome message (also the menu)
WELCOME_MSG = f"""
{STYLES["underline"]}{STYLES["blue"]}Welcome to the ADVANCED OMEGA CALCULATOR!{STYLES["end_style"]}\n
{STYLES["cyan"]}This calculator supports the following operations:{STYLES["end_style"]}\n
\t +: addition, in form of {STYLES["cyan"]}<operand>+<operand>{STYLES["end_style"]}\n
\t -: submission, in form of {STYLES["cyan"]}<operand>-<operand>{STYLES["end_style"]}\n
\t *: multiplication, in form of {STYLES["cyan"]}<operand>*<operand>{STYLES["end_style"]}\n
\t /: division, in form of {STYLES["cyan"]}<operand>/<operand>{STYLES["end_style"]}\n
\t ^: power, in form of {STYLES["cyan"]}<operand>^<operand>{STYLES["end_style"]}\n
\t $: maximum, in form of {STYLES["cyan"]}<operand>$<operand>{STYLES["end_style"]}\n
\t &: minimum, in form of {STYLES["cyan"]}<operand>&<operand>{STYLES["end_style"]}\n
\t @: average, in form of {STYLES["cyan"]}<operand>@<operand>{STYLES["end_style"]}\n
\t %: module, in form of {STYLES["cyan"]}<operand>%<operand>{STYLES["end_style"]}\n
\t ~: negative, in form of {STYLES["cyan"]}~<operand>{STYLES["end_style"]}\n
\t !: factorial, in form of {STYLES["cyan"]}<operand>!{STYLES["end_style"]}\n
\t #: sum digits, in form of {STYLES["cyan"]}<operand>#{STYLES["end_style"]}\n
To display the menu again, please enter: {STYLES["blue"]}MENU{STYLES["end_style"]}\n
To exit, please enter: {STYLES["yellow"]}EXIT{STYLES["end_style"]}\n
------------------------------------------------------------\n
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
        display_info(f"{STYLES['yellow']}{e} ---> exiting program...{STYLES['end_style']}")
        exit(0)


def get_equation() -> str:
    """
    This function asks the user to enter an equation, and returns the users equation input.
    :return: The users equation string input.
    """
    return get_input("Please enter your equation: ")


def display_welcome_msg():
    """
    This function shows the user the calculator's UI menu.
    :return: None.
    """
    display_info(WELCOME_MSG)


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
    display_info(f"{STYLES['green']}{equation} = {solution}{STYLES['end_style']}")


def display_exception(equation: str, exception: str):
    """
    This function shows the user the equation with the exception message for why it failed to execute.
    :param equation: The read equation.
    :param exception: Exception message.
    :return: None.
    """
    display_info(f"{STYLES['red']}{equation} ---> {exception}{STYLES['end_style']}")
    get_input(f"\npress {STYLES['bold']}ENTER{STYLES['end_style']} to continue...")


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
    display_info("\n--------------------------------------------------------------------------------------------\n")
