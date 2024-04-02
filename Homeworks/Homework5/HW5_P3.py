#Import Libraries
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

def driver():

    #Define Number of Nodal Points
    n_nodal=[5,10,20,40]

    for i in range(len(n_nodal)):

        #Create Nodal Points
        x_nodal=np.linspace(0,np.pi/3,n_nodal[i])

        #Create eval points
        x_eval=np.linspace(0,np.pi/3,1000)

        #create nodal data and evaluate targets for error analysis
        f = lambda x: np.sin(9*x)
        y_nodal=f(x_nodal)
        y_eval=f(x_eval)
    

    
        #cubic periodic spline
        cs=CubicSpline(x_nodal,y_nodal,bc_type='periodic')

        #create error

        #plot error
        error=np.log10(abs(cs(x_eval)-y_eval))
        plt.plot(x_eval,error,label='n='+str(n_nodal[i]))
        #plt.plot(x_eval,cs(x_eval))
        #plt.plot(x_eval,y_eval)

    #Plot Parameters
    plt.legend()
    plt.ylabel('log10 of interpolation error')
    plt.xlabel('x')
    plt.title('Periodic Cubic Spline Interpolation Error for f(x)=sin(9x) with n Nodal Points')
    plt.show()
    

    return
driver()
