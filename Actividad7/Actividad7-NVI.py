# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 18:12:30 2023

@author: josia
"""

import threading
import time
import random

# define the parking lot object
parking_lot = []

# define a lock to control access to the parking lot object
lock = threading.Lock()

# define a variable to keep track of the maximum number of cars in the parking lot
MAX_PARKING_LOT_SIZE = 10

# define the producer function
def producer(arrival_frequency):
    global parking_lot
    while True:
        # wait for the user-specified amount of time
        time.sleep(arrival_frequency)

        # acquire the lock
        lock.acquire()

        # check if the parking lot is full
        if len(parking_lot) >= MAX_PARKING_LOT_SIZE:
            print("Parking lot is full. Car not added.")

        else:
            # generate a new car object
            new_car = "Car " + str(len(parking_lot)+1)

            # add the new car to the parking lot
            parking_lot.append(new_car)
            print("New car arrived:", new_car)

        # release the lock
        lock.release()

# define the consumer function
def consumer(departure_frequency):
    global parking_lot
    while True:
        # wait for the user-specified amount of time
        time.sleep(departure_frequency)

        # acquire the lock
        lock.acquire()

        # check if the parking lot is empty
        if len(parking_lot) == 0:
            print("Parking lot is empty. No car to remove.")

        else:
            # remove the first car from the parking lot
            removed_car = parking_lot.pop(0)
            print("Car removed from parking lot:", removed_car)

        # release the lock
        lock.release()

# get user input for the arrival and departure frequencies
arrival_frequency = float(input("Enter the frequency of car arrivals (in seconds): "))
departure_frequency = float(input("Enter the frequency of car departures (in seconds): "))

# create and start the producer and consumer threads
producer_thread = threading.Thread(target=producer, args=(arrival_frequency,))
consumer_thread = threading.Thread(target=consumer, args=(departure_frequency,))
producer_thread.start()
consumer_thread.start()
