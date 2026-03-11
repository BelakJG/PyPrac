import ctypes
import random
import quicksort
import time
import multiprocessing
from multiprocessing import shared_memory
import numpy

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            print("Array is not sorted")
            return
    print("Array is sorted")

def main():
    num_to_sort = 5000000
    data = numpy.zeros(num_to_sort)
    for i in range(num_to_sort):
        data[i] = random.randint(0, num_to_sort * 20)
    shared_mem = shared_memory.SharedMemory(create=True, size=data.nbytes)

    shared_arr = numpy.ndarray(data.shape, dtype=data.dtype, buffer=shared_mem.buf)
    shared_arr[:] = data[:]

    semaphore = multiprocessing.Semaphore(multiprocessing.cpu_count())
    start = time.time()
    quicksort.sort(shared_arr, semaphore)
    end = time.time()

    is_sorted(shared_arr)
    print(f"Time to sort {num_to_sort} digits is {(end - start):.2f} seconds")

    shared_mem.close()
    shared_mem.unlink()

if __name__ == '__main__':
    main()