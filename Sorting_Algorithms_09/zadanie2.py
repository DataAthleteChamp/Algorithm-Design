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


def partition(arr, low, high, step_by_step=False):
    i = (low - 1)
    pivot = arr[high]['cena']

    for j in range(low, high):
        if arr[j]['cena'] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quick_sort(arr, low, high, step_by_step=False):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high, step_by_step)

        if step_by_step:
            print(f"Lista cen po podziale: {[robot['cena'] for robot in arr]}")

        quick_sort(arr, low, pi - 1, step_by_step)
        quick_sort(arr, pi + 1, high, step_by_step)


def save_robots_to_json_file(robots, file_name):
    with open(file_name, 'w') as f:
        json.dump(robots, f, ensure_ascii=False, indent=4)


def load_robots_from_json_file(file_name):
    with open(file_name, 'r') as f:
        robots = json.load(f)
    return robots


def main():
    loaded_robots = load_robots_from_json_file('robots.json')
    print(f"Nieposortowane roboty: {[robot['cena'] for robot in loaded_robots]}")

    quick_sort(loaded_robots, 0, len(loaded_robots) - 1, True)

    print(f"Posortowane roboty: {[robot['cena'] for robot in loaded_robots]}")
    save_robots_to_json_file(loaded_robots, 'sorted_robots_quick.json')


if __name__ == "__main__":
    main()
