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


def counting_sort(robots):
    max_range = 101  # Ustalamy maksymalny zasięg robota na 100
    count = [0] * max_range

    for robot in robots:
        count[robot['zasieg']] += 1

    sorted_robots = []
    for i in range(max_range):
        while count[i] > 0:
            for robot in robots:
                if robot['zasieg'] == i:
                    sorted_robots.append(robot)
                    robots.remove(robot)
                    break
            count[i] -= 1

    return sorted_robots


def save_robots_to_json_file(robots, file_name):
    with open(file_name, 'w') as f:
        json.dump(robots, f, ensure_ascii=False, indent=4)


def load_robots_from_json_file(file_name):
    with open(file_name, 'r') as f:
        robots = json.load(f)
    return robots


def main():
    loaded_robots = load_robots_from_json_file('robots.json')
    print(f"Nieposortowane zasięgi robotów: {[robot['zasieg'] for robot in loaded_robots]}")

    sorted_robots = counting_sort(loaded_robots)

    print(f"Posortowane zasięgi robotów: {[robot['zasieg'] for robot in sorted_robots]}")
    save_robots_to_json_file(sorted_robots, 'sorted_robots_count.json')


if __name__ == "__main__":
    main()
