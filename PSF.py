"""
Module with functions for generating PSFs
"""
import numpy as np
import scipy as sp

def get_normalized_PSF(pupil):
    return normalize(get_PSF(pupil))

def normalize(arr):
    return (arr-np.min(arr))/(np.max(arr)-np.min(arr))

def generate_circle(arr, r, x=1):
    '''Generates a circle of x with radius r at the center of the array arr'''
    d = len(arr)//2 -r
    for i in range(2*r):
        for j in range(2*r):
            if (i-r)**2 + (j-r)**2 <= r**2:
                arr[i+d][j+d] = x

def add_struts(pupil, width=1):
    '''Adds 4 struts width width width to the pupil function'''
    c = len(pupil)//2
    w = width//2
    for i in range(len(pupil)):
        pupil[i, c-w:c+w] = 0
        pupil[c-w:c+w, i] = 0

def generate_cassegrain_pupil(N, outer_radius, inner_radius, strut_width = 0):
    '''Returns a cassegrain pupil with outer and inner radii and four struts of width strut_width centered on an NxN array'''
    arr = np.zeros((N, N))

    generate_circle(arr, outer_radius)
    generate_circle(arr, inner_radius, 0)
    if strut_width:
        add_struts(arr, strut_width)
    
    return arr

def generate_circular_pupil(N, radius, strut_width = 0):
    '''Generates a circular pupil with radius radius and struts of width strut_width centered on an NxN array'''
    arr = np.zeros((N, N))
    generate_circle(arr, radius)
    if strut_width:
        add_struts(arr, strut_width)
    
    return arr

def get_PSF(pupil):
    '''Get the PSF from the pupil function'''
    #Take Fourier Transform
    ft = sp.fft.fftshift(sp.fft.fft2(pupil))

    #Return complex square of Fourier transform
    return np.real(np.multiply(ft, ft.conjugate()))
