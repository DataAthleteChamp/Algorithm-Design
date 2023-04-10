#Algorytm rekurencyjny dla ciągu 1
def ciag_1(n):
    if n == 0:
        return 1
    else:
        return 3**n + ciag_1(n-1)

# Wzór analityczny
#
# x(n) = 3^n + 3^(n-1) + 3^(n-2) + ... + 3^1 + 3^0 = (3^(n+1) - 1) / 2

#Procedura weryfikująca poprawność
def ciag1_weryfikacja(N):
    for n in range(N+1):
        wynik_analityczny = (3**(n+1) - 1) / 2
        wynik_numeryczny = ciag_1(n)
        if wynik_analityczny == wynik_numeryczny:
            print(f"n={n}: WYNIK POPRAWNY: {wynik_numeryczny}")
        else:
            print(f"n={n}: BŁĄD! wynik_analityczny={wynik_analityczny}, wynik_numeryczny={wynik_numeryczny}")

#Algorytm rekurencyjny dla ciągu 2
def ciag_2(n):
    if n == -1 or n == 0:
        return 0
    else:
        return n + ciag_2(n-2)

# Wzór analityczny
#
# x(n) = ((n + 1) // 2) ** 2  dla n nieparzytych
#x(n) = (n // 2) * (n + 2)//2      dla n parzystych
#jednak inne podejscie
#n[pierwszy element] + ((n - 2)//2) [ilosc wyrazów] * (n//2)[srednia watosc mnozenia]

#Procedura weryfikująca poprawność
def ciag2_weryfikacja(N):
    for n in range(N+1):
        #wynik_analityczny = ((n + 1) // 2) ** 2 #n nieparzyste
        #wynik_analityczny = (n // 2) * (n + 2)//2 #n parzytse
        wynik_analityczny = n + ((n - 2)//2 + n %2) * (n//2)
        wynik_numeryczny = ciag_2(n)
        if wynik_analityczny == wynik_numeryczny:
            print(f"n={n}: WYNIK POPRAWNY: {wynik_numeryczny}")
        else:
            print(f"n={n}: BŁĄD! wynik_analityczny={wynik_analityczny}, wynik_numeryczny={wynik_numeryczny}")



#Algorytm rekurencyjny dla ciągu 3 (ciągu Fibonacciego)
def ciag_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return ciag_fib(n-1) + ciag_fib(n-2)


# Wzór analityczny
#
# x(n) = (phi^n - (1-phi)^n) / sqrt(5),
# gdzie phi to tzw. złoty stosunek, czyli (1 + sqrt(5)) / 2


#Procedura weryfikująca poprawność
def ciag_fib_weryfikacja(N):
    phi = (1 + 5 ** 0.5) / 2
    for n in range(N+1):
        wynik_analityczny = int((phi ** n - (1-phi)**n) / 5 ** 0.5 + 0.5)
        wynik_numeryczny = ciag_fib(n)
        if wynik_analityczny == wynik_numeryczny:
            print(f"n={n}: WYNIK POPRAWNY: {wynik_numeryczny}")
        else:
            print(f"n={n}: BŁĄD! wynik_analityczny={wynik_analityczny}, wynik_numeryczny={wynik_numeryczny}")


######################################
n=10
N=10

print(f"ciag1 dla n={n} -> {ciag_1(n)}")
ciag1_weryfikacja(N)
print('-------------')

print(f"ciag2 dla n={n} -> {ciag_2(n)}")
ciag2_weryfikacja(N)
print('-------------')

print(f"ciag_fib dla n={n} -> {ciag_fib(n)}")
ciag_fib_weryfikacja(N)
print('-------------')