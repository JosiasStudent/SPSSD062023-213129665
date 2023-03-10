# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 00:30:03 2023

@author: josia
"""

class Process:
    def __init__(self, name, burst_time):
        self.name = name
        self.burst_time = burst_time
        self.remaining_time = burst_time
#inicio de algoritmo round robin
def round_robin(processes, quantum):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    time = 0
    queue = []
    for i in range(n):
        queue.append(processes[i])
    while True:
        all_done = True
        for i in range(n):
            process = queue.pop(0)
            if process.remaining_time > 0:
                all_done = False
                if process.remaining_time > quantum:
                    time += quantum
                    process.remaining_time -= quantum
                    queue.append(process)
                else:
                    time += process.remaining_time
                    waiting_time[i] = time - process.burst_time
                    process.remaining_time = 0
                    turnaround_time[i] = time
        if all_done:
            break
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    total_waiting_time = 0
    total_turnaround_time = 0
    for i in range(n):
        print(processes[i].name, "\t\t", processes[i].burst_time, "\t\t", waiting_time[i], "\t\t", turnaround_time[i])
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]
   # print("Average waiting time:", total_waiting_time/n)
   # print("Average turnaround time:", total_turnaround_time/n)
#Apertura de archivos
filename = "procesosroundrobin.txt"
quantum = 3
# Inicializa la lista de procesos
processes = []

# Lee los archivos del documento y los añade a la lista
with open('procesosroundrobin.txt', 'r') as f:
    for line in f:
        process = line.strip().split(',')
        processes.append(process)

# Initialize the time slice and current time
time_slice = 10
current_time = 0

# Se iteran los procesos hasta completarlos todos
while processes:

    process = processes[0]
    
    print (int (process[0][0:1]))
    
    if  int (process[0][0:1])<= time_slice:
        
        processes.pop(0)
        
        
        current_time += int (process[0][0:1])
        
        
        print("Process", process[0], "completed at time", current_time)
    else:
        
        process[1] -= time_slice
        
        
        processes.append(process)
        
        
        current_time += time_slice
        
# Impresion del tiempo total de completado de todos los procesos
print("Total time taken to complete all processes:", current_time)

round_robin(processes, quantum)
