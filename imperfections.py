import PSF as psf
import gaussian_fields as gf
import numpy as np
import matplotlib.pyplot as plt
import PSF_plotter

def generate_circular_complex_pupil(N, r, Pk, params):
    '''Generates a circular pupil w/ radius r on a NxN with phase due to gaussian field generated with kc and alpha'''
    pupil = psf.generate_circular_pupil(N, r)

    g_field = gf.gaussian_random_field(Pk, params, N)

    return pupil * np.exp(-1j * 2 * np.pi * g_field)

def generate_imperfect_PSF(N, r, Pk, params):
    '''Generates an imperfect circular PSF'''
    complex_pupil = generate_circular_complex_pupil(N, r, Pk, params)

    return psf.get_PSF(complex_pupil)

def long_exposure(N, r, Pk, params, frames):
    '''Generates a number of imperfect PSF frames and averages over them'''
    total = np.zeros((N, N))
    for _ in range(frames):
        total += generate_imperfect_PSF(N, r, Pk, params)
    total = total /frames

    PSF_plotter.plot_2D(total)


if __name__ == '__main__':
    N = 1000
    r = 100
    kc = 100
    alpha = -0.1
    params = [kc, alpha]

    def Pk(k, params):
        kc = params[0]
        alpha = params[1]
        return k**alpha * np.exp(-k**2/(kc**2))
    
    arr = generate_circular_complex_pupil(N, r, Pk, params)
    
    plt.imshow(arr.imag)
    plt.show()
    PSF_plotter.plot_2D(generate_imperfect_PSF(N, r, Pk, params))
    #long_exposure(N, r, high_pass, kc, 100)