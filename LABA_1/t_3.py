import threading
import time
import subprocess

print("Запущен процесс 3")
    
subprocess.run(["python3", "t_4.py"])
time.sleep(10)

subprocess.run(["python3", "t_4.py"])
time.sleep(10)
        
print("Процесс 3 завершен")
