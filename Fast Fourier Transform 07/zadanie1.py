def naive_polynomial_multiplication(poly1, poly2):
    result = [0] * (len(poly1) + len(poly2) - 1)

    for i, coef1 in enumerate(poly1):
        for j, coef2 in enumerate(poly2):
            result[i + j] += coef1 * coef2

    return result

# Przykład użycia:
poly1 = [1, 2, 3]  # Wielomian: 1 + 2x + 3x^2
poly2 = [4, 5]     # Wielomian: 4 + 5x

result = naive_polynomial_multiplication(poly1, poly2)
print(result)      # Wypisze: [4, 13, 22, 15, 3], reprezentujące wielomian 4 + 13x + 22x^2 + 15x^3 + 3x^4
