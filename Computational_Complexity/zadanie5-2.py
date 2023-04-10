import matplotlib.pyplot as plt
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

def wykres_czasu_dzialania_programu(dolny, gorny, krok):
    czasy = []
    for n in range(dolny, gorny + krok, krok):
        czas = mierz_czas_dzialania_programu(n)
        czasy.append((n, czas))

    n = [c[0] for c in czasy]
    czas = [c[1] for c in czasy]

    plt.plot(n, czas, 'o-')
    plt.xlabel('Rozmiar macierzy')
    plt.title('Zależność czasu działania programu od n')
    plt.ylabel('Czas działania (s)')
    plt.grid(True)
    plt.savefig('wykres5-2.png')

    plt.show()

wykres_czasu_dzialania_programu(20, 400, 20)
