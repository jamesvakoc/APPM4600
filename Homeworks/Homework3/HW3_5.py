# import libraries
import numpy as np
import matplotlib.pyplot as plt
    
def driver():
     #plotting function
     t = np.arange(-2,8,0.05)
     g = lambda t: t-4*np.sin(2*t)-3
     y=g(t)
     z=0*t

     plt.plot(t,y)
     plt.plot(t,z)
     plt.xlabel('x')
     plt.ylabel('x-4sin(2x)-3')
     plt.show()


# defining itteration
     f1 = lambda x: -1*np.sin(2*x)+5*x/4-3/4



     Nmax = 100

# test f1 '''
     x0v=np.array([-0.9,-0.5,1.7,3,4.5])

     for i in range(0,5):
          x0 = x0v[i]
          [xstar,ier] = fixedpt(f1,x0,Nmax)
          print('the approximate fixed point is:',xstar)
          print('f1(xstar):',f1(xstar))
          print('Error message reads:',ier)
          print('\n')
    




# define routines
def fixedpt(f,x0,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       if (abs(x1-x0) < abs(x0)*0.5*10**-10):
          xstar = x1
          ier = 0
          return [xstar,ier]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier]
    

driver()
