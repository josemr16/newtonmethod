Description

This is a python program that enforces the Newton's method algorithm.

What is the Newton's method?

 -Newton's method is a root-finding algorithm which produces approximations to the roots of a mathematical function in the form p(x) = 0.

 How does it work?

 -The algorithm requires an approximation which then will be used to compute a better root of the function. to start finding the roots using Newton's method, the given approximation is evaluated at the function, then the evaluation divided by the derivative of the function is subtracted from the given approximation.

 For example:

 x1 = x0 - f(x0)/f'(x0)
 x2 = x1 - f(x1)/f'(x1)
 xn = (xn-1) - f(xn-1)/f'(xn-1)
 xn+1 = xn - f(xn)/f'(xn)

 where x0 is the given approximation require by the algorithm.

Instruction to run the program

-The program consists in two parts. A python class that finds the derivative of a polynomial function and evaluates a function given a number. The other part is the actual program that computes the Newton's method algorithm.

-To use the program run Finalproject.py and choose the input type:

Keyboard: Use the keyboard to enter your input.

File: Use a file that contains the information needed to compute the algorithm.





 


