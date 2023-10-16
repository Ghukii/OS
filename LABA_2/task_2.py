import threading
import random

def add_matrices(matrix1, matrix2, result, start_row, end_row):
    for i in range(start_row, end_row):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

# Функция для запуска многопоточного сложения матриц
def main():
    M = int(input("Введите количество строк (M) матрицы: "))
    N = int(input("Введите количество столбцов (N) матрицы: "))

    # Создаем две матрицы с случайными значениями
    matrix1 = [[random.randint(1, 10) for _ in range(N)] for _ in range(M)]
    matrix2 = [[random.randint(1, 10) for _ in range(N)] for _ in range(M)]

    # Создаем результатную матрицу с нулевыми значениями
    result = [[0 for _ in range(N)] for _ in range(M)]

    # Введите количество потоков (M потоков для M строк матрицы)
    num_threads = M

    # Создаем список для хранения объектов потоков
    threads = []

    # Рассчитываем размер отрезка для каждого потока
    segment_size = M // num_threads

    # Создаем и запускаем потоки
    for i in range(num_threads):
        start_row = i * segment_size
        end_row = (i + 1) * segment_size if i < num_threads - 1 else M
        thread = threading.Thread(target=add_matrices, args=(matrix1, matrix2, result, start_row, end_row))
        thread.start()
        threads.append(thread)

    # Ожидаем завершения всех потоков
    for thread in threads:
        thread.join()

    # Выводим исходные матрицы и результат
    print("\nМатрица 1:")
    for row in matrix1:
        print(row)

    print("\nМатрица 2:")
    for row in matrix2:
        print(row)

    print("\nРезультат сложения:")
    for row in result:
        print(row)

    # Проверяем результат однопоточным сложением
    single_thread_result = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            single_thread_result[i][j] = matrix1[i][j] + matrix2[i][j]

    # Сравниваем результаты
    if result == single_thread_result:
        print("\nРезультаты совпадают с однопоточным сложением.")
    else:
        print("\nРезультаты не совпадают с однопоточным сложением.")

if __name__ == "__main__":
    main()
