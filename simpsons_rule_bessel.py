import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def BesselJ1(x):
    '''J1 bessel function evaluated at point x generated via simpson's rule'''

    def f(theta, x):
        '''Local function for integrand'''
        return np.cos(theta - (x * np.sin(theta)))

    a = 0
    b = np.pi
    num_points = 1000 #Number of Points
    h = np.pi / num_points 
    sum = f(a, x) + f(b, x) #Start the sum with the endpoints

    #Sum over odd
    for k in range(1, num_points, 2):
        sum += 4 * f(a + k*h, x)

    #Sum over even
    for k in range(0, num_points, 2):
        sum += 2 * f(a + k*h, x)

    return h/(3 * np.pi) * sum

xs = np.linspace(0, 20, 1000)
simpson_ys = BesselJ1(xs)
scipy_ys = sp.special.j1(xs)

fig, ax = plt.subplots(3, 1, sharex=True)
plt.xlabel("x")
ax[0].plot(xs, simpson_ys)
ax[0].set_ylabel("Simpson's Rule J1")
ax[1].plot(xs, scipy_ys)
ax[1].set_ylabel("Scipy J1")
ax[2].plot(xs, simpson_ys - scipy_ys)
ax[2].set_ylabel("Difference")
plt.show()
