from EquationSolver import *
from InputOutput import *
"""
The main module of the calculator app. In charge of the UI factuality.
"""


def exit_calc():
    """
    This function displays a goodbye message and exits the program.
    """
    display_info("Good Bye!")
    exit(0)


# dictionary for all the program commands
PROGRAM_COMMANDS = {"EXIT": exit_calc, "MENU": display_welcome_msg}


def check_for_program_command(command: str):
    """
    This function checks if the entered info is a program command. If it is, it activates the command's function.
    :param command: the user's input
    :return: True if the command is a program command, False otherwise
    """
    command = command.upper()
    if command in PROGRAM_COMMANDS.keys():
        PROGRAM_COMMANDS[command]()
        return True
    return False


def main():
    """
    The main function of the calculator.
    This function gets equations and solves them (if possible, if not shows informative message about the error).
    It also follows some program commands.
    """
    display_welcome_msg()
    while True:
        equation = get_equation()
        if not check_for_program_command(equation):
            display_result(*solve_equation(equation))


if __name__ == '__main__':
    main()
