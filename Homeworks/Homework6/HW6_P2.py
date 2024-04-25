#importing libraries
import numpy as np
from scipy import integrate

def driver():

    #defining paramters for trapezoidal and simpson's quadrature
    a = -5
    b = 5
    n_trap=1291
    n_simp = 108
    f = lambda x: 1/(1+x**2)

    print('\n')

    #Trapezoidal
    I_trap,t_trap = eval_composite_trap(n_trap,a,b,f)
    error_trap = abs(I_trap-2*np.arctan(5))
    print("Composite Trapezoidal Quadrature Gives the Approximation", I_trap)
    print("The associated error is", error_trap)
    print("The function f was evaluated", len(t_trap), "times")

    print('\n')

    #Simpsons
    I_simp,t_simp = eval_composite_simp(n_simp,a,b,f)
    error_simp = abs(I_simp - 2*np.arctan(5))
    print("Composite Simpson's Quadrature Gives the Approximation",I_simp)
    print("The associated error is", error_simp)
    print("The function f was evaluated", len(t_simp), "times")

    print('\n')

    #SCIPY Quad with Error Tolerance 1e-6
    I_scip, err_scip, infodict= integrate.quad(f,a,b,full_output=1,epsabs=10**-6)
    print("SCIPY quad routine evaluates the integral to", I_scip, "with an absolute tolerance of 10**-6")
    print("The associated error is", abs(I_scip - 2*np.arctan(5)))
    print("The scipy quadrature took",infodict['neval'], "function evaluations")

    print('\n')

    #SCIPY Quad with Error Tolerance 13-4
    I_scip, err_scip, infodict= integrate.quad(f,a,b,full_output=1,epsabs=10**-4)
    print("SCIPY quad routine evaluates the integral to", I_scip, "with an absolute tolerance of 10**-4")
    print("The associated error is", abs(I_scip - 2*np.arctan(5)))
    print("The scipy quadrature took",infodict['neval'], "function evaluations")

    print('\n')

#Composite Trapezoidal Subroutine
def eval_composite_trap(n,a,b,f):

    #Partitioning Interval and Defining Step Size
    t=np.linspace(a,b,n+1)
    h=(b-a)/(n)

    #Trapezoidal Weights
    w=h*np.ones(n+1)
    w[0]=0.5*w[0]
    w[n]=0.5*w[n]

    #Approximating Integral
    I_trap = np.sum(f(t)*w)
    return I_trap,t


#Composite Simpson's Subroutine
def eval_composite_simp(n,a,b,f):

    #Partitioning Interval and Defining Step Size
    t = np.linspace(a,b,n+1)
    h=(b-a)/n

    #Simpson's Weight (1,4,2,4,...,2,4,1)
    w=(h/3)*np.ones(n+1)
    w[1:n:2]=4*w[1:n:2]
    w[2:n-1:2]=2*w[2:n-1:2]
    
    #Approximating Integral
    I_simp=np.sum(f(t)*w)
    return I_simp,t
    
    

driver()
