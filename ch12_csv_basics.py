"""A basic csv reading program."""
import csv
from datetime import datetime
import pprint

# A simple dump of the raw data
with open('ch12_csv_buzzers.csv') as raw_data:
    print(raw_data.read())
    print()

# Using a csv reader to read the raw data
with open('ch12_csv_buzzers.csv') as data:
    for line in csv.reader(data):
        print(line)
    print()

# Storing the raw data into a dictionary
with open('ch12_csv_buzzers.csv') as data:
    ignore = data.readline()                # Ignore the header data
    flights = {}                            # Empty dictionary to store the data from the csv
    for line in data:
        k, v = line.strip().split(',')      # First strips any \n and spaces, then splits the data
        flights[k] = v

print(flights, '\n')
