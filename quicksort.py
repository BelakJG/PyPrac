import random

def sort(arr, left = 0, right = None):
    if right is None:
        right = len(arr) - 1

    #random pivot
    rand_index = random.randint(left, right)
    pivot = arr[rand_index]
    arr[rand_index], arr[right] = arr[right], pivot

    swap_index = left - 1
    for i in range(left, right):
        if arr[i] < pivot:
            swap_index += 1
            arr[swap_index], arr[i] = arr[i], arr[swap_index]

    swap_index += 1
    arr[swap_index], arr[right] = arr[right], arr[swap_index]

    if left < swap_index - 1:
        sort(arr, left, swap_index - 1)
    if swap_index + 1 < right:
        sort(arr, swap_index + 1, right)