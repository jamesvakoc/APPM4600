# import libraries
import numpy as np
    
def driver():

     np.set_printoptions(precision=32)

# test functions 
     f1 = lambda x: (10/(x+4))**0.5
# fixed point is alpha1 = 1.4987....

     #f2 = lambda x: 3+2*np.sin(x)
#fixed point is alpha2 = 3.09... 

     Nmax = 100
     tol = 1e-10

# test f1 '''
     x0 = 1.5
     [xstar,ier,v,count] = fixedpt(f1,x0,tol,Nmax)
     [A]=Aitken(v,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
     print('The apprixmation for the fixed point at each iteration is :', v)
     print('The algorithm took', count, 'iterations to converge within the desired tolerance')
     
     #This only works for when v coverges in exactly 12 iterations
     print('The order of convergence is', np.log(np.absolute(v[11]-v[12])/np.absolute(v[10]-v[12]))/ np.log(np.absolute(v[10]-v[12])/np.absolute(v[9]-v[12])))
     
     print('\n')
     print('Using Aitkens Method, the fixed point is:', A[len(v)-3])
     
     #This does not work yet 
     #print('The order of convergence is', np.log(np.absolute(A[len(v)-4]-A[len(v)-3])/np.absolute(A[len(v)-5]-A[len(v)-3]))/ np.log(np.absolute(A[len(v)-5]-A[len(v)-3])/np.absolute(A[len(v)-6]-A[len(v)-3])))
     
     print(A)
     
    
#test f2 '''
     #x0 = 0.0
     #[xstar,ier,v,count] = fixedpt(f2,x0,tol,Nmax)
     #print('the approximate fixed point is:',xstar)
     #print('f2(xstar):',f2(xstar))
     #print('Error message reads:',ier)
     #print('The apprixmation for the fixed point at each iteration is :', v)



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
               return [xstar,ier,v,count]
          x0 = x1
     
     xstar = x1
     ier = 1
     return [xstar, ier,v]

def Aitken(v,tol,Nmax):
     A=np.zeros((len(v)-2,1))
     for i in range(0,len(v)-2):
          A[i]=v[i]-((v[i+1]-v[i])**2)/(v[i+2]-2*v[i+1]+v[i])
     return [A]
    

driver()
