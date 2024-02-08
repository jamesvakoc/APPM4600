#import library
import numpy as np

def driver():

    #define vector t with values ranging from 0 to pi (inclusive) with step size of pi/30
    t=np.arange(0,3.142,np.pi/30)

    #define vector y=cos(t)
    f = lambda t: np.cos(t)
    y=f(t)

    #Define Value for N
    N=30

    #Initializing Sum at S=0
    S=0

    #Calcualting the product of equivalent entries from vectors and adding these prodcuts to S up to the Nth entry
    for i in range(N+1):

        #Prodcut
        b=t[i]*y[i]

        #Sum
        S=S+b

    #Printing the final Sum
    print("the sum is: ", S)
    
    return
driver()
