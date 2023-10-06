import os
import time

print('PID:', os.getpid())
print('PPID:', os.getppid())

while True:
	print("процесс в работе")
	time.sleep(5)
