# Store the raw data into a dictionary
with open('ch12_csv_buzzers.csv') as data:
    ignore = data.readline()                # Ignore the header data
    flights = {}                            # Empty dictionary to store the data from the csv
    for line in data:
        k, v = line.strip().split(',')      # First strips any \n and spaces, then splits the data
        flights[k] = v

print(flights, '\n')


# Create a list of the destinations, not using Comprehensions
destinations1 = []
for dest in flights.values():
    destinations1.append(dest.title())
print(destinations1)


# Using a Comprehension
destinations2 = [dest.title() for dest in flights.values()]
print(destinations2)
