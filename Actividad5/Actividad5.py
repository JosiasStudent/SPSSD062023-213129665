# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:13:52 2023

@author: josia
"""
class MemoryBlock:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.size = end - start
        self.is_allocated = False

    def allocate(self, size):
        self.is_allocated = True

    def deallocate(self):
        self.is_allocated = False


class MemoryManager:
    def __init__(self, memory_size):
        self.memory_size = memory_size
        self.memory_blocks = [MemoryBlock(0, memory_size)]

    def allocate_best_fit(self, size):
        best_block = None
        for block in self.memory_blocks:
            if not block.is_allocated and block.size >= size:
                if best_block is None or block.size < best_block.size:
                    best_block = block

        if best_block is not None:
            best_block.allocate(size)
            return best_block.start

        return None

    def allocate_worst_fit(self, size):
        worst_block = None
        for block in self.memory_blocks:
            if not block.is_allocated and block.size >= size:
                if worst_block is None or block.size > worst_block.size:
                    worst_block = block

        if worst_block is not None:
            worst_block.allocate(size)
            return worst_block.start

        return None

    def allocate_next_fit(self, size):
        next_block = None
        for block in self.memory_blocks:
            if not block.is_allocated and block.size >= size:
                if next_block is None:
                    next_block = block
                elif block.start > next_block.start:
                    next_block = block

        if next_block is not None:
            next_block.allocate(size)
            return next_block.start

        return None

    def allocate_first_fit(self, size):
        for block in self.memory_blocks:
            if not block.is_allocated and block.size >= size:
                block.allocate(size)
                return block.start

        return None

    def deallocate(self, start):
        for block in self.memory_blocks:
            if block.start == start:
                block.deallocate()

    def add_memory_block(self, start, end):
        self.memory_blocks.append(MemoryBlock(start, end))


if __name__ == '__main__':
    # Example usage

    # Initialize memory manager with a memory size of 1000
    memory_manager = MemoryManager(1000)

    # Read memory sizes from file
    with open("archivos.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                # Split line by comma to extract file name and memory size
                parts = line.split(",")
                if len(parts) == 2:
                    try:
                        size = int(parts[1].strip().rstrip("kb"))
                        memory_manager.add_memory_block(memory_manager.memory_blocks[-1].end, memory_manager.memory_blocks[-1].end + size)
                    except ValueError:
                        print(f"Error: Failed to parse line '{line}' as integer")
                else:
                    print(f"Error: Failed to parse line '{line}'")

    # Allocate memory using different algorithms
    print("Best Fit:")
    print(memory_manager.allocate_best_fit(500))  # Should print the start address of the allocated block or None if not found
    print("Worst Fit:")
    print(memory_manager.allocate_worst_fit(300))
    print("Next Fit:")
    print(memory_manager.allocate_next_fit(200))  # Should print the start address of the allocated block or
    print("First Fit:")
    print(memory_manager.allocate_first_fit(100))  # Should print the start address of the allocated block or None if not found

    # Deallocate memory
    memory_manager.deallocate(0)  # Deallocating block starting from address 0


