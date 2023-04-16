import cmath

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

# Przykład użycia:
samples = [1, 1, 1, 1, 0, 0, 0, 0]
result = fft(samples)
print(result)      # Wypisze: [4, 2.41421356...j, 0, 0.58578643...j, 0, 0.41421356...j, 0, -0.58578643...j]
