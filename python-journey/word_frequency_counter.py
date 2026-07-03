def word_count(words):
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

count = word_count(["apple", "banana", "apple", "orange", "banana", "apple"])
print(count)
