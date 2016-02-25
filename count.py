def vowels(string):
    """method to return the number of vowels in a string"""

    return len([x for x in string if x in 'aeiou'])


def vowel_frequency(string):
    """method to return a dictionary with the vowels and frequency
    of each"""

    counts = {}
    for s in string:
        if s in 'aeiou':
            counts[s] = counts.get(s, 0) + 1

    return counts
