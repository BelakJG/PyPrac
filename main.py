import random
import quicksort
import time

def main():
    array = []

    num_to_sort = 500000
    for _ in range(num_to_sort):
        array.append(random.randint(0, num_to_sort * 20))

    start = time.process_time()
    quicksort.sort(array)
    end = time.process_time()

    print(f"Time to sort {num_to_sort} digits is {(end - start):.2f} seconds")

if __name__ == '__main__':
    main()