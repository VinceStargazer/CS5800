"""
problem4 task(a)
Kexuan Chen, Guoqing Yu, Shengmin Chen, Lingping Gu
"""


import time
import random


# quicksort method
# arr: input array, low: left boundary, 
# high: right boundary, stats: record comparison and swap status
def quicksort(arr, low, high, stats):
    if low < high:
        # get the index pivot
        pivot = partition(arr, low, high, stats)
        
        # recursively call quicksort
        quicksort(arr, low, pivot - 1, stats)
        quicksort(arr, pivot + 1, high, stats)


# partition, return the index of pivot after sorted
# arr: input array, low: left boundary, 
# high: right boundary, stats: record comparison and swap status
def partition(arr, low, high, stats):
    # set the pivot as the last (right-most) element
    pivot = arr[high]  
    # lomuto partition
    # p = 1st, r = last, i = p - 1
    i = low - 1  
    
    for j in range(low, high):
        # increase comparison
        stats['comparisons'] += 1
        if arr[j] < pivot:
            # move index i forward, since current number should stay left
            i += 1
            # swap
            arr[i], arr[j] = arr[j], arr[i] 
            # increase swap
            stats['swaps'] += 1
    
    # swap pivot into correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1] 
    # increase swaps
    stats['swaps'] += 1
    # the index of pivot
    return i + 1


# quicksort_wrapper: sort the arr and measure the running time
# arr: input array
def quicksort_wrapper(arr):
    # used to count the total comparison and swap
    stats = {'comparisons': 0, 'swaps': 0}

    # get the start time
    start_time = time.time()
    # call quicksort function
    quicksort(arr, 0, len(arr) - 1, stats)
    # get the end time
    end_time = time.time()
    # calculate total runtime, convert to microseconds
    running_time = (end_time - start_time) * 1_000_000
    
    #output to see result
    print(f"Total comparisons: {stats['comparisons']}")
    print(f"Total swaps: {stats['swaps']}")
    print(f"Running time (microseconds): {running_time:.2f}")


# test cases
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
