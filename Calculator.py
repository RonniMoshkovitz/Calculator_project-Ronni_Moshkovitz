from EquationSolver import solve_equation
from InputOutput import *
"""
The main module of the calculator app. In charge of the UI functionality.
"""


def exit_calc():
    """
    This function displays a goodbye message and exits the program.
    :return: None.
    """
    display_info("Thank you for using this calculator, see you next time!")
    exit(0)


# dictionary for all the program commands
PROGRAM_COMMANDS = {"EXIT": exit_calc, "MENU": display_welcome_msg}


def check_for_program_command(command: str):
    """
    This function checks if the entered info is a program command. If it is, it activates the command's function.
    :param command: The user's input.
    :return: True if the command is a program command, False otherwise.
    """
    command = command.upper()
    # preform command if is a program command
    if command in PROGRAM_COMMANDS.keys():
        PROGRAM_COMMANDS[command]()
        return True
    return False


def main():
    """
    The main function of the calculator.
    This function gets equations and solves them (if possible, if not shows informative message about the error).
    It also follows some program commands.
    :return: None.
    """
    display_welcome_msg()
    while True:
        equation = get_equation()
        if not check_for_program_command(equation):
            display_result(*solve_equation(equation))


if __name__ == '__main__':
    main()
