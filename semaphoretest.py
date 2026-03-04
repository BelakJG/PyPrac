import threading
import time

MAX_PARA = 4
semaphore = threading.Semaphore(MAX_PARA)
lock = threading.Lock()

def limit_task(num):
    with semaphore:
        time.sleep(1)
        with lock:
            print(f"Thread {num} done")


num_threads = 24
threads = []

start = time.time()
for i in range(num_threads):
    thread = threading.Thread(target=limit_task, args=(i+1,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
end = time.time()

print("All threads done")
print(f"{num_threads} threads took {(end - start):.2f} seconds")
