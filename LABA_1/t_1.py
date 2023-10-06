import threading
import time
import subprocess

print("Запущен процесс 1")
        
subprocess.run(["python3", "t_2.py"])
time.sleep(10)
subprocess.run(["python3", "t_2.py"])
time.sleep(10)
subprocess.run(["python3", "t_3.py"])
time.sleep(10)
subprocess.run(["python3", "t_4.py"])
time.sleep(10)

print("Процесс 1 завершен")
