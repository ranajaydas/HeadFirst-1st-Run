"""Finds vowels inside an inputted string."""

vowels = ['a', 'e', 'i', 'o', 'u']
found = []
word = input('Enter the word to find vowels in:').lower()

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

if found:
    print('Found the following vowels:', found)
else:
    print('No vowels found.')
