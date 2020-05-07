text = input('Please enter the text: ')
word_to_count = {}
words = text.split(' ' or ',' or '.')

for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

print(word_to_count)
longest_word = max(len(word) for word in words)

sorted_words = list(word_to_count.keys())
sorted_words.sort()

for sorted_word in sorted_words:
    print("{:>{}} = {}".format(sorted_word, longest_word, word_to_count[sorted_word]))
