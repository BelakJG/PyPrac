import random

def sort(arr, left = 0, right = None):
    if right is None:
        right = len(arr) - 1
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

        #random pivot
        rand_index = random.randint(left, right)
        arr[rand_index], arr[left] = arr[left], arr[rand_index]
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
            sort(arr, left, j)
            left = j + 1
        else:
            sort(arr, j + 1, right)
            right = j
