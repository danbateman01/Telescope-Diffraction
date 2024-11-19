"""
Modified example code to generate Gaussian random fields
Currently uses generate_even for the initial random array. This leads to the random fields having a certain symmetry that they shouldn't have
"""
import numpy as np
import matplotlib.pyplot as plt
import generate_even

def fftIndgen(n):
    '''Generate a list integers from 0 to n/2 + -n/2 to 0, basically the coordinates of an array that python thinks is even'''
    a = list(range(0, n//2+1))
    b = list(range(1, n//2))
    b.reverse()
    b = [-i for i in b]
    return a + b

def gaussian_random_field(Pk = lambda k : k**-3.0 * np.exp(-k**2), size = 101):
    '''Generate a random gaussian field with Pk'''

    # Handle case where kx =ky =0
    def Pk2(kx, ky):
        if kx == 0 and ky == 0:
            return 0.0
        return np.sqrt(Pk(np.sqrt(kx**2 + ky**2)))

    # Get fft of even random field size nxn
    noise = np.fft.fft2(generate_even.gen_even_random(size))

    # Generate amplitudes from grid of kx, ky (created using fftIndgen), Apply Pk(kx, ky) at all points
    amplitude = np.zeros((size,size))
    for i, kx in enumerate(fftIndgen(size)):
        for j, ky in enumerate(fftIndgen(size)):
            amplitude[i, j] = Pk2(kx, ky)

    # Multipy the fft of the even random field by the grid of Pk(kx, ky)
    return np.fft.ifft2(noise * amplitude)

for alpha in [-4.0, -3.0, -2.0]:
    kc = 20
    out = gaussian_random_field(Pk = lambda k: k**alpha * np.exp(-k**2/(kc**2)), size=255)
    plt.figure()
    plt.imshow(out.real, interpolation='none')
    plt.show()
