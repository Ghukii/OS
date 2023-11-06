import random

class PageTable:
    def __init__(self):
        self.page_table = {}

    def update_page_table(self, virtual_page, physical_page):
        self.page_table[virtual_page] = physical_page

    def get_physical_page(self, virtual_page):
        return self.page_table.get(virtual_page, None)

class Memory:
    def __init__(self, num_pages):
        self.physical_memory = [None] * num_pages

    def allocate_page(self, page):
        available_page = None
        for i in range(len(self.physical_memory)):
            if self.physical_memory[i] is None:
                available_page = i
                break
        if available_page is not None:
            self.physical_memory[available_page] = page
        return available_page

    def evict_page(self):
        page_to_evict = random.choice(self.physical_memory)
        for i in range(len(self.physical_memory)):
            if self.physical_memory[i] == page_to_evict:
                self.physical_memory[i] = None
                break
        return page_to_evict

class Disk:
    def __init__(self, filename):
        self.filename = filename

    def save_page(self, page):
        with open(self.filename, 'a') as file:
            file.write(page)

def simulate_memory_dispatcher(num_pages, num_processes):
    virtual_address_space = [i for i in range(num_pages)]
    page_table = PageTable()
    memory = Memory(num_pages)
    disk = Disk('disk.txt')

    for i in range(num_processes):
        process_id = i + 1
        print(f"Process {process_id}:")
        
        for _ in range(10):
            virtual_page = random.choice(virtual_address_space)
            
            physical_page = page_table.get_physical_page(virtual_page)
            if physical_page is not None:
                print(f"Accessing page {virtual_page} in physical page {physical_page}")
            else:
                allocated_page = memory.allocate_page(virtual_page)
                if allocated_page is not None:
                    page_table.update_page_table(virtual_page, allocated_page)
                    print(f"Allocating page {virtual_page} in physical page {allocated_page}")
                else:
                    evicted_page = memory.evict_page()
                    disk.save_page(str(evicted_page))
                    allocated_page = memory.allocate_page(virtual_page)
                    page_table.update_page_table(virtual_page, allocated_page)
                    print(f"Allocating page {virtual_page} in physical page {allocated_page}, evicting page {evicted_page} to disk")

simulate_memory_dispatcher(10, 3)
