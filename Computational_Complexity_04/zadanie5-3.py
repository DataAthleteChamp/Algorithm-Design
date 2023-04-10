import matplotlib.pyplot as plt
import random
import timeit
from itertools import chain, combinations


def generuj_losowa_liste(n):
    return [random.randint(-1000, 1000) for _ in range(n)]


def czy_istnieje_podzbiór_o_sumie_zero(zbior):
    for podzbior in chain.from_iterable(combinations(zbior, r) for r in range(1, len(zbior) + 1)):
        if sum(podzbior) == 0:
            if len(podzbior) == 0:
                return False
            return True
    return False


def mierz_czas_dzialania_programu(n):
    czas = timeit.timeit(lambda: czy_istnieje_podzbiór_o_sumie_zero(generuj_losowa_liste(n)), number=10)
    return czas / 10


def wykres_czasu_dzialania_programu(dolny, gorny, krok):
    czasy = []
    for n in range(dolny, gorny + krok, krok):
        czas = mierz_czas_dzialania_programu(n)
        czasy.append((n, czas))

    n = [c[0] for c in czasy]
    czas = [c[1] for c in czasy]

    plt.plot(n, czas)
    plt.xlabel('Długość listy')
    plt.ylabel('Czas działania (s)')
    plt.title('Zależność czasu działania programu od n')
    plt.grid(True)
    plt.savefig('wykres5-3.png')
    plt.show()


wykres_czasu_dzialania_programu(1000, 100000, 100)
