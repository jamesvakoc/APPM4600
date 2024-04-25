# importing libraries
import numpy as np
from scipy.special import gamma, factorial
from scipy import integrate

def driver():

    #defining t values
    t=[2,4,6,8,10]

    #defining parameters for trapezoidal approximation and adaptive quadrature
    a=0
    b=[10,16,23,31,41]
    n=np.zeros(len(t))
    for i in range(len(t)):
        n[i]=10*b[i]
        
    print('\n')

    #Calulcating gamma(t) for each t using each method
    for i in range(len(t)):

        #Defining gamma function integrand
        f = lambda x: x**(t[i]-1)*np.exp(-x)

        #Defining polynomial for Gausian quadrature
        g = lambda x: x**(t[i]-1)

        #Trapezoidal Approximation and Associated Relative Error
        I_trap,s_trap = eval_composite_trap(int(n[i]),a,b[i],f)
        err_trap=abs((gamma(t[i])-I_trap)/gamma(t[i]))

        #Addaptive Quadrature and Associated Relative Error
        I_adap, error, infodict = integrate.quad(f,a,b[i],full_output=1)
        err_adap=abs((gamma(t[i])-I_adap)/gamma(t[i]))

        #Gaussian Quadrature
        sp,w = np.polynomial.laguerre.laggauss(int(t[i]/2))
        I_laggauss=np.sum(g(sp)*w)
        

        #Printing Results
        print("Evaluating the gamma function with a trapezoidal approximation at t =",t[i],"gives",I_trap)
        print("This trapezoidal approximation produces a relative error of", err_trap, "and evaluates f", len(s_trap), "times")
        print("Evaluating the gamma function with adaptive quadrature at t =",t[i],"gives",I_adap)
        print("This adaptive quadrature produces a relative error of", err_adap, "and evaluates f", infodict['neval'], "times")
        print("Evaluating the gamma function with Gauss-Laguerre quadrature at t =",t[i],"gives",I_laggauss)
        
        print('\n')

    
    
#Defining Composite Trapezoidal Subroutine
def eval_composite_trap(n,a,b,f):

    #Partitioning Interval and Defining Step Size
    s=np.linspace(a,b,n+1)  
    h=(b-a)/(n)

    #Defining Trapezoidal Weights
    w=h*np.ones(n+1)
    w[0]=0.5*w[0]
    w[n]=0.5*w[n]

    #Computing Integral
    I_trap = np.sum(f(s)*w)
    return I_trap,s

driver()
