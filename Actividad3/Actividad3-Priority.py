# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 22:57:03 2023

@author: josia
"""

class Process:
    def __init__(self, name, arrival_time, burst_time, priority):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

def priority_scheduling(processes):
    n = len(processes)
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0
    time = 0
    while True:
        remaining_processes = [p for p in processes if p.arrival_time <= time and p.burst_time > 0]
        if len(remaining_processes) == 0:
            break
        selected_process = min(remaining_processes, key=lambda x: x.priority)
        selected_process_index = processes.index(selected_process)
        processes[selected_process_index].burst_time -= 1
        time += 1
        if processes[selected_process_index].burst_time == 0:
            completion_time[selected_process_index] = time
            turnaround_time[selected_process_index] = completion_time[selected_process_index] - processes[selected_process_index].arrival_time
            waiting_time[selected_process_index] = turnaround_time[selected_process_index] - processes[selected_process_index].burst_time
            total_waiting_time += waiting_time[selected_process_index]
            total_turnaround_time += turnaround_time[selected_process_index]
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n
    print("Process\tArrival Time\tBurst Time\tPriority\tCompletion Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(processes[i].name, "\t\t", processes[i].arrival_time, "\t\t", processes[i].burst_time, "\t\t", processes[i].priority, "\t\t", completion_time[i], "\t\t", waiting_time[i], "\t\t", turnaround_time[i])
    print("Average waiting time:", average_waiting_time)
    print("Average turnaround time:", average_turnaround_time)

filename = "procesosprioridad.txt" # abre el archivo
processes = []
with open(filename) as f:
    for line in f:
        name, arrival_time, burst_time, priority = line.strip().split()
        processes.append(Process(name, int(arrival_time), int(burst_time), int(priority)))

processes.sort(key=lambda x: x.arrival_time)

priority_scheduling(processes)
