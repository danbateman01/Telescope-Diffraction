"""
Generates and saves the PSF of a cassegrain aperture
"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import PSF as psf
import PSF_plotter

# Grid Size
N = 500

inner_radius = 20
outer_radius = 50
strut_width  = 5

arr = psf.generate_cassegrain_pupil(N, outer_radius, inner_radius, strut_width)

# Plot Aperature
plt.imshow(arr)
plt.show()


PSF = psf.get_PSF(arr)
np.save('Cassegrain_PSF.npy', PSF)

PSF_plotter.plot_2D(PSF)
PSF_plotter.plot_radially(PSF)
