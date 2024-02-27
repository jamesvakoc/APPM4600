#import libraries
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=16)

def driver():

    #define vector of h values, halfing the value at each itteration
    h=0.01*2.**(-np.arange(0,10))
    print(h)

    #define value at which we're approximating the derivative
    s=np.pi/2

    #calcualting forward and centered differences
    fderror = ((np.cos(s+h)-np.cos(s))/h)
    cd = ((np.cos(s+h)-np.cos(s-h))/(2*h))

    #calculating associated errors
    fderror = np.absolute(((np.cos(s+h)-np.cos(s))/h)+1)
    cderror = np.absolute(((np.cos(s+h)-np.cos(s-h))/(2*h))+1)
    
    print('The forward difference approximations for the derivative of f at s are', ((np.cos(s+h)-np.cos(s))/h))
    print('The centered difference approximations for the derivative of f at s are', ((np.cos(s+h)-np.cos(s-h))/(2*h)))
    
    #plotting errors as a function of h
    plt.plot(h,fderror,'r',label='Forward Difference Error')
    plt.plot(h,cderror,'b',label='Centered Difference Error')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('h')
    plt.ylabel('error')
    plt.legend()
    plt.show()

driver()
    
    
    
