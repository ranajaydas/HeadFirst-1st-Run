"""Finds vowels inside an inputted string using sets."""

vowels = set('aeiou')
word = input('Enter the word to find vowels in:').lower()

found = vowels.intersection(set(word))

if found:
    print('Found the following vowels:', sorted(found))
else:
    print('No vowels found.')
