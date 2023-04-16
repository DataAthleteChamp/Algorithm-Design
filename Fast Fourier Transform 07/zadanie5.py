import numpy as np
import matplotlib.pyplot as plt
import cmath
import random


def generate_signal(A, a, B, b, T, num_samples):
    t = np.linspace(0, T, num_samples)
    signal = np.zeros(num_samples)

    for A_i, a_i in zip(A, a):
        signal += A_i * np.sin(a_i * t)

    for B_j, b_j in zip(B, b):
        signal += B_j * np.cos(b_j * t)

    return t, signal

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

# Przykładowe współczynniki sygnału
A = [2, 4]
a = [1, 5]
B = [3]
b = [8]
T = 10
num_samples = 1024

# Generowanie sygnału
t, signal = generate_signal(A, a, B, b, T, num_samples)

# FFT
freqs = np.fft.fftfreq(num_samples, T / num_samples)
signal_fft = fft(signal)

# Wykresy przed filtracją
fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
ax1.plot(t, signal)
ax1.set_title('Sygnał przed filtracją')
ax2.plot(freqs[:num_samples // 2], np.abs(signal_fft)[:num_samples // 2])
ax2.set_title('Częstotliwości przed filtracją')
plt.savefig('przed filtracja.png')
plt.close(fig1)

# Usuwanie częstotliwości
to_remove = [1, 2,3,4,5,6,7,8,9,10,0.8,0.79]  # Przykładowe częstotliwości do usunięcia
for freq in to_remove:
    idx = np.where(np.abs(freqs - freq) < 1e-6)[0]
    if idx.size > 0:
        signal_fft[idx[0]] = 0
        signal_fft[-idx[0]] = 0


# IFFT
filtered_signal = np.real(ifft(signal_fft))

# Wykresy po filtracji
fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
ax1.plot(t, filtered_signal)
ax1.set_title('Sygnał po filtracji')
ax2.plot(freqs[:num_samples // 2], np.abs(signal_fft)[:num_samples // 2])
ax2.set_title('Częstotliwości po filtracji')
plt.savefig('po filtracji.png')
plt.close(fig2)

plt.show()
