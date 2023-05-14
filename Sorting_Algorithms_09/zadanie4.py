
def get_input_matrix():
    rows = int(input("Podaj liczbę wierszy: "))
    cols = int(input("Podaj liczbę kolumn: "))

    matrix = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(int(input(f"Podaj element dla wiersza {r + 1}, kolumny {c + 1}: ")))
        matrix.append(row)

    return matrix


def counting_sort_for_radix(input_array, digit_index):
    size = len(input_array)
    output = [0] * size
    count = [0] * 10

    for i in range(size):
        index = abs(input_array[i]) // 10 ** digit_index % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = abs(input_array[i]) // 10 ** digit_index % 10
        output[count[index] - 1] = input_array[i]
        count[index] -= 1
        i -= 1

    for i in range(size):
        input_array[i] = output[i]


def radixsort(input_array):
    # Szukanie maksymalnej liczby, aby poznać liczbę cyfr
    max_element = max(input_array)
    digit_place = 0

    # Wykonywanie sortowania przez zliczanie dla każdej cyfry
    while 10 ** digit_place <= max_element:
        counting_sort_for_radix(input_array, digit_place)
        digit_place += 1


def sort_matrix(matrix):
    transposed_matrix = [list(x) for x in zip(*matrix)]  # Transponowanie macierzy
    for row in transposed_matrix:
        radixsort(row)  # Sortowanie każdego wiersza
    return [list(x) for x in zip(*transposed_matrix)]  # Ponowne transponowanie, by wrócić do pierwotnej formy


# Pobranie macierzy od użytkownika
matrix = get_input_matrix()

# Sortowanie macierzy
sorted_matrix = sort_matrix(matrix)

print("Posortowana macierz:")
for row in sorted_matrix:
    print(row)
