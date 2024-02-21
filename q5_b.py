"""
problem4 task(b)
Kexuan Chen, Guoqing Yu, Shengmin Chen, Lingping Gu
"""


import time
import random


# partition, return the index of pivot after sorted
# arr: input array, low: left boundary, 
# high: right boundary, stats: record comparison and swap status
def hoare_partition(arr, low, high, stats):
    # use the first element as the pivot for Hoare’s Partition Algorithm. 
    pivot = arr[low]
    startIndex = low - 1
    endIndex = high + 1
    while True:
        # move i to the right
        # as long as elements are less than the pivot
        startIndex += 1
        while arr[startIndex] < pivot:
            startIndex += 1
            stats['comparisons'] += 1
        
        # move j to the left
        # as long as elements are greater than the pivot
        endIndex -= 1
        while arr[endIndex] > pivot:
            endIndex -= 1
            stats['comparisons'] += 1
        
        # if pointers meets, means it is sorted
        # return the partition index
        if startIndex >= endIndex:
            return endIndex
        
        # swap elements at startIndex and endIndex
        arr[startIndex], arr[endIndex] = arr[endIndex], arr[startIndex]
        stats['swaps'] += 1


# hoare_partition method 
# arr: input array, low: left boundary, 
# high: right boundary, stats: record comparison and swap status
def hoare_quicksort(arr, low, high, stats):
    if low < high:
        pivot = hoare_partition(arr, low, high, stats)
        hoare_quicksort(arr, low, pivot, stats)
        hoare_quicksort(arr, pivot + 1, high, stats)


# quicksort_wrapper: sort the arr and measure the running time
# arr: input array
def quicksort_wrapper(arr):
    stats = {'comparisons': 0, 'swaps': 0}
    start_time = time.time()
    
    hoare_quicksort(arr, 0, len(arr) - 1, stats)
    
    end_time = time.time()
    running_time = (end_time - start_time) * 1_000_000  # Convert to microseconds
    
    print(f"Total comparisons: {stats['comparisons']}")
    print(f"Total swaps: {stats['swaps']}")
    print(f"Running time (microseconds): {running_time:.2f}")


# test arrays from the assignment
test_arrays = [
    [2, 8, 7, 1, 3, 5, 6, 4],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [8, 5, 3, 4, 2, 6, 1, 7],
    [random.randint(1, 1000) for _ in range(100000)]  # Random array of size 100,000
]

for arr in test_arrays:
    print(f"Original array: {arr[:10]}")
    quicksort_wrapper(arr)
    print(f"Sorted array: {arr[:10]}\n")
    print("\n")
