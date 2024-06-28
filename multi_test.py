from stress_test import run_stress_test
from concurrent.futures import ThreadPoolExecutor
import time
import os
import multiprocessing


num_cores = os.cpu_count() or multiprocessing.cpu_count()
num_cores = num_cores -1
print(f"Cores numbres: {num_cores}")


def run_selenium_task():
    start_time = time.time()
    run_stress_test()
    print(f"Time taken: {time.time() - start_time}")

with ThreadPoolExecutor(max_workers=num_cores) as executor:
    for _ in range(num_cores):
        executor.submit(run_selenium_task)


