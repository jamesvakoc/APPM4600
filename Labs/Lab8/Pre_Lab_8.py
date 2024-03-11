#import library
import numpy as np

def driver():
    #Define points (x_0,f(x_0)) and (x_1,f(x_1)) which defines the line
    x0=3
    y0=9
    x1=6
    y1=-4

    #Define evaluation point a
    a=4.5

    #Call evalLine function
    [m,b,fa]=evalLine(x0,x1,y0,y1,a)

    #Print line equation and line evaluation at x = a
    print('The equation of the line is y =',m,'x +',b)
    print('The evaluation of the line at x = a is',fa)
    return

#Define evalLine function. Returns slope, y-intercept, and f(a)
def evalLine(x0,x1,y0,y1,a):
    m = (y1-y0)/(x1-x0)
    b = -m*x0+y0
    fa = m*a+b
    return[m,b,fa]

driver()
