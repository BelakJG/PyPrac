import random
import quicksort
import time

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            print("Array is not sorted")
            return
    print("Array is sorted")

def main():
    num_to_sort = 500000
    array = list(range(num_to_sort))

    for i in range(num_to_sort):
        array[i] = random.randint(0, num_to_sort * 20)

    start = time.process_time()
    quicksort.sort(array)
    end = time.process_time()

    is_sorted(array)
    print(f"Time to sort {num_to_sort} digits is {(end - start):.2f} seconds")

if __name__ == '__main__':
    main()