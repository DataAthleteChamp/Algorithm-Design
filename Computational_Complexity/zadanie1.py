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


liczby = input("Wprowadź listę liczb oddzielonych spacjami: ")
lista = [int(x) for x in liczby.split()]

print("Lista liczb:", lista)
print("największy element:", znajdz_najwiekszy_element(lista))
print("drugi największy element:", znajdz_drugi_najwiekszy_element(lista))
print("srednia:", oblicz_srednia(lista))

# 1
# Znajdowanie największego elementu na liście:
# Algorytm iteruje przez listę raz, porównując każdy element z aktualnie największym elementem.
# Złożoność czasowa wynosi O(n), gdzie n to liczba elementów na liście.

# 2
# Znajdowanie drugiego największego elementu na liście:
# Algorytm iteruje przez listę raz, utrzymując dwie zmienne dla największego i drugiego największego elementu.
# Złożoność czasowa wynosi O(n), gdzie n to liczba elementów na liście.

# 3
# Obliczanie średniej elementów na liście:
# Algorytm sumuje elementy listy, a następnie dzieli sumę przez liczbę elementów.
# Złożoność czasowa wynosi O(n) dla sumowania elementów, gdzie n to liczba elementów na liście.
# Dzielenie to pojedyncza operacja, więc złożoność całkowita wynosi O(n).