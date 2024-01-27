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
(многопроцессорность)
'''
import time
import random
import multiprocessing

arr = [random.randint(1, 100) for _ in range(1000000)]

def calculate_sum(start, end, total_sum):
    local_sum = 0
    for i in range(start, end):
        local_sum += arr[i]
    # Захватываем общую переменную и добавляем к ней локальную сумму
    with total_sum.get_lock():
        total_sum.value += local_sum

if __name__ == "__main__":
    total_sum = multiprocessing.Value('i', 0)
    # Создаем и запускаем 10 процессов для параллельного вычисления суммы  
    start_time = time.time()
    processes = []
    for i in range(10):
        start = i * 100000
        end = start + 100000
        process = multiprocessing.Process(target=calculate_sum, args=(start, end, total_sum))
        processes.append(process)
        process.start()
                
    for process in processes:
        process.join()

    print("Total sum:", total_sum.value)
    print(f"time in {time.time() - start_time:.2f} seconds")