# -*- coding: utf-8 -*-
"""
Created on Mon May  1 18:48:23 2023

@author: josia
"""

import time
import random
import threading

# function to write to file
def write_to_file(writer_id, file, num):
    while True:
        time.sleep(random.choice([1, 1.5, 2])) # wait randomly between 1, 1.5 or 2 seconds
        with threading.Lock():
            file.write(f"Writer {writer_id} wrote: {num}\n")
            file.flush() # ensure data is written to file immediately
            num += 1
        print(f"Writer {writer_id} wrote to file.")

# function to read from file
def read_from_file(reader_id, file):
    while True:
        time.sleep(random.choice([1, 1.5, 2])) # wait randomly between 1, 1.5 or 2 seconds
        with threading.Lock():
            line = file.readline().strip()
            if not line:
                continue # if no line is read, skip iteration and try again
        print(f"Reader {reader_id} read from file.")
        print(f"Read line: {line}")

# main program
if __name__ == '__main__':
    # create file object for writing
    with open('file.txt', 'w') as f:
        num = 1 # initialize number to write
        # create two writer threads
        writer1 = threading.Thread(target=write_to_file, args=('Writer 1', f, num+1))
        writer2 = threading.Thread(target=write_to_file, args=('Writer 2', f, num+1))

        # create two reader threads
        reader1 = threading.Thread(target=read_from_file, args=('Writer 1', f))
        reader2 = threading.Thread(target=read_from_file, args=('Writer 2', f))

        # start all threads
        writer1.start()
        writer2.start()
        reader1.start()
        reader2.start()

        # wait for threads to complete
        writer1.join()
        writer2.join()
        reader1.join()
        reader2.join()

