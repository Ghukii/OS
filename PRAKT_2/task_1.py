import threading
import time

def summa(start, end, thread_id):
    numbers = list(range(start, end + 1))
    total_sum = sum(numbers)
    print(f"Поток {thread_id} Числа {numbers} сумма {total_sum}")


def potok(N, M):
    threads = list()
    size = N // M

    for i in range(M):
        start = i * size + 1
        end = (i + 1) * size if i < M - 1 else N
        thread = threading.Thread(target=summa, args=(start, end, i))
        thread.start()
        time.sleep(10)
        threads.append(thread)

    time.sleep(30)

    for thread in threads:
        thread.join()

N, M = int(input("Введите N: ")), int(input("Введите M: "))

potok(N, M)
