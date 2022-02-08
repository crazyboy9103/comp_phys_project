import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
#%% DEFINE TRAPEZOIDAL
'''
class trapezoidal(function: has to be written in the form of (lambda x: expresion in x)
                  lower, upper: lower limit and upper limit of the integral
                  epsilon: desired relative accuracy (better to keep this 1E-6, which can be 
                                                      set smaller))

    func initial_guess : starts the iteration by passing the initial step size and 
                        guess to the next function, next_guess
        
    func next_guess(I_prev: the previous guess, h_prev: the previous step size)
        : continues the iteration until the convergence criterion is reached
        (recursively written)
                    
'''
#%%
integral_erf = 0.5 * math.erf(2)
print('Analytic result:', integral_erf)
#%%
class Trapezoidal():
    def __init__(self, function, lower, upper, epsilon):
        self.f = function
        self.a = lower
        self.b = upper
        self.k = 0 #iteration 
        self.e = epsilon
   
        self.I_list = []
        self.TS_list = []
    def initial_guess(self):
        
        h = self.b-self.a
        I = h/2 *(self.f(self.b)+self.f(self.a))
        self.k += 1
        self.I_list.append(I)
        return I, h
    
    def next_guess(self, I_prev, h_prev):
        h = h_prev/2
        x = lambda i: self.a +i*h
    
        n = (self.b-self.a)/h +1
        sum1 = 0
        
        N = 0
        
        for i in range(1, int((n-1)/2)):
            N += 1
            sum1 += self.f(x(2*i-1))
        
        I_next = 1/2 * I_prev + h*sum1
        
        delta = np.absolute((I_next-I_prev)/I_prev)
        
        self.I_list.append(I_next)
        #to use j+1 th iteration value, to later evaluate jth simpson's integral
        
        self.TS_list.append([I_prev, self.k, N])
        if delta > self.e:
            
            self.k += 1
            
            return self.next_guess(I_next, h)
        
        else:
            
            return self.k, I_prev, self.TS_list
        
#%% USE OF TRAPEZOIDAL TO COMPUTE SIMPSON'S INTEGRATION RESULT
'''
class Simpsons()
    : inherits trapezoidal class
    func simpson : brings the results from trapezoidal integration, and use them
                    to compute the integral
                    
                    return the total iteration and the list of integral result              
'''
#%%
class Simpsons(Trapezoidal):
    def simpson(self):
        n = len(self.I_list) # length
        S = []
        N = 0
        for i in range(n-1):
            self.k += 1
            N += 1
            S_j = 4/3 * self.I_list[i+1]- 1/3* self.I_list[i]
            S.append([S_j, self.k, N])
            
        
        
                
        return self.k, S

#%% EXECUTION OF THE CODE
'''
func execution_trap, execution_simp(function: the integrand (e.g. lambda x: np.e**(x)), 
                    lower, upper: lower and upper limit of integral
                    epsilon: the relative accuracy to be achieved |((I_next-I_prev)/I_prev)|<epsilon):
    Executes trapezoidal and simpsons integration
    
'''
#%%
def execution_trap(function, lower, upper, epsilon):
    setup = Trapezoidal(function, lower, upper, epsilon)
    trap_initial = setup.initial_guess()
    h1 = trap_initial[1]
    I1 = trap_initial[0]
    
    I = setup.next_guess(I1, h1)
    
    I_result = I[1]
    k = I[0]
    
    TS_list =I[2]
    print('Trapezoidal integration from', lower,'to',
          upper,'with tolerance', epsilon, 'is', I_result, 'with iterations', k)
    
    return TS_list
    
def execution_simp(function, lower, upper, epsilon):
    simpson_setup = Simpsons(function, lower, upper, epsilon)
    simpson_initial = simpson_setup.initial_guess()
    h1 = simpson_initial[1]
    I1 = simpson_initial[0]
    simpson_setup.next_guess(I1, h1) #to save integrals in self.I_list
    T = simpson_setup.simpson()
    
    S = T[1]
    
    
    #print('Simpson integration from', lower,'to',
        #  upper,'with tolerance', epsilon, 'is', S, 'with iterations', k)
    
    return S
#%%
'''
class MCIS(function: integrand
           lower, upper: limits
           epsilon: accuracy):
    
'''


#%%
class MCIS():
    def __init__(self, function, lower, upper, epsilon):
        self.f = function
        self.a = lower
        self.b = upper
        self.e = epsilon
        
        self.flat_pdf = 1/(self.b-self.a)
        self.linear_pdf = lambda x: -0.48*x + 0.98
        self.k = 0
        
        self.MC_list = []
#%%        
    def MC_flat_pdf(self, N):
        self.k += 1
        
        Q = self.f
        sum_Q = 0
        for i in range(N):
            x = np.random.uniform(self.a, self.b)
            sum_Q += Q(x)/self.flat_pdf
            
        sum_Q /= N
        
        print(sum_Q)
        return sum_Q, N
    
    def MC_flat_iter(self, prev_sum_Q, prev_N):
        N = 10 * prev_N
        
        Q = self.f
        next_sum_Q = 0
        
        for i in range(N):
            x = np.random.uniform(self.a, self.b)
            next_sum_Q += Q(x)/self.flat_pdf
        
        next_sum_Q /= N
        
        delta = np.absolute((next_sum_Q-prev_sum_Q)/prev_sum_Q)
        
        self.MC_list.append([prev_sum_Q, self.k, prev_N])
        
        if delta > self.e:
            
            self.k += 1
            
            print('Now there are', N, 'samples')
            
            return self.MC_flat_iter(next_sum_Q, N)
        
        else:
            print('Iterations', self.k)
            
            return prev_sum_Q, self.MC_list
#%%        
    def MC_linear_pdf(self, N):
        self.k += 1
        Q = self.f
        sum_Q = 0
        
        for i in range(N):
            x = np.random.uniform(0, 1)
            
            y = (0.98-np.sqrt(0.98**2-0.96*x))/0.48
            sum_Q += Q(y)/self.linear_pdf(y)
       
        sum_Q /= N
        print(sum_Q)
        
        return sum_Q, N
    
    def MC_linear_iter(self, prev_sum_Q, prev_N):
        N = 10 * prev_N
        Q = self.f
        next_sum_Q = 0
        
        for i in range(N):
            x = np.random.uniform(0,1)
            
            y =(0.98-np.sqrt(0.98**2-0.96*x))/0.48
            
            next_sum_Q += Q(y)/self.linear_pdf(y) 
            
        next_sum_Q /= N     
        
        delta = np.absolute((next_sum_Q-prev_sum_Q)/prev_sum_Q)
        
        self.MC_list.append([prev_sum_Q, self.k, prev_N])
        
        if delta > self.e:
            
            self.k +=1 
            print('Now there are', N, 'samples')
            
            return self.MC_linear_iter(next_sum_Q, N)
        
        else:
            print('Iterations', self.k)
            
            return prev_sum_Q, self.MC_list
#%%
  
        
#%%
Psi_squared= lambda z: 1/np.pi**(1/2) * np.e**(-z**2)

TS_list=execution_trap(Psi_squared, 0, 2, 1E-6)
S_list =execution_simp(Psi_squared, 0, 2, 1E-6)
'''
print('TS',TS_list, 'S',S_list)

x=MCIS(lambda x: 1/np.sqrt(np.pi) *np.e**(-x**2), 0, 2, 1E-3)

init = x.MC_flat_pdf(1000)
final = x.MC_flat_iter(init[0], init[1])
print(final[0])
MC_list = final[1]
print(MC_list)

init = x.MC_linear_pdf(1000)
final = x.MC_linear_iter(init[0], init[1])
print(final[0])
MC_list = final[1]
print(MC_list)
'''
#%%


