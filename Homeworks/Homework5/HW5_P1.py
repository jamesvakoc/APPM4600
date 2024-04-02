#Import Libraries
import numpy as np
from scipy.special import binom
import matplotlib.pyplot as plt

def driver():

    #Define Paramteres
    n=15
    h=2/n

    #Initializing Nodal and Weight Arrays
    x_equi=np.zeros(n+1)
    w_equi=np.zeros(n+1)

    x_cheb=np.zeros(n+1)
    w_cheb=np.zeros(n+1)

    #Create target points
    z=np.linspace(-1,1,1001)

   
    #Creating Nodal Points and Weight Values
    for i in range(n+1):
        x_equi[i]=-1+(i)*h
        w_equi[i]=((-1)**i)*binom(n,i)

        x_cheb[i]=np.cos(((2*i+1)*np.pi)/(2*n+2))
        w_cheb[i]=((-1)**i)*np.sin(((2*i+1)*np.pi)/(2*n+2))

    #Defining Function and Associated y-values
    f = lambda x: 1/(1+(16*x)**2)
    y_equi=f(x_equi)
    y_cheb=f(x_cheb)

    #Target y-values for comparison
    g = lambda z: 1/(1+(16*z)**2)
    a=g(z)

    #Creating Interpolation with Equispaced Nodes
    p=evalLagrange(x_equi,w_equi,y_equi,z,n)
    m=evalMonic(x_equi,z,n)

    #Plotting equispaced interpolation
    plt.plot(x_equi,y_equi,'o',label='nodes')
    plt.plot(z,p,label='interpolation')
    plt.plot(z,a,label='f(x)')
    plt.plot(z,np.log10(abs(m)),label='log10 monic')
    plt.title('Equispaced Nodes')
    plt.legend()
    plt.show()

    
    #Creating Interpolation with Chebyshev Nodes
    p=evalLagrange(x_cheb,w_cheb,y_cheb,z,n)
    m=evalMonic(x_cheb,z,n)

    #Plotting Chebyshev Interpolation
    plt.plot(x_cheb,y_cheb,'o',label='nodes')
    plt.plot(z,p,label='interpolation')
    plt.plot(z,a,label='f(x)')
    plt.plot(z,np.log10(abs(m)),label='log10 monic')
    plt.title('Chebyshev Nodes')
    plt.legend()
    plt.show()
        
#Function Creating Barycentric Lagrange
def evalLagrange(x,w,y,z,n):
    #Initilize Vecotrs
    p=np.zeros(len(z))
    num=np.zeros(len(z))
    den=np.zeros(len(z))

    #Code for Second barycentric formula
    for k in range(len(z)):
        
        for j in range(n+1):
            if (z[k] != x[j]):
                num[j]=(w[j]*y[j])/(z[k]-x[j])
                den[j]=w[j]/(z[k]-x[j])
            else:
                p[k]=y[j]
                break
        
        p[k]=np.sum(num)/np.sum(den)
        
    return p
#Function for Monic Polynomial for Error Analysis
def evalMonic(x,z,n):
    m=np.ones(len(z))
    for k in range(len(z)):
        for j in range(n+1):
            m[k]=(z[k]-x[j])*m[k]
    return m
        
        
   

driver()

    
