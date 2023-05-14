import random
from typing import List, Tuple, Union


def generuj_robota() -> Tuple[str, float, int, int]:
    typy = ["AGV", "AFV", "ASV", "AUV"]
    typ = random.choice(typy)
    cena = round(random.uniform(0, 10000), 2)
    zasieg = random.randint(0, 100)
    kamera = random.randint(0, 1)

    return typ, cena, zasieg, kamera


def generuj_liste_robotow(n: int) -> List[Tuple[str, float, int, int]]:
    return [generuj_robota() for _ in range(n)]


def wyswietl_roboty(roboty: List[Tuple[str, float, int, int]]):
    print("TYP   CENA       ZASIEG     KAMERA")
    for robot in roboty:
        print(f"{robot[0]:<5} {robot[1]:<9.2f} {robot[2]:<9} {robot[3]}")


def zapisz_roboty_do_pliku(roboty: List[Tuple[str, float, int, int]], nazwa_pliku: str):
    with open(nazwa_pliku, "w") as plik:
        for robot in roboty:
            plik.write(f"{robot[0]} {robot[1]} {robot[2]} {robot[3]}\n")


def odczytaj_roboty_z_pliku(nazwa_pliku: str) -> List[Tuple[str, float, int, int]]:
    roboty = []

    with open(nazwa_pliku, "r") as plik:
        for linia in plik:
            typ, cena, zasieg, kamera = linia.strip().split()
            roboty.append((typ, float(cena), int(zasieg), int(kamera)))

    return roboty


def wyszukaj_robota(roboty: List[Tuple[str, float, int, int]],
                    szukane_parametry: List[Union[str, float, int, list, None]]) -> Union[str, Tuple[str, float, int, int]]:
    for robot in roboty:
        if all(parametr is None or robot[i] in parametr if isinstance(parametr, list) else robot[i] == parametr for
               i, parametr in enumerate(szukane_parametry)):
            return robot

    return "brak"

##################################################
#wyszukiwanie binarne

def parametr_do_indeksu(parametr: str) -> int:
    if parametr == "TYP":
        return 0
    elif parametr == "CENA":
        return 1
    elif parametr == "ZASIEG":
        return 2
    elif parametr == "KAMERA":
        return 3
    else:
        raise ValueError("Nieprawidłowy parametr")


def wyszukaj_binarnie(roboty: List[Tuple[str, float, int, int]], parametr: str, dopuszczalne_wartosci: list) -> Union[str, Tuple[str, float, int, int]]:
    indeks = parametr_do_indeksu(parametr)
    roboty.sort(key=lambda x: x[indeks])

    lewy, prawy = 0, len(roboty) - 1
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        wartosc_srodka = roboty[srodek][indeks]

        if wartosc_srodka in dopuszczalne_wartosci:
            return roboty[srodek]
        elif wartosc_srodka < min(dopuszczalne_wartosci):
            lewy = srodek + 1
        else:
            prawy = srodek - 1

    return "brak"


def pobierz_parametr():
    parametr = input("Podaj parametr wyszukiwania (TYP, CENA, ZASIĘG, KAMERA): ")
    while parametr not in ["TYP", "CENA", "ZASIĘG", "KAMERA"]:
        print("Nieprawidłowy parametr. Spróbuj ponownie.")
        parametr = input("Podaj parametr wyszukiwania (TYP, CENA, ZASIĘG, KAMERA): ")
    return parametr


def pobierz_dopuszczalne_wartosci(parametr):
    if parametr == "TYP":
        return input("Podaj listę dopuszczalnych wartości TYP oddzielonych przecinkami: ").split(',')
    elif parametr == "CENA":
        return list(map(float, input("Podaj listę dopuszczalnych wartości CENA oddzielonych przecinkami: ").split(',')))
    elif parametr == "ZASIĘG":
        return list(map(int, input("Podaj listę dopuszczalnych wartości ZASIĘG oddzielonych przecinkami: ").split(',')))
    elif parametr == "KAMERA":
        return list(map(int, input("Podaj listę dopuszczalnych wartości KAMERA oddzielonych przecinkami: ").split(',')))


def main():
    N = int(input("Podaj długość listy robotów: "))
    roboty = generuj_liste_robotow(N)
    #wyswietl_roboty(roboty)
    zapisz_roboty_do_pliku(roboty, "roboty.txt")

    roboty_z_pliku = odczytaj_roboty_z_pliku("roboty.txt")
    wyswietl_roboty(roboty_z_pliku)

    parametr = pobierz_parametr()
    dopuszczalne_wartosci = pobierz_dopuszczalne_wartosci(parametr)
    znaleziony_robot_binarnie = wyszukaj_binarnie(roboty_z_pliku, parametr, dopuszczalne_wartosci)
    print(f"Znaleziony robot (wyszukiwanie binarne): {znaleziony_robot_binarnie}")


if __name__ == "__main__":
    main()
