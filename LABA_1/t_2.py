import threading
import time
import subprocess

print("Запущен процесс 2")

subprocess.run(["python3", "t_3.py"])
time.sleep(10)

subprocess.run(["python3", "t_3.py"])
time.sleep(10)

subprocess.run(["python3", "t_3.py"])
time.sleep(10)

print("Процесс 2 завершен")
