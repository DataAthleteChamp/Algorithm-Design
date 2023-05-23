class StosRobotow:
    def __init__(self):
        self.stos = []

    def dodaj_robota(self):
        typ = input("Podaj typ robota: ")
        cena = float(input("Podaj cenę robota: "))
        zasieg = int(input("Podaj zasięg robota: "))
        kamera = bool(int(input("Czy robot ma kamerę? (1 - tak, 0 - nie): ")))

        robot = {'typ': typ, 'cena': cena, 'zasieg': zasieg, 'kamera': kamera}
        self.stos.append(robot)

    def usun_robota(self):
        if len(self.stos) == 0:
            print("Stos jest pusty.")
            return None
        else:
            robot = self.stos.pop()
            print(f"Usunięto robota: {robot}")
            return robot

    def wyczysc_stos(self):
        while len(self.stos) > 0:
            self.usun_robota()

    def pokaz_elementy(self):
        if len(self.stos) == 0:
            print("Stos jest pusty.")
        else:
            print("Elementy na stosie:")
            for robot in reversed(self.stos):
                print(robot)


stos_robotow = StosRobotow()

q = int(input('ile robotów dodac: '))
for _ in range(q):
    stos_robotow.dodaj_robota()

k = int(input('ile robotów usunąć: '))
for _ in range(k):
    stos_robotow.usun_robota()

n = int(input('czy wyczyścić stos? 1 -TAK 0 - NIE'))
if n == 1:
    stos_robotow.wyczysc_stos()
else:
    print('nie wyczyszczono stosu')

stos_robotow.pokaz_elementy()
