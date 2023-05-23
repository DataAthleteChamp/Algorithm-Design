class KolejkaRobotow:
    def __init__(self):
        self.kolejka = []

    def dodaj_robota(self):
        typ = input("Podaj typ robota: ")
        cena = float(input("Podaj cenę robota: "))
        zasieg = int(input("Podaj zasięg robota: "))
        kamera = bool(int(input("Czy robot ma kamerę? (1 - tak, 0 - nie): ")))

        robot = {'typ': typ, 'cena': cena, 'zasieg': zasieg, 'kamera': kamera}
        self.kolejka.append(robot)

    def usun_robota(self):
        if len(self.kolejka) == 0:
            print("Kolejka jest pusta.")
            return None
        else:
            robot = self.kolejka.pop(0)
            print(f"Usunięto robota: {robot}")
            return robot

    def wyczysc_kolejke(self):
        while len(self.kolejka) > 0:
            self.usun_robota()


kolejka_robotow = KolejkaRobotow()

q = int(input('Ile robotów dodać: '))

for _ in range(q):
    kolejka_robotow.dodaj_robota()

print('Aktualna kolejka robotów:')
for i, robot in enumerate(kolejka_robotow.kolejka, 1):
    print(f"{i}. {robot}")

k = int(input('Ile robotów usunąć: '))

print('Usunięte roboty:')
for _ in range(k):
    robot = kolejka_robotow.usun_robota()
    if robot:
        print(robot)

n = int(input('Czy wyczyścić kolejkę? 1 - TAK, 0 - NIE: '))
if n == 0:
    print('Nie wyczyszczono kolejki')
else:
    kolejka_robotow.wyczysc_kolejke()
    print('Wyczyszczono kolejkę')
