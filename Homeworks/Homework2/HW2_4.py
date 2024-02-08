import numpy as np

def driver():
    t=np.arange(0,3.142,np.pi/30)
    f = lambda t: np.cos(t)
    y=f(t)
    #print(t)
    #print(y)
    
    N=30
    S=0
    for i in range(N+1):
        b=t[i]*y[i]
        S=S+b

    print("the sum is: ", S)
    return
driver()
