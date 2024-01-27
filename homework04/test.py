
import random
import time

arr = [random.randint(1, 100) for _ in range(1000000)]
if __name__ == "__main__":
    start_time = time.time()
    a=sum(arr)
    print("Total sum:", a)
    print(f"time in {time.time() - start_time:.2f} seconds")