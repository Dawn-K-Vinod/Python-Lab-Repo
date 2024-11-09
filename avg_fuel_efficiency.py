"""
Author: Dawn K Vinod
Date: 08-11-2024
Description: Python program to calculate the average fuel efficiency.
"""
n=int(input("Enter the number of trips:"))
total_distance=0
total_fuel=0

for i in range(n):
    distance=float(input(f"Enter the distance(in km) for trip {i+1}:"))
    fuel=float(input(f"Enter the fuel consumed(in litres) for trip {i+1}:"))
    total_distance += distance
    total_fuel += fuel

avg_fuel_efficiency=(total_distance/total_fuel)
print(f"The average fuel efficiency is {avg_fuel_efficiency} km/l")

