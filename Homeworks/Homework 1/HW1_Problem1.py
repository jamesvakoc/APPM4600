# importing libraries
import numpy as np
import matplotlib.pyplot as plt



def driver():

	# defining the domain
	x = np.arange(1.920,2.080,0.001)

	# defining the function in its factored and expanded forms
	f = lambda x: (x-2)**9
	g = lambda x: (x**9)-(18*x**8)+(144*x**7)-(672*x**6)+(2016*x**5)-(4032*x**4)+(5376*x**3)-(4608*x**2)+2304*x-512

        # assigning function to a variable
	y=f(x)
	w=g(x)

	# plotting the factored and expanded p(x) expressions over the domain
	plt.plot(x,y,'r',label="evaluated via factored expression")
	plt.plot(x,w,'b',label="evaluated via its coefficients")

	# labeling axes
	plt.xlabel('x')
	plt.ylabel('p(x)')

	# showing legend and plot
	plt.legend()
	plt.show()
	
	return

# calling driver
driver()
