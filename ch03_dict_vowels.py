"""Finds vowels inside an inputted string, with frequency count."""

vowels = ['a', 'e', 'i', 'o', 'u']
found = {}
word = input('Enter the word to find vowels in:').lower()

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)             # Much simpler way of initializing dictionaries
        found[letter] += 1

if found:
    for k, v in sorted(found.items()):
        print("'{}' was found {} time(s).".format(k, v))
else:
    print('No vowels found.')
