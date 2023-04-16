
import random
from pycryptodome.Util import number


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def xgcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def mod_inverse(a, m):
    g, x, _ = xgcd(a, m)
    if g == 1:
        return x % m


def generate_keypair(bits):
    p = number.getPrime(bits)
    q = number.getPrime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)
    return (e, n), (d, n)


def encrypt(pk, plaintext):
    e, n = pk
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext


def decrypt(sk, ciphertext):
    d, n = sk
    plaintext = ''.join(chr(pow(char, d, n)) for char in ciphertext)
    return plaintext


if __name__ == '__main__':
    bits = 256
    public_key, private_key = generate_keypair(bits)
    print("Klucz publiczny:", public_key)
    print("Klucz prywatny:", private_key)

    message = "Przykładowy tekst do zaszyfrowania"
    encrypted_msg = encrypt(public_key, message)
    print("Zaszyfrowana wiadomość:", encrypted_msg)

    decrypted_msg = decrypt(private_key, encrypted_msg)
    print("Odszyfrowana wiadomość:", decrypted_msg)
