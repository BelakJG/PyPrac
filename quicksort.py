import random

def sort(arr, left = 0, right = None):
    if right is None:
        right = len(arr) - 1
    while left < right:
        #random pivot
        rand_index = random.randint(left, right)
        pivot = arr[rand_index]
        arr[rand_index], arr[right] = arr[right], arr[rand_index]

        #partition lesser values to left of pivot
        swap_index = left - 1
        for i in range(left, right):
            if arr[i] <= pivot:
                swap_index += 1
                arr[swap_index], arr[i] = arr[i], arr[swap_index]

        #swap end of array with pivot and continue recursion
        swap_index += 1
        arr[swap_index], arr[right] = arr[right], arr[swap_index]

        #tail elimination
        if ((swap_index - 1) - left) < (right - (swap_index + 1)):
            sort(arr, left, swap_index - 1)
            left = swap_index + 1
        else:
            sort(arr, swap_index + 1, right)
            right = swap_index - 1
