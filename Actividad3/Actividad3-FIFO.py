# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 22:42:51 2023

@author: josia
"""

class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time

def first_in_first_out(processes):
    n = len(processes)
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0
    for i in range(n):
        if i == 0:
            completion_time[i] = processes[i].burst_time
        else:
            completion_time[i] = completion_time[i-1] + processes[i].burst_time
        turnaround_time[i] = completion_time[i] - processes[i].arrival_time
        waiting_time[i] = turnaround_time[i] - processes[i].burst_time
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n
    print("Process\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(processes[i].name, "\t\t", processes[i].arrival_time, "\t\t", processes[i].burst_time, "\t\t", completion_time[i], "\t\t", waiting_time[i], "\t\t", turnaround_time[i])
    print("Average waiting time:", average_waiting_time)
    print("Average turnaround time:", average_turnaround_time)

filename = "procesos.txt" # abre el archivo
processes = []
with open(filename) as f:
    for i, line in enumerate(f):
        if i == 20:
            break
        name, arrival_time, burst_time = line.strip().split()
        processes.append(Process(name, int(arrival_time), int(burst_time)))

processes.sort(key=lambda x: x.arrival_time)

first_in_first_out(processes)

