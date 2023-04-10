import random
import timeit
import matplotlib.pyplot as plt


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

#atos cybertech

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

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    polowa = len(lista) // 2
    lewa = lista[:polowa]
    prawa = lista[polowa:]
    lewa_posortowana = merge_sort(lewa)
    prawa_posortowana = merge_sort(prawa)
    return scalanie(lewa_posortowana, prawa_posortowana)



def time_function(func, input_data):
    start_time = timeit.default_timer()
    func(input_data)
    end_time = timeit.default_timer()
    return end_time - start_time


def generate_random_input(size):
    return [random.randint(1, 1000) for _ in range(size)]


input_sizes = list(range(10000, 30001, 50))
znajdz_najwiekszy_element_times = []
znajdz_drugi_najwiekszy_element_times = []
oblicz_srednia_times = []
merge_sort_times = []

for size in input_sizes:
    random_input = generate_random_input(size)
    znajdz_najwiekszy_element_times.append(time_function(znajdz_najwiekszy_element, random_input))
    znajdz_drugi_najwiekszy_element_times.append(time_function(znajdz_drugi_najwiekszy_element, random_input))
    oblicz_srednia_times.append(time_function(oblicz_srednia, random_input))
    merge_sort_times.append(time_function(merge_sort, random_input))

plt.plot(input_sizes, znajdz_najwiekszy_element_times, label='znajdz_najwiekszy_element')
plt.plot(input_sizes, znajdz_drugi_najwiekszy_element_times, label='znajdz_drugi_najwiekszy_element')
plt.plot(input_sizes, oblicz_srednia_times, label='oblicz_srednia')
plt.plot(input_sizes,merge_sort_times,label='merge_sort')
plt.xlabel('Rozmiar wejścia')
plt.ylabel('Czas działania (s)')
plt.legend()
plt.savefig('zadanie5_1.png')
plt.show()
