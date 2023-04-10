class AutomatSkończony:
    def __init__(self, stany, alfabet, przejścia, stan_początkowy, stany_akceptujące):

        self.stany = stany
        self.alfabet = alfabet
        self.przejścia = przejścia
        self.stan_początkowy = stan_początkowy
        self.stany_akceptujące = stany_akceptujące

    def uruchom(self, ciąg_wejściowy):

        bieżący_stan = self.stan_początkowy  # ustawiamy stan początkowy jako bieżący stan
        for symbol in ciąg_wejściowy:
            if symbol not in self.alfabet:  # sprawdzamy, czy symbol należy do alfabetu automatu
                return False  # jeśli symbol nie należy do alfabetu, to kończymy działanie funkcji i zwracamy False
            # sprawdzamy, czy istnieje przejście ze stanu bieżącego do kolejnego stanu po otrzymaniu danego symbolu
            bieżący_stan = self.przejścia.get((bieżący_stan, symbol), None)
            if bieżący_stan is None:  # jeśli takie przejście nie istnieje, to kończymy działanie funkcji i zwracamy False
                return False
        # jeśli przetworzyliśmy cały ciąg wejściowy i bieżący stan jest stanem akceptującym, to zwracamy True, w przeciwnym
        # wypadku zwracamy False
        return bieżący_stan in self.stany_akceptujące

# Na początku ustawiamy stan bieżący na stan początkowy automatu.
# Następnie dla każdego symbolu z ciągu wejściowego sprawdzamy,
# czy znajduje się w alfabecie automatu. Jeśli symbol nie znajduje się w alfabecie,
# to kończymy działanie funkcji i zwracamy wartość False.
# W przeciwnym wypadku sprawdzamy, czy istnieje przejście z bieżącego stanu do kolejnego stanu za pomocą słownika transitions.
# Jeśli takie przejście nie istnieje, to kończymy działanie funkcji i zwracamy wartość False.
# Jeśli natomiast istnieje przejście, to przechodzimy do kolejnego stanu i kontynuujemy przetwarzanie ciągu wejściowego.
# Po przetworzeniu całego ciągu wejściowego sprawdzamy, czy bieżący stan znajduje się w zbiorze stanów akceptujących automatu.
# Jeśli tak, to zwracamy wartość True. W przeciwnym wypadku zwracamy wartość False.



# zadanie2

stany2 = {'q0','q1','q2','q3','q4','q5','q6'}
alfabet2 = {'a','b','c'}
przejścia2 = {
    ('q0', 'a'): 'q2',
    ('q0', 'b'): 'q2',
    ('q0', 'c'): 'q2',
    ('q1', 'a'): 'q4',
    ('q1', 'b'): 'q0',
    ('q1', 'c'): 'q3',
    ('q2', 'a'): 'q1',
    ('q2', 'b'): 'q1',
    ('q2', 'c'): 'q6',
    ('q3', 'a'): 'q3',
    ('q3', 'b'): 'q3',
    ('q3', 'c'): 'q3',
    ('q4', 'a'): 'q0',
    ('q4', 'b'): 'q5',
    ('q4', 'c'): 'q5',
    ('q5', 'a'): 'q4',
    ('q5', 'b'): 'q4',
    ('q5', 'c'): 'q4',
    ('q6', 'a'): 'q3',
    ('q6', 'b'): 'q3',
    ('q6', 'c'): 'q3',
}
stan_początkowy2 = 'q0'
stany_akceptujące2 = {'q3','q5'}
automat2 = AutomatSkończony(stany2, alfabet2, przejścia2, stan_początkowy2, stany_akceptujące2)

print('zadanie2')
ciąg1 = 'abbcac'
if automat2.uruchom(ciąg1):
    print(f'Ciąg {ciąg1} jest akceptowany przez automat.')
else:
    print(f'Ciąg {ciąg1} nie jest akceptowany przez automat.')

ciąg2 = 'baaabb'
if automat2.uruchom(ciąg2):
    print(f'Ciąg {ciąg2} jest akceptowany przez automat.')
else:
    print(f'Ciąg {ciąg2} nie jest akceptowany przez automat.')

# zadanie3
# stany3 = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'}
# alfabet3 = {'0', '1', 'a'}
# przejścia3 = {
#     ('q0', 'a'): 'q1',
#     ('q1', 'a'): 'q1',
#     ('q1', '0'): 'q2',
#     ('q1', '1'): 'q2',
#     ('q2', '0'): 'q3',
#     ('q2', '1'): 'q3',
#     ('q3', 'a'): 'q4',
#     ('q4', '0'): 'q5',
#     ('q4', '1'): 'q5',
#     ('q5', 'a'): 'q6',
#     ('q6', '0'): 'q7',
#     ('q6', '1'): 'q7',
#     ('q7', 'a'): 'q7',
#     ('q7', '0'): 'q7',
#     ('q7', '1'): 'q7'
# }
# stan_początkowy3 = 'q0'
# stany_akceptujące3 = {'q7'}

stany3 = {'q0','q1','q2','q3'}
alfabet3 = {0,1,'a'}
przejścia3 = {
    ('q0', '0'): 'q1',
    ('q0', '1'): 'q0',
    ('q0', 'a'): 'q3',
    ('q1', '0'): 'q0',
    ('q1', '1'): 'q2',
    ('q1', 'a'): 'q0',
    ('q2', '0'): 'q2',
    ('q2', '1'): 'q0',
    ('q2', 'a'): 'q1',
    ('q3', '0'): 'q1',
    ('q3', '1'): 'q2',
    ('q3', 'a'): 'q0',
}
stan_początkowy3 = 'q0'
stany_akceptujące3 = {'q2','q3'}
automat3 = AutomatSkończony(stany3, alfabet3, przejścia3, stan_początkowy3, stany_akceptujące3)

print('----------------------')
print('zadanie3')

ciąg1 = 'a'
if automat3.uruchom(ciąg1):
    print(f'Ciąg {ciąg1} jest akceptowany przez automat.')
else:
    print(f'Ciąg {ciąg1} nie jest akceptowany przez automat.')

ciąg2 = 'a1001a'
if automat3.uruchom(ciąg2):
    print(f'Ciąg {ciąg2} jest akceptowany przez automat.')
else:
    print(f'Ciąg {ciąg2} nie jest akceptowany przez automat.')


# zadanie 4
# q0 akceptuje dowolną liczbę liter a,
# następnie q1 akceptuje literę b,
# a następnie q2 akceptuje dokładnie trzy litery bcd.
# Ostatecznie, q4 akceptuje dowolną liczbę liter d lub brak liter d.

stany4 = {'q0','q1','q2','q3','q4'}
alfabet4 = {'a','b','c','d'}
przejścia4 = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q4',
    ('q0', 'c'): 'q4',
    ('q0', 'd'): 'q4',
    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q2',
    ('q1', 'c'): 'q4',
    ('q1', 'd'): 'q4',
    ('q2', 'a'): 'q3',
    ('q2', 'b'): 'q4',
    ('q2', 'c'): 'q4',
    ('q2', 'd'): 'q4',
    ('q3', 'a'): 'q3',
    ('q3', 'b'): 'q4',
    ('q3', 'c'): 'q2',
    ('q3', 'd'): 'q4',
    ('q4', 'a'): 'q4',
    ('q4', 'b'): 'q4',
    ('q4', 'c'): 'q4',
    ('q4', 'd'): 'q4'
}

stan_początkowy4 = 'q0'
stany_akceptujące4 = {'q2','q4'}
automat4 = AutomatSkończony(stany4, alfabet4, przejścia4, stan_początkowy4, stany_akceptujące4)

print('----------------------')
print('zadanie4')

ciąg1 = 'aba'
if automat4.uruchom(ciąg1):
    print(f'Ciąg {ciąg1} jest akceptowany przez automat.')
else:
    print(f'Ciąg {ciąg1} nie jest akceptowany przez automat.')

ciąg2 = 'abcdc'
if automat4.uruchom(ciąg2):
    print(f'Ciąg {ciąg2} jest akceptowany przez automat.')
else:
    print(f'Ciąg {ciąg2} nie jest akceptowany przez automat.')

# zadanie5
print('----------------------')
print('zadanie5')

with open('automat.txt', 'r') as file:
    lines = file.readlines()
    stany = set(map(int, lines[0].split()))
    alfabet = set(lines[1].split())
    przejścia = {}
    for line in lines[2:-2]:
        a, symbol, b = line.split()
        przejścia[(int(a), symbol)] = int(b)
    stan_początkowy = int(lines[-2])
    stany_akceptujące = set(map(int, lines[-1].split()))

automat = AutomatSkończony(stany, alfabet, przejścia, stan_początkowy, stany_akceptujące)

# testujemy działanie automatu na konkretnych ciągach wejściowych
ciąg1 = 'abababa'
if automat.uruchom(ciąg1):
    print(f'Ciąg {ciąg1} jest akceptowany przez automat.')
else:
    print(f'Ciąg {ciąg1} nie jest akceptowany przez automat.')

ciąg2 = 'baaabb'
if automat.uruchom(ciąg2):
    print(f'Ciąg {ciąg2} jest akceptowany przez automat.')
else:
    print(f'Ciąg {ciąg2} nie jest akceptowany przez automat.')


# zadanie5 plik txt
# Pierwsza linia zawiera stany oddzielone spacjami.
# Druga linia zawiera symbole alfabetu oddzielone spacjami.
# Kolejne linie zawierają definicje przejść w formacie stan symbol stan.
# Przy czym wartości liczbowe są oddzielone spacjami, a symbol jest pojedynczym znakiem.
# Przedostatnia linia zawiera stan początkowy,
# a ostatnia linia zawiera stany akceptujące oddzielone spacjami.