import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import PSF as psf
import circular

def airy(x, r):
    '''Gives the airy function for x where x = theta / lambda, and D is the diameter of the aperature'''
    D=r*2
    return (2*sp.special.j1(np.pi * D * x)/(np.pi * D * x))**2

def getResiduals(r, N):
    PSF = np.fft.ifftshift(circular.circular_PSF(r, N))
    numeric = np.fft.fftshift(PSF[0])
    xs = np.fft.fftshift(np.fft.fftfreq(N))

    analytic = airy(xs, r) * np.max(numeric)

    return [xs, numeric-analytic]

if __name__ == "__main__":
    for N in [2000, 5000, 10000]:
        for r in [200, 500, 1000]:
            xs, res = getResiduals(r, N)
            plt.plot(xs, res)
        plt.xscale('log')
        plt.show()