import multiprocessing
import time

MAX_PROC = 5
semaphore = multiprocessing.Semaphore(MAX_PROC)
lock = multiprocessing.Lock()

def inc_test(arr, index):
    with semaphore:
        time.sleep(1)
        arr[index] += 1

if __name__ == '__main__':
    num_pro = 25
    array = multiprocessing.Array("i", num_pro)
    for i in range(num_pro):
        array[i] = i
    print(array[:])

    start = time.time()
    processes = []
    for i in range(num_pro):
        p = multiprocessing.Process(target=inc_test, args=(array, i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
    end = time.time()

    print(array[:])
    print(f"All done! took {(end - start):.2f} seconds")
