import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import PSF as psf
import circular

def airy(x, r):
    '''Gives the airy function for x where x = theta / lambda, and D is the diameter of the aperature'''
    D=r*2
    return np.nan_to_num((2*sp.special.j1(np.pi * D * x)/(np.pi * D * x))**2, nan=1)

def getResidualsHorizontal(N, r):
    PSF = np.fft.ifftshift(circular.circular_PSF(N, r))
    numeric = np.fft.fftshift(PSF[0])
    xs = np.fft.fftshift(np.fft.fftfreq(N))

    analytic = airy(xs, r)

    return [xs, (numeric-analytic)**2]

if __name__ == "__main__":
    Ns = [1000, 2000, 5000, 10000]
    for N in Ns:
        xs, res = getResidualsHorizontal(N, 500)
        plt.plot(xs[N//2::], res[N//2::])
    plt.xscale('log')
    plt.legend(list(map(str, Ns)))
    plt.show()

    rs = [100, 200, 500, 1000, 2000, 2500]
    avgs = []
    for r in rs:
        xs, res = getResidualsHorizontal(5000, r)
        avgs.append(np.average(res))
        plt.plot(xs, res)
    plt.yscale('log')
    plt.legend(list(map(str, rs)))
    plt.show()

    plt.plot(rs, avgs)
    plt.yscale('log')
    plt.show()
