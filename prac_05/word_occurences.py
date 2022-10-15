"""
CP1404/CP5632 - Practical 5
State Names
This program counts the occurrences of words in a string.
Estimate: 30 minutes
Actual:
"""

TEXT_TO_COUNT = {}
text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
for word in words:
    count = TEXT_TO_COUNT.get(word, 0)
    TEXT_TO_COUNT[word] = count + 1
print(TEXT_TO_COUNT)
