import random


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_prime(bits):
    while True:
        prime_candidate = random.getrandbits(bits) | 1  # Upewnij się, że liczba jest nieparzysta
        if is_prime(prime_candidate):
            return prime_candidate


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


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


def encrypt_rsa(plaintext, public_key):
    e, n = public_key["e"], public_key["n"]
    encrypted = [pow(ord(c), e, n) for c in plaintext]
    return encrypted


def decrypt_rsa(encrypted, private_key):
    d, n = private_key["d"], private_key["n"]
    decrypted = [chr(pow(c, d, n)) for c in encrypted]
    return "".join(decrypted)


# Testowanie algorytmu RSA
public_key, private_key = generate_keypair(16)

plaintext = "Tekst do zaszyfrowania"
encrypted = encrypt_rsa(plaintext, public_key)
decrypted = decrypt_rsa(encrypted, private_key)

print("Tekst jawny:", plaintext)
print("Zaszyfrowany tekst:", encrypted)
print("Odszyfrowany tekst:", decrypted)
