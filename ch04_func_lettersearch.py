def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of 'letters' found in 'phrase'."""
    return set(letters.lower()).intersection(set(phrase.lower()))
