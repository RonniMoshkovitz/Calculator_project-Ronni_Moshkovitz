from EquationSolver import *

"""
Pytest testing for the calculator.
"""


def test_syntax_errors():
    """
    This function tests syntax errors.
    """
    test_cases = ["2+*7", "4--(9", "5#4", "8(7)", "12..12"]
    for equation, result in map(solve_equation, test_cases):
        # solve_equation returns a string if invalid equation was entered (syntax error)
        assert type(result) is str


def test_nonsense():
    """
    This function tests a nonsense string as the equation input.
    """
    nonsense = "td-- 653eu+"
    _, result = solve_equation(nonsense)
    # solve_equation returns a string if invalid equation was entered
    assert type(result) is str


def test_empty():
    """
    This function tests an empty string as the equation input.
    """
    empty = ""
    _, result = solve_equation(empty)
    # solve_equation returns a string if invalid equation was entered
    assert type(result) is str


def test_white_space():
    """
    This function tests a white space string as the equation input.
    """
    white_space = "     "
    _, result = solve_equation(white_space)
    # solve_equation returns a string if invalid equation was entered
    assert type(result) is str


def test_simple():
    """
    This function tests simple equations.
    """
    test_cases = {"2*7": 14.0, "4-9": -5.0, "5*-4": -20.0, "8@(7)": 7.5, "123#": 6.0, "1.2+7": 8.2, "3!": 6.0,
                  "~12": -12.0, "12/4": 3.0, "13%10": 3.0, "2^3": 8.0, "4$6": 6.0, "-2&2": -2.0, "-123#": -6,
                  "--4!": 24}
    for equation, right_result in test_cases.items():
        _, result = solve_equation(equation)
        assert result == right_result


def test_complicated():
    """
    This function tests complicated equations (at least 20 symbols long).
    """
    test_cases = {"----2*(7--(6.3-2.6/2)! +   12$5)---~---3": 275.0,
                  "(4*------ --9 /(2&4)^2!) -100^3   ": -999991.0,
                  "2.1+5-1+5*(2/2+2^4)+1": 92.1,
                  "~17$30*3.3&5.5-(12#-2!)": 98.0,
                  "(5%2+300@10)-    3^2/9+55&3": 158.0,
                  "30*0.1$2--~5+(10!*2-30)%5-(30/5+1)": 48.0,
                  "(5+6-7*8+9^2)/2-38&36+(10 @2---10#)*~1": -23.0,
                  "6!-3^3*2+  (~2/~1+2#)*1-3%2+1": 670.0,
                  "100&99/33+1.1^2-(3!+~1)%2+7*7": 52.21,
                  "(8-7*6% 5+4&3-2!+~1)*2+100^0-3.12#": -3.0,
                  "3#*4!+30@(5%3)-15&10   +2/2-1": 78.0,
                  "1+2^3/4-5*6+(7&8+9$10)#+11%~22.3": -30.3,
                  "(2.3*(8!$10)-5#)@3+13% 2 &13/2": 46367.5,
                  "(30.5*4+(4^4%3)-10)/121#+~5+(5-3!)": 23.0,
                  "13%2+(6!$50+(3+3+2^5)+~1)-5.5": 752.5,
                  "~5/10--15.3#*(33+(5!^2-1)*3)+1": 389070.5,
                  "8^2+1.2&89#-(5^(3%2+1)-5!@73)": 136.7,
                  "~6+3.3-6@2+(10%7-3)$35+3*2.2": 34.9,
                  "5$(4*-123#^2 /12.7@5.3)-100%(12*2.5)": 6.0,
                  "8@(7)+-------12      /4 $(25^0.5*0.1)": 4.5}
    for equation, right_result in test_cases.items():
        _, result = solve_equation(equation)
        assert result == right_result
