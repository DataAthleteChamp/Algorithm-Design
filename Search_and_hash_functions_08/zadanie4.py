import random
import math
import sys


def generuj_robota():
    typy = ["AGV", "AFV", "ASV", "AUV"]
    cena = round(random.uniform(0, 10000), 2)
    zasieg = random.randint(0, 100)
    kamera = random.randint(0, 1)
    return typy[random.randint(0, len(typy) - 1)], cena, zasieg, kamera


def stworz_liste_robotow(N):
    return [generuj_robota() for _ in range(N)]


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


###########################################3
# wyszukiwanie z wykorzystaniem funkcji haszującej

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


N = int(input("Podaj długość listy robotów: "))
roboty = stworz_liste_robotow(N)
# wyswietl_roboty(roboty)
zapisz_roboty_do_pliku(roboty, "roboty.txt")

wczytane_roboty = wczytaj_roboty_z_pliku("roboty.txt")
wyswietl_roboty(wczytane_roboty)
#
# parametry_wyszukiwania = ["AGV", None, [5, 6, 7, 8, 9, 10], 1]
# wynik = wyszukiwanie_liniowe(wczytane_roboty, parametry_wyszukiwania)
# print("Wynik wyszukiwania liniowego:", wynik)
#
# indeks_parametru = 1
# posortowane_roboty = sorted(wczytane_roboty, key=lambda x: x[indeks_parametru])
# wartosc_szukana = 2500
# wynik = wyszukiwanie_binarne(posortowane_roboty, wartosc_szukana, 0, len(posortowane_roboty) - 1, indeks_parametru)
# print("Wynik wyszukiwania binarnego:", wynik)

alpha = float(input("Podaj współczynnik wypełnienia tablicy α: "))
rozmiar_tablicy_haszujacej = math.ceil(len(roboty) / alpha)
indeks_parametru = int(input("Wybierz indeks parametru szukanego robota (0 - Typ, 1 - Cena, 2 - Zasięg, 3 - Kamera): "))
tabela_haszujaca = stworz_tabele_haszujaca(roboty, rozmiar_tablicy_haszujacej, indeks_parametru)

if indeks_parametru in [1, 2, 3]:  # jeśli parametr to Cena, Zasięg lub Kamera
    try:
        wartosc_szukana = float(input("Podaj wartość szukanego parametru: "))
    except ValueError:
        print("Wartość parametru powinna być liczbą.")
        sys.exit(1)
else:
    wartosc_szukana = input("Podaj wartość szukanego parametru: ")

wynik = wyszukiwanie_z_funkcja_haszujaca(tabela_haszujaca, wartosc_szukana, rozmiar_tablicy_haszujacej,
                                         indeks_parametru)
print("Wynik wyszukiwania z wykorzystaniem funkcji haszującej:", wynik)
