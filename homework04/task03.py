'''
Напишите программу на Python, которая будет находить
сумму элементов массива из 1000000 целых чисел.
Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
Массив должен быть заполнен случайными целыми числами
от 1 до 100.
При решении задачи нужно использовать многопоточность,
многопроцессорность и асинхронность.
В каждом решении нужно вывести время выполнения
вычислений.
(асинхронность)
'''

import time
import random
import asyncio

arr = [random.randint(1, 100) for _ in range(1000000)]

async def calculate_sum(start, end, arr):
    local_sum = sum(arr[start:end])
    return local_sum

async def main():
    total_sum = 0
    tasks = []
    for i in range(10):
        start = i * 100000
        end = start + 100000
        task = asyncio.create_task(calculate_sum(start, end, arr))
        tasks.append(task)

    local_sums = await asyncio.gather(*tasks)
    total_sum = sum(local_sums)
    print("Total sum:", total_sum)

start_time = time.time()
asyncio.run(main())
print(f"time in {time.time() - start_time:.2f} seconds")