import random
import sys


def is_prime(n, k=5):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    d = n - 1
    while d % 2 == 0:
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        while d != n - 1:
            x = pow(x, 2, n)
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            continue
        break
    return True


def generate_prime(bits):
    while True:
        candidate = random.getrandbits(bits)
        if is_prime(candidate):
            return candidate


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
    p = generate_prime(bits)
    q = generate_prime(bits)
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
    plaintext = ''.join(chr(pow(char, d, n) % sys.maxunicode) for char in ciphertext)
    return plaintext

#
# def decrypt(sk, ciphertext):
#     d, n = sk
#     #plaintext = ''.join(chr(pow(char, d, n) % 1_114_112) for char in ciphertext)
#     plaintext = ''.join(chr(pow(char, d, n)) for char in ciphertext)
#     #plaintext = ''.join(chr(pow(char, d, n)) for char in ciphertext)
#     return plaintext


def encrypt_long(pk, plaintext, chunk_size):
    e, n = pk
    chunks = [plaintext[i:i + chunk_size] for i in range(0, len(plaintext), chunk_size)]
    encrypted_chunks = [encrypt(pk, chunk) for chunk in chunks]
    return encrypted_chunks


def decrypt_long(sk, encrypted_chunks):
    decrypted_chunks = [decrypt(sk, chunk) for chunk in encrypted_chunks]
    return ''.join(decrypted_chunks)

def text_to_int(text):
    return int.from_bytes(text.encode('utf-8'), 'big')

def int_to_text(number):
    return number.to_bytes((number.bit_length() + 7) // 8, 'big').decode('utf-8')


if __name__ == '__main__':
    bits = 512
    public_key, private_key = generate_keypair(bits)
    print("Klucz publiczny:", public_key)
    print("Klucz prywatny:", private_key)

    message = "poezja"
    encrypted_msg = encrypt(public_key, message)
    print("Zaszyfrowana wiadomość:", encrypted_msg)

    decrypted_msg = decrypt(private_key, encrypted_msg)
    print("Odszyfrowana wiadomość:", decrypted_msg)

    chunk_size = 10
    long_message = "qwertyiupoasfdhgkjlxzvcnbm."
    encrypted_chunks = encrypt_long(public_key, long_message, chunk_size)
    print("Zaszyfrowana dłuższa wiadomość:", encrypted_chunks)

    decrypted_long_message = decrypt_long(private_key, encrypted_chunks)
    print("Odszyfrowana dłuższa wiadomość:", decrypted_long_message)

