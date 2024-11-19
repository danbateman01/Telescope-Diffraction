"""
Module to generate random complex arrays with symmetry such that the Fourier transform is real
"""
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

def complex_random(size=1):
    return np.random.normal(size = size) + 1j * np.random.normal(size = size)

def gen_even_random(N):
    '''Function to generate an even 2D array of dimension NxN, N must be odd for function to be completely even'''
    n = N//2

    q1 = complex_random((n, n))
    q2 = complex_random((n, n))

    x_ax_pos = complex_random(n)
    y_ax_pos = complex_random(n)

    zero = 0

    # Add the x axis to the first quadrent
    x_q1 = np.vstack((x_ax_pos, q1))

    # Combine zero and the positive y axis
    zero_y = np.hstack((zero, y_ax_pos))

    # Add the y axis to the first quadrent x axis combo
    full_q1 = np.insert(x_q1, 0, zero_y, 1) 

    # Add the inverted x axis to the 2nd quadrent
    full_q2 = np.vstack((np.conjugate(np.flip(x_ax_pos)), q2))

    # Add 1st and 2nd quadrents together
    q12 = np.hstack((full_q1, full_q2))

    # Generate the 3rd and 4th quadrents as rotations of the 1st and 2nd
    q3 = np.conjugate(np.rot90(q1, 2))
    q4 = np.conjugate(np.rot90(q2, 2))

    # add inverted y axis to the 4th quadrent
    full_q4 = np.insert(q4, 0, np.conjugate(np.flip(y_ax_pos)), 1)

    # add 4th and 3rd quadrents together
    q43 = np.hstack((full_q4, q3))

    # return all four quadrents added together
    return np.vstack((q12, q43))

if __name__ == '__main__':
    arr = gen_even_random(7)

    #Imaginary Component of FFt should be zero if arr is even
    print("Total Imaginary component of FFT", np.sum(np.absolute(sp.fft.fft2(arr).imag)))

    plt.figure()
    plt.imshow(np.absolute(arr))
    plt.colorbar()
    plt.title("Even Random Array")
    plt.show()


