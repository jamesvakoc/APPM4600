# import libraries
import numpy as np
    
def driver():

# test functions 
     f1 = lambda x: 1+0.5*np.sin(x)
# fixed point is alpha1 = 1.4987....

     f2 = lambda x: 3+2*np.sin(x)
#fixed point is alpha2 = 3.09... 

     Nmax = 100
     tol = 1e-6

# test f1 '''
     x0 = 0.0
     [xstar,ier,v] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
     print('The apprixmation for the fixed point at each iteration is :', v)
    
#test f2 '''
     x0 = 0.0
     [xstar,ier,v] = fixedpt(f2,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f2(xstar):',f2(xstar))
     print('Error message reads:',ier)
     print('The apprixmation for the fixed point at each iteration is :', v)



# define routines
def fixedpt(f,x0,tol,Nmax):
     ''' x0 = initial guess''' 
     ''' Nmax = max number of iterations'''
     ''' tol = stopping tolerance'''
     v=np.zeros((Nmax,1))
     count = 0
     while (count <Nmax):
          v[count]=x0
          count = count +1
          x1 = f(x0)
          if (abs(x1-x0) <tol):
               xstar = x1
               ier = 0
               v[count]=x1
               for i in range(count+1,Nmax):
                    v=np.delete(v,count+1)
               return [xstar,ier,v]
          x0 = x1
     
     xstar = x1
     ier = 1
     return [xstar, ier,v]
    

driver()
