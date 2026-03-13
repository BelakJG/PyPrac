import random
import math
import heapsort

def sort(arr):
    left = 0
    right = len(arr) - 1
    max_depth = math.log2(len(arr)) * 2
    quicksort(arr, left, right, max_depth)

def quicksort(arr, left, right, depth):
    while left < right:
        #insertion sort once partition is small enough
        if right - left <= 16:
            for i in range(left + 1, right + 1):
                key = arr[i]
                j = i - 1
                while j >= left and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
            return

        #heapsort if stack is too deep
        if depth <= 0:
            heapsort.sort(arr, left, right)
            return

        #use median for pivot
        median_index = statistics.median([left, right, int((left+right) / 2)])
        arr[median_index], arr[left] = arr[left], arr[median_index]

        #hoare partition to limit memory swaps
        pivot = arr[left]
        i = left - 1
        j = right + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1

            if i >= j:
                break

            arr[i], arr[j] = arr[j], arr[i]

        #tail elimination
        if (j - left) < (right - j):
            quicksort(arr, left, j, depth - 1)
            left = j + 1
        else:
            quicksort(arr, j + 1, right, depth - 1)
            right = j
