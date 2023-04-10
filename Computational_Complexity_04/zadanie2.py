def wczytaj_macierz(n):
    macierz = []
    for i in range(n):
        wiersz = input(f"Wprowadź wiersz {i + 1} macierzy (liczby oddzielone spacjami): ")
        macierz.append([float(x) for x in wiersz.split()])
    return macierz

def mnoz_macierze(macierz_a, macierz_b):
    n = len(macierz_a)
    wynik = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                wynik[i][j] += macierz_a[i][k] * macierz_b[k][j]

    return wynik

# def wypisz_macierz(macierz):
#     for wiersz in macierz:
#         print(" ".join([str(x) for x in wiersz]))

n = int(input("Podaj rozmiar macierzy kwadratowych: "))
print("Wprowadź macierz A:")
macierz_a = wczytaj_macierz(n)
print("Wprowadź macierz B:")
macierz_b = wczytaj_macierz(n)


wynik = mnoz_macierze(macierz_a, macierz_b)

print("Wynik mnożenia macierzy A i B:")
# wypisz_macierz(wynik)

print(wynik)

# Funkcja wczytaj_macierz(n) ma złożoność O(n^2), ponieważ wczytujemy n wierszy, a każdy wiersz ma n elementów.
# Funkcja mnoz_macierze(macierz_a, macierz_b) ma złożoność O(n^3) z powodu trzech zagnieżdżonych pętli.
# Część wczytywania macierzy A i B ma łączną złożoność O(2n^2) = O(n^2).
# Cały kod ma złożoność O(n^2 + n^3), ale dominującym czynnikiem wzrostu jest n^3, więc łączna złożoność czasowa algorytmu wynosi O(n^3).