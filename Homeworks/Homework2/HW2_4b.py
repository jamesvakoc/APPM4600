#import libraries
import numpy as np
import matplotlib.pyplot as plt

def driver():
    #defining graph 1 constants
    R0=1.2
    r0=0.1
    f0=15
    p0=0

    #defing theta domain
    theta = np.arange(0,6.29,np.pi/300)

    #graph 1 functions
    g0 = lambda theta: R0*(1+r0*np.sin(f0*theta+p0))*np.cos(theta)
    h0 = lambda theta: R0*(1+r0*np.sin(f0*theta+p0))*np.sin(theta)
    x0=g0(theta)
    y0=h0(theta)

    #initialzing graph two arrays of variables
    R=[0]*10
    f=[0]*10
    p=[0]*10
    r=0.05
    x=[0]*10
    y=[0]*10

    #seperate plots, plotting graph 1, and plot labels
    fig, axs = plt.subplots(2)
    axs[0].plot(x0,y0)
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('y')
    fig.suptitle('Problem 4 Graphs')

    #defining the 10 curves for 2nd graph
    for i in range(0,10):

        #defining parameters
        R[i]=i+1
        f[i]=3+i
        p[i]=np.random.uniform(0,2)

        #defining functions
        x[i]=R[i]*(1+r*np.sin(f[i]*theta+p[i]))*np.cos(theta)
        y[i]=R[i]*(1+r*np.sin(f[i]*theta+p[i]))*np.sin(theta)

        #plotting
        axs[1].plot(x[i],y[i],label = i+1)
        axs[1].set_xlabel('x')
        axs[1].set_ylabel('y')
        
    #show plot     
    plt.legend(title='Values of i')
    plt.show()

    return
driver()
