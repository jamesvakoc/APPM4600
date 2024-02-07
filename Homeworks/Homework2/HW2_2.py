#import libraries
import numpy as np
from numpy import linalg as LA

#set high precision
np.set_printoptions(precision=20
                    )
def driver():
    #define matrix A                  
    a=np.array([[1,1],[1+10**-10,1-10**-10]])
    A=1/2*a
    print(A)

    #calculate condition number
    k=LA.cond(A,p=2)

    #print k
    print(k)

    return 

driver()


