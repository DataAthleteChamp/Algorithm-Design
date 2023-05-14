import json
import heapq
import random
from typing import List, Tuple, Dict, Union


def generuj_robota() -> dict[str, Union[str, float, int]]:
    typy = ["AGV", "AFV", "ASV", "AUV"]
    typ = random.choice(typy)
    cena = round(random.uniform(0, 10000), 2)
    zasieg = random.randint(0, 100)
    kamera = random.randint(0, 1)

    return {'typ': typ, 'cena': cena, 'zasieg': zasieg, 'kamera': kamera}


def generuj_liste_robotow(n: int) -> list[dict[str, Union[str, float, int]]]:
    return [generuj_robota() for _ in range(n)]


def heapify(arr, n, i, step_by_step=False):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i]['cena'] < arr[left]['cena']:
        largest = left

    if right < n and arr[largest]['cena'] < arr[right]['cena']:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, step_by_step)


def heap_sort(arr, step_by_step=False):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i, step_by_step)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, step_by_step)

        if step_by_step:
            print(f"Ceny robotów po iteracji: {[robot['cena'] for robot in arr]}")




def save_robots_to_json_file(robots, file_name):
    with open(file_name, 'w') as f:
        json.dump(robots, f, ensure_ascii=False, indent=4)


def load_robots_from_json_file(file_name):
    with open(file_name, 'r') as f:
        robots = json.load(f)
    return robots


def main():
    loaded_robots = load_robots_from_json_file('robots.json')
    print(f"Nieposortowane ceny robotów: {[robot['cena'] for robot in loaded_robots]}")

    heap_sort(loaded_robots, True)

    print(f"Posortowane ceny robotów: {[robot['cena'] for robot in loaded_robots]}")
    save_robots_to_json_file(loaded_robots, 'sorted_robots_heap.json')


if __name__ == "__main__":
    main()