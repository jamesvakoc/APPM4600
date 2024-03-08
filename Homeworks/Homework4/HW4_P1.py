# import libraries
import numpy as np
import math
import time
from numpy.linalg import inv
from numpy.linalg import norm
import matplotlib.pyplot as plt;

def driver():

    # define initial guess and inputs
    x0 = np.array([1, 1])

    Nmax = 100
    tol = 1e-10

    #Newton's Method
    t = time.time()
    for j in range(20):
        [xstar,xlist,ier,its] =  Newton(x0,tol,Nmax);
    elapsed = time.time()-t;
    print(xstar);
    err = np.sum((xlist-xstar)**2,axis=1);
    plt.plot(np.arange(its),np.log10(err[0:its]));
    plt.xlabel('Iteration')
    plt.ylabel('Log Error')
    plt.title('Newton')
    plt.show();

    #Fixed Point Iteration
    t = time.time()
    for j in range(20):
      [xstar,xlist,ier,its] =  LazyNewton(x0,tol,Nmax);
    elapsed = time.time()-t
    print(xstar);
    err2 = np.sum((xlist-xstar)**2,axis=1);
    plt.plot(np.arange(its),np.log10(err2[0:its]));
    plt.xlabel('Iteration')
    plt.ylabel('Log Error')
    plt.title('Lazy Newton')
    plt.show();

#Evaluating the System
def evalF(x):

    F = np.zeros(2)

    F[0] = 3*x[0]**2-x[1]**2
    F[1] = 3*x[0]*x[1]**2-x[0]**3-1
    
    return F

#Evaluating Jacobian Matrix
def evalJ(x):


    J = np.array([[6*x[0],-2*x[1]],[3*x[1]**2-3*x[0]**2,6*x[0]*x[1]]])
    return J

#Newton's Method
def Newton(x0,tol,Nmax):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''
    xlist = np.zeros((Nmax+1,len(x0)));
    xlist[0] = x0;

    for its in range(Nmax):
       J = evalJ(x0)
       F = evalF(x0);

       x1 = x0 - np.linalg.solve(J,F);
       xlist[its+1]=x1;

       if (norm(x1-x0) < tol*norm(x0)):
           xstar = x1
           ier =0
           return[xstar, xlist,ier, its];

       x0 = x1

    xstar = x1
    ier = 1
    return[xstar,xlist,ier,its];

#Fixed Point Method
def LazyNewton(x0,tol,Nmax):

    ''' Lazy Newton = use only the inverse of the Jacobian for initial guess'''
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    xlist = np.zeros((Nmax+1,len(x0)));
    xlist[0] = x0;

    J = np.array([[1/6,1/18],[0,1/6]])
    for its in range(Nmax):

       F = evalF(x0)
       x1 = x0 - np.matmul(J,F)
       xlist[its+1]=x1;

       if (norm(x1-x0) < tol*norm(x0)):
           xstar = x1
           ier =0
           return[xstar,xlist, ier,its];

       x0 = x1

    xstar = x1
    ier = 1
    return[xstar,xlist,ier,its];

if __name__ == '__main__':
    # run the drivers only if this is called from the command line
    driver();
