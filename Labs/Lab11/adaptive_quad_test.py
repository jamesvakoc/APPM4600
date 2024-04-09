# This script tests the convergence of adaptive quad
# and compares to a non adaptive routine

# get adaptive_quad routine and numpy from adaptive_quad.py
from adaptive_quad import *
# get plot routines
import matplotlib.pyplot as plt

# specify the quadrature method
# (eval_gauss_quad, eval_composite_trap, eval_composite_simpsons)
method = eval_gauss_quad

# interval of integration [a,b]
#a = 0; b = 1.
# function to integrate and true values
# TRYME: uncomment and comment to try different funcs
#        make sure to adjust I_true values if using different interval!
#f = lambda x: np.log(x+(x==0))**2; I_true = 2; labl = '$\log^2(x)$'
#f = lambda x: 1./(np.power(x,(1./5.))); I_true = 5./4.; labl = '$\\frac{1}{x^{1/5}}$'
#f = lambda x: np.exp(np.cos(x)); I_true = 2.3415748417130531; labl = '$\exp(\cos(x))$'
#f = lambda x: x**20; I_true = 1./21.; labl = '$x^{20}$'
# below is for a=0.1, b = 2
a=0.1; b=2;
f = lambda x: np.sin(1./x); I_true = 1.1455808341; labl = '$\sin(1/x)$'

# absolute tolerance for adaptive quad
tol = 1e-3
# machine eps in numpy
eps = np.finfo(float).eps

# number of nodes and weights, per subinterval
Ms = 5
# storage for error
err_old = 0
err_new = 0


# loop over quadrature orders
# compute integral with non adaptive and adaptive
# compute errors for both
M = Ms;
# non adaptive routine
# Note: the _,_ are dummy vars/Python convention
# to store uneeded returns from the routine
I_old,_,_ = method(M,a,b,f)
# adaptive routine
I_new,X,nsplit = adaptive_quad(a,b,f,tol,M,method)
err_old = np.abs(I_old-I_true)/I_true
err_new = np.abs(I_new-I_true)/I_true
# clean the error for nice plots
if err_old < eps:
  err_old = eps
if err_new < eps:
  err_new = eps
# save grids for M = 2
if M == Ms:
  mesh = X

# plot the old and new error for each f and M
fig,ax = plt.subplots(1,2)
ax[0].semilogy(Ms,err_old,'ro--')
ax[0].set_ylim([1e-16,2]);
ax[0].set_xlabel('$M$')
ax[0].set_title('Non-adaptive')
ax[0].set_ylabel('Relative Error');
ax[1].semilogy(Ms,err_new,'ro--',label=labl)
ax[1].set_ylim([1e-16,2]);
ax[1].set_xlabel('$M$')
ax[1].set_title('Adaptive')
ax[1].legend()
plt.show()

# plot the adaptive mesh for M=2
fig,ax = plt.subplots(1,1)
ax.semilogy(mesh,f(mesh),'ro',label=labl)
ax.legend()
plt.show()
