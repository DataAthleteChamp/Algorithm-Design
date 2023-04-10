def rozklad(n):
    czynniki = []
    i = 2
    while i*i <= n:  # do ⌊√n⌋)
        if n % i == 0:
            czynniki.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        czynniki.append(n)
    return czynniki

n = int(input("Wprowadź liczbę do rozkładu: "))
print("Czynniki pierwsze liczby", n, "to:", rozklad(n))
