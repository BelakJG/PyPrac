def heapify(arr, left, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[left + l] > arr[left + largest]:
        largest = l

    if r < n and arr[left + r] > arr[left + largest]:
        largest = r

    if largest != i:
        arr[left + i], arr[left + largest] = arr[left + largest], arr[left + i]
        heapify(arr, left, n, largest)


def sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    n = right - left + 1

    # build heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, left, n, i)

    # extract elements
    for i in range(n - 1, 0, -1):
        arr[left], arr[left + i] = arr[left + i], arr[left]
        heapify(arr, left, i, 0)


if __name__ == '__main__':
    import random
    num_len = 10
    arr = list(range(num_len))
    for i in range(num_len):
        arr[i] = random.randint(0, num_len * 10)
    print(arr)
    sort(arr)
    print(arr)