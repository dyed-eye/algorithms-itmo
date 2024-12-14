import time
import random
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import asyncio

T1, load1 = 2, 0.25
T2, load2 = 1, 0.15
T3, load3 = 0.5, 0.01

U1 = 10
U2 = 5
U3 = 20

def process_action(action_time, cpu_load):
    time.sleep(action_time)
    print(f"Processed action with load: {cpu_load * 100}% for {action_time} seconds.")

def sequential_processing():
    print("Starting sequential processing...")
    for _ in range(U1):
        process_action(T1, load1)
    for _ in range(U2):
        process_action(T2, load2)
    for _ in range(U3):
        process_action(T3, load3)

def thread_processing():
    print("Starting thread processing...")
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        for _ in range(U1):
            futures.append(executor.submit(process_action, T1, load1))
        for _ in range(U2):
            futures.append(executor.submit(process_action, T2, load2))
        for _ in range(U3):
            futures.append(executor.submit(process_action, T3, load3))
        for future in futures:
            future.result()

def subprocess_processing():
    print("Starting subprocess processing...")
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = []
        for _ in range(U1):
            futures.append(executor.submit(process_action, T1, load1))
        for _ in range(U2):
            futures.append(executor.submit(process_action, T2, load2))
        for _ in range(U3):
            futures.append(executor.submit(process_action, T3, load3))
        for future in futures:
            future.result()

async def async_process_action(action_time, cpu_load):
    await asyncio.sleep(action_time)
    print(f"Processed action with load: {cpu_load * 100}% for {action_time} seconds.")

async def async_processing():
    print("Starting asynchronous processing...")
    tasks = []
    for _ in range(U1):
        tasks.append(async_process_action(T1, load1))
    for _ in range(U2):
        tasks.append(async_process_action(T2, load2))
    for _ in range(U3):
        tasks.append(async_process_action(T3, load3))
    await asyncio.gather(*tasks)

def main():
    print("=== Sequential Processing ===")
    sequential_processing()
    
    print("\n=== Thread Processing ===")
    thread_processing()
    
    print("\n=== Subprocess Processing ===")
    subprocess_processing()
    
    print("\n=== Asynchronous Processing ===")
    asyncio.run(async_processing())

if __name__ == "__main__":
    main()

