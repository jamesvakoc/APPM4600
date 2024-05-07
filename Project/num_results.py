#importing libraries
import numpy as np
import matplotlib.pyplot as plt
from remez_poly import *
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

#defining interval and order of approximation/interpolation
#Note: [a,b] = [-1,1] for chebyshev interpolation
a=-1
b=1
n=2

#defining function to be approximated/interpolated
#f is used for generating minimax polynomial (nees mpmath exponential), g is used for numerical calculations
#both f and g should be the same function
f = lambda x: mp.exp(x)
g = lambda x:np.exp(x)

#calls remez algorithm to produce minimax polynomial coefficients
minimax_coeffs, max_error = remez(f, n, a, b)

#defining chebyshev nodes and evaluating f at chebyshev nodes
c = [0] * (n+1)
for i in range(n+1):
    c[i]=np.cos(np.pi*(2*i+1)/(2*(n+1)))

cheb_poly=lagrange(c,g(c))


#defining x-values to be plotted
x = numpy.linspace(a, b, 100)

#generating minimax, chebyshev, and exact y-values
y_minimax = numpy.polyval(minimax_coeffs[::-1], x)
y_cheb = cheb_poly(x)
y_exact = g(x)

#generating minimax and chebyshev errors
err_minimax = abs(y_exact - y_minimax)
err_cheb = abs(y_exact - y_cheb)


#plotting polynomials
fig, axs = plt.subplots(2,sharex=True)

axs[0].plot(x, y_exact,'r',label='f(x)',linewidth=4)
axs[0].plot(x,y_cheb,color='b',label='Chebyshev Interpolation',linewidth=2)
axs[0].plot(x, y_minimax,color='lime',linestyle='-.', label='Minimax Approximation')
axs[0].legend()

#plotting errors
axs[1].plot(x, np.log10(err_minimax), label='Minimax Error')
axs[1].plot(x, np.log10(err_cheb),label='Chebyshev Error')
axs[1].legend()
plt.show()
