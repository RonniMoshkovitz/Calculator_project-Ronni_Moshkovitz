# Calculator project - Ronni Moshkovitz:

""
This project is an advanced calculator (Omega Calculator).

This calculator supports the following operands:

 +: addition, in form of  operand + operand

 -: submission, in form of  operand - operand  

 *: multiplication, in form of operand * operand

 /: division, in form of operand / operand

 ^: power, in form of operand ^ operand 

 $: maximum, in form of operand $ operand

 &: minimum, in form of operand & operand

 @: average, in form of operand @ operand

 %: module, in form of operand % operand

 ~: negative, in form of ~ operand

 !: factorial, in form of operand !

 #: sum digits, in form of operand #
""


<h3>This calculator is divided to different modules to preform different tasks in the process.</h3>

<h3>The Modules:</h3>

""@ Calculator - The main module of the calculator app. It is in charge of the UI functionality.

@ InputOutput - This module is in charge of the user communication. It gets input from the user and present information to the user.

@ CalculatorExceptions - This module contains classes for all the Exceptions that may be raised by the calculator program.

@ ValidateInput - This module validates the entered string (to be parsed in the next step). It checks for invalid appearances in the equation.

@ EquationParser - This module parses the string equation, to a list equation containing operands, operators and brackets.

@ EquationReader - This module defines a reader object EquationReader. This reader reads the equation list, and tries to solve it. 
The reader reads the equation step by step according to the execution order and solves it accordingly.

@ TreatMinusSign - This module treats the extra minus signs in an equation. This module works according to the 2nd approach.

@ MathematicsOperations - This module contains all the mathematics operations functions supported on this calculator.

@ OperationCheck - This module contains all the operation validations for the supported operations on the calculator.

@ OperationPerformer - This module preforms the mathematical operations supported by the calculator.
It matches the operator to its functions, checks that it can be preformed, and then preforms it if possible.

@ EquationSolver - This module solves the equation. from string equation to final results. It also treats exceptions that might occur during the process.

@ configuration - Configuration file that contains Constants that are used in multiple modules of the program.

@ test_calculator - Pytest testing for the calculator. Tests the equation solving algorithm.
""