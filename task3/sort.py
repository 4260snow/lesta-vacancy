import time
from random import randint


def heapify(arr, index, size):
    left = 2 * index + 1
    right = 2 * index + 2
    if (left < size and arr[left] > arr[index]):
        largest = left
    else:
        largest = index
    if (right < size and arr[right] > arr[largest]):
        largest = right
    if (largest != index):
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, size)


def heapsort(arr):
    size = len(arr)
    for i in range(size, -1, -1):
        heapify(arr, i, size)
    for i in range(size - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)


# Обратно отсортированный массив
"""
arr = [i for i in range(100000, 0, -1)]
t_start = time.process_time()

# sorted(arr)    # 0.03
# arr.sort()     # 0.015
# heapsort(arr)    # 1.061

dt = time.process_time() - t_start
print(dt)
"""

# Случайный порядок случайных чисел

arr = [randint(0, 10000000) for i in range(100000)]
t_start = time.process_time()

# sorted(arr)    # 0.03
# arr.sort()     # 0.03
heapsort(arr)    # 1.2

dt = time.process_time() - t_start
print(dt)
