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
(многопоточность)
'''
import time
import random
import threading

arr = [random.randint(1, 100) for _ in range(1000000)]

def calculate_sum(start, end):
    global total_sum
    local_sum = 0
    for i in range(start, end):
        local_sum += arr[i]
    # Захватываем общую переменную и добавляем к ней локальную сумму
    with total_sum_lock:
        total_sum += local_sum


if __name__=="__main__":
    total_sum = 0
    start_time = time.time()
    total_sum_lock = threading.Lock()

    # Создаем и запускаем 10 потоков для параллельного вычисления суммы
    threads = []
    for i in range(10):
        start = i * 100000
        end = start + 100000
        thread = threading.Thread(target=calculate_sum, args=(start, end))
        threads.append(thread)
        thread.start()

    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()

    print("Total sum:", total_sum)
    print(f"time in {time.time() - start_time:.2f}seconds")
