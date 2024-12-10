"""
Generates and saves the PSF of a cassegrain aperture
"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import PSF as psf
import PSF_plotter


def cassegrain_PSF(N, r_outer, r_inner, strut_width = 0, show=False):
    arr = psf.generate_cassegrain_pupil(N, r_outer, r_inner, strut_width)
    PSF = psf.get_PSF(arr)

    if show:
        #Plot Pupil function
        plt.imshow(arr)
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
        plt.show()

        #Plot PSF
        PSF_plotter.plot_2D(PSF)
        PSF_plotter.plot_radially(PSF)

    return PSF

if __name__ == '__main__':

    # Grid Size
    N = 2000

    # Pupil Parameters
    r_inner = 100
    r_outer = 200
    strut_width  = 10

    # Get and sace PSF
    PSF = cassegrain_PSF(N, r_outer, r_inner, strut_width, True)
    np.save('Cassegrain_PSF.npy', PSF)

