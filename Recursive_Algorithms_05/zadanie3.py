def scalanie(lewa, prawa):
    wynik = []
    i, j = 0, 0
    while i < len(lewa) and j < len(prawa):
        if lewa[i] < prawa[j]:
            wynik.append(lewa[i])
            i += 1
        else:
            wynik.append(prawa[j])
            j += 1
    wynik.extend(lewa[i:])
    wynik.extend(prawa[j:])
    return wynik


# porownujemy pierwsze elementy list
# wybieramy mniejszy elemnt i wpisujemy go do listy wynikowej
# usuwamy element z bazowej listy po dodaniu do wynikowej
# powtarzamy czynnosci az do oproznienia list

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    polowa = len(lista) // 2
    lewa = lista[:polowa]
    prawa = lista[polowa:]
    lewa_posortowana = merge_sort(lewa)
    prawa_posortowana = merge_sort(prawa)
    return scalanie(lewa_posortowana, prawa_posortowana)


lista = input("Podaj liczby oddzielone przecinkami: ").split(",")
lista = [int(x) for x in lista]

posortowana_lista = merge_sort(lista)

print(f"Posortowana lista: {posortowana_lista}")

# Algorytm sortowania przez scalanie działa w następujący sposób:
#
# Jeśli lista ma jeden lub mniej elementów, to jest już posortowana i zwracana jako wynik.
# Dzielę listę na dwie połowy i rekurencyjnie sortuję każdą z połówek.
# Łączę dwie posortowane połowy w jedną posortowaną listę, wykorzystując funkcję scalanie.
# Funkcja scalanie porównuje elementy z dwóch posortowanych list
# i tworzy nową listę zawierającą elementy w kolejności od najmniejszego do największego.

# Algorytm sortowania przez scalanie działa w czasie O(n log n) dla list o długości n.

#https://pl.wikipedia.org/wiki/Sortowanie_przez_scalanie