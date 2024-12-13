"""
Modified example code to generate Gaussian random fields
"""
import numpy as np
import matplotlib.pyplot as plt
import generate_even

def fftIndgen(n):
    '''Generate a list integers from 0 to n/2 + -n/2 to 0, basically the coordinates of an array that python thinks is even'''
    a = list(range(0, n//2+1))
    b = list(range(1, n//2+1))
    b.reverse()
    b = [-i for i in b]
    return a + b

def gaussian_random_field(Pk, params, n, debug=False):
    '''Generate a nxn (n must be even) random gaussian field with Pk'''
    size = 2*n+1

    # Handle case where kx =ky =0
    def Pk2(kx, ky):
        if kx == 0 and ky == 0:
            return 0.0
        return np.sqrt(Pk(np.sqrt(kx**2 + ky**2), params))

    # Get fft of even random field size nxn
    initial = generate_even.gen_even_random(size)
    
    noise = np.fft.fft2(initial)

    # Generate amplitudes from grid of kx, ky (created using fftIndgen), Apply Pk(kx, ky) at all points
    amplitude = np.zeros((size,size))
    for i, kx in enumerate(fftIndgen(size)):
        for j, ky in enumerate(fftIndgen(size)):
            amplitude[i, j] = Pk2(kx, ky)

    if debug:
        plt.figure()
        plt.title('Real Component of Initial Noise')
        plt.imshow(initial.real)
        plt.show()

        plt.title('Imaginary Component of Initial Noise')
        plt.imshow(initial.imag)
        plt.show()

        plt.title('P(k)')
        plt.imshow(amplitude)
        plt.show()

    # Multipy the fft of the even random field by the grid of Pk(kx, ky)
    return np.fft.ifft2(noise * amplitude)[:size//2, :size//2].real

if __name__ == '__main__':
    def Pk(k, params):
        alpha = params[1]
        kc = params[0]
        return k**alpha * np.exp(-k**2/(kc**2))
    
    for kc in [1, 10, 100]:
        alpha = -1
        out = gaussian_random_field(Pk, [kc, alpha], 1000)

        plt.figure()
        plt.imshow(out.real, interpolation='none')
        plt.colorbar()
        plt.show()