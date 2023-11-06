import psutil

memory = psutil.virtual_memory()

total = memory.total

free = memory.available

print(f'Количесво страниц физической памяти: {total}')
print(f'Количесво свободных страниц физической памяти: {free}')