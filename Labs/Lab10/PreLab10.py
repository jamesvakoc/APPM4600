import numpy as np

def driver():

    n=5
    x=7

    p = eval_legendre(n,x)
    print(p)

    return

def eval_legendre(n,x):
    p=np.zeros(n+1)

    p[0]=1
    p[1]=x
    for i in range(2,n+1):
        p[i]=1/(n+1)*((2*n+1)*x*p[i]-n*p[i-1])

    return p

driver()
