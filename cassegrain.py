import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import PSF as psf

N = 2000
arr = np.zeros((N, N))

psf.generate_circle(arr, 50)
psf.generate_circle(arr, 10, 0)
psf.add_struts(arr, 6)

plt.imshow(arr)
plt.show()

PSF = psf.get_PSF(arr)
np.save('Cassegrain_PSF.npy', PSF)

plt.imshow(PSF)
plt.show()