README for Gill_K_Project 2.py
====================================
The assignment was done on Python, since I thought that translating the complex algorithms into computational language is easier on Python than other languages.

OOP is mainly used, for two main numerical methods: quadrature and Monte-Carlo method. 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
QUADRATURE METHOD

Two classes and one sub-class were made.

class Trapezoidal performs the integration using trapezoidal method. 

To make the process handy, execution_trap and execution_simp functions are created. 

Putting in the function, lower and upper limits of the integral, and desired accuracy epsilon into the arguments would set-up the integral
i.e. execution_trap(lambda x: x**2, 1, 2, 1E-6)
execution_simp(lambda x:x**2, 1, 2, 1E-6)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
MONTE-CARLO METHOD
 
MCIS class was created, so it's same as above, but a few manual executions of the code are required.

1. Initialize MCIS integrator
i.e. init = MCIS(lambda x:x**2, 1,2, 1E-6)
2. Choose between flat and linear sampling pdf
-Flat 
flat_init = MC_flat_pdf(number of initial samples)
flat_iter = MC_flat_iter(flat_init[0], flat_init[1])

-Linear
linear_init = MC_linear_pdf(number of initial samples)
linear_iter = MC_linear_iter(linear_init[0], linear_init[1])

3. Print the required values
-Final result
flat_iter[0] or linear_iter[0]

-List of iterated values
flat_iter[1] or linear_iter[1]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Sometimes, since the code is written recursively, the recursion depth limit is exceeded. If so, the following should help:

1. import sys
2. sys.getrecursionlimit() => returns a number n
3. sys.setrecursionlimit(N)  where N>>n
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------