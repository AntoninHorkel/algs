import numpy as np
# import numba as nb
import time
# import matplotlib.pyplot as plt

def swap(data: np.ndarray, idx1: int, idx2: int) -> np.ndarray:
    data[idx1], data[idx2] = data[idx2], data[idx1]
    return data

def quick_sort(data: np.ndarray) -> np.ndarray:
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = data[data < pivot]
    mid = data[data == pivot]
    right = data[data > pivot]
    return np.concatenate((quick_sort(left), mid, quick_sort(right)))

def heapify(data: np.ndarray, n: int, i: int):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and data[left] > data[largest]:
        largest = left
    if right < n and data[right] > data[largest]:
        largest = right
    if largest != i:
        swap(data, i, largest)
        heapify(data, n, largest)

def heap_sort(data: np.ndarray) -> np.ndarray:
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)
    for i in range(n - 1, 0, -1):
        swap(data, i, 0)
        heapify(data, i, 0)
    return data

def merge(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    result = np.empty(len(left) + len(right), dtype=left.dtype)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result[k] = left[i]
            i += 1
        else:
            result[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        result[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        result[k] = right[j]
        j += 1
        k += 1
    return result

def merge_sort(data: np.ndarray) -> np.ndarray:
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)

def radix_sort(data: np.ndarray) -> np.ndarray:
    if len(data) == 0:
        return data
    max_val = np.max(data)
    exp = 1
    output = np.empty_like(data)
    while max_val // exp > 0:
        count = np.zeros(10, dtype=int)
        for num in data:
            index = (num // exp) % 10
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for i in range(len(data) - 1, -1, -1):
            index = (data[i] // exp) % 10
            output[count[index] - 1] = data[i]
            count[index] -= 1
        np.copyto(data, output)
        exp *= 10
    return data

def insertion_sort(data: np.ndarray) -> np.ndarray:
    for i in range(1, len(data)):
        x = data[i]
        start = 0
        end = i
        while start < end:
            mid = (start + end) // 2
            if data[mid] < x:
                start = mid + 1
            else:
                end = mid
        # data[start:i + 1] = np.roll(data[start:i + 1], 1)
        data[start + 1:i + 1] = data[start:i]
        data[start] = x
    return data

def bubble_sort(data: np.ndarray) -> np.ndarray:
    for i in range(len(data) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if data[j] > data[j + 1]:
                swap(data, j, j + 1)
                # data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data

def selection_sort(data: np.ndarray) -> np.ndarray:
    for i in range(len(data) - 1):
        swap(data[i:], 0, np.argmin(data[i:]))
    return data

if __name__ == "__main__":
    A = [
        (quick_sort, "quick_sort"),
        (heap_sort, "heap_sort"),
        (merge_sort, "merge_sort"),
        (radix_sort, "radix_sort"),
        (insertion_sort, "insertion_sort"),
        (bubble_sort, "bubble_sort"),
        (selection_sort, "selection_sort"),
    ]
    B = A[:-3]
    C = [
        ("rando_1M_cela_cisla.txt", np.uint32, "%u", B),
        ("random_words_1M.txt", np.str_, "%s", B),
        ("random_integers_10M.txt", np.int64, "%i", B), # 32-bit?
        ("random_10M_interval.txt", np.float32, "%f", B),
        ("integers_0_to_4294967295.txt", np.uint32, "%u", B),
    ]
    for (file_name, dtype, fmt, algs) in C:
        # for (alg, alg_name) in algs:
            data = np.loadtxt("./in_data/" + file_name, dtype=dtype)
            tic = time.perf_counter()
            # data = alg(data)
            data = insertion_sort(data)
            toc = time.perf_counter()
            np.savetxt("./out_data/" + file_name, data, fmt=fmt)
            elapsed_time = toc - tic
            print(f"Seřazení souboru {file_name} pomocí {"insertion_sort"} trvalo {elapsed_time:0.4f} sekund")
