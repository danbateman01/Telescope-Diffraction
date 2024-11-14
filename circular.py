import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import PSF as psf

#Simple Circular aperature test

#Circular pupil radius
r = 10

#Grid size
N = 500
arr = np.zeros((N, N))

psf.generate_circle(arr, r)

#Plot Pupil function
plt.imshow(arr)
plt.show()

#Get PSF
PSF = psf.get_PSF(arr)

#Plot PSF
plt.imshow(PSF)
plt.show()
