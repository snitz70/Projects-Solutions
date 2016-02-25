def vowels(string):
    return len([x for x in string if x in 'aeiou'])


def vowel_frequency(string):
    counts = {}
    for s in string:
        if s in 'aeiou':
            counts[s] = counts.get(s, 0) + 1

    return counts
