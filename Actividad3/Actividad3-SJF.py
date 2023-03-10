# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 22:28:51 2023

@author: josia
"""

class Process:
    def __init__(self, name, burst_time):
        self.name = name
        self.burst_time = burst_time

def shortest_job_first(processes):
    n = len(processes)
    remaining_time = [0] * n
    for i in range(n):
        remaining_time[i] = processes[i].burst_time
    completed = 0
    time = 0
    waiting_time = 0
    while True:
        min_burst_time = float('inf')
        min_index = n
        for i in range(n):
            if remaining_time[i] > 0 and remaining_time[i] < min_burst_time:
                min_burst_time = remaining_time[i]
                min_index = i
        if min_index == n:
            break
        process = processes[min_index]
        waiting_time += time
        time += process.burst_time
        remaining_time[min_index] = 0
        completed += 1
    average_waiting_time = waiting_time / n
    print("Process\tBurst Time\tWaiting Time")
    for i in range(n):
        waiting_time = time - processes[i].burst_time
        print(processes[i].name, "\t\t", processes[i].burst_time, "\t\t", waiting_time)
    print("Average waiting time:", average_waiting_time)

filename = "procesossjf.txt" # abre el archivo
processes = []
with open(filename) as f:
    for line in f:
        name, burst_time = line.strip().split()
        processes.append(Process(name, int(burst_time)))

processes.sort(key=lambda x: x.burst_time)

shortest_job_first(processes)
