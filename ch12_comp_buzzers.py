from datetime import datetime
import pprint

# Store the raw data into a dictionary
with open('ch12_csv_buzzers.csv') as data:
    ignore = data.readline()                # Ignore the header data
    flights = {}                            # Empty dictionary to store the data from the csv
    for line in data:
        k, v = line.strip().split(',')      # First strips any \n and spaces, then splits the data
        flights[k] = v

print(flights, '\n')

# Transform the data
print("""Three transformations are required for the data:
1. Change the time from 24h to AM/PM.
2. Change the Destinations to Title case.
3. Convert the dictionary to use 
   Destination as key: Times as values.
""")


# Function to covert 24h time to AM/PM time
def convert2ampm(time24h: str) -> str:
    return datetime.strptime(time24h, '%H:%M').strftime('%I:%M %p')


print('Transformations 1 & 2 using a dictcomp:')
flights2 = {convert2ampm(k): v.title() for k, v in flights.items()}
pprint.pprint(flights2)


print('\nTransformation 3 using a simple comprehension:')
when = {}
for dest in set(flights2.values()):
    when[dest] = [k for k, v in flights2.items() if dest == v]
pprint.pprint(when)


print('\nTransformation 3 using a complex comprehension:')
when2 = {dest: [k
                for k, v in flights2.items()
                if dest == v]
         for dest in set(flights2.values())}
pprint.pprint(when2)
