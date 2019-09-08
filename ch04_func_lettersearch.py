# Copy of this function in the 'ch04_func_installing_into_sitepackages' folder


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of 'letters' found in 'phrase'."""
    return set(letters.lower()).intersection(set(phrase.lower()))
