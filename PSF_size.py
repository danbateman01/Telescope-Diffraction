"""
Generates a .npy file with the sizes of PSFs (width at 1/2 max) versus the circular aperture radius
"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import PSF as psf

def get_PSF_size(N, r):
    '''Gets the width at half max of a PSF generated from a circular aperature with radius r centered on a NxN grid'''
    arr = np.zeros((N,N))
    psf.generate_circle(arr, r)
    PSF = psf.get_PSF(arr)

    half_max = np.max(PSF)/2
    central = np.nonzero(PSF[N//2] > half_max)
    size = np.max(central) - np.min(central)

    return np.fft.fftfreq(N)[size]

def get_1st_min(N, r):
    arr = np.zeros((N,N))
    psf.generate_circle(arr, r)
    PSF = psf.get_normalized_PSF(arr)
    radially = PSF[N//2][N//2::]
    
    last = 1
    for i, v in enumerate(radially):
        if last < v:
            return i -1
        last = v
        
    return N//2

def Psize_vs_Psize(N, r_start, r_stop, r_step):
    '''Generates a .npy file containing the width of PSF for circular aperatures of various radii'''
    rs = np.arange(r_start, r_stop, r_step)
    ws = []
    for r in rs:
        ws.append(get_PSF_size(N, r))
    
    np.save('PSF_size.npy', [rs, ws])

Psize_vs_Psize(2000, 10, 500, 20)