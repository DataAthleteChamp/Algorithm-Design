import random
import timeit

def generuj_losowa_macierz(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]

def mnoz_macierze(macierz_a, macierz_b):
    n = len(macierz_a)
    wynik = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                wynik[i][j] += macierz_a[i][k] * macierz_b[k][j]

    return wynik

def mierz_czas_dzialania_programu(n):
    macierz_a = generuj_losowa_macierz(n)
    macierz_b = generuj_losowa_macierz(n)
    czas = timeit.timeit(lambda: mnoz_macierze(macierz_a, macierz_b), number=10)
    return czas / 10

n = int(input("Podaj rozmiar macierzy kwadratowych: "))

czas = mierz_czas_dzialania_programu(n)

print(f"Czas działania programu dla n = {n}: {czas:.6f} sekund")
