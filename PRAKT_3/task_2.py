import os

class FileSystem:
    def __init__(self, total_space=64 * 1024, block_size=512):
        self.total_space = total_space
        self.block_size = block_size
        self.blocks = total_space // block_size
        self.files = {}

    def create_file(self, file_name, file_size):
        if file_name in self.files:
            print(f"Ошибка: Файл {file_name} уже существует.")
            return

        required_blocks = (file_size + self.block_size - 1) // self.block_size
        if required_blocks > self.get_free_blocks():
            print("Ошибка: Недостаточно места для создания файла.")
            return

        self.files[file_name] = {
            'size': file_size,
            'blocks': required_blocks
        }
        print(f"Файл {file_name} создан успешно.")

    def delete_file(self, file_name):
        if file_name not in self.files:
            print(f"Ошибка: Файл {file_name} не найден.")
            return

        del self.files[file_name]
        print(f"Файл {file_name} удален успешно.")

    def copy_file(self, source_file, destination_file):
        if source_file not in self.files:
            print(f"Ошибка: Файл {source_file} не найден.")
            return

        file_size = self.files[source_file]['size']
        self.create_file(destination_file, file_size)
        print(f"Файл {source_file} скопирован в {destination_file} успешно.")

    def move_file(self, source_file, destination_path):
        if source_file not in self.files:
            print(f"Ошибка: Файл {source_file} не найден.")
            return

        file_size = self.files[source_file]['size']
        required_blocks = (file_size + self.block_size - 1) // self.block_size

        if required_blocks > self.get_free_blocks():
            print("Ошибка: Недостаточно места для перемещения файла.")
            return

        del self.files[source_file]
        self.files[destination_path] = {
            'size': file_size,
            'blocks': required_blocks
        }
        print(f"Файл {source_file} перемещен в {destination_path} успешно.")

    def rename_file(self, old_name, new_name):
        if old_name not in self.files:
            print(f"Ошибка: Файл {old_name} не найден.")
            return

        self.files[new_name] = self.files.pop(old_name)
        print(f"Файл {old_name} переименован в {new_name} успешно.")

    def get_free_blocks(self):
        used_blocks = sum(file_info['blocks'] for file_info in self.files.values())
        return self.blocks - used_blocks


fs = FileSystem()

fs.create_file("file1.txt", 1024)
fs.create_file("file2.txt", 2048)

fs.copy_file("file1.txt", "file3.txt")

fs.move_file("file2.txt", "folder1/file2.txt")

fs.rename_file("file1.txt", "new_file1.txt")

fs.delete_file("file3.txt")
