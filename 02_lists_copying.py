"""Program to illustrate good and bad ways of copying lists"""

list1 = [1, 2, 3, 4, 5]

# Bad way of copying
list2 = list1

# Good way of copying
list3 = list1.copy()

# And here's why
list2.append(6)
list3.append(7)

print(list1)        # SHIEEEEETTT SON...the original list got fucked!
print(list2)
print(list3)
