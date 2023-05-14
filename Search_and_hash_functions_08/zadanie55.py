import random
import math
import time
import sys
import matplotlib.pyplot as plt


def generuj_robota(istniejace_ceny):
    typy = ["AGV", "AFV", "ASV", "AUV"]

    while True:
        cena = round(random.uniform(0, 10000), 2)
        if cena not in istniejace_ceny:
            istniejace_ceny.add(cena)
            break

    zasieg = random.randint(0, 100)
    kamera = random.randint(0, 1)
    return typy[random.randint(0, len(typy) - 1)], cena, zasieg, kamera


def stworz_liste_robotow(N):
    istniejace_ceny = set()
    return [generuj_robota(istniejace_ceny) for _ in range(N)]


def wyswietl_roboty(roboty):
    print("TYP   CENA       ZASIEG     KAMERA")
    for robot in roboty:
        print(f"{robot[0]}   {robot[1]:<9.2f} {robot[2]:<9} {robot[3]}")


def zapisz_roboty_do_pliku(roboty, nazwa_pliku):
    with open(nazwa_pliku, "w") as plik:
        for robot in roboty:
            plik.write(",".join(map(str, robot)) + "\n")


def wczytaj_roboty_z_pliku(nazwa_pliku):
    roboty = []
    with open(nazwa_pliku, "r") as plik:
        for linia in plik:
            dane_robota = linia.strip().split(",")
            robot = (dane_robota[0], float(dane_robota[1]), int(dane_robota[2]), int(dane_robota[3]))
            roboty.append(robot)
    return roboty


def wyszukiwanie_liniowe(roboty, parametry_szukania):
    for robot in roboty:
        pasuje = True
        for i, parametr in enumerate(parametry_szukania):
            if parametr is None:
                continue
            if isinstance(parametr, list) and robot[i] not in parametr:
                pasuje = False
                break
            if not isinstance(parametr, list) and robot[i] != parametr:
                pasuje = False
                break
        if pasuje:
            return robot
    return "brak"


def wyszukiwanie_binarne(posortowane_roboty, wartosc, poczatek, koniec, indeks_parametru):
    if poczatek > koniec:
        return "brak"

    srodek = (poczatek + koniec) // 2
    robot = posortowane_roboty[srodek]

    if robot[indeks_parametru] == wartosc:
        return robot
    elif robot[indeks_parametru] < wartosc:
        return wyszukiwanie_binarne(posortowane_roboty, wartosc, srodek + 1, koniec, indeks_parametru)
    else:
        return wyszukiwanie_binarne(posortowane_roboty, wartosc, poczatek, srodek - 1, indeks_parametru)




def funkcja_haszujaca(klucz, i, rozmiar_tablicy_haszujacej):
    h1 = sum(ord(c) for c in str(klucz)) % rozmiar_tablicy_haszujacej
    # h1 = klucz % rozmiar_tablicy_haszujacej
    # h2 = 1 + (klucz % (rozmiar_tablicy_haszujacej - 1))
    h2 = 1 + (sum(ord(c) for c in str(klucz)) % (rozmiar_tablicy_haszujacej - 1))

    return int((h1 + i * h2) % rozmiar_tablicy_haszujacej)


def stworz_tabele_haszujaca(roboty, rozmiar_tablicy_haszujacej, indeks_parametru):
    tabela_haszujaca = [None] * rozmiar_tablicy_haszujacej
    for robot in roboty:
        klucz = robot[indeks_parametru]
        i = 0
        while True:
            indeks = funkcja_haszujaca(klucz, i, rozmiar_tablicy_haszujacej)
            if tabela_haszujaca[indeks] is None:
                tabela_haszujaca[indeks] = robot
                break
            i += 1
    return tabela_haszujaca


def wyszukiwanie_z_funkcja_haszujaca(tabela_haszujaca, wartosc, rozmiar_tablicy_haszujacej, indeks_parametru):
    i = 0
    while True:
        indeks = funkcja_haszujaca(wartosc, i, rozmiar_tablicy_haszujacej)
        if tabela_haszujaca[indeks] is None:
            return "brak"
        if tabela_haszujaca[indeks][indeks_parametru] == wartosc:
            return tabela_haszujaca[indeks]
        i += 1


def porownaj_algorytmy_wyszukiwania(roboty, posortowane_roboty, tabela_haszujaca, rozmiar_tablicy_haszujacej, alpha):
    liczba_prob = len(roboty)
    srednie_czasy_liniowe = []
    srednie_czasy_binarnych = []
    srednie_czasy_haszujace = []

    for proba in range(liczba_prob):
        start = time.perf_counter()
        wyszukiwanie_liniowe(roboty, [None, posortowane_roboty[proba][1], None, None])
        koniec = time.perf_counter()
        srednie_czasy_liniowe.append((koniec - start) / liczba_prob)

        start = time.perf_counter()
        wyszukiwanie_binarne(posortowane_roboty, posortowane_roboty[proba][1], 0, len(posortowane_roboty) - 1, 1)
        koniec = time.perf_counter()
        srednie_czasy_binarnych.append((koniec - start) / liczba_prob)

        start = time.perf_counter()
        wyszukiwanie_z_funkcja_haszujaca(tabela_haszujaca, posortowane_roboty[proba][1], rozmiar_tablicy_haszujacej, 1)
        koniec = time.perf_counter()
        srednie_czasy_haszujace.append((koniec - start) / liczba_prob)

    plt.plot(range(1, liczba_prob + 1), srednie_czasy_liniowe, label="Wyszukiwanie liniowe")
    plt.plot(range(1, liczba_prob + 1), srednie_czasy_binarnych, label="Wyszukiwanie binarne")
    plt.plot(range(1, liczba_prob + 1), srednie_czasy_haszujace, label="Wyszukiwanie z funkcją haszującą")

    plt.xlabel("Numer próby")
    plt.ylabel("Średni czas wyszukiwania")
    plt.title("Porównanie algorytmów wyszukiwania")
    plt.legend()
    plt.savefig('zadanie5')
    plt.show()


N = int(input("Podaj długość listy robotów: "))
alpha = float(input("Podaj współczynnik wypełnienia tablicy α: "))
indeks_parametru = int(input("Wybierz indeks parametru szukanego robota (0 - Typ, 1 - Cena, 2 - Zasięg, 3 - Kamera): "))

roboty = stworz_liste_robotow(N)
posortowane_roboty = sorted(roboty, key=lambda x: x[1])
rozmiar_tablicy_haszujacej = math.ceil(len(roboty) / alpha)
tabela_haszujaca = stworz_tabele_haszujaca(roboty, rozmiar_tablicy_haszujacej, indeks_parametru)

porownaj_algorytmy_wyszukiwania(roboty, posortowane_roboty, tabela_haszujaca, rozmiar_tablicy_haszujacej, alpha)
