def sito_eratostenesa(p):
    sito = [True] * (p+1)
    sito[0] = False
    sito[1] = False
    for i in range(2, int(p**0.5)+1):
        if sito[i]:
            for j in range(i**2, p+1, i):
                sito[j] = False
    return [liczba for liczba in range(p+1) if sito[liczba]]



p = int(input("wprowadz liczba naturalna p > 1:"))
print("Liczby pierwsze nie wieksze od p =", p, "to:", sito_eratostenesa(p))


""""
Algorytm sita Eratostenesa polega na oznaczaniu jako złożone (czyli nie-pierwsze) 
kolejnych wielokrotności liczb pierwszych począwszy od 2, aż do pierwiastka kwadratowego z p. 
W ten sposób zostaną oznaczone wszystkie złożone liczby, pozostawiając tylko liczby pierwsze.


"""