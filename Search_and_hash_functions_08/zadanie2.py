import random
import os
from typing import List, Tuple, Union


def losowy_typ() -> str:
    return random.choice(["AGV", "AFV", "ASV", "AUV"])


def losowa_cena() -> float:
    return round(random.uniform(0, 10000), 2)


def losowy_zasieg() -> int:
    return random.randint(0, 100)


def losowa_kamera() -> int:
    return random.choice([0, 1])


def generuj_robota() -> Tuple[str, float, int, int]:
    return losowy_typ(), losowa_cena(), losowy_zasieg(), losowa_kamera()


def generuj_liste_robotow(N: int) -> List[Tuple[str, float, int, int]]:
    return [generuj_robota() for _ in range(N)]


def wyswietl_roboty(roboty: List[Tuple[str, float, int, int]]) -> None:
    print(f"{'TYP':<5} {'CENA':<10} {'ZASIEG':<10} {'KAMERA':<10}")
    for robot in roboty:
        print(f"{robot[0]:<5} {robot[1]:<10} {robot[2]:<10} {robot[3]:<10}")


def zapisz_roboty_do_pliku(roboty: List[Tuple[str, float, int, int]], nazwa_pliku: str) -> None:
    with open(nazwa_pliku, "w") as plik:
        for robot in roboty:
            plik.write(f"{robot[0]} {robot[1]} {robot[2]} {robot[3]}\n")


def odczytaj_roboty_z_pliku(nazwa_pliku: str) -> List[Tuple[str, float, int, int]]:
    roboty = []
    if os.path.isfile(nazwa_pliku):
        with open(nazwa_pliku, "r") as plik:
            for linia in plik.readlines():
                TYP, CENA, ZASIEG, KAMERA = linia.strip().split()
                roboty.append((TYP, float(CENA), int(ZASIEG), int(KAMERA)))
    return roboty


####################################################
#wyszukiwanie liniowe

def dopasuj_parametr(wartosc: str, dopuszczalne_wartosci) -> bool:
    if dopuszczalne_wartosci is None:
        return True
    elif isinstance(dopuszczalne_wartosci, list):
        return wartosc in dopuszczalne_wartosci
    else:
        return wartosc == dopuszczalne_wartosci


def wyszukaj_robota(roboty: List[Tuple[str, float, int, int]], parametry: List) -> Union[
    str, Tuple[str, float, int, int]]:
    for robot in roboty:
        if (
                dopasuj_parametr(robot[0], parametry[0]) and
                dopasuj_parametr(robot[1], parametry[1]) and
                dopasuj_parametr(robot[2], parametry[2]) and
                dopasuj_parametr(robot[3], parametry[3])
        ):
            return robot
    return "brak"


N = int(input("Podaj długość listy robotów: "))
nazwa_pliku = "roboty.txt"

roboty = generuj_liste_robotow(N)
# wyswietl_roboty(roboty)
zapisz_roboty_do_pliku(roboty, nazwa_pliku)

roboty_odczytane = odczytaj_roboty_z_pliku(nazwa_pliku)
wyswietl_roboty(roboty_odczytane)

szukane_parametry = ["AGV", None, [5, 6, 7, 8, 9, 10], 1]
znaleziony_robot = wyszukaj_robota(roboty_odczytane, szukane_parametry)

print("--------------------")

if znaleziony_robot != "brak":
    print("Znaleziony robot:", znaleziony_robot)
else:
    print("Brak robota spełniającego kryteria wyszukiwania.")
