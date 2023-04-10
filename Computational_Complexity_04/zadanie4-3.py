import random
import timeit
from itertools import chain, combinations

def generuj_losowa_liste(n):
    return [random.randint(-1000, 1000) for _ in range(n)]

def czy_istnieje_podzbiór_o_sumie_zero(zbior):
    for podzbior in chain.from_iterable(combinations(zbior, r) for r in range(1, len(zbior) + 1)):
        if sum(podzbior) == 0:
            print(f"Znaleziono podzbiór o sumie równiej 0: {podzbior}")
            if len(podzbior) == 0:
                print("zbiór pusty")
                return False
            return True
    return False

# def mierz_czas_dzialania_programu(n):
#     lista = generuj_losowa_liste(n)
#     czas = timeit.timeit(lambda: czy_istnieje_podzbiór_o_sumie_zero(lista), number=10)
#     return czas / 10

def mierz_czas_dzialania_programu(n):
    czas = timeit.timeit(lambda: czy_istnieje_podzbiór_o_sumie_zero(generuj_losowa_liste(n)), number=10)
    return czas / 10


n = int(input("Podaj długość listy liczb: "))

czas = mierz_czas_dzialania_programu(n)

print(f"Czas działania programu dla n = {n}: {czas:.6f} sekund")
