import numpy as np
import matplotlib.pyplot as plt


def driver():
	delta=np.geomspace(10**-16,10**0,17)
	x1=np.pi
	x2=10**6
	

	print(x1)
	print(x2)
	
	f = lambda delta: np.absolute((-2*np.sin(x1+(delta/2))*np.sin(delta/2))-(np.cos(x1+delta)-np.cos(x1)))
	g = lambda delta: np.absolute((-2*np.sin(x2+(delta/2))*np.sin(delta/2))-(np.cos(x2+delta)-np.cos(x2)))

	h = lambda delta: np.absolute(-1*(delta*np.sin(x1)+0.5*delta**2*np.cos((x1+delta)/2))-(np.cos(x1+delta)-np.cos(x1)))
	i = lambda delta: np.absolute(-1*(delta*np.sin(x2)+0.5*delta**2*np.cos((x2+delta)/1))-(np.cos(x2+delta)-np.cos(x2)))


	y=f(delta)
	w=g(delta)
	
	r=h(delta)
	s=i(delta)

	plt.plot(delta,y,'r', label = "New Expression (x = pi)")
	plt.plot(delta,w,'b', label = "New Expression (x = 1e+6)")
	plt.plot(delta,r,'g', label = "Taylor Expansion Algorithm (x = pi)")
	plt.plot(delta,s,'y', label = "Taylor Expansion Algorithm (x= 1e+6)")
	plt.xscale("log")
	plt.yscale("log")
	plt.xlabel('delta')
	plt.ylabel('absolute difference')
	plt.legend()
	plt.show()
	

	return
	

driver() 