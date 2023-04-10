from itertools import chain, combinations


def wczytaj_zbior():
    liczby = input("Wprowadź zbiór liczb całkowitych oddzielonych spacjami: ")
    return [int(x) for x in liczby.split()]


def czy_istnieje_podzbiór_o_sumie_zero(zbior):
    for podzbior in chain.from_iterable(combinations(zbior, r) for r in range(1, len(zbior) + 1)):
        if sum(podzbior) == 0:
            print(f"Znaleziono podzbiór o sumie równiej 0: {podzbior}")
            if len(podzbior) == 0:
                print("zbiór pusty")
                return False
            return True
    return False


zbior = wczytaj_zbior()

wynik = czy_istnieje_podzbiór_o_sumie_zero(zbior)

if wynik:
    print("Istnieje podzbiór o sumie równiej 0.")
else:
    print("Nie istnieje podzbiór o sumie równiej 0.")




#Iterujemy przez wszystkie podzbiory (2^n podzbiorów)
#Dla każdego z tych podzbiorów, obliczamy sumę elementów (w najgorszym przypadku n elementów)
#
# Generowanie wszystkich możliwych podzbiorów zbioru wejściowego:
# liczba wszystkich podzbiorów zbioru n-elementowego wynosi 2^n,
# gdyż każdy element może być obecny lub nieobecny w podzbiorze.
# W tym przypadku pomijamy pusty podzbiór, więc liczba możliwych podzbiorów wynosi 2^n - 1.

# Iteracja po wszystkich podzbiorach ma złożoność O(2^n),
# ponieważ musimy sprawdzić wszystkie możliwe podzbiory.
# W przypadku sumowania wartości podzbioru, złożoność czasowa sumowania dla każdego podzbioru jest O(n),
# ponieważ w najgorszym przypadku każdy podzbiór będzie zawierał wszystkie n elementy.