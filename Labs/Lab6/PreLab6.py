#import libraries
import numpy as np
import matplotlib.pyplot as plt

def driver():

    #define vector of h values, halfing the value at each itteration
    h=0.01*2.**(-np.arange(0,10))

    #define value at which we're approximating the derivative
    s=np.pi/2

    #calcualting forward and centered differences
    fd = (np.cos(s+h)-np.cos(s))/h
    cd = (np.cos(s+h)-np.cos(s-h))/(2*h)

    #calculating associated errors
    fderror = np.absolute(fd+1)
    cderror = np.absolute(cd+1)
    
    print('The forward difference approximations for the derivative of f at s are', fd)
    print('The centered difference approximations for the derivative of f at s are', cd)
    
    #plotting errors as a function of h
    plt.plot(fderror,h,'r',label='Forward Difference Error')
    plt.plot(cderror,h,'b',label='Centered Difference Error')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('h')
    plt.ylabel('error')
    plt.legend()
    plt.show()

driver()
    
    
    
