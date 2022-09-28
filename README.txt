README for Gill_K_Project 2.py
====================================
The assignment was done on Python.

OOP is used for two main numerical methods: quadrature and Monte-Carlo method. 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
QUADRATURE METHOD

class Trapezoidal performs the integration using trapezoidal method. 


Putting lower and upper limits of the integral, and desired accuracy epsilon as arguments to ```execution_trap``` or ```execution_simp```would start the calculation.
e.g. 
```execution_trap(lambda x: x**2, 1, 2, 1E-6)```
```execution_simp(lambda x:x**2, 1, 2, 1E-6)```
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
MONTE-CARLO METHOD
 
1. Initialize MCIS integrator
e.g. ```init = MCIS(lambda x:x**2, 1,2, 1E-6)```
2. Choose between flat and linear sampling pdf
-Flat 
```flat_init = MC_flat_pdf(number of initial samples)```
```flat_iter = MC_flat_iter(flat_init[0], flat_init[1])```

-Linear
```linear_init = MC_linear_pdf(number of initial samples)```
```linear_iter = MC_linear_iter(linear_init[0], linear_init[1])``

3. Print the required values
-Final result
```flat_iter[0]``` or ```linear_iter[0]```

-List of iterated values
```flat_iter[1]``` or ```linear_iter[1]```
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
The recursion depth limit can be exceeded, which can cause error. If this happens, the following should help:

1. ```import sys``
2. ```sys.getrecursionlimit()``` => returns a number n
3. ```sys.setrecursionlimit(N)```  where N>>n
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
