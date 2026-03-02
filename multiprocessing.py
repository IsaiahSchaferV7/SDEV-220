import multiprocessing
import os
import time
import random

def process_task(process_id):
    wait_time = random.randint(0, 2)  # Random wait time between 0 and 2 seconds
    time.sleep(wait_time)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # Format the current time
    print(f"Process {process_id} (PID: {os.getpid()}) waited for {wait_time:.4f} seconds and finished at: {current_time}")

if __name__ == "__main__":
    num_processes = 3  # Number of processes to create
    processes = []

    for i in range(num_processes):
        p = multiprocessing.Process(target=process_task, args=(i+1,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes have completed.")