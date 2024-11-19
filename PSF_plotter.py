"""
Module to plot the PSF, either in 2D or radially
Run the module to plot a npy file
"""
import numpy as np
import matplotlib.pyplot as plt
# scale using log or sinh-1(x/x0)

def plot_2D(arr):
    '''Plots the PSF in the array arr'''

    #Plot in 2D space
    plt.imshow(np.log(arr))
    plt.xlabel(r'$\theta_x / \lambda$')
    plt.ylabel(r'$\theta_y / \lambda$')
    plt.show()

def plot_radially(arr):
    #Plot in radial direction
    plt.plot(arr[len(arr)//2][len(arr)//2::])
    plt.xlabel(r'$\theta_x / \lambda$')
    plt.ylabel('Intensity')
    plt.show()

if __name__ == '__main__':
    #Load file
    #fname = 'Cassegrain_PSF.npy'
    fname = 'Circular_PSF.npy'
    arr = np.load(fname)

    plot_2D(arr)
    plot_radially(arr)