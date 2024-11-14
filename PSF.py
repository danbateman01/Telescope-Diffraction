import numpy as np
import scipy as sp

def generate_circle(arr, r, x=1):
    '''Generates a circle of x with radius r at the center of the array arr'''
    d = len(arr)//2 -r
    for i in range(2*r):
        for j in range(2*r):
            if (i-r)**2 + (j-r)**2 <= r**2:
                arr[i+d][j+d] = x

def add_struts(pupil, width=1):
    '''Adds 4 struts to the pupil function'''
    c = len(pupil)//2
    w = width//2
    for i in range(len(pupil)):
        pupil[i, c-w:c+w] = 0
        pupil[c-w:c+w, i] = 0


def get_PSF(pupil):
    '''Get the PSF from the pupil function'''
    #Take Fourier Transform
    ft = sp.fft.fftshift(sp.fft.fft2(pupil))

    #Return complex square of Fourier transform
    return np.real(np.multiply(ft, ft.conjugate()))
