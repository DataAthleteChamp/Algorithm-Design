def znajdz_najwiekszy_element(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        polowa = len(lista) // 2
        lewa_polowa = lista[:polowa]
        prawa_polowa = lista[polowa:]
        max_lewej = znajdz_najwiekszy_element(lewa_polowa)
        max_prawej = znajdz_najwiekszy_element(prawa_polowa)
        return max(max_lewej, max_prawej)


# Złożoność czasowa tego algorytmu wynosi O(n*log(n))
# dzielenie na połowy logn
# porównywanie n

def znajdz_drugi_najwiekszy_element(lista):
    if len(lista) == 2:
        return min(lista[0], lista[1]), max(lista[0], lista[1])
    elif len(lista) == 1:
        return lista[0], None
    else:
        polowa = len(lista) // 2
        lewa_polowa = lista[:polowa]
        prawa_polowa = lista[polowa:]
        lewy_min, lewy_max = znajdz_drugi_najwiekszy_element(lewa_polowa)
        prawy_min, prawy_max = znajdz_drugi_najwiekszy_element(prawa_polowa)
        if prawy_max is None:
            return lewy_min, max(lewy_max, prawy_min)
        elif lewy_max is None:
            return prawy_min, max(prawy_max, lewy_min)
        else:
            return max(lewy_min, prawy_min), max(max(lewy_max, prawy_min), max(prawy_max, lewy_min))


# Złożoność czasowa tego algorytmu wynosi O(n*log(n))
# dzielenie na połowy logn
# porównywanie n


def oblicz_srednia(lista):
    n = len(lista)
    if n == 1:
        return lista[0]
    elif n == 2:
        return (lista[0] + lista[1]) / 2
    else:
        polowa = n // 2
        lewa_polowa = lista[:polowa]
        prawa_polowa = lista[polowa:]
        suma_lewej = oblicz_srednia(lewa_polowa)
        suma_prawej = oblicz_srednia(prawa_polowa)
        return (suma_lewej * len(lewa_polowa) + suma_prawej * len(prawa_polowa)) / n


# Złożoność czasowa tego algorytmu wynosi O(n*log(n))
# dzielenie na połowy logn
# porównywanie n


lista = input("Podaj liczby oddzielone przecinkami: ").split(",")
# lista = [int(x) for x in lista]

print("Największy element na liście:")
print(znajdz_najwiekszy_element(lista))
print('-----------')

print("Drugi największy element na liście:")
print(znajdz_drugi_najwiekszy_element(lista)[0])
print('-----------')

print("Średnia elementów na liście:")
print(oblicz_srednia(lista))
