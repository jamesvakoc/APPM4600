import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import scipy.linalg as scila
import time


def driver():

     ''' create  matrix for testing different ways of solving a square 
     linear system'''

     '''' N = size of system'''
     N = 100
 
     ''' Right hand side'''
     b = np.random.rand(N,1)
     A = np.random.rand(N,N)

     print(N)

     start_time=time.perf_counter()
     x=scila.solve(A,b)
     print("The regular solve took", time.perf_counter()-start_time, "seconds to solve")

     start_time=time.perf_counter()
     lu, piv = scila.lu_factor(A)
     lu_time=time.perf_counter()
     x_lu = scila.lu_solve((lu, piv), b)
     finish_time=time.perf_counter()
     print("The LU factorization took", lu_time-start_time, "seconds")
     print("The LU solve took", finish_time-lu_time, "seconds")
     print("The total time for the LU method was", finish_time-start_time, "seconds")
     print('\n')
     
     test = np.matmul(A,x)
     test_la = np.matmul(A,x_lu)
     r = la.norm(test-b)
     r_la = la.norm(test_la-b)
     
     #print(r)
     #print(r_la)

     ''' Create an ill-conditioned rectangular matrix '''
     N = 10
     M = 5
     A = create_rect(N,M)     
     b = np.random.rand(N,1)

     
     AT=np.transpose(A)
     x_n=scila.solve(np.matmul(AT,A),np.matmul(AT,b))

     q,r=scila.qr(A)
     qT=np.transpose(q)
     print(qT)
     x_qr=scila.solve(r,np.matmul(qT,b))

     
def create_rect(N,M):
     ''' this subroutine creates an ill-conditioned rectangular matrix'''
     a = np.linspace(1,10,M)
     d = 10**(-a)
     
     D2 = np.zeros((N,M))
     for j in range(0,M):
        D2[j,j] = d[j]
     
     '''' create matrices needed to manufacture the low rank matrix'''
     A = np.random.rand(N,N)
     Q1, R = la.qr(A)
     test = np.matmul(Q1,R)
     A =    np.random.rand(M,M)
     Q2,R = la.qr(A)
     test = np.matmul(Q2,R)
     
     B = np.matmul(Q1,D2)
     B = np.matmul(B,Q2)
     return B     
          
  

driver()       
