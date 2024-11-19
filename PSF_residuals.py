import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import PSF as psf

# Not finished yet, will generate the residual as a function theta/lambda between the airy disk and and the comptuationally generated PSF of a circular aperature

def airy(x, D):
    '''Gives the airy function for x where x = theta / lambda, and D is the diameter of the aperature'''
    return (sp.special.j1(np.pi * D * x)/(np.pi * D * x))**2

xs = np.linspace(0, 100, 1000)
plt.plot(xs, airy(xs, 0.1))
plt.show()
