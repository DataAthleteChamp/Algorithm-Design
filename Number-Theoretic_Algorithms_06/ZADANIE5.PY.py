import random
import math

# czy jest pierwsza
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# generowanie liczby o okreslonej ilości bitów i sprawdzanie czy jest pierwsza
def generate_prime(bits):
    while True:
        prime_candidate = random.getrandbits(bits) | 1  # Upewnij się, że liczba jest nieparzysta
        if is_prime(prime_candidate):
            return prime_candidate

# nwd euklides
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# odwrotność modularna do klucza prywatnego
def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return None
    return x % m

# rozszerzony algorytm euklidesa - potrzebny do znalezienia odwrotności modularnej
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y

# para kluczy rsa
def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)
    return {"e": e, "n": n}, {"d": d, "n": n}

# szyfrowanie tekstu do potegi e modulo n
# wykorzystuje klucz publiczny
def encrypt_rsa(plaintext, public_key):
    e, n = public_key["e"], public_key["n"]
    encrypted = [pow(ord(c), e, n) for c in plaintext]
    return encrypted

# odszyfrowanie tekstu podnosi do potegi d modulo n
# klucz prywatny
def decrypt_rsa(encrypted, private_key):
    d, n = private_key["d"], private_key["n"]
    decrypted = [chr(pow(c, d, n)) for c in encrypted]
    return "".join(decrypted)


# Testowanie algorytmu RSA
public_key, private_key = generate_keypair(32)

plaintext = "Tekst do zaszyfrowania olek to koks"
encrypted = encrypt_rsa(plaintext, public_key)
decrypted = decrypt_rsa(encrypted, private_key)

print("Tekst jawny:", plaintext)
print("Zaszyfrowany tekst:", encrypted)
print("Odszyfrowany tekst:", decrypted)