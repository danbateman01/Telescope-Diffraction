"""
Module to plot the PSF, either in 2D or radially
Run the module to plot a npy file
"""
import numpy as np
import matplotlib.pyplot as plt
# scale using log or sinh-1(x/x0)

def plot_2D(arr, zoom = 1):
    '''Plots the PSF in the array arr'''

    #zoom code
    center = len(arr)//2
    lower = center - center//zoom
    upper = center + center//zoom

    N = len(arr)
    xs = np.fft.fftshift(np.fft.fftfreq(N))
    xmin = xs[lower]
    xmax = xs[upper-1]

    #Plot in 2D space
    plt.imshow(np.log(arr)[lower:upper, lower:upper], extent=[xmin, xmax, xmin, xmax])
    plt.xlabel(r'$\theta_x / \lambda$')
    plt.ylabel(r'$\theta_y / \lambda$')
    plt.show()

def plot_radially(arr, zoom = 1):
    '''Plots a PSF in array arr radially from N//2 to N'''

    #zoom code
    center = len(arr)//2
    cutoff = len(arr)//(2*zoom) + center
    
    #Plot in radial direction
    plt.plot(arr[center][center:cutoff])
    plt.xlabel(r'$\theta_x / \lambda$')
    plt.ylabel('Intensity')
    plt.show()

if __name__ == '__main__':
    #Load file
    fname = 'Cassegrain_PSF.npy'
    #fname = 'Circular_PSF.npy'
    arr = np.load(fname)

    plot_2D(arr, zoom=8)
    plot_radially(arr, zoom=8)