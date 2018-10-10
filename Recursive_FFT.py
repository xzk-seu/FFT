import math
import numpy as np


def get_list():
    n1 = int(input('n = '))
    r = list()
    for i in range(n1):
        t = int(input('a[%d] = ' % i))
        r.append(t)
    return r


def recursive_fft(a):
    n = len(a)
    if n == 1:
        return a
    y = list(range(n))
    w_n = np.exp((2 * np.pi * 1j) / n)
    w = 1
    a_even = list()
    a_odd = list()
    for j in range(0, n-1, 2):
        a_even.append(a[j])
        a_odd.append(a[j + 1])
    y_even = recursive_fft(a_even)
    y_odd = recursive_fft(a_odd)
    for k in range(0, n//2):
        t = y_odd[k]*w
        y[k] = y_even[k]+t
        y[k+n//2] = y_even[k]-t
        w *= w_n
    return y


if __name__ == '__main__':
    a1 = get_list()
    result = recursive_fft(a1)
    print(result)
    t = np.fft.fft(a1)
    print(t)

