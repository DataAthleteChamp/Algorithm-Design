import random


def potega_modulo(a, k, p):
    if k == 0:
        return 1
    if k % 2 == 1:
        return (a * potega_modulo(a, k - 1, p)) % p
    else:
        b = potega_modulo(a, k // 2, p)
        return (b * b) % p


def test_fermata(n, k=10):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(k):
        a = random.randint(2, n - 2)
        if potega_modulo(a, n - 1, n) != 1:
            return False
    return True


def test_miller_rabina(n, k=10):
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
        a = random.randint(2, n - 2)
        x = potega_modulo(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


n = int(input("Wprowadź liczbę do sprawdzenia pierwszosci: "))

if test_fermata(n):
    print('test fermata:', n, "jest prawdopodobnie pierwsza")
else:
    print('test fermata:', n, "jest złożona")

if test_miller_rabina(n):
    print('test rabina:', n, "jest prawdopodobnie pierwsza")
else:
    print('test rabina:', n, "jest złożona")

"""
Funkcja potega_modulo służy do szybkiego obliczania potęg modulo za pomocą algorytmu iteracyjnego. 

Funkcja test_fermata implementuje test pierwszości Fermata, który polega na sprawdzeniu, 
czy dla losowo wybranej liczby a zachodzi a^(n-1) ≡ 1 (mod n). 

Funkcja test_miller_rabina implementuje test pierwszości Millera-Rabina, 
który również wykorzystuje losowo wybrane liczby i potęgi modulo, ale jest bardziej skomplikowany.

k określa ilość powtórzeń testu dla każdej liczby. 
Im większa wartość k, tym mniejsze jest prawdopodobieństwo, 
że liczba złożona zostanie uznana za pierwszą. Jednakże, 
większa ilość powtórzeń oznacza dłuższy czas wykonania testów
"""
