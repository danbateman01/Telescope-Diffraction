"""
Generates and saves the PSF of a circular aperature
"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import PSF as psf
import PSF_plotter

#Simple Circular aperature test

#Circular pupil radius
r = 20

#Grid size
N = 500

arr = psf.generate_circular_pupil(N, r)

#Plot Pupil function
plt.imshow(arr)
plt.show()

#Get PSF
PSF = psf.get_PSF(arr)

np.save('Circular_PSF.npy', PSF)

PSF_plotter.plot_2D(PSF)
PSF_plotter.plot_radially(PSF)