#import libraries
import numpy as np

def driver():

    #Inputs
    a=0
    b=5
    N=60
    f = lambda x: np.exp(x)

    #Call and Print Integral
    I_t = eval_composite_trap(a,b,N,f)
    print("Using composite trapezoidal quadrature, the value of the integral is", I_t)

    I_s = eval_composite_simpsons(a,b,N,f)
    print("Using composite simpson's quadrature, the value of the integral is", I_s)
    
    return

#Trapezoidal Composite
def eval_composite_trap(a,b,N,f):
    #define points,h, and weights
    x=np.linspace(a,b,N)
    h=(b-a)/N
    w = h*np.ones(N)
    w[0]=0.5*w[0]
    w[N-1]=0.5*w[N-1]

    #sum
    I_hat = np.sum(f(x)*w)
    return I_hat

#Simpson's Composite
def eval_composite_simpsons(a,b,N,f):
    #define points,h, and weights
    x=np.linspace(a,b,N)
    h=(b-a)/(N-1)
    w=(h/3)*np.ones(N)
    for i in range(1,N-1,2):
        w[i]=4*w[i]
        w[i+1]=2*w[i+1]

    #sum
    I_hat = np.sum(f(x)*w)
    return I_hat

driver()


