"""
CP1404/CP5632 - Practical 5
Word Occurrence
This program counts the occurrences of words in a string.
Estimate: 30 minutes
Actual:   110 minutes
"""

word_to_count = {}
is_valid = False
while not is_valid:
    try:
        text = input("Text: ")
        words = text.split()
        for word in words:
            count = word_to_count.get(word, 0)
            word_to_count[word] = count + 1
        words = sorted(list(word_to_count.keys()))
        word_length = max((len(word) for word in words))
        for word in words:
            print(f"{word:{word_length}} : {word_to_count[word]}")
        is_valid = True
    except ValueError:
        print("Invalid input!Empty input not allowed.")


