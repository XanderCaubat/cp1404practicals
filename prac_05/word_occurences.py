"""
CP1404/CP5632 - Practical 5
State Names
This program counts the occurrences of words in a string.
Estimate: 30 minutes
Actual:
"""

word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    count = word_to_count.get(word, 0)
    word_to_count[word] = count + 1
print(word_to_count)
