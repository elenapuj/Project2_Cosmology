import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


#First we define some constants that we will need through the project

G = 6.67e-8  #cm³/gs²

H0 = 2.72e-18  #1/s

kB = 1.38e-16  #cm²kg/sK

T0 = 2.725  #K

hbar = 1.055e-27  #cm²g/s

c = 3e10  #cm/s

Neff = 3

tau = 1700  #s

q = 2.53

Z = 5.93e9






#SECTION C)

#We will calculate the value of Omega_r0 here


Or = ( (8*(np.pi)**3) / 45 ) * ( G / (H0**2) ) * ( (kB*T0)**4 / ( (hbar**3) * (c**5) ) ) * ( 1 + Neff * (7/8) * (4/11)**(4/3) )

print("O_r =", Or)






#SECTION F)


#First, we will introduce some functions in order to calculate the integral

def I(x):

	I1 = ( (x+q)**2 * (x**2 - 1)**(1/2) * x ) / ( (1 + np.exp( x*Z/T )) * (1 + np.exp( -(x+q)*Z/Tv) ) )

	I2 = ( (x+q)**2 * (x**2 - 1)**(1/2) * x ) / ( (1 + np.exp( -x*Z/T )) * (1 + np.exp( (x-q)*Z/Tv )) )

	return(I1+I2)



def Int(T, q):

	Tv = ( (4/11)**(1/3) ) * T

	return(sp.quad(I, 1, np.inf))


def Dif(t, Y):

	y = np.zeros(2)


