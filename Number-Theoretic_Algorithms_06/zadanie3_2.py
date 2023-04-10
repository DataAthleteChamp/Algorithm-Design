import timeit
import matplotlib.pyplot as plt


def nwd_rozkład(a, b):
    czynniki_a = rozklad(a)
    czynniki_b = rozklad(b)
    i = 0
    j = 0
    wynik = 1
    while i < len(czynniki_a) and j < len(czynniki_b):
        if czynniki_a[i] == czynniki_b[j]:
            wynik *= czynniki_a[i]
            i += 1
            j += 1
        elif czynniki_a[i] < czynniki_b[j]:
            i += 1
        else:
            j += 1
    return wynik


def rozklad(n):
    czynniki = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            czynniki.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        czynniki.append(n)
    return czynniki




def nwd_euklides(a, b):
    while b != 0:
        a, b = b, a % b
    return a




n = 123456789
m = 1000

czas_rozkład = []
czas_euklides = []

for q in range(1, m+1):
    czas = timeit.timeit(lambda: nwd_rozkład(n, q), number=100)
    czas_rozkład.append(czas)

    czas = timeit.timeit(lambda: nwd_euklides(n, q), number=100)
    czas_euklides.append(czas)

plt.plot(range(1, m+1), czas_rozkład, label='RNWD')
plt.plot(range(1, m+1), czas_euklides, label='ENWD')
plt.legend()
plt.xlabel('q')
plt.ylabel('czas (s)')
plt.savefig('zadanie3_2.png')
plt.show()
