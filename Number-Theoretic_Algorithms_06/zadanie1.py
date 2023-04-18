def rozklad(n, i=2, czynniki=None):
    if czynniki is None:
        czynniki = []

    if i * i > n:
        if n > 1:
            czynniki.append(n)
        return czynniki

    if n % i == 0:
        czynniki.append(i)
        return rozklad(n // i, i, czynniki)
    else:
        return rozklad(n, i + 1, czynniki)

n = int(input("Wprowadź liczbę do rozkładu: "))
print("Czynniki pierwsze liczby", n, "to:", rozklad(n))
