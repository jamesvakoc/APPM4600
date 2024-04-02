import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

def driver():

    n_nodal=5
    x_nodal=np.linspace(0,3*np.pi/9,n_nodal)

    x_eval=np.linspace(0,3*np.pi/9,1000)
    
    f = lambda x: np.sin(9*x)
    y_nodal=f(x_nodal)
    y_eval=f(x_eval)
    

    
    
    cs=CubicSpline(x_nodal,y_nodal,bc_type='periodic')

    error=np.log10(abs(cs(x_eval)-y_eval))
    plt.plot(x_eval,error)
    plt.plot(x_eval,cs(x_eval))
    plt.plot(x_eval,y_eval)
    plt.show()

    
    
    print(x)
    

    return
driver()
