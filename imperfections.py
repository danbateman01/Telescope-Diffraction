import PSF as psf
import gaussian_fields as gf
import numpy as np
import matplotlib.pyplot as plt
import PSF_plotter

def generate_cassegrain_complex_pupil(N, r_outer, r_inner, strut_width, wavelength, noise_strength, Pk, params):
    '''Generates a cassegrain pupil w/ radius r on a NxN with phase due to gaussian field generated with kc and alpha'''
    pupil = psf.generate_cassegrain_pupil(N, r_outer, r_inner, strut_width)

    g_field = gf.gaussian_random_field(Pk, params, N) * noise_strength
    # plt.imshow(g_field)
    # plt.show()

    return pupil * np.exp(-1j * 2 * np.pi * g_field/wavelength)

def generate_imperfect_PSF(N, r_outer, r_inner, strut_width, wavelength, noise_strength, Pk, params):
    '''Generates an imperfect cassegrain PSF'''
    complex_pupil = generate_cassegrain_complex_pupil(N, r_outer, r_inner, strut_width, wavelength, noise_strength, Pk, params)

    return psf.get_PSF(complex_pupil)

def long_exposure(N, r_outer, r_inner, strut_width, wavelength, noise_strength, Pk, params, frames):
    '''Generates a number of imperfect PSF frames and averages over them'''
    total = np.zeros((N, N))
    for _ in range(frames):
        total += generate_imperfect_PSF(N, r_outer, r_inner, strut_width, wavelength, noise_strength, Pk, params)
    total = total /frames

    PSF_plotter.plot_2D(total)
    return total


if __name__ == '__main__':
    # Parameters of aperture
    N = 1000
    r_outer = 200
    r_inner = 100
    strut_width = 20

    # Parameters of complex pupil
    wavelength = 1
    noise_strength = 20 #5k for kc =1, 20 for kc=100
    kc = 100
    alpha = -1
    
    params = [kc, alpha]

    def Pk(k, params):
        kc = params[0]
        alpha = params[1]
        return k**alpha * np.exp(-k**2/(kc**2))
    
    # Generate an imperfect PSF
    PSF = generate_imperfect_PSF(N, r_outer, r_inner, strut_width, wavelength, noise_strength, Pk, params)
    
    # Plot PSF
    PSF_plotter.plot_2D(PSF, zoom=8)
    PSF_plotter.plot_2D(PSF)

    # Generate a long exposure PSF
    frames = 10
    PSF = long_exposure(N, r_outer, r_inner, strut_width, wavelength, noise_strength, Pk, params, frames)
    # Save long exposure PSF for later ploting
    np.save('long_exposure.npy', PSF)