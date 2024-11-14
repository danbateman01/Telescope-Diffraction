import numpy as np
import matplotlib.pyplot as plt

arr = np.load('Cassegrain_PSF.npy')

plt.imshow(arr)
plt.show()