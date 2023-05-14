import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import copy


def heapify(nums, heap_size, root_index, steps):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        steps.append(copy.deepcopy(nums))
        heapify(nums, heap_size, largest, steps)


def heap_sort(nums):
    steps = [copy.deepcopy(nums)]
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i, steps)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        steps.append(copy.deepcopy(nums))
        heapify(nums, i, 0, steps)

    return steps


def partition(data, low, high):
    steps = []
    i = low - 1
    pivot = data[high]
    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            steps.append(copy.deepcopy(data))
    data[i + 1], data[high] = data[high], data[i + 1]
    steps.append(copy.deepcopy(data))
    return i + 1, steps


def quick_sort(data, low, high):
    steps = []
    if low < high:
        pi, new_steps = partition(data, low, high)
        steps += new_steps
        left_steps = quick_sort(data, low, pi - 1)
        right_steps = quick_sort(data, pi + 1, high)
        steps += left_steps + right_steps
    return steps


data = [3, 8, 5, 1, 9, 6, 0, 7, 4, 2, 5]

heap_steps = heap_sort(copy.deepcopy(data))
quick_steps = quick_sort(copy.deepcopy(data), 0, len(data) - 1)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].set_title("Heap Sort")
axs[1].set_title("Quick Sort")

axs[0].set_ylim([0, len(data)])
axs[1].set_ylim([0, len(data)])

heap_rects = axs[0].bar(range(len(data)), data, align='edge')
quick_rects = axs[1].bar(range(len(data)), data, align='edge')


def update(num):
    for rect, val in zip(heap_rects, heap_steps[num]):
        rect.set_height(val)
    for rect, val in zip(quick_rects, quick_steps[num]):
        rect.set_height(val)

# Upewnij się, że obie listy kroków mają taką samą długość
if len(heap_steps) < len(quick_steps):
    heap_steps += [heap_steps[-1]] * (len(quick_steps) - len(heap_steps))
elif len(quick_steps) < len(heap_steps):
    quick_steps += [quick_steps[-1]] * (len(heap_steps) - len(quick_steps))

ani = animation.FuncAnimation(fig, update, frames=len(heap_steps), interval=500)

plt.show()
