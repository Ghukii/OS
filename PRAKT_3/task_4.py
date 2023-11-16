import os

directory = '/home/ghukii/Zakharov_Andrew/prak5/input'

files = os.listdir(directory)

print(*files)

words = 0

for file in files:
    with open(directory + '/' + file, 'r') as f:
        data = f.read()
        words += len(list(filter(lambda x: x.isalpha(), data)))
    f.close()

out_dir = '/home/ghukii/Zakharov_Andrew/prak5/output'

with open(out_dir + '/' + 'out.txt', 'w') as f:
    f.write(str(words))
f.close()

print(*os.listdir(out_dir))