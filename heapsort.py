def heapify(arr,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)


def sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr,n,i)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr,i,0)


if __name__ == '__main__':
    import random
    num_len = 10
    arr = list(range(num_len))
    for i in range(num_len):
        arr[i] = random.randint(0, num_len * 10)
    print(arr)
    sort(arr)
    print(arr)