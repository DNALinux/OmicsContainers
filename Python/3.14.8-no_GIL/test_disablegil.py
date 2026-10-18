"""
Script to test GIL.

How to test:

Test when GIL is disabled (it should be faster):

# python3 -X gil=0 test_disablegil.py
Testing with 8 cores ...
Time elapsed: 10.04 seconds
Is GIL enabled: False

Test when GIL is enabled (it should be slower):

# python3 -X gil=1 test_disablegil.py
Testing with 8 cores ...
Time elapsed: 35.41 seconds
Is GIL enabled: True
"""

import threading
import time
import sys
from os import cpu_count


def worker():
    result = 0
    for x in range(10**8):
        result += 1


def test_multithreading():
    num_threads = cpu_count()
    print(f"Testing with {num_threads} cores ...")
    threads = [threading.Thread(target=worker) for x in range(num_threads)]
    start_time = time.time()
    for x in threads:
        x.start()
    for x in threads:
        x.join()
    time_elapsed = time.time() - start_time    
    print(f"Time elapsed: {time_elapsed:.2f} seconds")
    
test_multithreading()
print(f"Is GIL enabled: {sys._is_gil_enabled()}")
