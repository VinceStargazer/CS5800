"""
problem4 task(a)
Kexuan Chen, Guoqing Yu, Shengmin Chen, Lingping Gu
"""

import time
import random


# heapify: build a heap according to the input array
# arr: input array, n: ize of the heap.
# root: index of the root element of the heap.
# stats: record comparison and swap status
def heapify(arr, n, root, stats):
    # initialize largest as root
    largest = root
    # start of it's left children
    l = 2 * root + 1
    # start of it's right children
    r = 2 * root + 2

    # check if left children less than root
    if l < n:
        stats['comparisons'] += 1
        # heapify to make the tree legal
        if arr[l] > arr[largest]:
            largest = l

    # check if right children less than root
    if r < n:
        stats['comparisons'] += 1
        # heapify to make the tree legal
        if arr[r] > arr[largest]:
            largest = r


    # swap to change the root as the biggest
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        stats['swaps'] += 1
        # recursively heapify the tree
        heapify(arr, n, largest, stats)


# main function for heapsort
def heapsort(arr, stats):
    n = len(arr)

    # build a maxheap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i, stats)

    # shrink the arr size, and pop out element
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move current root to end
        stats['swaps'] += 1
        # as we get the biggest element sofar
        # decrease the array size
        heapify(arr, i, 0, stats)


# heapsort_wrapper: sort the arr and measure the running time
# arr: input array
def heapsort_wrapper(arr):
    stats = {'comparisons': 0, 'swaps': 0}
    start_time = time.time()

    heapsort(arr, stats)

    end_time = time.time()
    running_time = (end_time - start_time) * 1_000_000

    print(f"Total comparisons: {stats['comparisons']}")
    print(f"Total swaps: {stats['swaps']}")
    print(f"Running time (microseconds): {running_time:.2f}")

# Test arrays
test_arrays = [
    [2, 8, 7, 1, 3, 5, 6, 4],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [8, 5, 3, 4, 2, 6, 1, 7],
    [random.randint(1, 1000) for _ in range(100000)]  # Random array of size 100,000
]

for i, arr in enumerate(test_arrays, start=1):
    print(f"Original array: {arr[:10]}")
    heapsort_wrapper(arr)
    print(f"Sorted array: {arr[:10]}\n")
    print("\n")

