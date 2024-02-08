#import library
import numpy as np

#define precision
np.set_printoptions(precision=16
                    )

def driver():
    #define value of x
    x=9.999999995000000*10**-10

    #calculate and print e^x-1
    y=np.e**x
    a=y-1
    print(a)

    #calcualting and printing e^x-1 with polynomial approximation
    T=(x)+(1/2*x**2)+(1/6*x**3)  
    print(T)

    #calculating and printing relative error
    E=(np.e**x*x**4)/(24*10**-9)
    print(E)
    
    return
driver()
