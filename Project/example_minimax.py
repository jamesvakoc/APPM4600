import numpy as np
import matplotlib.pyplot as plt

a_0=0.5*(np.e-np.sinh(1)*np.log(np.sinh(1)))
a_1=np.sinh(1)
p = lambda x: (0*x)+(np.e-a_0-a_1)


q = lambda x: a_0+a_1*x
f = lambda x: np.exp(x)

x=np.linspace(-1,1,100)

y_exact = f(x)
y_minimax = q(x)
maxerr = p(x)

minerr = -1*p(x)

err = y_exact - y_minimax

fig, axs = plt.subplots(2,sharex=True)
axs[0].plot(x,y_exact,label='$e^x$')
axs[0].plot(x,y_minimax,label='$q_1(x)$')
axs[1].plot(x,err,label='$E(x)$')
axs[1].plot(x,maxerr, label='$p_n$')
axs[1].plot(x,-1*maxerr, label = '$-p_n$')
axs[0].legend()
axs[1].legend()

plt.show()
