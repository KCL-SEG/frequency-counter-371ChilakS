"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for value in items:
        value = str(value)
        if value in frequencies.keys():
            frequencies[value] += 1
        else:
            frequencies[value] = 1

    return frequencies
# print(frequencies([1,"ten","1",1,1]))
# print(frequencies([1,"ten","1",1,1,1.0]))
# print(frequencies(['a', 'a', 'b', 'b', 'b', 'c']))
# print(frequencies([100, 'Hello', '100', '100', 100]))