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
words = sorted(list(word_to_count.keys()))
print(words)
word_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{word_length}} : {word_to_count[word]}")



