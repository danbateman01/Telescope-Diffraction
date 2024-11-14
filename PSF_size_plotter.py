import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import PSF as psf

arr = np.load('PSF_size.npy')
plt.plot(arr[0], arr[1])
plt.ylabel('PSF Width at 1/2 Max')
plt.xlabel('Circular Pupil Radius')
plt.show()
