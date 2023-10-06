import threading
import time
import sys

def potok():
    while True:
        print("В работе")
        time.sleep(10)

potoki = list()

for _ in range(5):
    p = threading.Thread(target=potok)
    p.start()
    potoki.append(p)

for i in range(60):
    time.sleep(1)
    
for potok in potoki:
    potok.join()
