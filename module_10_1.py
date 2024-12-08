import threading
from time import sleep, time

def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

def measure_time(func, *args):
    start_time = time()
    func(*args)
    end_time = time()
    return end_time - start_time

print("Запуск записи в файлы...")
time_taken_1 = measure_time(write_words, 10, 'example1.txt')
time_taken_2 = measure_time(write_words, 30, 'example2.txt')
time_taken_3 = measure_time(write_words, 200, 'example3.txt')
time_taken_4 = measure_time(write_words, 100, 'example4.txt')

print(f"Время выполнения функций: {time_taken_1 + time_taken_2 + time_taken_3 + time_taken_4:.6f} секунд")

print("Запуск потоков...")
threads = []
file_params = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]

start_time_threads = time()

for params in file_params:
    thread = threading.Thread(target=write_words, args=params)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time_threads = time()
print(f"Работа потоков {end_time_threads - start_time_threads:.6f} секунд")
