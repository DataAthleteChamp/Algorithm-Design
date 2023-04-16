import random
import time
import matplotlib.pyplot as plt
import numpy as np
import cmath


# Implementacja FFT, jak podana wcześniej
def fft_recursive(signal):
    n = len(signal)
    if n <= 1:
        return signal

    even = fft_recursive(signal[0::2])
    odd = fft_recursive(signal[1::2])

    T = [cmath.exp(-2j * cmath.pi * k / n) * odd[k] for k in range(n // 2)]
    return [even[k] + T[k] for k in range(n // 2)] + [even[k] - T[k] for k in range(n // 2)]


def fft(signal):
    assert (len(signal) & (len(signal) - 1) == 0), "Długość sygnału musi być potęgą liczby 2"
    return fft_recursive(signal)


# Implementacja IFFT
def ifft_recursive(signal):
    n = len(signal)
    if n <= 1:
        return signal

    even = ifft_recursive(signal[0::2])
    odd = ifft_recursive(signal[1::2])

    T = [cmath.exp(2j * cmath.pi * k / n) * odd[k] for k in range(n // 2)]
    return [(even[k] + T[k]) / 2 for k in range(n // 2)] + [(even[k] - T[k]) / 2 for k in range(n // 2)]


def ifft(signal):
    assert (len(signal) & (len(signal) - 1) == 0), "Długość sygnału musi być potęgą liczby 2"
    return ifft_recursive(signal)


# Szybkie mnożenie wielomianów z użyciem FFT
def fast_polynomial_multiplication(poly1, poly2):
    n = len(poly1) + len(poly2) - 1
    size = 2 ** int(np.ceil(np.log2(n)))

    padded_poly1 = poly1 + [0] * (size - len(poly1))
    padded_poly2 = poly2 + [0] * (size - len(poly2))

    fft_poly1 = fft(padded_poly1)
    fft_poly2 = fft(padded_poly2)

    fft_result = [x * y for x, y in zip(fft_poly1, fft_poly2)]

    result = ifft(fft_result)

    return [round(x.real) for x in result[:n]]


# Naiwne mnożenie wielomianów
def naive_polynomial_multiplication(poly1, poly2):
    result = [0] * (len(poly1) + len(poly2) - 1)

    for i, coef1 in enumerate(poly1):
        for j, coef2 in enumerate(poly2):
            result[i + j] += coef1 * coef2

    return result


# Naiwne mnożenie wielomianów, szybkie mnożenie wielomianów z użyciem FFT
# (włączając implementacje funkcji fft i ifft), jak podane wcześniej

# Porównanie czasu wykonania
sizes = [2**i for i in range(3, 16)]
naive_times = []
fft_times = []

for size in sizes:
    poly1 = [random.randint(-10, 10) for _ in range(size)]
    poly2 = [random.randint(-10, 10) for _ in range(size)]

    start_time = time.time()
    naive_result = naive_polynomial_multiplication(poly1, poly2)
    naive_times.append(time.time() - start_time)

    start_time = time.time()
    fft_result = fast_polynomial_multiplication(poly1, poly2)
    fft_times.append(time.time() - start_time)

# Rysowanie wykresów
plt.plot(sizes, naive_times, 'o-', label='Naiwne mnożenie wielomianów')
plt.plot(sizes, fft_times, 'x-', label='Mnożenie z FFT')
plt.xlabel('Rozmiar wielomianu')
plt.ylabel('Czas działania (s)')
plt.legend()
plt.savefig('zadanie4')
plt.title('Porównanie czasu działania mnożenia wielomianów')
plt.show()
