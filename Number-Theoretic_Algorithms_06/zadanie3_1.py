def rozklad(n):
    czynniki = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            czynniki.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        czynniki.append(n)
    return czynniki


def nwd_rozkład(a, b):
    czynniki_a = rozklad(a)
    czynniki_b = rozklad(b)
    i = 0
    j = 0
    wynik = 1
    while i < len(czynniki_a) and j < len(czynniki_b):
        if czynniki_a[i] == czynniki_b[j]:
            wynik *= czynniki_a[i]
            i += 1
            j += 1
        elif czynniki_a[i] < czynniki_b[j]:
            i += 1
        else:
            j += 1
    return wynik


# alg euklidesa
# NWD(a, b) = NWD(b, a % b)

def nwd_euklides(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a = int(input("Wprowadź liczbę a: "))
b = int(input("Wprowadź liczbę b: "))

print("NWD euklides:(", a, ",", b, ") =", nwd_euklides(a, b))

print("NWD rozkład:(", a, ",", b, ") =", nwd_rozkład(a, b))
