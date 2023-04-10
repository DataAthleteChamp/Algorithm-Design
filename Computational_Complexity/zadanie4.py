import random
import timeit

def znajdz_najwiekszy_element(lista):
    najwiekszy = lista[0]
    for liczba in lista[1:]:
        if liczba > najwiekszy:
            najwiekszy = liczba
    return najwiekszy

def znajdz_drugi_najwiekszy_element(lista):
    if len(lista) < 2:
        return None
    max1, max2 = (lista[0], lista[1]) if lista[0] > lista[1] else (lista[1], lista[0])
    for liczba in lista[2:]:
        if liczba > max1:
            max2 = max1
            max1 = liczba
        elif liczba > max2:
            max2 = liczba
    return max2

def oblicz_srednia(lista):
    suma = sum(lista)
    srednia = suma / len(lista)
    return srednia

def generuj_liste_losowych_liczb(n):
    return [random.randint(1, 1000) for _ in range(n)]

def mierz_czas_dzialania_programu(n):
    lista = generuj_liste_losowych_liczb(n)
    czas = timeit.timeit(lambda: (
        znajdz_najwiekszy_element(lista),
        znajdz_drugi_najwiekszy_element(lista),
        oblicz_srednia(lista)
    ), number=10)
    return czas / 10

n = 1000000
czas = mierz_czas_dzialania_programu(n)
print(f"Czas działania programu dla n = {n}: {czas:.6f} sekund")
