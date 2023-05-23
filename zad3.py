import random
import json
from typing import Union


class Robot:
    def __init__(self, typ: str, cena: float, zasieg: int, kamera: int):
        self.typ = typ
        self.cena = cena
        self.zasieg = zasieg
        self.kamera = kamera


class ListaRobotow:
    def __init__(self):
        self.lista = []

    def dodaj_robota(self, robot: Robot):
        self.lista.append(robot)

    def usun_robota(self, typ: str):
        self.lista = [robot for robot in self.lista if robot.typ != typ]

    def wyszukaj_robota(self, typ: str) -> Union[Robot, None]:
        for robot in self.lista:
            if robot.typ == typ:
                return robot
        return None

    def sortuj_roboty(self):
        self.lista.sort(key=lambda robot: robot.cena)


def generuj_liste_robotow(n: int) -> ListaRobotow:
    lista_robotow = ListaRobotow()
    for _ in range(n):
        robot = generuj_robota()
        lista_robotow.dodaj_robota(robot)
    return lista_robotow


def generuj_robota() -> Robot:
    typy = ["AGV", "AFV", "ASV", "AUV"]
    typ = random.choice(typy)
    cena = round(random.uniform(0, 10000), 2)
    zasieg = random.randint(0, 100)
    kamera = random.randint(0, 1)

    return Robot(typ, cena, zasieg, kamera)


lista_robotow = generuj_liste_robotow(5)

print("Lista robotów przed usuwaniem:")
for robot in lista_robotow.lista:
    print(robot.__dict__)

typ = input('Podaj typ robota do usunięcia: ')
lista_robotow.usun_robota(typ)

print("Lista robotów po usuwaniu:")
for robot in lista_robotow.lista:
    print(robot.__dict__)

lista_robotow.sortuj_roboty()

print("Posortowana lista robotów:")
for robot in lista_robotow.lista:
    print(robot.__dict__)