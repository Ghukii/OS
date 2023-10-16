import threading
import time
import psutil

# Глобальная переменная для хранения состояния потоков
threads_paused = False

# Функция для выполнения работы в потоках
def worker_thread(thread_id):
    while True:
        if not threads_paused:
            print(f"Поток {thread_id} выполняет работу")
            time.sleep(1)
        else:
            print(f"Поток {thread_id} приостановлен")
            time.sleep(1)

# Функция для отслеживания загрузки процессора
def monitor_cpu_usage():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        print(f"Загрузка процессора: {cpu_percent}%")

# Создаем и запускаем потоки
threads = []
for i in range(2):
    thread = threading.Thread(target=worker_thread, args=(i,))
    thread.start()
    threads.append(thread)

# Создаем и запускаем поток для мониторинга загрузки процессора
cpu_monitor_thread = threading.Thread(target=monitor_cpu_usage)
cpu_monitor_thread.start()

while True:
    user_input = input("Введите 'пауза' для приостановки или 'возобновить' для возобновления потоков (или 'выход' для выхода): ")
    
    if user_input == 'пауза':
        threads_paused = True
    elif user_input == 'возобновить':
        threads_paused = False
    elif user_input == 'выход':
        # Завершаем все потоки
        for thread in threads:
            thread.join()
        cpu_monitor_thread.join()
        break
