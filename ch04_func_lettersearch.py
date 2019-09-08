def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


print(search4letters("Hitch-hiker's Guide to the Galaxy", "sky"))
print(search4letters("Ranajay Das is awesome", "pp"))
print(search4letters("Choot pakoda"))
print(help(search4letters))


