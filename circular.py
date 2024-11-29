"""
Generates and saves the PSF of a circular aperature
"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import PSF as psf
import PSF_plotter

#Simple Circular aperature test

def circular_PSF(r, N = 500, show=False):
    #Generate Pupil function
    arr = psf.generate_circular_pupil(N, r)

    #Get PSF
    PSF = psf.get_PSF(arr)

    if(show):
        #Plot Pupil function
        plt.imshow(arr)
        plt.show()

        #Plot PSF
        PSF_plotter.plot_2D(PSF)
        PSF_plotter.plot_radially(PSF)

    return PSF
if __name__ == '__main__':
    #Grid size
    N = 500

    #Circular pupil radius
    r = 20

    PSF = circular_PSF(r, N, True)

    np.save('Circular_PSF.npy', PSF)

