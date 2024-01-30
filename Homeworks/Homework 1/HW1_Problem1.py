import numpy as np
import matplotlib.pyplot as plt


def driver():

	# defining the domain as well as the polynomial p(x) in its factored and expanded form
	x = np.arange(1.920,2.080,0.001)
	f = lambda x: (x-2)**9
	g = lambda x: (x**9)-(18*x**8)+(144*x**7)-(672*x**6)+(2016*x**5)-(4032*x**4)+(5376*x**3)-(4608*x**2)+2304*x-512

	y=f(x)
	w=g(x)

	# plotting the factored and expanded p(x) expressions over the domain
	plt.plot(x,y,'r',label="evaluated via factored expression")
	plt.plot(x,w,'b',label="evaluated via its coefficients")
	plt.xlabel('x')
	plt.ylabel('p(x)')
	plt.legend()
	plt.show()
	return

driver()