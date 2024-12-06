import PSF as psf
import gaussian_fields as gf
import numpy as np
import matplotlib.pyplot as plt
import PSF_plotter

def generate_circular_complex_pupil(N, r, kc, alpha):
    '''Generates a circular pupil w/ radius r on a NxN with phase due to gaussian field generated with kc and alpha'''
    pupil = psf.generate_circular_pupil(N, r)

    g_field = gf.gaussian_random_field(kc, alpha, N)

    return pupil * np.exp(-1j * 2 * np.pi * g_field)

def generate_imperfect_PSF(N, r, kc, alpha):
    '''Generates an imperfect circular PSF'''
    complex_pupil = generate_circular_complex_pupil(N, r, kc, alpha)

    return psf.get_PSF(complex_pupil)

def long_exposure(N, r, kc, alpha, frames):
    total = np.zeros((N, N))
    for _ in range(frames):
        total += generate_imperfect_PSF(N, r, kc, alpha)
    total = total /frames

    PSF_plotter.plot_2D(total)

if __name__ == '__main__':
    N = 500
    r = 20
    kc = 100
    alpha = -0.1
    arr = generate_circular_complex_pupil(N, r, kc, alpha)
    
    plt.imshow(arr.imag)
    plt.show()
    PSF_plotter.plot_2D(generate_imperfect_PSF(N, r, kc, alpha))
    long_exposure(N, r, kc, alpha, 100)