import math
import random
#do dokończenia
def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def test_pierwszosci(n, k=10):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for i in range(k):
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for j in range(s-1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False
    return True

def generuj_klucze(p, q):
    if not (test_pierwszosci(p) and test_pierwszosci(q)):
        raise ValueError("p i q muszą być liczbami pierwszymi")
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    if nwd(e, phi) != 1:
        raise ValueError("e musi być względnie pierwsze z phi")
    d = pow(e, -1, phi)
    return (e, n), (d, n)

def dziel_tekst(tekst, dlugosc):
    return [tekst[i:i+dlugosc] for i in range(0, len(tekst), dlugosc)]

def szyfruj_tekst(tekst, klucz):
    e, n = klucz
    bloki = dziel_tekst(tekst, int(math.log(n, 256)))
    zaszyfrowany = []
    for blok in bloki:
        liczba = int.from_bytes(blok.encode(), 'big')
        zaszyfrowana = pow(liczba, e, n)
        zaszyfrowany.append(zaszyfrowana)
    return zaszyfrowany

def deszyfruj_tekst(zaszyfrowany, klucz):
    d, n = klucz
    odszyfrowany = []
    for zaszyfrowana in zaszyfrowany:
        liczba = pow(zaszyfrowana, d, n)
        odszyfrowana = liczba.to_bytes((liczba.bit_length() + 7) // 8, 'big').decode()
        odszyfrowany.append(odszyfrowana)
    return ''.join(odszyfrowany)

# przykładowe użycie
# wygenerowanie kluczy
p = 1373
q = 2099
klucz_publiczny, klucz_prywatny = generuj_klucze(p, q)
print("Klucz publiczny:", klucz_publiczny)
print("Klucz prywatny:", klucz_prywatny)

# przykładowy tekst do zaszyfrowania
tekst = "Ala ma kota i dzień jest piękny."

# podział tekstu na bloki i szyfrowanie
zaszyfrowany_tekst = szyfruj_tekst(tekst, klucz_publiczny)

# # odszyfrowanie i wyświetlenie tekstu
# odszyfrowany_tekst = deszyfruj_tekst(zaszyfrowany_tekst, klucz_prywatny)
# print("Odszyfrowany tekst:", odszyfrowany_tekst)

# odszyfrowanie i wyświetlenie tekstu
odszyfrowany_tekst = deszyfruj_tekst(zaszyfrowany_tekst, klucz_prywatny)
print("Odszyfrowany tekst:", odszyfrowany_tekst.encode('latin-1').decode('utf-8'))
